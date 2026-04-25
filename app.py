import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("🤖 AI Content Generator")

content_type = st.selectbox(
    "Select Content Type",
    ["Blog Post", "Instagram Caption", "Email"]
)

topic = st.text_input("Enter Topic")

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Casual", "Funny"]
)

st.caption("Note: Runs in demo mode if API quota is unavailable.")

if st.button("Generate Content"):
    if topic == "":
        st.warning("Please enter a topic")
    else:
        prompt = f"Write a {tone} {content_type} about {topic} in 100 words"

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            result = response.choices[0].message.content

        except Exception:
            result = f"""
            [Demo Output]

            This is a sample {content_type.lower()} on "{topic}" written in a {tone.lower()} tone.

            Artificial Intelligence is transforming industries by improving efficiency,
            enabling automation, and enhancing decision-making.
            """

        st.subheader("Generated Content:")
        st.write(result)

