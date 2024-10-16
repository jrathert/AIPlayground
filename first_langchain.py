#
# small tool that set us and runs a simple langchain chain
# also showing the use of OpenAI vs Azure OpenAI
#
import os
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

provider = os.getenv("LLM_PROVIDER")
model = None
if provider == "AZURE_OPENAI":
    model = AzureChatOpenAI(
        # azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    )
elif provider == "OPENAI":
    model = ChatOpenAI()
else:
    print("Need to specify LLM_PROVIDER, either 'AZURE_OPENAI' or 'OPENAI'")
    exit(1)

assert model != None


parser = StrOutputParser()

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

chain = prompt_template | model | parser

result = chain.invoke({"language": "italian", "text": "hi"})

print(result)