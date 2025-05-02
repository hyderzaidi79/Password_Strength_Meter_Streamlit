import streamlit as st
import re

st.title("🔒:rainbow[Password Strength Meter]")

if "password_visible" not in st.session_state:
    st.session_state.password_visible = False

def toggle_password():
    st.session_state.password_visible = not st.session_state.password_visible

password = st.text_input(
    "Enter Your Password",
    type="text" if st.session_state.password_visible else "password"
)


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if score == 4:
        return "✅ Strong Password!", "green", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "orange", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions below.", "red", feedback

if password:
    strength_msg, color, suggestions = check_password_strength(password)
    st.markdown(f"<h4 style='color: {color};'>{strength_msg}</h4>", unsafe_allow_html=True)

    if suggestions:
        for suggestion in suggestions:
            st.write(suggestion)
