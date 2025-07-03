from langchain.agents import initialize_agent,AgentType
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
import requests
from dotenv import load_dotenv

import os
load_dotenv()
llm = GoogleGenerativeAI(model='gemini-1.5-flash',google_api_key=os.getenv('GEMINI_API_KEY'))

@tool
def addTwoNumbers(input:str) -> int:
    """gives the addition of two numbers"""
    print(input)

@tool
def getLongitudeandLatitude(city_name:str):
    """return the longitude and latitude of city_name as 'lat,lon'"""
    """you need to run tool temperature when you got the langitude and latitude"""
    res = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid=4958285ef04106de1ae1e8c80dc1c5d6')
    json_resp = str(res.json()[0]["lat"]) + ',' + str(res.json()[0]["lon"])
    print(json_resp)
    return json_resp

@tool
def temperature(LongLat:str):
    """this tool get its parameter in the form 'lat,lon' from tool getLongitudeandLatitude"""
    latitude,longitude = LongLat.split(',')
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4958285ef04106de1ae1e8c80dc1c5d6&units=metric')
    json_res = res.json()
    print(f'temperature of {json_res["name"]} is: ',json_res["main"]['temp'])
    return json_res["main"]['temp']

agent = initialize_agent(
    tools=[addTwoNumbers,getLongitudeandLatitude,temperature],
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    llm=llm,
    verbose=False,
    max_iterations=3
)

agent.invoke("what is the temperature of mumbai right now")