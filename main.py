from langchain_core.messages import HumanMessage #High level framework that allows us to build AI applications
from langchain_openai import ChatOpenAI #Allows us to use OPENAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent #Complex framework that allows us to build AI agents
from dotenv import load_dotenv # Allows us to load these environmental variable files from within our Python script

load_dotenv()

def main_function():
    model= ChatOpenAI(temperature=0)
    tools=[]

    agent_executor=create_react_agent(model,tools)
    print("Hello! I am your AI assistant. Please type 'quit' if you wnat to exit.")
    print("You can ask me anything you want or chat with me.")

    while True:
        user_input=input("\n You:").strip()
        if user_input.lower()=="quit":
            print("Exiting!!")
            break

        print("Assistant: ",end="")
        for chunk in agent_exegutor.stream(
            {"messages":[HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk ["agent"]["messages"]:
                    print(message.content,end="")
        print()

if __name__ =="__main__":
    main_function()