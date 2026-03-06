import google.generativeai as genai
from PIL import Image

def generate_quiz_from_image(uploaded_image, num_questions=5):

    image = Image.open(uploaded_image)

    prompt = f"""
Read the study content in this image and generate {num_questions} MCQ questions.

Rules:
- 4 options per question
- Format exactly like:

Q1: Question
A) option
B) option
C) option
D) option
Correct Answer: A
"""

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content([prompt, image])

    lines = response.text.split("\n")
    questions = []
    current_q = {}

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("Q") and ":" in line:
            if current_q and "options" in current_q:
                questions.append(current_q)

            current_q = {
                "question": line.split(":",1)[1].strip(),
                "options": [],
                "answer": ""
            }

        elif line.startswith(("A)","B)","C)","D)")):
            current_q["options"].append(line)

        elif line.startswith("Correct Answer"):
            current_q["answer"] = line.split(":")[1].strip()

    if current_q:
        questions.append(current_q)

    return questions