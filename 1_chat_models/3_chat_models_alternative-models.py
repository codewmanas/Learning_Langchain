from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic

messages = [
     SystemMessage("You are an Expert in social Media content strategy "),
     HumanMessage("Give a short tip to create engagng post on instagram"),
      
]

model = ChatAnthropic(model="claude-3-opus-202402229")

result = model.invoke(messages)
print(f"Answer from Anthropic: {result.content}")

