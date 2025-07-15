import streamlit as st
import os
from crewai import Agent, Task, Crew

# Set your OpenAI API key using Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# App layout
st.set_page_config(page_title="AutoDev Lite", page_icon="🤖")
st.title("🤖 AutoDev Lite: Code Writing AI Agent")
st.markdown("Type any coding task below and let the agents plan, code, and test it for you!")

# User input
user_prompt = st.text_input("🧠 Enter your coding task:", placeholder="e.g., Write a Python program to check prime number")

if st.button("🚀 Run AutoDev"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a valid coding task.")
    else:
        with st.spinner("🤖 Agents are working..."):

            # Define agents
            planner_agent = Agent(
                role='Planner',
                goal='Break down coding tasks into clear steps.',
                backstory='You are an expert software project planner.',
                allow_delegation=False,
                verbose=True
            )

            coder_agent = Agent(
                role='Coder',
                goal='Write clean, correct Python code for the given task.',
                backstory='You are a Python coding expert.',
                allow_delegation=False,
                verbose=True
            )

            tester_agent = Agent(
                role='Tester',
                goal='Test and verify the Python code works.',
                backstory='You are responsible for code validation and testing.',
                allow_delegation=False,
                verbose=True
            )

            # Define tasks
            plan_task = Task(
                description=f"Break down the task: '{user_prompt}' into steps.",
                expected_output="A clear plan with steps to solve the coding problem.",
                agent=planner_agent
            )

            code_task = Task(
                description=f"Write Python code based on the plan for: '{user_prompt}'.",
                expected_output="Working Python code for the task.",
                agent=coder_agent
            )

            test_task = Task(
                description="Run and validate the code written above. Report success or errors.",
                expected_output="Result of code execution or errors.",
                agent=tester_agent
            )

            # Create the crew
            crew = Crew(
                agents=[planner_agent, coder_agent, tester_agent],
                tasks=[plan_task, code_task, test_task],
                verbose=True
            )

            # Run the crew
            result = crew.kickoff()
            st.success("✅ AutoDev Execution Complete")
            st.text_area("📋 Final Output:", result, height=400)
