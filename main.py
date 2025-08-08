from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)

result = llm.invoke("What is the capital of France?")  # Example usage

print(result.content)  # Output the result 