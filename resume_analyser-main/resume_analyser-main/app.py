import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
from PIL import Image
import matplotlib.pyplot as plt

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(input)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

def input_pdf_text(uploaded_file):
    try:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in range(len(reader.pages)):
            page = reader.pages[page]
            text += str(page.extract_text())
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

def create_doughnut_chart(percentage):
    fig, ax = plt.subplots(figsize=(4, 4))
    sizes = [percentage, 100 - percentage]
    colors = ['#4CAF50', '#E0E0E0']
    explode = (0.1, 0)
    ax.pie(sizes, colors=colors, startangle=90, explode=explode, wedgeprops=dict(width=0.3))
    ax.text(0, 0, f'{percentage}%', ha='center', va='center', fontsize=20, fontweight='bold')
    ax.set_title("Match Percentage", fontsize=14)
    ax.axis('equal')
    return fig

# Remove custom CSS and modern UI
st.set_page_config(page_title="CareerCraft Resume Analyzer", layout="centered", page_icon="📝")

# Top image
try:
    st.image("resume_analyser-main/images/icon1.png", width=100)
except Exception:
    st.warning("Top icon image is missing.")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #1abc9c;
    }
    .main .block-container {
        background: transparent;
        color: #fff;
        border-radius: 16px;
        box-shadow: none;
        padding: 2rem 2rem 2rem 2rem;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    .stTextInput > div > div > input, .stTextArea textarea {
        background: #16a085;
        color: #fff;
    }
    .stButton > button {
        background: #00695c;
        color: #fff;
    }
    h1, h2, h3, h4, h5, h6, .stMarkdown, .stText, .stHeader, .stSubheader, .stExpander, .st-cq, .st-cv {
        color: #fff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
jd = st.text_area("Paste the job description here", height=150)

submit = st.button("Analyze Resume")

if submit:
    if uploaded_file is not None and jd:
        with st.spinner("Analyzing your resume with Gemini AI..."):
            text = input_pdf_text(uploaded_file)
            input_prompt = f"""
            As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the JD (Job Description) and meticulously identify any missing keywords with utmost accuracy.
            resume: {text}
            description: {jd}
            I want the response in the following structure:
            The first line indicates the percentage match with the job description (JD).
            The second line presents a list of missing keywords.
            The third section provides a profile summary.
            Mention the title for all the three sections.
            While generating the response put some space to separate all the three sections.
            """
            response = get_gemini_response(input_prompt)
        if response:
            # Parse response
            try:
                lines = response.split('\n')
                percent = 0
                missing_keywords = []
                summary = ""
                for i, line in enumerate(lines):
                    if "percent" in line.lower():
                        percent = int(''.join(filter(str.isdigit, line)))
                    elif "keyword" in line.lower():
                        missing_keywords = [kw.strip() for kw in line.split(':', 1)[-1].split(',') if kw.strip()]
                    elif "summary" in line.lower():
                        summary = '\n'.join(lines[i+1:]).strip()
                        break
                st.subheader("Results")
                st.write(f"Match Percentage: {percent}%")
                st.write("Missing Keywords:")
                if missing_keywords:
                    st.write(", ".join(missing_keywords))
                else:
                    st.success("No major keywords missing!")
                st.write("Profile Summary:")
                st.write(summary)
            except Exception as e:
                st.error("Could not parse the AI response. Please try again.")
        else:
            st.error("No response from Gemini AI. Please check your API key and try again.")
    else:
        st.warning("Please upload a PDF resume and paste a job description.")

# Middle image
try:
    st.image("resume_analyser-main/images/icon2.png", width=100)
except Exception:
    st.warning("Middle icon image is missing.")

# Footer
st.markdown("""
---
<center><small>Made with ❤️ using Streamlit & Google Gemini AI</small></center>
""", unsafe_allow_html=True)

# FAQ Section
st.markdown("---")
st.header("Frequently Asked Questions (FAQ)")

with st.expander("What file formats are supported for resume upload?"):
    st.write("Currently, only PDF files are supported for resume upload.")

with st.expander("Is my data safe and private?"):
    st.write("Yes, your data is processed securely and is never stored.")

with st.expander("What does the match percentage mean?"):
    st.write("The match percentage indicates how closely your resume matches the provided job description based on keywords and content.")

with st.expander("How can I improve my resume score?"):
    st.write("Focus on including the missing keywords and tailoring your resume to the job description for a higher match percentage.")

with st.expander("Who powers the AI analysis?"):
    st.write("The analysis is powered by Google Gemini AI.")

# Bottom image
try:
    st.image("resume_analyser-main/images/icon3.png", width=100)
except Exception:
    st.warning("Bottom icon image is missing.")
