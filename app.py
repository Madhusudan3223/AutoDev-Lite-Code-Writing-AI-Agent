import streamlit as st
from datetime import datetime

st.set_page_config(page_title="🤖 AutoDev Lite", page_icon="🧠")

st.title("🤖 AutoDev Lite: Code Writing AI Agent")
st.markdown("🧠 *Enter your coding task below and get instant results!*")

task = st.text_area("📝 Enter your coding task:")

if st.button("🚀 Run Task"):
    if task:
        with st.spinner("Thinking... 🤔"):
            # === Simple example handler ===
            if "palindrome" in task.lower():
                st.code("""
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
""", language='python')
                st.success("✅ Code generated for palindrome check.")
            
            elif "sort" in task.lower() and "list" in task.lower():
                st.code("""
numbers = [12, 5, 23, 1, 34, 89, 67]
numbers.sort()
print("Sorted list:", numbers)
""", language='python')
                st.success("✅ Code generated for sorting list.")

            elif "sum" in task.lower():
                st.code("""
a = 5
b = 3.5
print("The sum of", a, "and", b, "is", a + b)
""", language='python')
                st.success("✅ Code generated for sum.")

            else:
                st.warning("⚠️ This is a demo. Add more logic for advanced tasks.")
    else:
        st.error("❌ Please enter a coding task.")
