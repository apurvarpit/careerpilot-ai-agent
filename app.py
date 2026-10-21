import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="CareerPilot AI", page_icon="🧭", layout="centered")
st.title("🧭 CareerPilot AI Agent")
st.caption("An AI career assistant for job seekers — improve a CV, tailor an application, or practise an interview.")

with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("OpenAI API key", type="password", help="Your key is used for this session only. Do not share it.")
    model = st.selectbox("Model", ["gpt-4.1-mini", "gpt-4.1"], index=0)
    st.caption("For a public deployment, configure OPENAI_API_KEY as a secret in your hosting platform instead of asking visitors for your key.")

task = st.radio("What would you like help with?", [
    "Review my CV",
    "Tailor my application",
    "Practise an interview",
    "Create a learning plan"
])
role = st.text_input("Target role", placeholder="e.g., Junior Data Engineer")
experience = st.text_area("Background / experience", placeholder="Paste relevant skills, experience, or a short CV summary.")
job_description = st.text_area("Job description (optional)", placeholder="Paste the vacancy description if you have one.")
question = st.text_area("Your request", placeholder="What should CareerPilot focus on?")

prompts = {
    "Review my CV": "Review the user's background for clarity, impact, relevance, and measurable achievements. Do not invent qualifications or experience. Give prioritized edits and an improved sample bullet.",
    "Tailor my application": "Tailor the user's real background to the supplied vacancy. Identify matching requirements, gaps, and draft a concise honest summary plus 3 tailored bullet points. Never fabricate experience.",
    "Practise an interview": "Act as a supportive interviewer for the target role. Ask one realistic question at a time. If the user asks for a complete practice pack, give questions, answer frameworks, and evaluation criteria.",
    "Create a learning plan": "Create a practical learning plan for the target role with milestones, hands-on projects, and ways to verify progress. Adapt to the user's background."
}

if st.button("Ask CareerPilot", type="primary", use_container_width=True):
    if not (api_key or os.getenv("OPENAI_API_KEY")):
        st.error("Add an API key in the sidebar or configure OPENAI_API_KEY in the hosting platform's secrets.")
    elif not (role.strip() or experience.strip() or question.strip()):
        st.warning("Enter at least a target role, background, or request.")
    else:
        with st.spinner("CareerPilot is preparing your response..."):
            try:
                client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
                system = (
                    "You are CareerPilot, a careful and practical AI career assistant. "
                    "Be specific, encouraging, and concise. Never invent credentials, employment, metrics, "
                    "certifications, or results. Clearly label assumptions and suggest human review for important applications. "
                    + prompts[task]
                )
                user = f"Task: {task}\nTarget role: {role}\nBackground: {experience}\nJob description: {job_description}\nSpecific request: {question}"
                response = client.responses.create(
                    model=model,
                    input=[{"role": "system", "content": system}, {"role": "user", "content": user}]
                )
                st.markdown("### CareerPilot's response")
                st.markdown(response.output_text)
            except Exception as exc:
                st.error(f"Could not complete the request. Check the API key, model access, and connection. Details: {exc}")

st.divider()
st.caption("Prototype notice: AI suggestions can be wrong. Verify facts and review all application materials before sending.")
