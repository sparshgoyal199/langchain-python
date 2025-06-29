# from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
# from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain,LLMChain
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = GoogleGenerativeAI(model='gemini-1.5-flash',google_api_key=os.getenv('GEMINI_API_KEY'))

#*********studying otherLLm's*********
# response = llm.invoke("what do you do? who are you")
# print(response)
# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACE_TOKEN")
# )
# chat_model = ChatHuggingFace(llm=llm)
# response = chat_model.invoke("hello")
# print(response)

#********Sequentialchaining and promptTemplate********
# prompt1 = PromptTemplate(template="is it a hindu name? {text}",input_variables=["text"])
# prompt2 = PromptTemplate(template="what is the meaning of the name {text} dont explain anything",input_variables=["text"])

# chain1 = LLMChain(llm=llm,prompt=prompt1)
# chain2 = LLMChain(llm=llm,prompt=prompt2)

# chains = SimpleSequentialChain(chains=[chain1,chain2])
# result = chains.invoke('sparsh')
# print(result)