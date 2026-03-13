import streamlit as st
import google.generativeai as genai
import google.generativeai as genai
from solver import solve_question
from image_solver import solve_image
from practice_generator import generate_practice
from concept_explainer import explain_concept
from formula_generator import generate_formulas
from test_generator import generate_test
from generate_note import generate_notes
from generat_quiz import  generate_quiz
from generate_pdf_quiz import generate_quiz_from_pdf
from generate_image_quiz import generate_quiz_from_image
from generate_plan import generate_study_plan

try:
   genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
      st.error(f"An error occurred: {e},Your's API key quota is reach the limit")
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("🎓 PCM Smart Study AI")
st.caption("Built by Kalpesh Pawar")

# Initialize history
if "history" not in st.session_state:
    st.session_state.history = []
if "question" not in st.session_state:
    st.session_state.question = ""

# Mode selection
mode = st.selectbox(
    "Select Mode",
    [
        "Solve Question",
        "Solve Image",
        "Practice Generator",
        "Concept Explainer",
        "Formula Generator",
        "Practice Test",
        "AI Notes Generator",
        "AI Quiz Mode",
        "Study planner"
    ]
)

# ---------------- TEXT QUESTION ----------------
if mode == "Solve Question":
   # Solution type selection
    solution_type = st.selectbox(
        "Select Solution Type",
        ["Detailed Solution", "Short Solution"]
    )

    # Question input
    question = st.text_area("Enter your question",key="question")

    col1, col2 = st.columns(2)

    # Solve button
    with col1:
        if st.button("Solve"):

            if st.session_state.question.strip() != "":

                with st.spinner("Solving..."):

                    answer = solve_question(st.session_state.question, solution_type)

                    st.session_state.history.append({
                        "question": st.session_state.question,
                        "answer": answer,
                        "type": solution_type
                    })

                    # st.success("Solved!")

                    st.success(answer)
                    

            else:
                st.warning("Please enter a question")

   
    with col2:
      if st.button("New Question"):
         try:
            st.session_state.question = ""
            st.rerun()
         except Exception as e:
             # Display the error in the UI for debugging
            st.error(f"An error occurred: {e},please do manually")

    
    
                        


# ---------------- IMAGE QUESTION ----------------
elif mode == "Solve Image":

    uploaded_file = st.file_uploader("Upload question image")

    if uploaded_file:
        if st.button("Solve Image"):
           with st.spinner("Analyzing Image..."):  
                answer = solve_image(uploaded_file)

                st.session_state.history.append({
                    "type": "image",
                    "question": "Image Question",
                    "answer": answer
                })

# ---------------- PRACTICE GENERATOR ----------------
elif mode == "Practice Generator":

    subject = st.selectbox(
        "Subject",
        ["Physics", "Chemistry", "Mathematics"]
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "JEE Level"]
    )

    if st.button("Generate Questions"):

        questions = generate_practice(subject, difficulty)
        st.markdown("Practice Questions")
        
        st.session_state.history.append({
            "type": "practice",
            "question": f"{subject} - {difficulty}",
            "answer": questions
        })
        st.write(question)


elif mode == "Concept Explainer":

    concept = st.text_input("Enter concept")

    if st.button("Explain"):

        if concept.strip() != "":

            with st.spinner("Explaining..."):

                explanation = explain_concept(concept)

                st.write(explanation)

        else:
            st.warning("Please enter a concept")
####
elif mode == "Formula Generator":

    topic = st.text_input("Enter topic")

    if st.button("Get Formulas"):

        if topic.strip() != "":

            with st.spinner("Generating formulas..."):

                formulas = generate_formulas(topic)

                st.write(formulas)

        else:
            st.warning("Please enter a topic")       
#####
elif mode == "Practice Test":

    subject = st.selectbox(
        "Select Subject",
        ["Physics", "Chemistry", "Mathematics"]
    )

    topic_2 = st.text_input("Enter topic")

    num_questions = st.slider("Number of questions", 5, 20, 10)

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    if st.button("Generate Test"):

        if topic_2.strip() != "":

            with st.spinner("Generating test..."):

                test = generate_test(subject, topic_2, num_questions, difficulty)

                st.write(test)

        else:
            st.warning("Please enter a topic")
st.sidebar.title("📚 Chat History")

if st.sidebar.button("Show History"):


    if len(st.session_state.history) == 0:
        st.sidebar.write("No questions solved yet.")

    else:
        for i, item in enumerate(st.session_state.history):

            with st.sidebar.expander(item["question"][:50] + "..."):

                st.write("**Question:**")
                st.write(item["question"])

                st.write("**Answer:**")
                st.write(item["answer"])

  
if st.sidebar.button("Clear History"):
    st.session_state.history = []                                      

elif mode=="AI Notes Generator":
    st.header("📚 AI Notes Generator")

    topic_1 = st.text_input("Enter topic")

    if st.button("Generate Notes"):

        if topic_1.strip() != "":

            with st.spinner("Generating notes..."):

                notes = generate_notes(topic_1)

                st.write(notes)

        else:
            st.warning("Please enter a topic")


elif mode == "AI Quiz Mode":

    st.header("🎯 AI Quiz Generator")
    
    def quiz_main():
        

        if st.session_state.quiz_questions:
            for i, q in enumerate(st.session_state.quiz_questions, 1):
                st.write(f"**Q{i}. {q.get('question','')}**")
                options = q.get("options", [])
                if options:
                    selected = st.radio("Select your answer:", options, key=f"q_{i}")
                    st.session_state.answers[f"q_{i}"] = selected

            if st.button("Submit Answers"):
                score = 0
                for i, q in enumerate(st.session_state.quiz_questions, 1):
                    correct = q.get("answer", "")
                    if st.session_state.answers.get(f"q_{i}","").startswith(correct):
                        score += 1
                st.success(f"Your Score: {score} / {len(st.session_state.quiz_questions)}")


    quiz_source = st.selectbox(
    "Quiz Source",
    ["From Topic", "From PDF", "From Image"]
    )

    if quiz_source == "From Topic":
        subject_input = st.selectbox("Select Subject", ["Physics","Chemistry","Mathematics"])
        topic_input = st.text_input("Enter Topic")
        difficulty_input = st.selectbox("Select Difficulty", ["Easy","Medium","Hard"])
        if "quiz_questions" not in st.session_state:
            st.session_state.quiz_questions = []

        if "answers" not in st.session_state:
            st.session_state.answers = {}
        if st.button("Generate Quiz"):
            with st.spinner("Generating Quiz..."):    
                if topic_input.strip():
                    st.session_state.quiz_questions = generate_quiz(subject_input, topic_input, difficulty_input)
                    st.session_state.answers = {}
        # quiz_main()
                else:
                    st.warning("Please enter a topic")
        quiz_main()
    elif quiz_source == "From PDF":

        uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])
        if "quiz_questions" not in st.session_state:
            st.session_state.quiz_questions = []

        if "answers" not in st.session_state:
            st.session_state.answers = {}

        if st.button("Generate Quiz from PDF"):
          with st.spinner("Generating Quiz..."):
            if uploaded_pdf is not None:

                st.session_state.quiz_questions = generate_quiz_from_pdf(uploaded_pdf)
                st.session_state.answers = {}    
                # quiz_main()
            else:
                    st.warning("Please upload pdf") 
        quiz_main()               
    elif quiz_source == "From Image":

        uploaded_image = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])
        if "quiz_questions" not in st.session_state:
            st.session_state.quiz_questions = []

        if "answers" not in st.session_state:
            st.session_state.answers = {}
        if st.button("Generate Quiz from Image"):
          with st.spinner("Generating Quiz..."):
            if uploaded_image is not None:

                st.session_state.quiz_questions = generate_quiz_from_image(uploaded_image)
                st.session_state.answers = {} 
                # quiz_main()           
            else:
                    st.warning("Please upload image")    
        quiz_main()            

elif mode== "Study planner":
        subject_plan = st.selectbox("Subject", ["Physics","Chemistry","Mathematics"])
        topic_plan = st.text_input("Topic")
        days_plan = st.number_input("Days Available", min_value=1, max_value=30)

        if st.button("Generate Study Plan"):
          with st.spinner("Generating Study Planner..."):
            if topic_plan.strip() != "":
                plan = generate_study_plan(subject_plan, topic_plan, days_plan)

                st.subheader("Your Study Plan")
                st.write(plan)       
