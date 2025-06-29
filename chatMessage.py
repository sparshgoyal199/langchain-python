from langchain_core.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain,LLMChain
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
llm = GoogleGenerativeAI(model='gemini-1.5-flash',google_api_key=os.getenv('GEMINI_API_KEY'))

prompt = PromptTemplate(template="this chat is only about the cricket,you need to answer only cricket question,here is your question {text}",input_variables=["text"])
chain = prompt | llm

while True:
    human_message = input("enter you text: ")
    res = chain.invoke(human_message)
    print(res)
#******but through that we are unable to chat like we cant provide the conext of early message*********