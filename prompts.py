
DETAILED_PROMPT = """
You are an expert PCM tutor helping students.

Solve the question with a detailed explanation.

Provide:
1. Concept used
2. Formula
3. Step-by-step solution
4. Final answer
5. One similar example

Question:
{question}
"""

SHORT_PROMPT = """
You are a PCM tutor.

Solve the question and give a short solution.

Rules:
- Keep explanation very short
- Show minimal steps
- Provide the final answer clearly

Question:
{question}
"""

PRACTICE_PROMPT = """
Generate 5 practice questions for {subject} at {difficulty} level.
Do not provide solutions.
"""

CONCEPT_PROMPT = """
You are an expert Physics, Chemistry, and Mathematics tutor.

Explain the following concept in simple language for students.

Concept: {concept}

Provide:
1. Simple explanation
2. Important formula (if any)
3. One real-life example
"""

FORMULA_PROMPT = """
You are an expert PCM tutor.

Give important formulas for the following topic.

Topic: {topic}

Provide formulas in a clean list.
"""

TEST_PROMPT = """
You are an expert PCM tutor.

Generate a practice test.

Subject: {subject}
Topic: {topic_2}
Number of questions: {num_questions}
Difficulty: {difficulty}

Do NOT give solutions.
Only give questions.
"""

NOTES_PROMPT = """
You are an expert PCM teacher.

Create short study notes for students.

Topic: {topic_1}

Provide:
1. Key concepts
2. Important formulas
3. Short explanation
4. One simple example
5. Quick revision points
"""

QUIZ_PROMPT = """
You are a PCM teacher.

Generate {num_questions} multiple choice questions with 4 options each for students.

Subject: {subject}
Topic: {topic_3}
Difficulty: {difficulty}

Provide the correct answer for each question at the end of the options like: 'Correct Answer: B'
Format:
Q1: ...
A)
B)
C)
D)
Correct Answer:
"""