import streamlit as st
import os
from crewai import Agent, Task, Crew

# ✅ Securely load OpenAI API key from Streamlit Secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# ✅ Streamlit UI setup
st.set_page_config(page_title="AutoDev Lite", page_icon="🤖")
st.title("🤖 AutoDev Lite: Code Writing AI Agent")
st.markdown("🧠 Enter your coding task below and get instant results!")

# ✅ User input
user_prompt = st.text_input("📝 Enter your coding task:")

# ✅ Button to trigger agents
if st.button("Run AutoDev"):
    if not user_prompt:
        st.warning("⚠️ Please enter a coding task!")
    else:
        with st.spinner("⏳ Running agents..."):

            # 1. Define agents
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
                goal='Test the code and report output or errors.',
                backstory='You are a QA engineer responsible for verifying correctness.',
                verbose=True
            )

            # 2. Define tasks
            plan_task = Task(
                description="Understand the user prompt: '{{ user_prompt }}'. Break it into clear steps.",
                expected_output="A step-by-step plan to solve the problem.",
                agent=planner_agent
            )

            code_task = Task(
                description="Use the plan to write Python code. Prompt: '{{ user_prompt }}'",
                expected_output="Python code that matches the user's request.",
                agent=coder_agent
            )

            test_task = Task(
                description="Test the code from the coder agent and show output or errors.",
                expected_output="Code output or traceback.",
                agent=tester_agent
            )

            # 3. Execute crew
            crew = Crew(
                agents=[planner_agent, coder_agent, tester_agent],
                tasks=[plan_task, code_task, test_task],
                verbose=True
            )

            result = crew.kickoff(inputs={"user_prompt": user_prompt})

        # ✅ Display output
        st.success("✅ AutoDev Execution Completed")
        st.text_area("📋 Output:", result, height=400)
