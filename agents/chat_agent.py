from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:c
    raise ValueError("GOOGLE_API_KEY environment variable is not set.")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.7, max_output_tokens=2048, google_api_key=API_KEY
)

chat_prompt = PromptTemplate.from_template("""
You are a fitness coach chatting in Instagram DMs.

Your goal:
- Talk like a real human (casual, friendly)
- Keep messages short (1-3 lines)
- Help with fitness (fat loss, muscle gain, etc.)
- Ask questions to understand user better
- Build trust step by step

Style:
- No long paragraphs
- No robotic tone
- Use simple English

Conversation so far:
{conversation}

User: {message}

Reply:
"""
)

chat_agent = chat_prompt | llm # this line creates a pipeline where the prompt is filled with the user's message and then passed to the language model to generate a reply.

def generate_reply(message, conversation):
    response = chat_agent.invoke({
        "message": message,
        "conversation": conversation
    })
    return response.content