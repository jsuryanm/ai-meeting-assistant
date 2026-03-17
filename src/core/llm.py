from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return ChatGroq(model="llama-3.3-70b-versatile")

# if __name__ == "__main__":
#     llm = get_llm()
#     print(llm.model_name)