from langchain_google_genai import GoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

import os
load_dotenv()
llm = GoogleGenerativeAI(model='gemini-1.5-flash',google_api_key=os.getenv('GEMINI_API_KEY'))

prompt_template = PromptTemplate(template="you just need to extract only two numbers from it and number should be comma seperated,user senetnce is {text}",input_variables=["text"])

@tool
def addTwoNumbers(input:str) -> int:
    """add two numbers"""
    print("input: ",input)

chain = RunnableSequence(
    prompt_template,llm,addTwoNumbers
)

res = chain.invoke("addition of 4 and 5 is")
#print(res)