from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo") # create a new instance of the ChatOpenAI class with the free GPT model and temperature set to 0

messages = [
     SystemMessage("You are an Expert in social Media content strategy "),
     HumanMessage("Give a short tip to create engagng post on instagram"),
      
]

result = llm.invoke(messages) # invoke is a method that takes a string as input and returns a string as output from llm model

print(result.content)