import streamlit as st
import os

HISTORY_FILE = "history.txt"

# ---------- Core Functions ----------

def show_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, 'r') as file:
        lines = file.readlines()
    return list(reversed([line.strip() for line in lines]))

def clear_history():
    open(HISTORY_FILE, 'w').close()

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        return "❌ Invalid input. Use format: number operator number (e.g., 8 + 2)"

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        return "❌ Please enter valid numbers."

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            return "❌ Cannot divide by zero."
        result = num1 / num2
    else:
        return "❌ Invalid operator. Use only + - * /"

    if int(result) == result:
        result = int(result)

    save_to_history(user_input, result)
    return f"✅ Result: {result}"

# ---------- Streamlit UI ----------

st.set_page_config(page_title="Calculator with History", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator with History")
st.write("Enter your expression in the format: `number operator number` (e.g., `8 + 2`)")

# Input field
user_input = st.text_input("Calculation", placeholder="Example: 10 * 5")

if st.button("Calculate"):
    if user_input.strip():
        result = calculate(user_input)
        st.success(result)

# Show history
st.markdown("## 📜 History")
history = show_history()
if history:
    st.code("\n".join(history))
else:
    st.info("No history found.")

# Clear history
if st.button("🗑️ Clear History"):
    clear_history()
    st.warning("History has been cleared.")

# Footer
# Footer with LinkedIn link
st.markdown("""
    <hr>
    <div style='text-align: center; color: gray; font-size: 16px;'>
        🚀 Built by Maria Khan | Python + Streamlit 💻 <br>
        🔗 Connect with me on 
        <a href="https://www.linkedin.com/in/maria-khan-52b527295/n" target="_blank" style="color: #0077b5; text-decoration: none; font-weight: bold;">
            LinkedIn
        </a>
    </div>
""", unsafe_allow_html=True)

