import streamlit as st
import os
from crewai import Agent, Task, Crew

# Get OpenAI API key from secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="AutoDev Lite", page_icon="🤖")
st.title("🤖 AutoDev Lite: Code Writing AI Agent")

user_prompt = st.text_input("🧠 Enter your coding task:")

if st.button("Run AutoDev"):
    if not user_prompt:
        st.warning("Please enter a coding task.")
    else:
        with st.spinner("Running agents..."):

            planner = Agent(
                role="Task Planner",
                goal="Break down coding tasks into steps.",
                backstory="You are an expert in task planning.",
                verbose=True,
            )

            coder = Agent(
                role="Python Coder",
                goal="Write clean Python code.",
                backstory="You are an experienced Python developer.",
                verbose=True,
            )

            tester = Agent(
                role="Code Tester",
                goal="Test the Python code and show output.",
                backstory="You are a QA engineer.",
                verbose=True,
            )

            plan_task = Task(
                description=f"Break down this prompt: {user_prompt}",
                expected_output="Step-by-step plan.",
                agent=planner,
            )

            code_task = Task(
                description=f"Write Python code for: {user_prompt}",
                expected_output="Working Python code.",
                agent=coder,
            )

            test_task = Task(
                description="Test the code and report the output.",
                expected_output="Result or error message.",
                agent=tester,
            )

            crew = Crew(
                agents=[planner, coder, tester],
                tasks=[plan_task, code_task, test_task],
                verbose=True,
            )

            result = crew.kickoff(inputs={"user_prompt": user_prompt})
            st.success("✅ Execution finished.")
            st.text_area("🧾 Output", result, height=300)
