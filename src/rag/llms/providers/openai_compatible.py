from typing import Optional

from openai import OpenAI

from src.rag.llms.base_llm import BaseLLM, LLMResponse
from src.utils.logger_config import logger


class OpenAICompatibleLLM(BaseLLM):

    def __init__(
        self,
        config,
        api_key: Optional[str] = None,
    ):

        super().__init__(
            config=config,
            api_key=api_key,
        )

        self.model = config.model_name
        self.temperature = config.temperature
        self.base_url = config.base_url
        self.client = self.initialize_client()

    def initialize_client(self):
        if self.api_key:

            if self.base_url:
                logger.info(
                    f"Initializing OpenAI client with custom base URL: {self.base_url}"
                )
                return OpenAI(api_key=self.api_key, base_url=self.base_url)
            else:
                logger.warning(
                    "No custom base URL provided, initializing OpenAI client using OpenAI LLM provider"
                )
                return OpenAI(api_key=self.api_key)

        else:
            logger.error("API key is required to initialize OpenAI client")
            raise ValueError(
                "API key is required to initialize OpenAI client. Please provide a valid API key in the .env file."
            )

    def generate(self, message: str) -> LLMResponse:

        # Append user message to the conversation history
        old_messages = self.chat_history.copy()
        old_messages.append({"role": "user", "content": message})

        try:
            response = self.client.chat.completions.create(
                model=self.model, messages=old_messages, temperature=self.temperature
            )

            llm_response = response.choices[0].message.content
            logger.info(f"Received response from OpenAI: {llm_response}")

            # Update the chat history with the new messages
            old_messages.append({"role": "assistant", "content": llm_response})
            self.chat_history = old_messages
            return LLMResponse(success=True, message=llm_response, status_code=200)

        except Exception as e:
            logger.error(f"Error during OpenAI API call: {e}")
            return LLMResponse(success=False, message="", status_code=500, error=str(e))
