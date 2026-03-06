import google.generativeai as genai
from prompts import NOTES_PROMPT

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_notes(topic_1):

    prompt = NOTES_PROMPT.format(topic_1=topic_1)

    response = model.generate_content(prompt)

    return response.text