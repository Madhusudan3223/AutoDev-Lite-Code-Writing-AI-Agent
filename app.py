import streamlit as st
import os
from crewai import Agent, Task, Crew

# Set your OpenAI API key (streamlit secrets)
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="AutoDev Lite", page_icon="🤖")
st.title("🤖 AutoDev Lite: Code Writing AI Agent")

user_prompt = st.text_input("🧠 Enter your coding task:")

if st.button("Run AutoDev"):
    if not user_prompt:
        st.warning("Please enter a coding task!")
    else:
        with st.spinner("Running agents..."):

            # Define agents
            planner = Agent(
                role="Planner",
                goal="Break down the task into clear steps.",
                backstory="An experienced software architect.",
                verbose=True
            )

            coder = Agent(
                role="Coder",
                goal="Generate Python code from plan.",
                backstory="A detail-oriented Python developer.",
                verbose=True
            )

            tester = Agent(
                role="Tester",
                goal="Execute and verify the code.",
                backstory="A testing automation expert.",
                verbose=True
            )

            # Define tasks
            plan_task = Task(
                description=f"Understand and break down this prompt: {user_prompt}",
                expected_output="A step-by-step plan.",
                agent=planner
            )

            code_task = Task(
                description=f"Write Python code to solve this: {user_prompt}",
                expected_output="Working Python code.",
                agent=coder
            )

            test_task = Task(
                description="Run and test the code written by the Coder.",
                expected_output="Execution result or error.",
                agent=tester
            )

            # Create Crew
            crew = Crew(
                agents=[planner, coder, tester],
                tasks=[plan_task, code_task, test_task],
                verbose=True
            )

            result = crew.kickoff()
            st.success("✅ AutoDev Execution Completed")
            st.text_area("📋 Output:", result, height=400)
