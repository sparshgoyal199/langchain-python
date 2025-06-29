from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

import os
load_dotenv()
llm = GoogleGenerativeAI(model='gemini-1.5-flash',google_api_key=os.getenv('GEMINI_API_KEY'))

try:
    loader = TextLoader("kitabay.txt")
except Exception as e:
    print("Error while loading file=", e)
    
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=os.getenv('GEMINI_API_KEY'))
text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=300)
index_creator = VectorstoreIndexCreator(text_splitter=text_splitter,embedding=embeddings)
    
index = index_creator.from_loaders([loader])
prompt = PromptTemplate(template="Please provide a concise answer in bullet points for the following: {text}",input_variables=(["text"]))

while True:
    user_message = input("Hi there! I'm KitabayBot. What can I do for you today?\n")
    if(user_message == "" or user_message == "exit"):
        break
    query = prompt.format(text=user_message)
    AI_res = index.query(query,llm=llm)
    print(AI_res)
    print()
    
print('I hope my support was helpful to you today')