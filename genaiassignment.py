import streamlit as st
from groq import Groq

# Set your Groq API Key
GROQ_API_KEY = "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"  # Replace with your real key
client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="AI Assistant for Farmers", layout="centered")
st.title("🌾 AI Assistant for Farmers")

# Sidebar
with st.sidebar:
    st.header("Options")
    language = st.selectbox("Select Output Language", ["English", "Hindi"])
    st.markdown("---")
    st.markdown("💡 Ask about crop disease, fertilizer, pest control, etc.")

# Groq call function
def ask_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # or "llama3-8b-8192"
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"

# Ask a Question
st.header("🧑‍🌾 Ask a Question")
user_query = st.text_input("Enter your question (in English):", "")

if st.button("Get Advice"):
    if user_query:
        prompt = f"""
You are an agricultural assistant. Answer the following farmer query simply and clearly.
Translate to {language} if needed.

Query: {user_query}
"""
        answer = ask_groq(prompt)
        st.success("Advice:")
        st.write(answer)
    else:
        st.warning("Please enter a question.")

# Crop Care Plan
st.header("📋 Generate Crop Care Plan")
crop = st.text_input("Enter crop name (e.g., wheat, tomato):", "")

if st.button("Generate Plan"):
    if crop:
        plan_prompt = f"""
Generate a weekly crop care plan for a small-scale farmer growing {crop}.
Include irrigation, fertilizer, and pest control steps.
Translate to {language} if needed.
"""
        plan = ask_groq(plan_prompt)
        st.success("Crop Care Plan:")
        st.write(plan)
    else:
        st.warning("Please enter a crop name.")
