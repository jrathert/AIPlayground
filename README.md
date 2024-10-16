# Project AIPlayground

This project contains a few example Python scripts that I wrote to play with several APIs and frameworks in the AI/LLM field and similar tools. It is mainly used to have it available as a "boilerplate template" whenever I start with these things on a new machine.

## Python dependencies

Several tools are leveraged in the various scripts:

 - `openpyxl` - Excel read (and write)
 - `spacy`- NLP processing
 - `fuzzywuzzy`- similarity search 
 - `python-levenshtein` - for an optimized `fuzzywuzzy` search
 - `pandas` - dataframe processing
 - `openai` - OpenAI and MS Azure OpenAI API
 - `pymilvus` - vector database
 - `langchain` and `langchain-openai` - advanced LLM framework

## Development dependencies

All of the tools above can be easily installed by using  `pipenv`: 
- If `pipenv` is not installed, use either 
  - `brew install pipenv` (on macOS) or 
  - `sudo apt install pipenv` (on Linux) 
  
  to install it.
- `pipenv sync` will then ensure all libraries and further dependencies are met

_Please note: You need Python 3.12 in order for this to work (`spacy` fails with 3.13)_

 ## Runtime dependencies

 ### Spacy data

 The `spacy` tools rely on downloading the relevant neural network models, e.g., by running 
 ```
 python -m spacy download en_core_web_sm
 ``` 
 
 See https://spacy.io/usage for details.

 ### Environment variables

 Most tools rely on respective environment variables to be set. Suggestion is to add them to an `.env` file in the local directory. This file can than either be parsed manually (`source .env`) before running any program or is read by your IDE (e.g., VS Code) when debugging or by your environment manager (I use `pipenv`).

 The `.env` file looks like this:

 ```
 LLM_PROVIDER=AZURE_OPENAI

 # Azure endpoint and key can be found in Azure OpenAI Studio (https://oai.azure.com/portal)
AZURE_OPENAI_ENDPOINT=https://<yourendpoint>.openai.azure.com/
AZURE_OPENAI_API_KEY=s0m3l0ngt3xtandnumber5tr1ng
AZURE_OPENAI_MODEL=gpt-4o-mini
AZURE_OPENAI_DEPLOYMENT_NAME=openai-gpt-4o-mini-deployment
OPENAI_API_VERSION=2024-06-01

OPENAI_API_KEY=an-evenl0ng3er5tr1ngfr0m0pena1ap1
```

# Example scripts

These are simple script that prove proper functioning of all APIs and frameworks

- `first_oai.py` - simple call of OpenAI chat completion API
- `first_azoi.py`- same as `first_oai.py`, but calling Azure OpenAI
- `first_langchain.py` - calling OpenAI or Azure OpenAI using a simple chain
- `first_spacy.py` - simple test of spacy NLP engine
- `first_milvus.py` - short test of milvus vector DB

# Applications

These are small applications (under development) that might leverage the above APIs and frameworks. They expect an XL file called `allcomp.xlsx` in the current directory with a sheet `Sheet1` in it, having in their first column a heading and then a list of strings. These will be processed.

- `name_checker.py` - uses `spacy` to identify personal information in the strings
- `name_normalizer.py` - uses `fuzzywuzzy` and a super inefficient algorithm (of O^2) to identify similarities

Both tools are WIP, and as can be seen, do not use any AI functionality yet.



