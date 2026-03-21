

--- Page 1 ---

Predicting Sovereign Debt Crises

Paolo Manasse, Nouriel Roubini, and Axel Schimmelpfennig

--- Page 2 ---

IMF Working Paper

Fiscal Affairs Department

Predicting Sovereign Debt Crises

Prepared by Paolo Manasse, Nouiel Roubini, and Axel Schimmelpfennig'

Authonized for distribution by Richard Hemming

November 2003

Abstract

The vicws cxpressed in this Working Papcr are thosc ofthe author(s) and do not necessarily epresent those ofthe IMF or IMF policy. Working Papers describe research in progress by the author(s) and are published to elicit comments and to fuuther debate

We develop an early-warning model of sovereign debt crises. A country is defined to be in a debt crisis ifit is classified as in default by Standard & Poor's, or if it has access to nonconcessional IMF financing in excess of 10O percent of quota: By means oflogit and binary recursive tree analysis; we identify mnacroeconomic variables reflecting solvency and liquidity factors that predict a debt-crisis episode one year in advance . The Iogit model predicts 74 percent of all crises entries while sending few false alarms, and the recursive tree 89 percent while sending more false alarms. being

JEL Classification Numbers: H63, E66, C53

Keywords: Early-wamning system; sovereign debt crises, sovereign default

Authors 's E-Mail Addresses: manasse@spbo unibo it; nroubini@stern nyu edu;

aschimmelpfennig@imf org

Paolo Manasse; University of Bologna; Nouriel Roubini, New York University; and Axel Schimmelpfemnig, International Monetary Fund. We thank Andy Berg Mazk De Brock; Jamnes Daniel, Bob Flood Rex Ghosh, Richard Heming; Jun Il Kim, Dan Mathieson, Mauro Mecagni, Christian Mulder , and Schuknecht for many helpful comments Annette Kyobe provided outstanding research assistance:. Ludger

--- Page 3 ---

| Contents                                                                             |   Page |
|--------------------------------------------------------------------------------------|--------|
| Predicting Sovereign Debt Crises .                                                   |      3 |
| II Related Literature                                                                |        |
| IIL. Data; Descriptive Statistics, and Event Study Analysis                          |      8 |
| A The Data                                                                           |      8 |
| B. Descriptive Statistics                                                            |     10 |
| C. Event Study Analysis                                                              |     12 |
| IV . The Logit Early-Warning System                                                  |     18 |
| A Estimation Approach                                                                |     18 |
| B. Specifying the Logit EWS.                                                         |     20 |
| V. The Tree EWS                                                                      |     27 |
| A. The Tree-Analysis Methodology_                                                    |     27 |
| B. Results fromn the Tree Analysis                                                   |     29 |
| C. Combining the Logit and the Tree EWS                                              |     32 |
|                                                                                      |     33 |
| Text Tables                                                                          |        |
| 1. Counties aud Debt-C1isis Episodes in the Full Samnple                             |      9 |
| 2. Mean of Variables Used in the Regressions                                         |        |
| 3. Regression Results: Coefticient Estimates; 1990 Onward Sample                     |     22 |
| 4 Regression Results: Model Performance, 1990 Onward Sample                          |     23 |
| 5.Regression Results: Coefficient Estimnates: Full Sample                            |     24 |
| 6. Regression Results: Model Performance, Full Sample.                               |     25 |
| 7 The Empirical Iree: Model Performance                                              |     31 |
| Figures                                                                              |        |
| 1. Event Study Analysis: Short-Teiu Debt Variables                                   |     13 |
| 2 Event Stidy Analysis: Total Debt, Public Debt, and Debt-Service Variables          |     14 |
| 3  Event Study Analysis: Balance of Payments Variables                               |     15 |
| Event Study Analysis: Selected Macrovariables                                        |     16 |
| 5 Example of Tree Methodology                                                        |     29 |
| 6.                                                                                   |     30 |
| Appendixes                                                                           |        |
| Sensitivity Anal of the Logit EWS_ ysis                                              |     36 |
| II Iree Analysis: Prior Probabilities; Misclassification Costs; and Assignment Rules |     38 |
| References                                                                           |     39 |

--- Page 4 ---

I PREDICTING SOVEREIGN DEBT CRISES

As more counties are moving toward flexible exchange rates; cunency crises associated with the collapse of a fixed exchange rate regime are becoming less frequent . Sovereign debt-sexvicing difficulties and, in some cases; outright defaults, by contrast, have become more common in recent years. The macroeconomic misalignents leading to debt crises, however, are still not well understood: the literature has mostly been in the business of attempting to predict currency crises; with some success; and the associated banking crises in some of these episodes. Ihere is a large empirical literature on "twin banking crises, but little work has lately been done on predicting sovereign debt crises.

In recent years; sovereign debt-servicing difficulties have taken different forms , from outright default on domestic and external debt to rollover/liquidity crises where a solvent; but illiquid, country was on the verge of default on its debt because of investors' unwillingness to roll over short-term debts coming to maturity. We observed outright defaults on domestic andor external debt in Russia, Ecuador, Argentina; episodes of semi-coercive restructuring in 1999, and Uruguay in 2003; and other episodes where the country was most likely solvent but illiquid and a debt-servicing crisis was in part avoided via amounts of official support by the intemnational financial institutions (IFIs), as well as less coercive fomms of pivate sector involvement in crisis resolution (Mexico in 1994 95, Korea and Thailand in 1997-98, Brazil in 1999 and 2002, Turkey in 2001, and Uruguay in 2002). In many of the external or domestic debt obligations of the sovereign or of the private sector (the private banks in Korea; for example), rather than excessive debt associated with a clear insolvency situation. The decision of domestic and intemnational investors not to roll over such shortteim liabilities the country on the verge of outright default, which was avoided in tuough the financial suppont of the official sector. In addition to tie cases cited above; several other countries have large debt burdens and may be subject to debt-setvicing problems in the foreseeable future. Thus, sovereign debt-servicing difficulties (both ofthe illiquidity and insolvency vatieties) that were severe during the 1980s debt crisis, have becomne relatively frequent phenomnena in the last decade. Tlus. assessing and predicting debt sustainability is of great empirical and policy importance. large part, put again

This paper employs a variety of techniques to assess the role of macroeconomic fudamentals in affecting the risk of sovereign default and a debt crisis; for a large sample of countries loosely defined as market access and for different definitions of a debt ctisis. One innovation in our work is that the crisis definitions include not only cases of through the provision of large-scale official financing by the IMF We ask the followving questions: What is the set of economic fundamentals whose misalignment is more likely to result in a debt-servicing crisis? What is the role of such imbalances in getting into a crisis VeISUS gelting out of a cisis? Are these effects asymetic? Can we identify critical thresholds beyond which default risks rise considerably? Can we design an early wamning systems (EWS) model of debt crises that can help predict early on the vulnerability to such a having

--- Page 5 ---

combination of the two approaches .

Based on OUr empirical analysis; we reach the following main conclusions.

- The empirical evidence suggests that a number of macrocconomic factors predict a 'solvency' matter: higl levels of foreign debt (relative to a measure of the increase the probability of a default and entry into default . Measures of illiquidity; particularly short-term debt (relative to foreign reserves), and measures of debt servicing obligations also matter in predicting debt crises, consistent with the view and insolvency. Other macroeconomic variables suggested from the analytical literature on debt sustainability also significantly matter for predicting debt crises: low GDP growth; cuzrent account imbalances; low trade openness; tight liquidity and monetary conditions in the Group of seven countries; monetary mismanagement (in inflation); and political uncertainty leading to economic uncertainty (years of presidential elections) Among the fiscal variables, only the ratio of public debt to revenuc has somc predictive power. However; data availability severely limits the ability to appropriately test for the role of such variables. From a number of political economy variables, a dummy for presidential election years, reflecting political uncertainty; and a index of political freedom help crises prediction; crises move fast while institutions change slowly; so that finding significant effects is likely to remain problematic.
- Sovereign debt crises ; unlike currency crisis, last and show persistence. Once a country is in a crisis; it is not easy to get out of one, as these episodes often have Even when a country wrangles its way out of a default, the macroeconomic picture is often not as positive as for those countries that have successfully avoided default. long long spells.
- Although we concentrate on understanding the factors that trigger a countty 's entry into a debt crisis, the importance of obtaining an early-wamning sip of a crisis, we also consider whether these factors affect the likelihood of exit fiom a crisis . The model predicts much better entry into a crisis than exit from it, since it is pat, this is due to the fact that even the definition of exit is somewhat ambiguous: do default crises end when the default is cured (as in the case of Brady plans for the 1980s crises) or when economic adjustment and reforms lead to economic recovely? gnal
- Heterogeneity across countries and interdependence of economic variables within countries should not be overlooked when searching for ~the critical thresholds that signal the likelihood of a future crisis. We find that countries with extemnal debt greater than 50 percent of GDP are more likely to experience default episodes.

--- Page 6 ---

Default is even more likely; if inflation; public debt; andor extemnal financing requirements are high: Countries with low extemal debts may still suffer a high risk of crisis when faced with liquidity problems, political uncertainty, and fiscal mismanagement, OI when the exchange rate is overvalued and international capital markets are tight.

- In terms of EWS models, our two models of predicting debt crises outperform the curent state-of-the-ant literature on early-waming models of curency crises (indicating that it is easier to predict debt crises and entty into crises than to predict curency crises). Our logit model predicts 74 percent of entries into a crisis while sending out few false alarms (ie. , predicting a crisis when one does not occur) The recursive tree approach correctly predicts 89 percent of entries into a crisis while sending out more false alamms.

Overall, this paper improves on the empirical literature on debt crises in several respects: data; crisis definition; empirical methodology; and we think results. Although a considerable amount of work has been done to analyze the crises of the 1980s, very little has done on a sample that includes the 1990s. In this respect, our model makes some progress by paying special attention to factors that help predict more recent crisis episodes. been the dataset, description of the crisis definition; descriptive statistics, and an event study analysis. Section [V presents and estimates a logit model, and discusses the results obtained wvith this model and the robustness of these results . Section V presents the results from the binary recursive tree technique . The section also discusses options of combining the logit EWS and the tree EWS to inform policymakers about possible debt-servicing vulnerabilities Section VIprescnts some concluding remarks and suggestions for extensions of this work .

1

Tle literature on debt cuisis falls into four broad categories: theoretical mnodels of sovereign default; empirical studies of the detenminants of debt crisis; empirical studies of the predictive power of credit ratings; and empirical studies of the determination of spreads . Most studies focus on a together, the literatue suggests a nunber of macroeconomic and other factors that influences the likelihood of sovereign debt-servicing difficulties and default.

The theoretical literature highlights a variety of factors that can trigger sovereign default and debt crises On the one side, countries can be unwilling to repay their debt, based on an

See Roubini (2001) for a recent overview of debt sustainability and solvency; aud Eaton and Femandez (1995) for a systematic suvey of the literature on sovereign debt. Hemming and Petrie (2002) present an extensive and broad discussion of the concept of fiscal vulnerability; the concept includes the failure to avoid excessive deficits and debt. The concept of fiscal sustainability is. for example; discussed in Hemming and Chalk (2000)

--- Page 7 ---

intetemporal optimization calculus . On the other side; countries can be unable to repay their debt because they are either insolvent or illiquid . In empirical applications , a host of macroeconomic and institutional variables have thus been used   Whether a sovereign is insolvent or not depends on its stock of debt relative to its ability to pay, measured, for example, by GDP, expots; Or govemment revenues A sovercign is solvent, ifthe discounted value of future prinary balances is greater Or to the cunent public debt stock. Likewise, a country is solvent, if the discounted value of future trade balances exceeds the curent stock of extemnal debt.  Ihe exchange rate regime and exchange rate misalignment impact these considerations because an overvaluation can cause an extemnal imbalance that leads to debt accumulation Moreover; a cunency crisis triggered by overvaluation can lead the costs of default and thus a country' s willingness to default or not. Measures of macroeconomic stability; such as low intlation or low money growth; reflect policy credibility and predictability and thus influence investors7 debt crisis can also occur if a country is illiquid rather than insolvent. Hence; liquidity measures, such as shont-term debt to reserves or M2 to reserves, are included in some models. Finally; institutional and political factors affect policy credibility; as well as a govemnment 's willingness to pursue policies consistent with a sustainable debt equal path.

Empirical studies use different crisis definition depending on the specific research question and the information available in the data source used A priori; there is no single empirical definition of what should constitute a sovereigu default or a debt cisis. Some studies comnpile a list of debt crisis or default from case studies and anecdotal evidence (e.g Beers and Bhatia , 1999; or Beimn and Calomiris; 2001). Other studies rely on a more quantitative approach: For example, Detragiache and Spilimbcrgo (2001) dcfinc a country to be in a debt crisis if the country has arrears on external obligations toward commnercial creditors in excess of 5 percent of commercial debt outstanding or has a rescheduling or restnucturing agreement with commercial creditors . This definition does not differentiate between sovereign or private sector arrears andor rescheduling due to data limitations:. Another problem of this quantitative definition is that it might exclude some incipient debt crises that were only avoided by large-scale financial support fromn official creditors (IFIs aud/or bilateral) . Ideally, one could attempt to define a continuous crisis pressure metric similar to the exchange market pressure index underlying some currency crisis studies. A data source that provides uniformly compiled information on sovereign default is Standard & Poor 's (2002) who define a country to be in default as as the sovereign is not curent on any of its debt obligation Jong

Studies of the determinants of debt crisis are closest in nature to an early-wamning signal model. Factors influencing the probability of a debt crisis occuring are identified by means of probitllogit regressions or signals models. Most studies have focused on the debt crisis of the 1980s, but there are also some recent efforts that look at crisis occuring in the 19905. Taken together; mneasures of solvency; such as the debt-to-GDP ratio; aud measues of

See for example Detragiache and Spilimbergo (2001) for a study including recent episodes.

--- Page 8 ---

liquidity, such as short-termn debt to resexves or exports and debt service to resexves Or exports; are significant explanatory variables in addition to macroeconomic controls, such as real growth, inflation; exchange rate overvaluation; and the fiscal balance. Reinhart (2002) finds that in 84 percent of the cases in her sample, a debt crisis is preceded by a curency crisis. Hence, variables that are well-suited for predicting curency crisis should also have explanatory power in models for sovereign default (see also Hemmning et al, 2003) Detragiache and Spilimbergo (2001) carty out a number of interesting tests . find that short-termn debt, debt service, and reserves enter their model separately and the null of equal coefficients is rejected. ratios such as short-term debt to reserves, therefore; imposes a restriction that is not suppoited by the data. They also find that short-term debt is endogenous a debt crisis. While most studies use macroeconomic variables only in levels, Catào and Sutton (2002) also include measures of volatility in their model. The in-sample predictive power increases markedly when measures of ters of trade volatility; fiscal policy volatility; monetary policy volatility, and exchange rate policy volatility are added to a model fiscal balance; the U.S. interest rate; and the real effective exchange rate They Using Jong

The predictive power of credit ratings for currency crisis and sovereign default is suprisingly poor: Ihis became evident in the Asian crisis or, more recently, in the Argentinean crisis. Systematic evidence in this is presented in Reinhart (2002); Rojas-Suarez (2001); and credits ratings. Some studies test whether credit ratings are significantly conrelated with a range of economic fundamentals . Measures of extemnal debt, default history; as well as other macroeconomic and political variables are found to be conrelated with default/debt-crisis events Haque, Nelson; and Mathieson; 1998; Cantor and Packer; 1996, and Lee; 1993) regard (e.g,

The detenmninants of sovereign spreads have been analyzed in several studies: For example; nonbailout of Russia in 1998, suggesting that spreads are compressed by moral hazard (see also Lane and Phillips (2001), for other tests of moral hazard that provide mixed results) However; the power of these spreads in predicting debt crisis has not been assessed systematically due to data limitations. Many debt crisis and defaults occured in the 1980s, wvhile measures of sovereign spread became widely available only in the 1990s, after the widely issued and traded. spreads are not available for many poorer developing experienced debt-servicing problems in their obligations to official creditors . Also,

Taken together; the existing literature suggests several regularities that could form the backbone of an empirical model attempting to predict sovereign default:

- Measures of solvency; such as public and extemnal debt relative to capacity to pay.
- possibly in relation to reserves or exports .

--- Page 9 ---

- Vaiables used in mnodels of cureucy cisis such as the IMF s EWS.
- Measures of extemnal volatility and volatility in economic policies.
- Macroeconomic (control) variables, such as real growth;, inflation; exchange rate, etc
- Political aud institutional variables capturing a country's willingness to pay.

IL DATA, DESCRIPTIVE STATISTICS, AND EvENT STUDY ANALYSIS

A. Ihe Data

The dataset includes information on 47 economies with market access for the period 1970 to 2002 (Table 1) The debt-crisis indicator is derived from data provided by Standard & Poor S and data on IMF lending. Data on extemnal debt and public debt is taken from the World Bank 's Global Developmnent Finance database (GDF) as well as fromn IMF sources. Data on public finance and other macroeconomic variables are taken from the IMF= 5 World Economic Outlook database as well as the Govemnment Finance Statistics database (GFS) A detailed description ofthe variables and their source is provided in Appendix IV.

A country is defined to be in a debt crisis ifit is classified as being in default by Standard & Poor ifit receives a large nouconcessional [MF loan defined as access in excess of 100 percent of quota . Standard & Poor s rates sovereign issuers in default, if a government fails to meet principal or interest payment on extemnal obligation on due date (including exchange offers; debt equity swaps, and back for cash) A potential problem with this infonation is that it may not capture quasi defaults that were only prevented tlrough an adjustment program and a large financial package from the IMF . We therefore augment the infonation obtained from Standard & Poor's with data on IMF nonconcessional lending from the IMF' s Finance Department. We use infonmation on the loans approved approval dates andthe actual disbursement of the loans . Based on the information on IMF lending; a country is classified as in debt crisis if a nonconcessional loan is approved and a disbursement under this loan is actally made in the first year . The definition of debt crisis thus encompasses actual defaults on debt recorded by Standard & Poor's and 'incipient' defaults that wvere avoided only through a scale financial suppont from the IMF Based this definition; a county can be in debt crisis for an extended pcriod of time. Initially; we define a IMF loan as in excess of 100 percent of quota; this threshold selects the 10 percent of loans when ranked by the loan to quota ratio . As sensitivity analysis; we also use a 50 percent and a 150 percent threshold to define the debt-crisis indicator. buy being large large lange being top

The full dataset includes information on 76 countries. For transition economies, the sample period is 1995 to 2002. Not every variable is available for all countries or for the full time period

Mainly SBA and EFF lending.

--- Page 10 ---

Table 1 Countries and Debt-Crisis Episodes in the Full Sample 1/ 2/

|                             | Number of Crises   | Average Length   | Years in Cisis   | Cisis episodes (eutry_exit)        |
|-----------------------------|--------------------|------------------|------------------|------------------------------------|
| Algcria                     |                    | 6.0              | 6                | 1991-97                            |
| Argentina                   | 3                  | 5.0              | 15               | 1982-94, 1995-96. 2001             |
| Bolivia                     | 2                  | 65               | 13               | 1980-85, 1986-94                   |
| Bazil                       | 3                  | 5.3              | 16               | 1983-95. 1998-00. 2001             |
| Chilc                       |                    | 8.0              | 8                | 1983-91                            |
| China                       | 0                  |                  | 0                |                                    |
| Colombia                    | 0                  |                  | 0                |                                    |
| Costa Rica                  | 1                  | 10               | 10               | 1981-91                            |
| Cyprus                      | 0                  |                  | 0                |                                    |
| Czech Republic 3/           | 0                  |                  | 0                |                                    |
| Dominican Republic          |                    | 22               | 22               | 1981 -                             |
| Ecuador                     |                    | 8.0              | 16               | 1982-96. 1999-2001                 |
| Egypt                       |                    | 10               |                  | 1984 85                            |
| El Salvador                 |                    | 16               | 16               | 1981-97                            |
| Estonia 3/                  |                    |                  |                  |                                    |
| Guatcmala                   | 8                  | 10               |                  | 1986-87                            |
| Hungary 3/                  |                    |                  | 0                |                                    |
| India                       | 0                  |                  | 0                |                                    |
| Indonesia                   | 2                  | 25               | 5                | 1997-2001 2002 _                   |
| Israel                      |                    |                  | 0                |                                    |
| Jamaica                     | 3                  | 4.7              | 14               | 1978-80, 1981-86, 1987-94          |
| Jordan                      | 1                  | 5.0              | 5                | 1989-94                            |
| Kazakhstan 3/               | 2                  |                  | 0                |                                    |
| Korea                       |                    | 20               | 4                | 1980-82, 1997-99                   |
| Latvia 3/                   | 0                  |                  | 0                |                                    |
| Lithuania 3/                | 0                  |                  | 0                |                                    |
| Malaysia Mexico             | 0 2                | 5.0              | 0 10             | 1982-91, 1995-96                   |
| Morocco                     | 2                  | 3.0              | 6                | 1983-84, 1986-91                   |
|                             | 0                  |                  | 0                |                                    |
| Pakistan                    |                    | 2.0              | 12               | 1998-2000                          |
| Panama                      | ;                  | 14               |                  | 1983-97                            |
| Paraguay                    |                    | 70               |                  | 1986-93                            |
| Peru                        |                    | 6.3              | 19               | 1976-77, 1978-81. 1983-98          |
| Philippines                 | 0                  | 10               | 10 0             | 198393                             |
| Poland 3/                   |                    |                  | 0                |                                    |
| Romania 3/                  | 8                  |                  |                  |                                    |
| Russia 3                    |                    | 3.0              | 3                | 1998-2001                          |
| Slovak Republic 3/          |                    |                  | 0                |                                    |
| South Africa                | 4                  | 18               | 7                | 1976-78, 1985-88                   |
| Thailand                    |                    | 10               | 2                | 1981-82, 1997-98                   |
| Irinidad and Tobago Tunisia |                    | 10               | 1                | 1988-90 1991-92                    |
|                             |                    | 2.0              | 2                |                                    |
| Turkey                      |                    |                  |                  |                                    |
| Ukaine 3/ Unguay            | 1 3                | 3.0 2.0          | 3 6              | 1998-2001 1983-86, 1987-88. 199092 |
| Venezuela                   |                    |                  | 10               | 1983-89,1990-91 1995_98            |
|                             | 3                  | 3.3              |                  |                                    |

Sources: IMF: Standard & Poor's; World Bank: and authors calculations

2/ Data 1970-2002. from

1/ A country is defined to be in a debt-crisis ifit is classified as in default by Standard & Poor's or 1eceives a noncossional IMF loan in excess of 100 percent of quota being

3/ Transition countries are included only fiom 1995 onward

--- Page 11 ---

As another robustness check; we use only the Standard & Poor's data excluding debt-crisis episodes that relate only to exceptional IMF lending.

B. Descriptive Statistics

The potential explanatory variables are largely drawn from a list of usual suspects. In particular; we use various measures of extemnal debt and 'public debt; measures of solvency and liquidity; regressors included in the IMF 5 cunrency crisis EWS as there is a possible link fiscal flow variables. Iable 2 gives the respective mean of these variables in the full sample, for noncrisis episodes, for years before a country enters a debt crisis, for in-crisis years, and for years before a country exits a crisis. In general, the of means from noncrisis to into crisis and finally exit fromn crisis is as expected. path entry

- The various measures of external debt (including debt servicing) are relatively low in noncrisis followed by another noncrisis vear: increase in the before crisis and most mneasures increase even funther within crisis. Ihe measures again in the year before a countty exits from crisis, though they are still higher than before the crisis. The mneasures of public extemnal debt follow the same pattern; suggesting that public extemnal debt is apossible driving force behind extemal debt developments (as in many countries a large fraction of extemnal debt is public extemnal debt). years year drop entry;
- Tle macroeconomnic variables ~including those fromn the IMF's cuency crisis EWS_indicate a worsening of the macroeconomic sitation in the nun-1p to a crisis and within a crisis, and an improvement in the situation when exiting from crisis. For example; the curent account deficit increases in the year immediately preceding a crisis a cisis. Real growth falters in the year before crisis entry while inflation spikes. The overall balance as well as primary balance deteriorate in the run-up to crisis . It is interesting to note that both the LIBOR as well as the U.S. treasury bill rate increase in years preceding a crisis, suggesting that tight monetary conditions in the G7 area may reduce capital flows to emerging market economies and thus contribute to debt vicing difficulties (as it happened in 1982 for example) entry,

Taken together, the descriptive statistics depict a worsening of the debt situation as well as the overall macroeconomic situation in the un-up to a crisis; and an improvement in these best, and the indicated relationships require more rigorous statistical or econometric testing .

Appendix Table 8 reproduces this table for episodes staiting in or after 1990.

--- Page 12 ---

Table 2 Mean of Variables Used in the Regressions

| Cutrent year                                                         | All       | Noncrisis Noncrisis   | Nonctisis Crisis   | Crisis Crisis   | Crisis Noncrisis   | No. of Obs   |
|----------------------------------------------------------------------|-----------|-----------------------|--------------------|-----------------|--------------------|--------------|
| Next year                                                            | All 45.5  | 37.0                  | 54 7               | 71.4            | 63.7               | 1,05         |
| Total external debt in percent of GDP Iotal external debt to exports | 290       | 239                   | 359.               | 455.            | 350.               | 1.05         |
| Short-term extemal debt (OM in percent of GDP                        | 7.2       | 6.1                   | 9.5                | 10.6            | 8.0                | 1.01         |
| Short-terz extemnal debt (OM to reserves)                            | 11        | 0.8                   | 1.9                | 2.1             | 1.0                | 1.01         |
| Short-termn extemal debt (RM in percent of GDP                       | 10.9      | 9.4                   |                    |                 |                    | 993          |
| Short-term extemnal debt (RM to reserves)                            | 1.7       | 1.2                   | 2.9                | 2.9             | 2.2                | 948          |
| Interest on short-term extemnal debt in percent of                   | 0.5       | 0.5                   | 0.8                | 0.6             |                    | 754          |
| Interest on shot-term extemnal debt to reserves                      | 0.1       | 0.1                   | 0.2                | 0.1             | 0.1                | 754          |
| Debt service on short-term extemal debt in percent of GDP            | 5.3       | 4.8                   | 6.9                | 6.4             | 71                 | 1.05         |
| Debt service on short-tern extemal debt to reserves                  | 0.8       | 0.7                   | 1.5                | 1.2             | 0.9                | 1.05         |
| Public external debt in percent of GDP                               | 32.2      | 25.5                  | 36.4               | 53.0            | 46.5               | 1.05         |
| Public external debt to revenue                                      | 1.7       | 1.3                   | 1.9                | 3.0             | 2.3                | 827          |
| of GDP                                                               | 47.5      | 46.4                  | 38.2               | 57.3            | 54.0               | 462          |
| Central government debt in percent of GDP                            | 51.7      | 50.4                  | 28.4               | 75.5            | 51.6               | 305          |
| Augmcnted Consolidated central government dcbt in percent of GDP     | 50 7      | 47.8                  | 41.5               | 67.7            | 54.8               | 591          |
| Overvaluation                                                        | 0.0       |                       | 0.0                |                 | 0.0                | 799          |
| Curent account balance in percent of GDP                             |           |                       |                    |                 |                    | 1.23         |
| Reserves grouth                                                      | 19.1      | 20.8                  |                    | 17.8            | 22.9               | 115          |
| Export gronth                                                        | 12.0      | 13.8                  | 4.9                | 6.4             |                    | 127          |
| M to reserves                                                        | 5.6       | 5.3                   | 7.9                | 6.2             | 6.2                |              |
| Financing requirement to rescrves                                    | 1.6       | 1.3                   | 3.0                | 2.4             | 1.4                | 986          |
| External resource gap in percent of GDP                              |           |                       |                    | 1.3             | 2.9                |              |
| Trade balance in percent of GDP                                      | "3.7      | 44.0                  | "2                 |                 |                    | 127          |
| LBOR                                                                 | 9.7       | 9.5                   | 10.5               | 10.5            | 9.4                | 1.22         |
| U.S. treasuy bill rate                                               | 6.4       | 6.3                   | 78                 | 6.9             | 6.3                | 122          |
| Inflation (year-on-year , in percent)                                | 546       | 175                   | 241                | 169             | 84.9               | 1.27         |
| Unemployment rate                                                    | 9.7       | 9.0                   |                    | 10.9            | 11.6               | 740          |
| Nominal GDP growth                                                   | 55.9      | 22.8                  | 249.               | 148-            | 96.0               | 127          |
| Real GDP growth                                                      | 4.1       | 4.8                   |                    | 2.1             | 2.2                | 1.27         |
| REER growth                                                          | 121       | 124                   | 139                | 111.            |                    | 937          |
| Impont growth                                                        | 10.0      | 12.3                  | 5.3                | 4.8             | 6.9                | 902          |
| FDI in percent of GDP                                                | 1.7       | 1.9                   | 1.1                | L.0             | 1.5                | 1,02 983     |
| FDI gouth Openness                                                   | 28.0 71.2 | 26.3 71.3             | 52.6               | 22.6 72.1       | 53.6 72.5          | 903          |
| Overall balauce iu perceut Of GDP                                    |           |                       | 64.1 "6.3          |                 |                    | 1,01         |
|                                                                      | 0.6       |                       |                    | 2.0             | 15                 | 616          |
| Primary balance in percent of GDP Primary gap                        | 6.6       | 0.3 5.7               | 23.1               | 59.0            | 415.0              | 122          |
| Revenue in percent of GDP                                            | 24.3      | 25.4                  | 22.7               | 20.1            | 24.2               | 1.01         |
| Iax revenue in perceut of total                                      | 82.5      | 82.2                  | 85.                | 82.7            | 83.5               | 819          |
| Intemational trade revenue in pcrcent of total                       | 13.7      | 13.7                  | 12.1               | 14.7            | 11.3               | 814          |
| Nontax revenue in percent of total                                   | 15.0      | 15.0                  |                    | 15.4            | 14.8               | 822          |
| Giants in percent of total                                           |           | 3.0                   | 0.7                | 1.4             | 2.1                | 522          |
| Expenditure in percent of GDP                                        | 28.6      | 29.7                  | 29.0               | 23.9            | 28.3               | 1.01         |
| Interest expenditure in percent of total                             |           | 9.8                   | 11.0               | 15.4            | 15.1               | 799          |
|                                                                      | 23,4      | 22.8                  | 23.9               | 25.9            | 23.3               |              |
| Wages in percent of total                                            | 6.5       | 6.1                   | 5.4                | 8.5             | 6.0                | 713 625      |
| Health expenditure in percent of total                               |           |                       |                    |                 |                    | 663          |
| Social expenditure in percent of total                               | 17.5      | 171                   | 19,4               | 17.8            | 22.2               |              |

Sources: IMF: Standard & Poor's; World Bank; and authors' calculations .

--- Page 13 ---

C. Event Study Analysis

Event study analysis is a simple gaphical approach tat can provide somne insights as to how variables behave around the time of an event, such as a sovereign debt crisis. Ihe figures show as a broken horizontal line the sample average of a panticular variable for all noncrisis episodes (ie. those episodes that fall outside a window starting three years before crisis entry and ending three years after crisis exit). Tle solid bold line depicts the average of the particular variable in the three years preceding crisis entry (exit), the crisis entry (exit) year; and the three years following the crisis (exit). The two broken lines give the 95 percent confidence interval around the crises obsenvations . If the solid horizontal line depicting the noncrisis cpisodes is outside the 95 percent confidence intezval, the respective variable belaves significantly different during tlue To focus ideas, we discuss ouly the more interesting variables in our dataset . enty . event.

The event study figures show a worsening debt situation and adverse external and domestic developments in the years before into crisis (Figures 1 through 4). Developments around exit fromn crisis are more diverse.

We eliminate overlapping entry (exit) windows by dropping entries (exits that occur within country exits from crisis immediately after entering, and then enters another crisis in the following year .

We generate the event study figures through regression of the respective variable on a set of seven dummies for the three years preceding crisis entiy (exit) the crisis entiy (exit) year itself, aud the thuree years follow crisis eutry (exit) . Tle estimnated constant is the mnean of all nondefault episodes, depicted as the broken horizontal line. The estimated coefficients on the dummies give the difference from the nondefault episode mean to the respective event (crisis OI exit) . Hence; the mean for the respective event episode is calculated by adding the estimated constant and the estimated coefficient on the dummy. Tle confidence interval that indicates whether the means of the event is significantly different from the noncrisis means is calculated fromn the confidence interval around the estimated event episode dummies , by adding the lower and upper bound of the confidence interval to the estimated constant. This is a simple graphical representation of the test whether the coefficients on the episodes are significantly different from the noncrisis mean ing entry

We show event study charts based on data because it lends itself to easy interpretation Alternatively, standardized data can be used which eliminates the effect of outliers or different levels across counties. Charts based on standardized data show the same tends as those presented here and are available upon request.

--- Page 14 ---

Figure 1. Event Study Analysis: Short-Tem Debt Variables 1/

Short-term extemnal debt on original maturity basis to reserves

Short-term external debt on remaining maturity basis to reserves

Interest on shont-term external debt on original matuity basis to Ieserves

Sources: IMF: Standard & Poor's; World Bank: and authors calculations 1/ Bold broken line: average of observations outside a +/- 3 year intenval around default episodes; bold solid line: average of observations for the years falling in the +/- 3 years interval around default entry (exit): broken lines around bold solid line: 95 percent confidence interval.

--- Page 15 ---

Figure 2 Event Study Analysis: Total Debt; Public Debt, and Debt-Service Variables 1/

Sources: IMF: Standard & Poor's; World Bank: and authors calculations line: average of observations for the years falling in the +/- 3 years interval around default entry (exit): broken

--- Page 16 ---

Figure 3 . Event Study Analysis: Balance of Payments Variables 1/

Change innational curency per USD

External financing requirement to reserves

Total reserves growth (in percent)

Curent account balance in percent of GDP

Sources: IMF: Standard & Poor's; World Bank; and authors calculations .

lines around bold solid line: 95 percent confidence interval.

1/ Bold broken line: average of observations outside a +/- 3 year interval around default episodes; bold solid line: average of observations for the years falling in the +/- 3 years interval around default entry (exit); broken

--- Page 17 ---

Figure 4. Event Study Analysis: Selected Macrovariables 1/

Real GDP growth (in percent)

Sources: IMF: Standard & Poor's; World Bank; and authors calculations 1/ Bold broken line: average of observations outside a +/- 3 year interval around default episodes: bold solid line: average of observations for the years lines around bold solid line: 95 percent confidence interval. falling

--- Page 18 ---

- The total extemnal debt as well as the public extemnal debt-to-GDP ratio increase in the uoucrisis episodes in the year before entry . In the year of exit from crisis; there is a peculiar spike In general , both total and public external debt remain noticeably higher in crisis countries even after exiting from crisis compared to noncrisis cpisodes. In tens of dynamics; public external debt appears to be the driving force behind the developments of the total extenal debt-to-GDP atio.
- Short-tenmn extemnal debt relative to reserves also increases in the run-up to an entry into debt crisis and is significantly higher tan in noncrisis episodes in the year before remnaining mnatunity basis. After entering into crisis; short-term debt falls to the level of noncrisis episodes, possibly reflecting difficulties defaulters face in bonrowing externally and/or the conversion of short-ten debt into longer debt in restucturing episodes. At the time of exit from crisis; shont-term debt relative to reserves remains around the level observed in noncrisis episodes .
- Debt service on external debt relative to reserves and interest on short-term external debt relative to reserves are higher than in noncrisis episodes in the year before entry into crisis. Both indicators fall to the level of noncrisis episodes after exit from crisis. could reflect resumption 0f payments close to the timne the default episode is resolved:
- On the extemnal side, the cunrent account deficit is larger before entry into crisis than in noncrisis episodes, and reserves growth plummets in the year before entry. As the of the cunent account deficit and short-term debt, the extemnal financing requirement relative to reseives is significantly higher in the year before eutry into crisis than in noncrisis episodes. At the time of exit from crisis, these indicators fall back to levels obseived during noncrisis episodes, with reserves growth spiking in the first year after exit. The exchange rate shows a depreciation the US. dollar in the year of entry into crisis (as many debt crises are associated with year of exit from crisis . For entry, this depreciation contributes to the increase in total extemnal debt relative to GDP large against
- Domestic developments arc adverse before crisis cntry and show a retun to normal afier exit. Real GDP growth is below that observed in noucrisis episodes and plummets in the year , pointing t0 the real costs of debt crisis for the economyWith inflation substantially in the entry year; nominal GDP growth also jumps up: The dramatic swings in the inflation rate and the slow stabilization in the three years after exit from a crisis to the domestic imbalances associated with external debt crises. Interestingly; the overall budget balance in the Iun-up to crisis does not differ significantly from noncrisis episodes, though there seems to be a modest improvement in the overall balance before exit from crisis entry rising point

--- Page 19 ---

IV.

A. Estimation Approach

We cmploy a modified gencral-to-specific modeling approach to identify an EWS for sovereign debt crisis. Variables are selected into the final mnodel on the basis of staudard specification criteria and, in addition; their ability to predict entry into crisis and in ctisis. In cases of crisis episodes that are longer than one year, entry into crisis relates to the first year of the episode, and remaining years until exit from crisis. The estimation technique used is the logit approach. We allow the regressors to have a different impact on the probability of entering into cisis and exiting frou cisis, as it is a not clear that the two should be identical The remainder of this section discusses the (technical) details of our estimation approach. being being piori

The modified general-to-specific approach allows us to test a large number of potential some 50 variables that differ substantially in availability. While our mnaximumn sample contains 1,276 observations , a joint sample for all potential regressor would muster only around 100 observations . Therefore; we proceed along a three-stage strategy. For this strategy; we divide the variables into six groups: extemal debt variables; public debt variables; variables from the IMF cunency crisis EWS; other macroeconomic variables: 10 fiscal variables; and political economy variables.

- At the first stage, we mun individual regressions for each variable to some insight as to how well each variable perfoms with respect to standard criteria and how well it predicts entry into crisis as well as in crisis. Given that our objective is to build an EWS for sovereign debt crisis; we place particular weight onhow well a variable is able to predict entry into crisis. An estimated model is defined to predict into crisis Or in crisis, if the estimated probability exceeds the naive; in11 sample probability ofbeing in crisis of 20.5 percent. gain bcing being entry
- At the second stage, we select the ~best performers within each group and run group horse-races"  between similar variables, for example shont-term debt in percent of GDP versus in relation to reserves . By best perfommers' we mnean variables that tumn out significant in the individual regressions andor have a high predictive power for crisis entiy as well as for in crisis. These groupwise regressions help us to futher narow down the variables to be included in th1e general model with variables from all other groups. As at the first stage, we select and variables based on standard tests and their predictive power. Ihis second stage is only employed for groups with several promising variables . bcing drop

10 The classification is somewhat arbitrary but has no impact on the outcome of the specification process.

11 Other possible cut-off value would for example, be 50 percent or the in-sample probability of entering into crisis; 5.6 percent.

--- Page 20 ---

- At the third stage, we combine the best performers from each group into a 'general? model. This general model is tested down by excluding those variables that are either

The model is estimated the logit approach. Compared to the probit approach; the logit typically perfoms better when the dependent variable is not evenly distributed between the two outcomes; in our data, only 20.5 percent of all outcomes are debt crisis and only 5.6 percent are crisis entries: We use a robust variance estimator (Huber White sandwich estimnator) witl country-specific vaiances. using

The estimation approach allows for different coefficients between entering crisis and exiting from crisis . A priori; it is not clear that a change say extemal debt, that triggers a crisis is necessarily the same as the change that would help a country exit from crisis Therefore; we estimate separate cocfficients for entering into crisis and for exiting from crisis year t is given by in, again.

<!-- formula-not-decoded -->

where denotes the vector of explanatory variables in the previous period, including the 12 constant. The coefficient on the first argument describes the relationship between the explanatory variable and the probability of entering into crisis in t, given that the country was the explanatory variable and the probability of in crisis (i.e not exiting from crisis) in t, given that the country was in crisis in t-1 _ This setup is equivalent to estimating separate models for entering into and exiting from crisis. However; it allows to formally test for coefficients for entering and exiting X;being equal logit model, if a variable that is part of the true model is omitted from the estimated model the estimated parameter of the included regressor is a linear combination of the parameter of that regressor and the parameter of the omitted variable. Unlike in the least squares case, this bias is present whether the included and the omitted regressor are coirelated or not. Hence; the estimnated coefficients in our vaiable by vaiable regressions are potentially biased (first

- First; the included variable is not of the true model but the estimated coefficient reflects the influence of omitted variables that are ofthe tiue model. In this case, variable that is not of the true mnodel could be eironeously retained. However the erroneously retained variable shonld out of the regression when the general model is estimated which should hopefully include most variables from the true model part part drop

12 By lagging the regressors one petiod, we also avoid a possible endogeneity bias .

--- Page 21 ---

- Second and more problematic, the bias could lead to the estimated coefficient of a variable that is of the tuue model to be zero. This may lead us to exclude a of our seusitivity analysis; wve include regressors that dropped out in the specification process into our final specification to see whether improve the modeL. part part they

B. Specifying the Logit EWS

We specify the logit EWS only for a subsample of cpisodes starting in o after 1990. Initial estimnation results indicated that a model specified for the whole sample starting in the seventies would not be very successfil in explaining debt crises of the nineties and beyond, 13 though it is successful at explaining debt crises in the seventies and eighties . Hence, we restrict ou sample to the years 1990 and onward for the process of identifying those variables that should be included in the logit EWS. We then estimate this specification for all years witl dala availability in ou sample, allowing for different coefficients for crises occuring as of 1990. This way; we can derive a model that predicts well the more recent episodes (and, thus, hopefully future episodes) while still using as much infomation from past episodes as possible.

Based on variable-by-variable and groupwise regressions; we include the following variables 14 in a

- From the list of extemnal debt variables, short-term extemnal debt to reserves on an original maturity; as well as on a remaining maturity basis; interest on short-term debt in percent of GDP and external debt service to resenves appear as best suited to explain crisis episodes in the 1990 onward sample. For the funther specification process; we also include total extemal debt in percent of GDP as a possible explanatory variable because this variable played an important role in related empirical work and is of theoretical interest as a measure of solvency.
- From the list of public debt variables, no indicator is significant at the 5 percent level; onward sample therefore, do not include any of these variables in the direct specification process. As a sensitivity test, we included public extemnal debt in the final specification but it did not improve the model consistent with the findings here. We,
- In addition, we also include the curent account balance in the general model
- From the list of other macroeconomic variables ; the U.S. treasuy bill rate, real GDP growth; FDIin percent of GDP , trade openness, and the financing requirement

13 A model

14 The results for the variable-by-variable regressions and the groupwise regressions are available from the authors upon request.

--- Page 22 ---

15 basis help explain and predict sovereign crisis episodes. In addition; inflation volatility measured as a 4-year moving average of the coefficient of variation is included in the 'general' mnodel

- From the list of fiscal variables; no indicator helps predict sovereign crisis episodes. We therefore did not include any fiscal variable in the general model.  However; as a sensitivity test; we included the overall balance in the preferred specification without achieving au improvement in performance.
- None of the political economy variables came out well in the variable-by-variable regressions. Suspecting some influence, ifmarginal we included the dumnmy for years with presidential election and an index of freedom status in the general model that appeared promising in initial estimations.

Based on the information from the variable-by-variable and groupwise analysis , we noW combine those variables that appear to help predict debt crises in a general model. We estimate this general model for a subsample that includes only the years 1990 and onward because initial experiments have shown that the more recent crisis episodes appear to differ from those of the seventies and eighties. We exclude insignificant variables and variables with a counter-intuitive dinection of influence from thuis general model to anive at a reduced model (Table 3 and Table 4) This reduced model is reestimated for the fill sample including observations from the seventies and eighties. For this, we allow the estimnated coefficients to differ for observations starting in or after 1990. Further excluding insignificant variables from the specification and testing whether the coefficient on certain regressors is equal for observations before or after 1990 yields the final specification; which we call the logit EWS (Table 5 and Table 6)

The logit EWS is estimated based on a sample of 594 observations for 37 market access variables included. The countries covered by this sample are listed in Table 6. into and being in crisis is explained by indicators ofexternal debt, mnacroeconomic conditions; and political economy factors. Entry

- Solvency problems make entering into crisis more likely. A high total extemnal debt to-GDP ratio is associated with a high probability of entering into crisis. This effect is pronounced in the 1990 onward period. However, the total extemnal debtto-GDP ratio not help explain remaining in crisis in the logit EWS. does

15 maturity basis and accounting for FDI flows. This definition is available only for a smaller number of obsenvations and did not lead to improved results .

--- Page 23 ---

Table 3. Regression Results: Cocfficient Estimates, 1990 Onward Sample 1/ (Dependent Variable: Generalized Standard & s Defanlt Indicator)

|                                                | Geueral Model      | Geueral Model   | Geueral Model   | Reduced Model   | Reduced Model   | Reduced Model   |
|------------------------------------------------|--------------------|-----------------|-----------------|-----------------|-----------------|-----------------|
|                                                | Marginal Effect 2/ | Logit Coef.     | z-value         | Marginal        | Logit Coef.     | z-value         |
| Total external debt in percent of GDP          |                    |                 |                 |                 |                 |                 |
| Entry into default                             | 0.002              | 0.065           | 2.730           | 0.002           | 0.054           | 3.240           |
| Exit from default                              | 0.000              | 0.013           | 1.010           |                 |                 |                 |
| Short-term debt; original matuity to reserves  |                    |                 |                 |                 |                 |                 |
| Entry into defanlt                             | -0.093             | -2.700          |                 |                 |                 |                 |
| Exit foiu default                              | 0.054              | 1.566           | 1.590           |                 |                 |                 |
| Short-term dcbt, rcmaining matuity to rcscives |                    |                 |                 | 0.008           | 0.268           | 2.170           |
| into default Entry                             | 0.000              | 0.003           | 0.010           |                 |                 |                 |
| Exit from default                              | 0.013              | -0.388          |                 |                 |                 |                 |
| Interest on short-tenu debt in percent of GDP  |                    |                 |                 |                 |                 |                 |
| Entry into default                             | 0.224              | 6.493           | 2.390           | 0.144           | 4.617           | 2.270           |
| Exit from default                              | 0.101              | -2.919          | -2.190          |                 |                 |                 |
| Extemnal debt service to reserves              |                    |                 |                 |                 |                 |                 |
| Entry into default                             | 0.051              | 1.486           | 1.880           | 0.032           | 1.038           |                 |
| Exit from default                              | 0.019              | 0.555           | 0.640           |                 |                 |                 |
| Cuurent account balance in percent of GDP      |                    |                 |                 |                 |                 |                 |
| Entry into default                             | -0.002             | 0.047           | -0.340          | 0.005           | -0.156          | -1.900          |
| Exit fiom dcfault                              | 0.002              |                 | -0.770          |                 |                 |                 |
| Reserves growth                                |                    |                 |                 |                 |                 |                 |
| Entry into default                             | 0.000              | -0.013          | -0.560          |                 |                 |                 |
| Exit foiu default                              | 0.000              | 0.000           | 0.150           |                 |                 |                 |
| US. treasury bill rate                         |                    |                 |                 |                 |                 |                 |
| Entry into default                             | 0.009              | 0.270           | 1.120           | 0.006           | 0.185           | 0.740           |
| Exit fom default                               | 0.001              | 0.043           | 0.240           |                 |                 |                 |
| Real GDP growth                                |                    |                 |                 |                 |                 |                 |
| Entry into default                             | -0.001             | ~0.032          | 0.440           | ~0.004          | -0.142          |                 |
| Exit from default                              | 0.000              | 0.009           | 0.100           |                 |                 |                 |
| FDI in percent of GDP                          |                    |                 |                 |                 |                 |                 |
| Entry into default                             | 0.004              | 0.119           | 0.550           |                 |                 |                 |
| Exit from default                              | 0.000              | -0.005          | -0.030          |                 |                 |                 |
| Openness                                       |                    |                 |                 |                 |                 |                 |
| Entry into default                             | -0.002             | -0.053          | -2.090          | 0.001           | -0.045          | -2.200          |
| Exit from dcfault                              | 0.000              | 0.004           | 0.540           |                 |                 |                 |
| Financing requirement to reserves              |                    |                 |                 |                 |                 |                 |
| Entry into defanlt                             | 0.050              | 1.444           | 1.310           |                 |                 |                 |
|                                                | 0.012              | 0.349           | 0.520           |                 |                 |                 |
| Inflation volatility                           | 0.000              | 0.001           | 1.920           | 0.000           | 0.001           | 1590            |
| Dummy for high inflation (>50 percent)         | 0.192              | 2.290           | 2.870           | 0.048           | 1.027           | 2.030           |
| Dummy for past default episodes                | 0.018              | 0.584           | 0.720           |                 |                 |                 |
| Year with presidential election                | 0.098              | 1.554           | 2.700           | 0.103           | 1.692           | 2.530           |
| Index of freedom status                        |                    |                 |                 | -0.025          | -0.790          | -2.070          |
| Entry into default                             | -0.021             | -0.620          |                 |                 |                 |                 |
| Exit fom default                               | 0.062              | -1.787          |                 |                 |                 |                 |
| Laggcd crisis indicator                        | 0.938              | 8.326           | 2.520           | 0.899           | 7.709           | 3.220           |
| Constant                                       |                    | -8.440          | -3.330          |                 | -6.753          | -2.710          |

Souces: IMF: Standard & Poor' s: World Bank: and authors' calculations_

2/ Marginal effects calculated at means. For dummy variables, marginal effects calculated for switch from zero to one. sample

1/ Logit regression witl robust variance estimates, allowing for country-specific variances (Huber White sandwich estimator) . z-valucs arc normally distributed

--- Page 24 ---

Table 4. Regression Results: Model Performance. 1990 Onward Samvle 1/ (Dependent Variable: Generalized Standard & Poor's Default Indicator)

|                                         | General Model                                                                                                                                                                                                                                                                       | Reduced Model                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Observations                            | 353                                                                                                                                                                                                                                                                                 | 353                                                                                                                                                                                                                                                                                                                       |
| Wald-test for joint significance        | Chi(31) = 273,189                                                                                                                                                                                                                                                                   | Chi(13) = 758                                                                                                                                                                                                                                                                                                             |
| Pseudo-R2                               | 0.66                                                                                                                                                                                                                                                                                | 0.60                                                                                                                                                                                                                                                                                                                      |
| Correctly called episodes               | 89.8                                                                                                                                                                                                                                                                                | 88.1                                                                                                                                                                                                                                                                                                                      |
| Coirectly called entries into default   | 69.2                                                                                                                                                                                                                                                                                | 69.2                                                                                                                                                                                                                                                                                                                      |
| Inconrectly called entries into default | 4.5                                                                                                                                                                                                                                                                                 | 5.3                                                                                                                                                                                                                                                                                                                       |
| Conrectly called exits from default     | 16.0                                                                                                                                                                                                                                                                                | 0.0                                                                                                                                                                                                                                                                                                                       |
| Incoirectly called exits from default   | 0.0                                                                                                                                                                                                                                                                                 | 0.0                                                                                                                                                                                                                                                                                                                       |
| Wald test reduced vs. general model     |                                                                                                                                                                                                                                                                                     | Chi2(18) = 24.5                                                                                                                                                                                                                                                                                                           |
| Debt-crisis entries conrectly predicted |                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                           |
| Nunber                                  |                                                                                                                                                                                                                                                                                     | 10                                                                                                                                                                                                                                                                                                                        |
| Debt-crisis entries                     | Argentina 2001; Brazil 1998,2001; Ecuador 1999; Mexico 1995; Pakistan 1998; Thailand 1997; Turkey 2000: Venezuela 1990                                                                                                                                                              | Argentina 2001; Brazil 1998; Ecuador 1999; Indonesia 1997; Mexico 1995; Pakistan 1998: Thailand 1997: Turkey 2000: Veuezuela 1990                                                                                                                                                                                         |
| Debt-crisis entries not predicted       |                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                           |
| Nuber                                   |                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                           |
| Debt-cisis entries                      | Argentina 1995; Indonesia 1997; Tunisia 1991; Venezela 1995                                                                                                                                                                                                                         | Argentina 1995; Brazil 2001: Tunisia 1991; Venezela 1995                                                                                                                                                                                                                                                                  |
| Countries included in regressions       |                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                           |
| Nunber                                  | 37                                                                                                                                                                                                                                                                                  | 37                                                                                                                                                                                                                                                                                                                        |
| Countries                               | Algeria; Argentina, Brazil, Chile, China, Colombia, Costa Rica, Dominican Indonesia; Kazakhstan; Latvia, Lithuania, Malaysia; Mexico, Morocco. Oman, Pakistan. Panama Slovak Republic, South Africa; Thailand. Trinidad and Tobago; Tuisia, Turkey, Ukraine; Uruguay, Vcnczucla Rep | Algeria; Argentina, Brazil, Chile, China, Colombia; Costa Rica, Dominican Ecuador, Egypt, India. Indonesia. Kazakhstan, Latvia; Lithuania; Malaysia; Mexico, Morocco; Oman; Pakistan Panama Peru Philippines; Poland  Romania Slovak Republic, South Afiica, Thailand Trinidad and Tobago, Tunisia; Turkey, Ukraine, Rep. |

--- Page 25 ---

Table 5. Regression Results: Coefficient Estimnates ; Full Sample 1/

(Dependent Wariable: Generalized Standard & Poor's Default Indicator)

|                                                | Reduced Model      | Reduced Model   | Reduced Model   | Logit EWS          | Logit EWS   | Logit EWS   |
|------------------------------------------------|--------------------|-----------------|-----------------|--------------------|-------------|-------------|
|                                                | Marginal Effect 2/ | Logit Coef      | Z-value         | Marginal Effect 2/ | Logit Cof   |             |
| Total external debt 1n percent of GDP          |                    |                 |                 |                    |             |             |
| Enty into default                              | 000o               | 0,003           | 0.190           |                    |             |             |
| duumy for 1990 onward                          | 0.004              | 0,047           | 2.270           | 0.004              | 0.052       | 3.330       |
| Short-term debt, remaining matuity to reserves | 0.033              | 0,400           | 1.260           | 0.035              | 0.407       | 3.180       |
| dummy for 1990 onward                          | 0.011              | -0.133          | -0.390          |                    |             |             |
| Iuterest ou shont-tenu debt in percent of GDP  |                    |                 |                 |                    |             |             |
| into default                                   | 0.040              | 0,486           | 0.930           |                    |             |             |
| dumny 1990 onward for                          | 0.331              | 4.054           | 1.970           | 0.404              | 4.710       | 2.540       |
| External debt service to reserves              |                    |                 |                 |                    |             |             |
| into default Enty                              | 0.042              | 0.511           | 0.830           | 0.048              | 0.557       | 1.670       |
| duuy for 1990 ouward                           | 0.038              | 0,461           | 0.550           |                    |             |             |
| Cunent account balance iu percent of GDP       |                    |                 |                 |                    |             |             |
| into default                                   | -0.009             | -0.106          | 41.200          |                    |             | 41.910      |
| duny for 1990 ouward                           |                    |                 | -0.320          |                    |             |             |
| Openness                                       |                    |                 |                 |                    |             |             |
| Enty into default                              | 0.001              |                 |                 |                    |             |             |
| dumy for 1990 onward                           |                    |                 | -1.370          |                    | -0.044      | "2410       |
| US. treasuy bill rate                          |                    |                 |                 |                    |             |             |
| into detault Enty                              | 0.008              | 0.099           | 0.810           | 0.011              | 0.130       | 1.620       |
| duumy for 1990 onward                          | 0.002              | 0,022           | 0.130           |                    |             |             |
| Real GDP growth                                |                    |                 |                 |                    |             |             |
| into default Enty                              | 0.011              |                 | 41.530          | -0.011             | 0.124       |             |
| dummy for 1990 onward                          | 0.001              | -0.010          |                 |                    |             |             |
| Inflation volatility                           |                    | 0.015           | 0.640           | 0.00o              | 0.001       | 1890        |
| dumny for' 1990 onward                         | 0.001              | -0.014          | -0.600          |                    |             |             |
| Dumny for high inflation (>50 percent)         | 0.034              | 0.371           | 0.710           | 0.089              | 0.821       | 1.660       |
| duny for 1990 onward                           | 0.063              | 0.620           | 1.000           |                    |             |             |
| Year with presidential election                | 0.383              |                 | 2,430           | 0.273              | 1.834       | 3.440       |
| dumy for 1990 onward                           | 0.047              |                 | 0.640           |                    |             |             |
| Index of freedom status                        | 0.089              | 1.088           | 2.090           | 0.089              | 1.038       | 2180        |
| dumny for 1990 onward                          | 0.155              |                 |                 | 0.160              | -1.862      | 3.610       |
| Lagged crisis indicator                        | 0.793              | 5,469           | 5.180           | 0.836              | 5.817       | 5.720       |
| dunny for 1990 onward                          | 0.183              | 1.484           | 1.520           | 0.128              | 1.100       | 1.110       |
| Coustant                                       |                    |                 | "4.280          |                    | -6.150      |             |

Sources: IMF Standard & Poor s: World Bank: and authors' calculations.

1/ Logit regression with robust variance estimates, allowing for country-specific variances (Huber White sandwich estimator) values are normally distributed

--- Page 26 ---

Iable 6. Regression Results: Model Performance; Full Sample 1/ (Dependent Variable: Genezalized Standard & Poor's Default Indicator)

|                                         | Reduced Model                                                                                                                                                                                                                                     | Logit EWS                                                                                                                                                                                                                                          |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Observations                            | 594                                                                                                                                                                                                                                               | 594                                                                                                                                                                                                                                                |
| Wald-test for joint significance        | Chi(26) = 3,350                                                                                                                                                                                                                                   | Chi(15) 431                                                                                                                                                                                                                                        |
| Pseudo-R2                               | 0.63                                                                                                                                                                                                                                              | 0.63                                                                                                                                                                                                                                               |
| Conrectly callcd cpisodes               | 88.9                                                                                                                                                                                                                                              | 89.4                                                                                                                                                                                                                                               |
| Conrectly called cntrics into dcfault   | 74.2                                                                                                                                                                                                                                              | 74.2                                                                                                                                                                                                                                               |
| Inconrectly called entries into default | 6.9                                                                                                                                                                                                                                               | 6.1                                                                                                                                                                                                                                                |
| Corectly called exits default           | 0.0                                                                                                                                                                                                                                               | 0.0                                                                                                                                                                                                                                                |
| Inconectly called exits frou default    | 0.0                                                                                                                                                                                                                                               | 0.0                                                                                                                                                                                                                                                |
| Wald test logit EWS vs. reduced model   |                                                                                                                                                                                                                                                   | Chi(1 1) 3.8                                                                                                                                                                                                                                       |
| Debt-ctisis entries correctly predicted |                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                    |
| Nunber                                  | 23                                                                                                                                                                                                                                                | 23                                                                                                                                                                                                                                                 |
| Debt-cisis entries                      | Argentina 1982, 2001: Brazil 1983 , 1998: Chile 1983: Costa Rica 1981; Dominican Republic 1981; Ecuador 1982, 1999; Indonesia 1997; Mexico 1982, 1995; Morocco 1983 1986; Pakistan 1998; Peru 1983: Philippines 1983: Thailand 1997; Irinidad and | Argentina 1982, 2001: Brazil 1983, 1998; Chile 1983: Costa Rica 1981; Dominican Republic 1981: Ecuador 1982, 1999; Indonesia 1997; Mexico 1982, 1995; Morocco 1983 , 1986: Pakistan 1998; Peru 1983: Philippines 1983: Tlailand 1997; Trinidad aud |
| Debt-crisis entries not predicted       |                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                    |
| Nunber                                  | 8                                                                                                                                                                                                                                                 | 8                                                                                                                                                                                                                                                  |
| Dcbt-cisis cntrics                      | Argentina 1995; Brazil 2001; Egypt 1984; El Salvador 1981; Ihailand 1981; Tunisia 1991; Uruguay 1987; Venezuela 1995                                                                                                                              | Argcntina 1995; Brazil 2001: Egypt 1984: El Salvador 1981; Thailand 1981; Tunisia 1991; Unguay 1987; Venezuela 1995                                                                                                                                |
| Nunber Countries                        | Algeria; Argentina; Brazil, Chile; China; Colombia; Costa Rica, Dominican Ecuador; Egypt El Salvador; Estonia, Hungary, India; Indonesia Rep.                                                                                                     | Algeria, Argentina, Brazil, Chile, China; Colombia, Costa Rica; Dominican Ecuador, Egypt, El Salvador; Estonia; Hungary; India, Indonesia, Kazakhstan, Latvia                                                                                      |
| Nunber Countries                        | Pen Philippines, Poland, Romania Slovak Republic , South Africa,                                                                                                                                                                                  | Peru Philippines; Poland, Romania Slovak Republic; South Afiica,                                                                                                                                                                                   |
| Nunber Countries                        | Thailand, Trinidad and Tobago, Tunisia; Turkey; Ukraine; Urguay ,                                                                                                                                                                                 | Thailand Irinidad and Tobago, Tunisia; Turkey, Ulraine, Unuguay;                                                                                                                                                                                   |
| Nunber Countries                        | Venezuela                                                                                                                                                                                                                                         | Venezela                                                                                                                                                                                                                                           |
| Nunber Countries                        |                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                    |

Sources: IMF; Standard & Poor's; World Bank; and authors calculations

1/ Logit regression with robust variance estimates, allowing for country-specific variances (Huber White sandwich estimator).

--- Page 27 ---

- Liquidity problems also make entering and remaining in crisis more likely . First, a high shoit-term debt on remaining maturity basis to reseives ratio is associated with a high probability of entering and remaining in crisis. This relationship is statistically identical for observations before and after 1990. Second, in the 1990 onward period. high interest payments in percent of GDP make entering into crisis more likely. Third, high extemal debt-service payments in relation to reserves make entering into crisis more likely; with this relationship statistically identical for observations before and after 1990. being
- Positive exteinal developments can reduce the probability of entering into cisis. Countries wither a high cunent account balance have a reduced probability of entering into crisis. This relationship is identical before and after 1990. From 1990 onward open reduces the probability of entering into crisis. Lastly; periods of tight international liquidity as proxied by the U.S. treasuy bill rate are associated with an increased probability of entering into crisis. While this relationship was particularly pronounced in the early eighties, it holds over the full sample period. being
- Positive domestic developments can also reduce the probability of enters and in crisis. High real GDP growth is associated with a reduced probability of entering into cisis. However; periods ofhigh inflation volatility (mneasured as the coefficient of variation of the inflation rate over the last four years) as well as periods ofhigh intlation (exceeding 50 percent) are associated with an increased probability of entering and remaining in crisis. These three links between domestic developments and the probability of crisis are identical before and after 1990. being ing
- Finally, political factors influence the probability of crisis. The probability of entering and remaining in crisis increases in years with presidential elections. In the period before 1990, countries with a better ranking on an index of political freedom appear to suffer fromn a raised probability of crisis. However; in the 1990 onward period, the effect is reversed and countries that rauk higher in tenns of political feedom have a reduced probability of crisis.

The logit EWS conrectly predicts 74 percent of all crisis entries across the whole sample while sending only 6 percent false alarms that are not followed by a crisis in the next year. For the period starting in 1990, the logit EWS corectly predicts 69 percent of all cisis entries and sends only 5 percent false alarus. It is interesting to look at the false alarmns in more detail. In 48 percent of all false alans; a debt cisis occurs two years after the signal was emitted rather than in the next year. If one were to consider these cases of false alaus as would drop to 3 percent. For the 1990 onward subsample, the share of false alarms that are followed by a debt crisis within two years is 38 percent . There are also some cases where a crisis that is not predicted in the year immediately preceding te entry is signaled two in advance Argentina , 1995; and Brazil, 2001). years (e.g,

Four crisis entries after 1990 are not anticipated by the logit EWS: Argentina (1995); Brazil (2001): Tunisia (1991); and Venezuela (1995).In the case of Argentina, a very

--- Page 28 ---

impontant factor leading to crisis in 1995, was the spillover effect from the Mexican crisis 1994/95 (the Tequila contagion effect). Since we do not include proxies for contagion effects in our model, it might not be suprising that the logit EWS does not anticipate this 16 episode. In Venezuela in 1995, the aftermath of a currency and banking crisis led to a short impending crisis but the crisis, at least for what concerns debt payments , was small. In Brazil 2001, the combination of a domestic energy shock; the U.S. economic slowdown and the worsening of the conditions in Argentina led to the need for a scale IMF package as a preventive way to avoid more serious debt-senvicing problems. But these shocks were largely unpredicted, of 2000, the year before the crisis. large

We probe the robustness of the logit results by nnning various sensitivity tests, for example with respect to outliers and the definition of the dependent variable; and find that the logit to 1995 only and then predict for the years 1995 and onwards. Out of sample; the logit EWS conrectly predicts 45 percent of the crisis entries while sending false alarms in 6 percent of the cases_ In addition to those crisis entries that were also missed in the in-sample prediction of the logit EWS (Argentina, 1995; Brazil 2001; and Venezuela, 1995), Indonesia and Thailand in 1997, as well as Argentina in 2001 are missed in the out of sample prediction. prior

THE TREE EWS

We use a statistical technique called Classification and Regression Tree (CART) analysis to identify possible (nonlinear) interactions between the potential variables that can help predict the probability of being in crisis. The resulting tree classifies observations into crisis-prone or not crisis-prone based on a few characteristics and their interactions . Information from the tee analysis is then integrated into the Teduced logit mnodel to test whether these interactious help improve the predictive power of our model

A Ihe Tree-Analysis Methodology

The CARI or tree analysis ~methodology produces a sequence of mules for predicting a binary outcome that can be illustrated in the fonm of a tree. These rules can also be viewed as mules of thumb that can help predict the outcome of a particular observation. soting

16 We do not include contagion effects because are difficult to implement in a forecasting environment. they

17 and UCSD (Ohlsen) and has been to several fields, including medicine; meteorology; advertising; and evaluation of credit default:. See Breiman et al. (1984) for a detailed description of CART,and Ghosh and Ghosh (2002) for an application in the field of economics. applied

--- Page 29 ---

CART is nonparametric and can detect complex relationships between dependent variable and explanatory variables . Therefore; CART is particularly suited for discovering nonlinear structures and variable interactions in datasets with a large number of potential explanatory variables. A rule is chosen to reduce the heterogeneity in the resulting groups compared to the larger group to which the 1ule is There can be a n nested rules that classify the observations into n+1 disjoint groups of obsevations. Observations in a particular group share characteristics according to the mles by which were classified applied. they

The following example in Figure 5 illustrates the procedure:. Suppose we have observations explanatory variables that refer to 100 episodes, of which 20 are defaults and 80 nondefaults: The 'unconditional" crisis probability in the sample (root node) 18 is 20 percent . wve sort half (50) observations to the right node 1 (those which satisfy the mule), and half observations to the left node (those with debt-GDP below 50 percent). In the "low debt' left the crisis probability conditional on the debt ratio below 50 percent) is only 10 percent noncrises . Here the conditional probability of a crisis rises to 30 (=15/50) percent . Nodes 2 and 3 are then determined by applying rule 2 to the observations in their parent node. The iule 2 sorts observations with inflation above 10 percent to the right (node 3, say 25 cases node found in the 'low intlation" left node 2, where the conditional crisis probability is 20 (=5/25) percent. We end up partitioning our sample into three terminal nodes: node 1 (low debt) with only 10 percent crisis probability; node 2 (high debt but low inflation) witl 20 percent crisis probability; and node 3 (high debt and high inflation) with 40 percent default probability . being

18 In this example we assume that the ex ante (prior) probability of a crisis coincides with the sample frequency.

--- Page 30 ---

Figure 5. Example of Tree Methodology

B Results from the Tree Analysis

The CART methodology selects the following nine variables from our dataset to partition 19 the sample into crisis episodes and noncrisis episodes (Figure 6 and Table 7): total exterual debt in percent of GDP shoit-ten debt on a remaining maturity basis to reserves; public extemnal debt to revenue; real growth; inflation; the U.S. treasury bill rate; exchange rate requirement to reserves; and the number of years before a branches: episodes with high extemnal debt (more than 49.7 percent of GDP) go to the right, here the conditional crisis probability rises fromn 20.5 percent in the entire to 45.4 percent; and episodes with low external debt to the left, wvith default probability of 9.7 percent . A number of interesting features emerge from the analysis: ing sample

19 Details of the tree specification process are available from the authors upon request.

--- Page 31 ---

1 2 1 2

--- Page 32 ---

Table 7 The Empirical Tree: Model Performance

|                                        | Full sample   | 199Os onwards   |
|----------------------------------------|---------------|-----------------|
| Observations                           | 1276          | 556             |
| Number of crisis episodes              | 261           | 114             |
| Number of crisis entry episodes        | 54            | 20              |
|                                        | (In percent)  | (In percent)    |
| Correctly called episodes              | 82.8          | 78.8            |
| Conrectly called entries into default  | 88.9          | 85.0            |
| Inconrcctly called cntics into dcfault | 18.5          | 15.0            |
| Correctly callcd cxits from dcfault    | 32.0          | 35.3            |
| Inconectly called exits from default   | 4.8           | 64.7            |
| Conrectly called default episodes      | 93.9          | 89.5            |
| Coirectly callednondefault episodes    | 79.9          | 76.0            |

Sources: IMF: Standard & Poor's: World Bank: and authors calculations

- Episodes of high debt (more than 49.7 percent of GDP) and high inflation (larger than 10.5 percent) incur the largest default risk, 66.8 percent, see terminal node 14 Notice that more than half of all the crisis episodes in the sample satisfy these twvo simple conditions .
- By contrast; the circumstance that are more favorable for reducing the risk ofbeing in cisis episode are low extemnal debt, low shont-termn debt to reserves on a remnaining maturity basis (below 1.3) and low public extemnal debt to revenue (below 2.1), coupled with high economic growth see terminal node 3. Under these circumstances the likelihood of in a crisis episode is just 2.3 percent. About 58.4 percent of all noncrisis episodes satisfy these conditions . being
- Low extemnal debt is not sufficient for eliminating the risk of default, however. Countries characterized by an intemmediate ratio of external debt (between 19 percent and 49.7 percent of GDP), but who have potentially serious liquidity problems (shoit term debt above 1.3 times reserves) , face political uncentainty (presidential elections closer than 5.5 years) , and possibly also have a history ofpegged exchange Iates (low moving average of past coefficient of variation of the exchange rate), also face a large 20 default risk (41.5 percent, see terminal node 7). In paticular; a stock ofpublic large

20 Crises in this node include Argentina; Brazil; Dominican Republic; El Salvador; India; Jamaica; Korea; Mexico; Pakistan; Pen; South Afiica; Trinidad and Tobago; Turkey; Ukraine; and Uuguay.

--- Page 33 ---

external debt relative to revenue, coupled with high inflation (see terminal node 5), raises the conditional crisis probability considerably (to 55 percent), even when the external debt-to-GDP ratio and shont-term debt are low

- Low extemnal debt is not a necessary condition for averting debt crises. Despite having external debt in excess of 49.7 percent of GDP , countries may not incur a cousiderable 1isk of crisis provided that inflation is below 10.5 percent, the extemal financing requirement to resexves ratio does not exceed 1.5, and the public debt to

Based on the set of mules of this tree, obsenvations can be classified as crisis-prone OL not crisis-prone. Obsenvations in a particular node are classified as crisis-prone (not crisis-prone) if the within node share of crisis observations is higher (lower) than a tlureshold. This threshold is a function of the share of crisis observations in the full sample of 20.5 percent and a cost parameter which is set for estimating the tree and determines the relative cost of missing a default episode versus missing a nondefault episode in the objective function 21 underlying the tree algorithu comes at the cost of sending 19 percent of false alams in years that are not followed by a crisis entry. Similarly to the EWS logit model, however; around 14 percent of these 'false' alars are 'early" alarms; so that the share of false alans would fall to 16 percent when counting signals two years in advance as early indications. The tree is also able to correctly predicts 32 percent of crisis exits. The predictive perfommance is only slightly worse when th1e focusing only on the 1990 onward period with 85 percent of all crisis entries conrectly predicted and 21 percent of false alans sent. Crisis entries in the 1990 onward period that are not anticipated by the tree are Algeria 1991, Argentina 1995, and Russia 1998.

C. Combining the Logit and the Iree EWS

Combining logit model and tree analysis builds on the different strengtls of each approach The strength of the logit approach is to discover relationships between dependent variable and explanatory variable that hold across the full sample. Ihe tree analysis is weak in this regard because for every rule, it considers only the information available in the subsample The strength of the tree analysis is to discover nonlinear variable combination that can help predict the outcomne of the dependent vaziable. The logit approach is weak in this regard because it does not include an automatic search mechanism applied

21 The relative pexformance of correctly predicting default entries while sending as few false alanns as possible can be influenced by a paramneter that detennines the relative cost of misclassifying a crisis relative to that of a noncrisis episode. We set this cost parameter to 7:1. As a consequence; a node is classified as crisis prone whenever the ratio of crises to

--- Page 34 ---

more directly related to our results; the logit EWS has a lower share of correct signals than the tree EWS, but it also has a lower share of false alarms than the tree EWS. A straightforward combination ofthe two techniques is to define dummy variables for the groups identified in the tree analysis as episodes belonging to a common terminal node and wvhether the groups identified in the tree analysis are statistically significant for predicting CIISIS _

Including dumnmies representing the nodes of the tree analysis further improves the 22 perfonmance of the logit EWS . Only a subset of dummies representing the nodes can be Such perfect predictions arise because some nodes contain only crisis or noncrisis episodes and because the sample of the logit EWS is substantially smaller than the sample for which the tree was specified on account of CARTs ability to use surogate data for missing values . When including the feasible subset of dummies representing nodes; the joint model conrectly anticipates 81 percent of all cisis entries while sending false alaius in ouly 6 percent of the cases Moreover; the joint model correctly predicts 16 percent of all exits from crisis. The dummies representing nodes are jointly significant and all canry a positive sign consistent with their classification as risk-prone except for the dummy denoting node 3 which is classified as not being risk-prone.

An alternative way of combining the logit EWS and the tree EWS is to integrate them into a two-tiered EWS. This EWS would build on the strength of the logit EWS of not sending many false alars and on the strength of the tree EWS of calling many crisis entries. The OI only the logit EWS predicts a crisis for the next year. In most cases; a single signal is likely to comne fiomn the tree EWS which has higher in-samnple predictive power at the cost of sending relatively more false alarms . The two-tiered EWS would indicate that a country is at the verge of crisis, if both tree and logit EWS predict a crisis for the next year. Countryspecific charts depicting the predicted crisis probability over time as well as the major regressors fromn the logit EWS can supplement the information from the two-tiered EWS. entry

VI SUMMARY AND CONCLUSIONS

In this paper, we have developed two EWS models of sovereign debt crises for a large sample of countries described as having market access. One EWS was based on the estimation of a logit model, the other EWS was based on the classification andregressiontree analysis. We found that variables suggested by economic theory are able to predict crises and, mnost important for early wamings; povide a mneasure of the probability of entening into a debt crisis. These variables include external debt ratios measur solvency and debt sustainability, measures of illiquidity or refinancing risk, measures of external imbalance and good ing

22 Results are available from the authors upon request.

--- Page 35 ---

debt-servicing pressures; other macrovariables that affect investors' confidence and the country's ability to service debt, macroeconomic (especially monetary) instability; and some political-economy factors leading to policy uncertainty . These results are robust. quite

The predictive power of the models is good, but this work would benefit from further extensions . Here are some of them quite

- First, we concentiated on the subset of developing countries that have mnarket access. But the history of the last thirty years shows that many poorer developing countries with little access to intemnational capital markets also faced debt-servicing difficulties and outright defaults (see the list of highly indebted poor countries (HIPCs)) . Since our dataset includes such countries , we plan to extend the study to these not predict crises in market-access countries and these poorer countries, since the latter have debt burdens that are much larger in relation to their GDPs, but are mostly owed (on partly concessional ters to official rather than private creditors. debt thresholds for crisis may differ for these two groups and parameter estimates may not long So,
- Second a large body of previous work has analyzed the crises of the 1980s, but little had been done to predict the debt crises of the 1990s. Our model makes some progress, but there is scope for futher improvements in predict the debt crises of the 1990s and sending fewer false alams (type-II enor). Many, but not all of these more recent crises had to do with illiquidity, rather than near insolvency; but even after controlling for measures of illiquidity; some entries into crises in the 1990s remain unpredicted.  Thus; more work needs to be done to try to assess which fundamental vulnerabilities andor investors' behavior can account for these more recent capital account cises. A sound EWS mnodel should be at predicting mnoIe systematically the more recent genre of crises without sending too many false alamms. It is also possible that the unpredictability of some recent episodes may be consistent with the view that, in a of fiagile fundamentals; multiple equilibria may occur; depending on investors' expectations and behavior. ting good region
- Third, many, but not all debt crises episodes have to do with fiscal vulnerabilities of the sovereign. However, there are better data on external debt and tradelexternal flows than there are about stocks of public debt and fiscal variables; such as real budget deficits and primary gaps. although some measures of fiscal imbalance aud public debt sustainability signal fragility in the data; lack of data has so fàr prevented us from testing more systematically for the effects of budget deficits and primary gaps and finding statistically significant effects of these fiscal vulnerability variables. Thus; extending the dataset to have better fiscal flow and debt data may be of great value in testing the role of these fiscal variables in debt crises. So,
- Fourth, in addition to macrovariables; market indicators of debt sustainability; such as credit ratings and spreads on emerging market debt, may have predictive power in explaining debt crises. Of course, the same macro factors that predict crises are the variables that are used to assess sovereign ratings and to estimate the determinants of

--- Page 36 ---

spreads. Still, it would be interesting to test whether, after controlling for our macro deteminants of crises, ratings , and spreads have additional predictive power or not. Ihis would be useful in the design of an appropriate EWS system of early debt crises . Some recent work suggests that credit agencies have fared poorly in predicting debt-servicing difficulties in recent crises carly on similarly; spreads are not always very reliable predictors until it is too late and a cisis is incipient. So, horse race between our models and ratings and/or spreads or such variables to our models may help to assess a country' 5 vulnerability to a debt crisis early on. rating doing adding

- Fiftl sometimes; but not always, debt crises have been associated with curency crises and banking crises (most recently in Argentina; Ecuador, and Russia). Although the precise causal relations among these three type of crises is complex, several ideas are interesting: study the interaction between these crises (i. when one Or two Or three of them occu simultaneously and whether similar variables predict them); and test whether currency and banking crises are leading indicators of debt crises aud thus are able to better forecast the latter. An early guess is thiat thiese variables may not be leading indicators as debt crises are often concomitant but not lagging curency and banking crises. e.,
- Sixth; it may be worth analyzing in more detail whether crisis cpisodes where default was avoided because of a large IMF package are different from other episodes in terms of the countries vulnerabilities . In some of these episodes, the IMF's 'catalytic approach of large financial support cum policy adjustment was attempted with 23 mixed success. Ideally, these should be cases of illiquidity with conditional solvency (ie, solvency conditional on policy adjustment) where exceptional official finance is appropiate. So, studying separately these episodes mnay be important. However a major data constraint is that these episodes are relatively rare and recent In OU sample dataset .

Given the reemergence of debt cises in the 1990s, after the end of the 1980s debt crisis, the impontance of assessing debt sustainability in emerging markets, the recent debates on bailins versus bailouts as crisis-resolution tools, the most recent policy debates on the appropriate regimes for orderly debt restmcturing (statutory approaches such as the sovereign debt restiucturing mechanism versus contractual approaches; such as collective-action clauses), and the need to provide IMF financial support only when appropriate; the importance of understanding the causes of sovereign debt crises and of predicting them early on cannot be overemphasized . Our study is a conttibution to answering somne of these important empirical and policy issues . large

23 For a theoretical model of the IMF's catalytic finance approach; see Corsetti; Guimaraes; and Roubini (2003). For an empirical assessment of this approach; see Cottarelli and Giannini (2002), and Mody and Saravia (2003).

--- Page 37 ---

I SENSITIVITY ANALYSIS OF TH LOGIT EWS

24 We canry out a number of sensitivity tests to see how robust the estimated logit EWS is.

- We observations witl extreme values for the regressors included in the logit 25 EWS The predictive performance of the logit EWS is not affected by this. The direction of influence of the regressors for which the extreme values are removed remains unchanged, and the coefficient estimates do not exhibit falls in the z -value_ drop large
- Varying the definition of the dependent variable lowers the predictive power of the logit EWS to some extent. All coefficient estimates exhibit the same direction of influence, but a few appear to be no longer relevant and show a worsening of the z-value (in particular, debt-service-to-resenves ratio and U.S. treasury bill rate). If predicts 63 percent of all crisis entries while sending false alarms in 4 percent of the cases. If we lower the threshold beyond which IMF loans are considered a crisis episodes to 50 percent of quota; the model conrectly predicts 58 percent of all crisis quota, the model correctly predicts 66 percent of all crisis entries while sending false alars in 6 percent of all cases We would conclude that these results indicate some robustness of our model with regard to variations in the dependent variable; though the results are by no means insensitive. large
- We reenter several variables that dropped out of the specification process into the logit EWS to ensure that our specification process was not adversely affected by an omitted vaviable bias . For example; we reenter the financing requirement; the resource gap, public debt, and the overall balance. In none of these cases do we see the models predictive power improved
- We also canied out a specification process based on the full sample (Table 18). While the resulting model fared well in terms of conectly predicting crisis entries in the full sample; it was not very successful at predicting crisis entries from 1990 onward. However OUI logit EWS that resulted fioun a specification process canied out for a

24 Results available fromn the authors upon request.

25 In separate regressions ; we exclude obsenvations with total extemnal debt in excess of 100 percent of GDP , obseivations with short-term external debt on a remaining mnaturity basis ratio to reserves in excess of 10, obsenvatious with an external debt-service ratio to reserves in excess of 3 obsenvations with a curent account balance greater than 10 percent of GDP or smaller than -10 percent of GDP, observations with real GDP growth greater than 10 percent or smaller than -10 percent; openness smaller than 200. In addition; we impose these sample restrictions jointly .

--- Page 38 ---

logit EWS did not do any worse at predicting crisis enties before 1990 than the model specified for the full sample. From this we conclude that there has becn some stuuctural break in what is driving crises since the beginning of the nineties. However; those indicators that help predict crises from 1990 onward are also usefil in predicting crises to 1990 prior

--- Page 39 ---

AND ASSIGNMENT RULES

problem of classification of N objects into j=1, Jclasses; characterized by a prior and a symmetric (unit) misclassification costs C(ilj)=€(j)=1, denoting the cost of classifying a type j erroneously as class i, can be refomulated as a problem with an arbitray symmetric misclassification costs; C(j), andnew et al. ch 4.3):

<!-- formula-not-decoded -->

In Our are equal to the sample probabilities(data), ie 7(1)=0.205, 70)=0.795. Hence the ncw priors are priors

Recall that the assignment mule for a problem with unit misclassification costs is to node n to class 1 when te within node relative probability exceed the sample wide relative probability: assign

--- Page 40 ---

References

- Beers; David I. and Ashok Bhatia, 1999,
- Beim, David 0 and Charles W. Calomiris, 2001 Emerging Financial Markets, (New York: McGraw-Hill Irwin)
- Olshen, RA. & Stone; C.J. 1983, Classification and Regression Trees, (Wadsworth Publishers) .
- Ratings;' Federal Reserve Bank of New York Policy Review (October), pP. 37-52.
- Catào, Luis, and Bennett Sutton; 2002, "Sovereign Defanlts: The Role of Volatility; IMF Working Paper 02/149 (Washington: Intemnational Monetaty Fund) .
- Corsetti, Giancarlo; Bemnardo Guimaràes; and Nouriel Roubini, 2003, "Intemational Lending of Last Resort and Moral Hazard: A Model of the IMFs Catalytic Fianance, http://www econ vale edul~corsentileurolimfpdf November (Unpublished; New Yok: New York University)
- 'Bedfellows, Hostages; or Perfect Strangers? Global Capital Markets andthe Catalytic Effect of IMF Crisis Lending;' IMF Paper 02/193 (Washington: Intemnational Monetary Fund)
- IMF Working Paper 02/181 (Washington: Intemnational Monetary Fund).
- Detragiache; Enrica; and Antonio Spilimbergo; 2001,  Crises and Liquidity: Evidence and Intempretation; IM Working Paper 01/2 (Washington: Intemational Monetary Fund) .
- 5131, Prepared for Handbook of International Economnics . Paper
- IMF Working Paper No: 02/9 (Washington: Intemational Mone Fund). tary
- Haque, Nadeem U. of Political and Economic Variables in Creditworthiness Ratings,' IMF Working Paper 98/46 (Washington: International Monetary Fund) .

--- Page 41 ---

- Hemming, Richard, Michael Kell, and Axel Schimmelpfennig, 2003, Fiscal Vulnerability and Financial Crises in Emerging Market Econonies , IMF Occasional Paper No. 218 (Washington: Intemnational Monetary Fund)
- Hemning, Richard, aud Muay Petie, 2002 A Framnework for Assessing Fiscal Vulnerability, MMF Working Paper 00/52 (Washington: Intemnational Monetaxy Fund) Hemming, Richard, and Nigel Chalk, 2000, Assessing Fiscal Sustainability in Theory and Practice;' IMF Working Paper 00/81 (Washington: Intemnational Monetary Fund) .
- Does IMF Financing Result in Moral Hazard?" IMF Working Paper 00/168 (Washington: Intemnational Monetary Fund)
- and Sovereign Credit Ratings;' OECD Development Centre Technical Papers No. 124 (Paris: Organisation for Economic Co-operation and Development).
- Lee, Suk Hu 1993 Are tle credit Tatings assigned by bankers based on the willingness of LDC bomrowers to repay?, In: Journal of Development Economics, Vol 40, pp. 349-359.
- Mody; Ashoka; and Saravia, 2003, 'Catalyzing Private Capital Flows: Do IMF Supported Programs Work as Commitment Devices?" Unpublished, IMF (Washington: Intemnational Monetary Fund). Diego
- 151-170.
- Rojas-Suarez; L 2001, Rating Banks in Emerging Markets, Institute for Intemnational Economics (Washington; DC) .
- Roubini, Nouriel, 2001, 'Debt Sustainability: How to Assess Whether a Country is Insolvent , York University) (December) .
- Standard & Poor' s, 2002 'Sovereign Defaults: Moving Higher Again in 20032, (September 24) [Reprinted for RatingsDirect]