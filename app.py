import streamlit as st
import os
from crewai import Agent, Task, Crew

# 🔐 Secure API key
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.title("🧠 AutoDev Lite - AI Code Writer")

task_input = st.text_input("Enter your coding task (e.g., 'Write a Python function to check for prime numbers')")

# 🧠 AI agent
code_agent = Agent(
    role="Senior Python Developer",
    goal="Generate clean and correct Python code",
    backstory="Expert Python coder who helps developers by writing useful code snippets.",
    verbose=True,
    allow_delegation=False,
)

# ✅ Define the task
coding_task = Task(
    description=f"Write Python code to: {task_input}",
    agent=code_agent,
)

# 🚀 Run crew
crew = Crew(
    agents=[code_agent],
    tasks=[coding_task],
    verbose=True,
)

if st.button("Generate Code"):
    if not task_input.strip():
        st.warning("Please enter a coding task.")
    else:
        try:
            result = crew.kickoff()
            st.code(result, language="python")
        except Exception as e:
            st.error(f"❌ Error: {e}")
