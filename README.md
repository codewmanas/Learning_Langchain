<div align="center">
     <img src="https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F28bvsfd0wuo0hnfqfk0w.jpeg" alt="Langchain Banner">
</div>
<br />

# What is Langchain?
LangChain is a framework for developing applications powered by large language models (LLMs).

LangChain simplifies every stage of the LLM application lifecycle:

Development: Build your applications using LangChain's open-source components and third-party integrations. Use LangGraph to build stateful agents with first-class streaming and human-in-the-loop support.
Productionization: Use LangSmith to inspect, monitor and evaluate your applications, so that you can continuously optimize and deploy with confidence.
Deployment: Turn your LangGraph applications into production-ready APIs and Assistants with LangGraph Platform.

<div align="center">
     <img src="https://python.langchain.com/svg/langchain_stack_112024_dark.svg" width="80%" alt="Langchain Stack">
</div>

## What is a Chat Model in Langchain?

A chat Model in Langchain is a component designed to communicate in a  structured way with LLMs like GPT-4 , Hugging Face and Claude Sonnet.

### Supported Chat Models in LangChain

| Provider                  | Tool Calling | Structured Output | JSON Mode | Local | Multimodal | Package                        |
|---------------------------|--------------|-------------------|-----------|-------|------------|--------------------------------|
| ChatAnthropic             | ✅           | ✅                | ❌        | ❌    | ✅         | `langchain-anthropic`         |
| ChatMistralAI             | ✅           | ✅                | ❌        | ❌    | ❌         | `langchain-mistralai`         |
| ChatFireworks             | ✅           | ✅                | ✅        | ❌    | ❌         | `langchain-fireworks`         |
| AzureChatOpenAI           | ✅           | ✅                | ✅        | ❌    | ✅         | `langchain-openai`            |
| ChatOpenAI                | ✅           | ✅                | ✅        | ❌    | ✅         | `langchain-openai`            |
| ChatTogether              | ✅           | ✅                | ✅        | ❌    | ❌         | `langchain-together`          |
| ChatVertexAI              | ✅           | ✅                | ❌        | ❌    | ✅         | `langchain-google-vertexai`   |
| ChatGoogleGenerativeAI    | ✅           | ✅                | ❌        | ❌    | ✅         | `langchain-google-genai`      |
| ChatGroq                  | ✅           | ✅                | ✅        | ❌    | ❌         | `langchain-groq`              |
| ChatCohere                | ✅           | ✅                | ❌        | ❌    | ❌         | `langchain-cohere`            |
| ChatBedrock               | ✅           | ✅                | ❌        | ❌    | ❌         | `langchain-aws`               |
| ChatHuggingFace           | ✅           | ✅                | ❌        | ✅    | ❌         | `langchain-huggingface`       |
| ChatNVIDIA                | ✅           | ✅                | ✅        | ✅    | ✅         | `langchain-nvidia-ai-endpoints` |
| ChatOllama                | ✅           | ✅                | ✅        | ✅    | ❌         | `langchain-ollama`            |
| ChatLlamaCpp              | ✅           | ✅                | ❌        | ✅    | ❌         | `langchain-community`         |
| ChatAI21                  | ✅           | ✅                | ❌        | ❌    | ❌         | `langchain-ai21`              |
| ChatUpstage               | ✅           | ✅                | ❌        | ❌    | ❌         | `langchain-upstage`           |
| ChatDatabricks            | ✅           | ✅                | ❌        | ❌    | ❌         | `databricks-langchain`        |
| ChatWatsonx               | ✅           | ✅                | ✅        | ❌    | ❌         | `langchain-ibm`               |
| ChatXAI                   | ✅           | ✅                | ❌        | ❌    | ❌         | `langchain-xai`               |


## Why use Langchain Chat Models?

1. Consistent Workflow :
Langchain's Chat models unify different APIs , saving you from managing each one's unique setup and quirks

2. Easy Switching Between LLMs
Want to switch from one  LLM to another ? Langchain's Chat model make it simple without code rewrites 

3. Context Management
Working with Langchain's Chat Models help manage conversation history, letting you keep context across multiple interactions seamlessly

4. Efficient Chaining
You can connect multiple LLm calls and tasks in one structured pipeline, which is tricky to set up manually.

5. Scalability
As Project grows , Langchain's interface supports more complex workflows , letting you focus on features , not API management 