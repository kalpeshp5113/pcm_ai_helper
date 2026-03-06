import google.generativeai as genai
from prompts import FORMULA_PROMPT

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_formulas(topic):

    prompt = FORMULA_PROMPT.format(topic=topic)

    response = model.generate_content(prompt)

    return response.text