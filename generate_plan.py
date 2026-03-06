import google.generativeai as genai
model = genai.GenerativeModel("gemini-2.5-flash")
def generate_study_plan(subject, topic_plan, days):

    prompt = f"""
Create a study plan for a student.

Subject: {subject}
Topic_4: {topic_plan}
Days Available: {days}

Create a daily study schedule.
"""

    response = model.generate_content(prompt)

    return response.text