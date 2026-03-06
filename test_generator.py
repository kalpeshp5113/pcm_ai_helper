import google.generativeai as genai
from prompts import TEST_PROMPT

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_test(subject, topic_2, num_questions, difficulty):

    prompt = TEST_PROMPT.format(
        subject=subject,
        topic_2=topic_2,
        num_questions=num_questions,
        difficulty=difficulty
    )

    response = model.generate_content(prompt)

    return response.text