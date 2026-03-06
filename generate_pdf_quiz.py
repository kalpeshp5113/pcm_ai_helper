from pypdf import PdfReader
import google.generativeai as genai

def generate_quiz_from_pdf(uploaded_file, num_questions=5):

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    text = text[:5000]

    prompt = f"""
Generate {num_questions} multiple choice questions from the notes below.

Rules:
- Each question must have 4 options
- Format exactly like this:

Q1: Question text
A) option
B) option
C) option
D) option
Correct Answer: A

Notes:
{text}
"""

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