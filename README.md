# Careercraft-ats-optimized-resume-analyzer-using-gemini-model
This project is a resume analysis tool built with Google Generative AI. It uses a Streamlit web app where users can upload their resume and a job description to get feedback on how well the resume matches the job.

## Features 

Easy-to-use interface with options to upload resumes, enter job descriptions, and see results.
Reads and extracts text from PDF resumes.
Uses Google Generative AI to analyze resumes.
Clean design with custom styling for better user experience.

## Technologies Used

Streamlit: Used to build the app’s user interface.
Python: The main programming language for the project.
Google Generative AI: Used to analyze and compare resumes.
dotenv: Helps keep secret keys and settings safe using a .env file.
PyPDF2: Extracts text from PDF resumes.
PIL: Used to work with images in the app.

## How It Works
1. **Setting Up**:
   * The app uses the `dotenv` library to load the API key from a `.env` file.
   * This key is used to connect with Google Generative AI.

2. **How the App Works (Streamlit)**:

   * The app has a clean layout where users can upload their resume, add a job description, and see the results.
   * It uses a function to read text from the uploaded PDF.
   * Another function sends this text and job description to the AI and gets the analysis.

3. **What Users Do**:

   * Users upload a PDF resume and type in the job description.
   * While the AI works, a spinner is shown.
   * Once done, the app shows the analysis.

4. **What the AI Tells You**:

   * It gives a match percentage, shows any missing keywords, and provides a short profile summary.
   * This helps users see how well their resume fits the job and what can be improved.

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


## Acknowledgements

- [Streamlit](https://streamlit.io/) for providing an easy-to-use web app framework.
- [Google Generative AI](https://developers.generativeai.google/) for the powerful AI model.
- [dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF text extraction.
- [PIL](https://pillow.readthedocs.io/en/stable/) for image handling in Python.
