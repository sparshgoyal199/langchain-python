from langchain_core.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain,LLMChain
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

#always use LLMchain with sequenmtial chaninig
llm = GoogleGenerativeAI(model='gemini-1.5-flash',google_api_key=os.getenv('GEMINI_API_KEY'))
# prompt1 = PromptTemplate(template="is it a hindu name? {text}",input_variables=["text"])
# prompt2 = PromptTemplate(template="what is the meaning of the name {text} dont explain anything",input_variables=["text"])

# chain1 = LLMChain(llm=llm,prompt=prompt1)
# chain2 = LLMChain(llm=llm,prompt=prompt2)

# chains = SimpleSequentialChain(chains=[chain1,chain2])
# result = chains.invoke('sparsh')
# print(result)

#***********pipe operator thing*************
prompt3 = PromptTemplate(template='create the story about two friends whoese names are {text}',input_variables=["text"])
prompt4 = PromptTemplate(template='what is the moral of the story {text}',input_variables=["text"])

chain3 = prompt3 | llm
# chain4 = prompt4 | llm
# chain = SimpleSequentialChain(chains=[chain3,chain4])
res = chain3.invoke({"text":"sparsh and rahil"})
print(res)
