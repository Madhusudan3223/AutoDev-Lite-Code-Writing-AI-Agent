import streamlit as st
import os
from crewai import Agent, Task, Crew

st.set_page_config(page_title="AutoDev Lite", page_icon="🤖")
st.title("🤖 AutoDev Lite: Code Writing AI Agent")

user_prompt = st.text_input("🧠 Enter your coding task:")

if st.button("Run AutoDev"):
    if not user_prompt:
        st.warning("Please enter a coding task!")
    else:
        with st.spinner("Running agents..."):

            # Agents
            planner_agent = Agent(
                role='Task Planner',
                goal='Break down coding tasks into clear steps.',
                backstory='You are a senior software architect.',
                verbose=True
            )

            coder_agent = Agent(
                role='Code Writer',
                goal='Write Python code based on the task plan.',
                backstory='You are a Python expert who writes clean code.',
                verbose=True
            )

            tester_agent = Agent(
                role='Code Tester',
                goal='Test the generated Python code and report output or errors.',
                backstory='You are a QA engineer.',
                verbose=True
            )

            # Tasks
            plan_task = Task(
                description="Understand the user prompt: '{{ user_prompt }}'. Break it into clear steps.",
                expected_output="Step-by-step plan to solve the problem.",
                agent=planner_agent
            )

            code_task = Task(
                description="Write Python code based on the plan. Prompt: '{{ user_prompt }}'",
                expected_output="Working Python code.",
                agent=coder_agent
            )

            test_task = Task(
                description="Test the code and report output or issues.",
                expected_output="Code output or error.",
                agent=tester_agent
            )

            crew = Crew(
                agents=[planner_agent, coder_agent, tester_agent],
                tasks=[plan_task, code_task, test_task],
                verbose=True
            )

            result = crew.kickoff(inputs={"user_prompt": user_prompt})
            st.success("✅ AutoDev Execution Completed")
            st.text_area("📋 Output:", result, height=300)
