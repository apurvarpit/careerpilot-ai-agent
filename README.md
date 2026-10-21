# CareerPilot AI Agent

CareerPilot is a small AI career assistant that can review CV content, tailor application materials to a job description, run interview practice, and create a role-specific learning plan.

## Run locally
1. Install Python 3.10 or newer.
2. In this folder, run: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`
4. Enter your OpenAI API key in the sidebar, or set `OPENAI_API_KEY` in your environment.

## Publish publicly on Streamlit Community Cloud
1. Create a GitHub repository and upload `app.py`, `requirements.txt`, and this README.
2. Sign in to Streamlit Community Cloud and choose **Create app**.
3. Select your repository, branch, and `app.py` as the main file.
4. In app settings, add `OPENAI_API_KEY` under **Secrets**. Never commit the key to GitHub.
5. Deploy. Share the resulting public app URL.

A public URL cannot be created from this project bundle alone: deployment requires signing in to a hosting account and configuring a secret/API key. Do not publish your private API key.

## Responsible use
- CareerPilot must not invent qualifications, employment history, certifications, or results.
- Review AI-generated material before submitting it to an employer.
- API usage may incur charges depending on the account and model.
