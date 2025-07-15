import streamlit as st
import os
from crewai import Agent, Task, Crew

# ✅ Use your OpenAI API key securely
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# 🧠 App title
st.title("🧠 AutoDev Lite - AI Code Writer")

# 📥 User input
task_input = st.text_input(
    "Enter your coding task (e.g., 'Write a Python function to check for prime numbers'):"
)

# ✅ Define the AI agent
code_agent = Agent(
    role="Senior Python Developer",
    goal="Generate correct and readable Python code",
    backstory="You are an expert in Python programming with years of experience writing clean, efficient code.",
    verbose=True,
    allow_delegation=False
)

# ✅ Define the task
coding_task = Task(
    description=f"Write Python code to: {task_input}",
    agent=code_agent
)

# ✅ Create Crew
crew = Crew(
    agents=[code_agent],
    tasks=[coding_task],
    verbose=True
)

# 🚀 Trigger on button click
if st.button("Generate Code"):
    if task_input.strip() == "":
        st.warning("Please enter a coding task.")
    else:
        try:
            result = crew.kickoff()  # ✅ Use `kickoff()` for latest CrewAI version
            st.code(result, language="python")
        except Exception as e:
            st.error(f"❌ Error: {e}")
