import os
import openai
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()
#openai_api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")
messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]
result=chat(messages)
print(result.content)

#from langchain.chains import ConversationChain  
  
#conversation = ConversationChain(llm=chat)  
#conversation.run("Translate this sentence from English to French: I love programming.")