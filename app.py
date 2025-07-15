import streamlit as st
import os
from crewai import Agent, Task, Crew

# ✅ Set your OpenAI key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# 🧠 Streamlit UI
st.set_page_config(page_title="AutoDev Lite", page_icon="🧠")
st.title("🧠 AutoDev Lite - AI Code Writer")

# 📝 User input
prompt = st.text_area("Enter your coding task (e.g., 'Write a Python function to check for prime numbers'):")

# 🚀 Generate Code
if st.button("Generate Code"):
    if prompt.strip() == "":
        st.warning("Please enter a valid coding task.")
    else:
        # 🤖 Define the AI Agent
        developer = Agent(
            role="Senior Python Developer",
            goal="Write clean and functional Python code",
            backstory="You are an expert Python developer who helps others write accurate code with explanations.",
            verbose=True
        )

        # 📋 Define the Task
        task = Task(
            description=prompt,
            expected_output="A working Python function or script with comments.",
            agent=developer
        )

        # 🛠️ Assemble the Crew
        crew = Crew(
            agents=[developer],
            tasks=[task],
            verbose=True
        )

        # 🏁 Run the Agent Task
        try:
            result = crew.run()
            st.success("✅ Code Generated Successfully!")
            st.code(result, language="python")
        except Exception as e:
            st.error(f"❌ Error: {e}")
