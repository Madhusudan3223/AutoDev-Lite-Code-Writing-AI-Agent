import streamlit as st
import os
from crewai import Agent, Task, Crew

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.title("🧠 AutoDev Lite - AI Code Writer")

developer = Agent(
    role="Python Developer",
    goal="Write clean Python code for given tasks",
    backstory="Expert in problem-solving using Python.",
    verbose=True
)

task = Task(
    description="Write a Python program to check whether a number is prime.",
    expected_output="A working Python script for prime number check",
    agent=developer
)

crew = Crew(agents=[developer], tasks=[task], verbose=True)

if st.button("Generate Code"):
    result = crew.run()
    st.code(result, language="python")
