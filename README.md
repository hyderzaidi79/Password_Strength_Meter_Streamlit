# 🔒 Password Strength Meter (Streamlit App)

An interactive web app built using **Streamlit** that allows users to check the strength of their passwords in real time. It provides helpful suggestions to improve password security using common best practices.

---

## 🌟 Features

- ✅ Real-time password strength evaluation
- 🧠 Smart feedback with improvement tips
- 👁️ Toggle password visibility
- 🎨 Color-coded feedback: **Green** (Strong), **Orange** (Moderate), **Red** (Weak)
- 🌐 Easy to deploy and run in-browser using Streamlit

---

## 🛠 Built With

- Python 3.x
- [Streamlit](https://streamlit.io/)
- `re` (Regex) module for pattern matching

---

## 🚀 How to Run

### 1. Install dependencies:
```bash
pip install streamlit

2. Save the script as password_strength_meter.py
3. Run the Streamlit app:

streamlit run password_strength_meter.py

🔍 Password Evaluation Criteria

The app checks your password against the following rules:
Rule	Points
🔤 At least 8 characters long	1
🔠 Contains both uppercase & lowercase	1
🔢 Includes at least one number (0-9)	1
🔣 Contains a special character (!@#$%^&*)	1

    4 Points → ✅ Strong

    3 Points → ⚠️ Moderate

    <3 Points → ❌ Weak

🧪 Example Output

    ✅ Strong Password!
    ❌ Password should be at least 8 characters long.
    ❌ Include at least one special character (!@#$%^&*).

💡 Future Enhancements

    Password entropy calculation

    Dark mode support

    Save password strength history (optional)

    Custom rule configuration for enterprise use

📄 License

This project is licensed under the MIT License.

