import os

from smolagents import OpenAIServerModel

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

geminiModel = OpenAIServerModel(
    model_id="gemini-2.5-flash-preview-05-20",
    api_key=GEMINI_API_KEY,
    api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
)
