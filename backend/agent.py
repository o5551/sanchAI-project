import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent, AgentType
from weather_tool import get_weather

load_dotenv()

llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

weather_tool = Tool(
    name="Weather Tool",
    func=get_weather,
    description="Get weather of a city"
)

agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(query: str):
    return agent.run(query)
