import google.generativeai as genai
from prompts import PRACTICE_PROMPT

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_practice(subject, difficulty):
    prompt = PRACTICE_PROMPT.format(
        subject=subject,
        difficulty=difficulty
    )

    response = model.generate_content(prompt)

    return response.text