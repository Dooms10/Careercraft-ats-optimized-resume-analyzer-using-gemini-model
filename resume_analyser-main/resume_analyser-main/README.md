# CareerCraft: ATS-Optimized Resume Analyzer Using Gemini Model - README

This project implements a resume analysis tool using Google Generative AI. The application is hosted on a Streamlit web application and allows users to upload resumes and input job descriptions for analysis, providing feedback on the compatibility of the resume with the job description.

## Features

- User-friendly UI with sections for uploading resumes, entering job descriptions, and viewing analysis results.
- PDF resume text extraction.
- Analysis of resumes using Google Generative AI.
- Custom styling for an enhanced user experience.

## Technologies Used

- **Streamlit**: A web application framework used to create the user interface.
- **Python**: The programming language used to develop the application.
- **Google Generative AI**: The AI model used to analyze resumes.
- **dotenv**: A Python library to load environment variables from a `.env` file.
- **PyPDF2**: Used to extract text from PDF files.
- **PIL (Python Imaging Library)**: Used for handling images within the app.

## How It Works

1. **Environment Setup**:
    - The application loads the API key from a `.env` file using the `dotenv` library.
    - The API key is used to configure the Google Generative AI client.

2. **Streamlit Application**:
    - The app initializes with a clean UI layout, including sections for uploading resumes, entering job descriptions, and viewing analysis results.
    - The `input_pdf_text` function extracts text from uploaded PDF resumes.
    - The `get_gemini_response` function sends the resume text and job description to the AI model and retrieves the analysis.

3. **User Interaction**:
    - Users upload their resumes in PDF format and enter job descriptions.
    - The application displays a spinner while waiting for the AI's analysis.
    - Once the analysis is complete, the results are displayed in the UI.

4. **Resume Analysis**:
    - The analysis includes a percentage match with the job description, a list of missing keywords, and a profile summary.
    - The results help users understand how well their resume matches the job description and identify areas for improvement.

## Setup Instructions

1. **Clone the Repository**:
    ```sh
    git clone <repository_url>
    cd resume-ats-tracker
    ```

2. **Install Dependencies**:
    ```sh
    pip install streamlit python-dotenv google-generativeai pypdf2 pillow
    ```

3. **Create a `.env` File**:
    - Add your Google API key to the `.env` file:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

4. **Run the Application**:
    ```sh
    streamlit run app.py
    ```

## File Structure

- `app.py`: The main application file containing the Streamlit app code.
- `.env`: Environment file containing the Google API key.

## Usage Instructions

1. **Start the application** by running `streamlit run app.py`.
2. **Upload your resume** in PDF format.
3. **Enter the job description** in the provided text area.
4. **Click "Submit"** to analyze your resume.
5. **View the analysis results** including the match percentage, missing keywords, and profile summary.
6. **Optimize your resume** based on the provided feedback.

## Deployment Link
- [Resume Analyzer](https://resume-analyser-q098.onrender.com)

## Acknowledgements

- [Streamlit](https://streamlit.io/) for providing an easy-to-use web app framework.
- [Google Generative AI](https://developers.generativeai.google/) for the powerful AI model.
- [dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF text extraction.
- [PIL](https://pillow.readthedocs.io/en/stable/) for image handling in Python.
