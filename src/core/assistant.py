from src.core.llm import get_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

llm = get_llm()
template = """
You are an expert AI Meeting Assistant.

Analyze the transcript and extract:

SUMMARY:
Short meeting summary.

KEY POINTS:
Bullet list.

DECISIONS:
Bullet list.

ACTION ITEMS:
Task | Owner | Deadline

RISKS:
Potential blockers.

Transcript:
{context}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": RunnablePassthrough()}
    | prompt 
    | llm 
    | StrOutputParser()
)

def generate_meeting_minutes(transcript):
    result = chain.invoke(transcript)
    return result

