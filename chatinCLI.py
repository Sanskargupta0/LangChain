from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)

chathistory = [
    SystemMessage(content="You are a helpful assistant."),
]

def chat_with_model(user_input):
    global chathistory
    chathistory.append(HumanMessage(content=user_input))
    response = model.invoke(chathistory)
    chathistory.append(AIMessage(content=response.content))
    return response.content

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        response = chat_with_model(user_input)
        print(f"AI: {response}")