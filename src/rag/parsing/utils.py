import hashlib


def generate_file_id(uploaded_file):
    file_bytes = uploaded_file.getbuffer()
    return hashlib.sha256(file_bytes).hexdigest()
