from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import AIMessage,HumanMessage,SystemMessage
from langchain.memory import ConversationBufferMemory,ConversationBufferWindowMemory,ConversationSummaryMemory,ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash',google_api_key=os.getenv('GEMINI_API_KEY'))

# prompt_template = ChatPromptTemplate.from_messages([
#     SystemMessage(content="you are a cricket bot,you have to act as per that only")]
# )
# prompt = prompt_template.format()
# while True:
#     user_input = input("Ask your query: ")
#     if(user_input == "exit"):
#         break
#     prompt_template.append(HumanMessage(content=user_input))
#     prompt = prompt_template.format()
#     response = llm.invoke(prompt)
#     print(response.content)
#     print(prompt_template)
#     prompt_template.append(AIMessage(content=response.content))

#*********conversational memory and conversationalChain*************
#memory = ConversationBufferWindowMemory(k = 10)
#memory = ConversationSummaryMemory(llm=llm)
memory = ConversationSummaryBufferMemory(llm=llm,max_token_limit=1000)
chain = ConversationChain(llm = llm,memory=memory)

while True:
    user_input = input("ask any question: ")
    if(user_input == "exit"):
        break
    response = chain.invoke(user_input)
    print(response)