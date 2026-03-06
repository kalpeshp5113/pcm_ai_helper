import google.generativeai as genai
from prompts import  QUIZ_PROMPT

model = genai.GenerativeModel("gemini-2.5-flash")
# def generate_quiz(subject, topic_3, num_questions, difficulty):

#     prompt = QUIZ_PROMPT.format(
#         subject=subject,
#         topic_3=topic_3,
#         num_questions=num_questions,
#         difficulty=difficulty
#     )

#     response = model.generate_content(prompt)

#     return response.text
def generate_quiz(subject, topic_3, difficulty, num_questions=5):
    prompt = QUIZ_PROMPT.format(
        subject=subject,
        topic_3=topic_3,
        difficulty=difficulty,
        num_questions=num_questions
    )
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    lines = response.text.split("\n")
    questions = []
    current_q = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("Q") and ":" in line:
            if current_q:
                # only append if options exist
                if "options" in current_q and current_q["options"]:
                    questions.append(current_q)
            current_q = {"question": line.split(":",1)[1].strip(), "options": [], "answer": ""}
        elif line.startswith(("A)","B)","C)","D)")):
            current_q.setdefault("options", []).append(line)
        elif line.startswith("Correct Answer:"):
            current_q["answer"] = line.split(":")[1].strip()
    if current_q and "options" in current_q and current_q["options"]:
        questions.append(current_q)

    return questions