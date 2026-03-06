import google.generativeai as genai
from prompts import CONCEPT_PROMPT

model = genai.GenerativeModel("gemini-2.5-flash")

def explain_concept(concept):

    prompt = CONCEPT_PROMPT.format(concept=concept)

    response = model.generate_content(prompt)

    return response.text