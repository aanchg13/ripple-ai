import streamlit as st
import anthropic
from dotenv import load_dotenv
import PyPDF2
import pandas as pd
import io
import json

load_dotenv()

client = anthropic.Anthropic()

st.set_page_config(page_title="UX Insight AI", page_icon="🔍", layout="wide")
st.title("🔍 UX Insight AI")
st.subheader("Upload user research transcripts and get instant insights")

uploaded_files = st.file_uploader(
    "Upload transcripts (TXT or PDF) or survey data (CSV)",
    type=["txt", "pdf", "csv"],
    accept_multiple_files=True
)

def extract_text(file):
    if file.type == "text/plain":
        return file.read().decode("utf-8")
    elif file.type == "application/pdf":
        reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
        return "\n".join([page.extract_text() for page in reader.pages])
    elif file.type == "text/csv":
        df = pd.read_csv(file)
        return df.to_string()

def analyze_transcript(text):
    prompt = f"""You are an expert UX researcher. Analyze the following user interview transcript and extract structured insights.

Return ONLY a valid JSON object with this exact structure, no other text before or after:
{{
  "themes": [
    {{
      "name": "theme name",
      "description": "brief description",
      "quotes": ["exact quote from transcript"],
      "frequency": 1,
      "severity": "high/medium/low"
    }}
  ],
  "pain_points": ["pain point 1", "pain point 2"],
  "user_needs": ["need 1", "need 2"],
  "summary": "2-3 sentence executive summary"
}}

Transcript:
{text}"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )

    response_text = message.content[0].text.strip()
    
    # Strip markdown code fences if present
    if response_text.startswith("```"):
        response_text = response_text.split("```")[1]
        if response_text.startswith("json"):
            response_text = response_text[4:]
    
    return json.loads(response_text.strip())

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")

    for file in uploaded_files:
        with st.expander(f"📄 {file.name}"):
            text = extract_text(file)
            st.text_area("Content preview", text[:500] + "...", height=150)

    if st.button("🔍 Analyze Transcripts", type="primary"):
        with st.spinner("Claude is analyzing your transcripts..."):
            all_texts = []
            for file in uploaded_files:
                file.seek(0)
                all_texts.append(extract_text(file))

            combined_text = "\n\n---NEW TRANSCRIPT---\n\n".join(all_texts)

            try:
                insights = analyze_transcript(combined_text)

                st.markdown("---")
                st.header("📊 Insights")

                st.subheader("📝 Executive Summary")
                st.info(insights["summary"])

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("🔴 Pain Points")
                    for point in insights["pain_points"]:
                        st.markdown(f"- {point}")

                with col2:
                    st.subheader("💡 User Needs")
                    for need in insights["user_needs"]:
                        st.markdown(f"- {need}")

                st.subheader("🗂️ Themes")
                for theme in insights["themes"]:
                    with st.expander(f"**{theme['name']}** — Severity: {theme['severity'].upper()}"):
                        st.write(theme["description"])
                        if theme["quotes"]:
                            st.markdown("**Supporting quotes:**")
                            for quote in theme["quotes"]:
                                st.markdown(f"> _{quote}_")

            except Exception as e:
                st.error(f"Something went wrong: {e}")