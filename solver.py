import google.generativeai as genai
from prompts import DETAILED_PROMPT, SHORT_PROMPT



model = genai.GenerativeModel("gemini-2.5-flash")

def solve_question(question, mode):

    if mode == "Detailed Solution":
        prompt = DETAILED_PROMPT.format(question=question)
    else:
        prompt = SHORT_PROMPT.format(question=question)

    response = model.generate_content(prompt)

    return response.text