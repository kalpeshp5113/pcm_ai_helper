import google.generativeai as genai
from PIL import Image

model = genai.GenerativeModel("gemini-2.5-flash")

def solve_image(uploaded_file):
    image = Image.open(uploaded_file)

    response = model.generate_content([
        "Solve this PCM question step-by-step",
        image
    ])

    return response.text