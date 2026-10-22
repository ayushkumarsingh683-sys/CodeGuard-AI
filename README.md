Markdown

# 🚀 CodeGuard-AI: AI-Powered Code Reviewer & Bug Fixing Agent

**CodeGuard-AI** is a full-stack developer assistant application built with **FastAPI**, **Streamlit**, and **Groq LLM**. It automatically scans code snippets for syntax errors, logical bugs, and security issues, provides clear explanations, and generates clean, production-ready fixed code.

---

## 📂 Project Structure

```text
CodeGuard-AI/
│
├── backend/
│   ├── __init__.py
│   ├── main.py          # FastAPI application & API endpoints
│   ├── agents.py        # Groq LLM integration & AI analysis logic
│   └── prompts.py       # System prompts for code review guidelines
│
├── frontend/
│   └── app.py           # Streamlit user interface dashboard
│
├── .env                 # Environment variables (Groq API Key)
├── .gitignore
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

🛠️ Tech Stack

    Frontend: Streamlit

    Backend: FastAPI, Pydantic, Uvicorn

    AI Engine: Groq API (openai/gpt-oss-120b)

    Environment Management: Python-dotenv
🏛️ System Architecture & Workflow

CodeGuard-AI ek clean, decoupled Client-Server Architecture par kaam karta hai jisme frontend aur backend alag-alag layers par communicate karte hain.
Plaintext

+-----------------------+              +-----------------------+              +------------------------+
|   Streamlit Frontend  |  HTTP (JSON) |    FastAPI Backend    |  Groq SDK    |    Groq LLM Engine     |
|   (Port: 8501)        | -----------> |    (Port: 8000)       | -----------> |  (openai/gpt-oss-120b) |
|  - User UI Dashboard  |              |  - Request Validation |              |  - Code Reasoning      |
|  - Code Input & View  | <----------- |  - Agent Logic Routing| <----------- |  - Structured JSON     |
+-----------------------+              +-----------------------+              +------------------------+

🔄 Request Flow:

    User Input: User Streamlit dashboard par koi bhi buggy code paste karke "Analyze & Fix Code" button click karta hai.

    API Request: Streamlit frontend ek HTTP POST request bhejta hai FastAPI backend ko ([http://127.0.0.1:8000/analyze](http://127.0.0.1:8000/analyze)), jisme code snippet JSON format mein hota hai.

    AI Agent Processing: FastAPI backend backend/agents.py ke zariye Groq client ko trigger karta hai, jahan openai/gpt-oss-120b model system prompt ke rules ke mutabiq code ko analyze karta hai.

    Structured JSON Response: Groq LLM bugs, explanations, aur fixed code ko ek structured JSON object ke roop mein return karta hai.

    UI Rendering: FastAPI us JSON ko validate karke frontend ko bhejta hai, aur Streamlit usko clean UI components (Markdown, Code Blocks) mein user ke samne display kar deta hai.

⚡ Getting Started & Installation
1. Clone the Repository
Bash

git clone [https://github.com/YOUR_USERNAME/CodeGuard-AI.git](https://github.com/YOUR_USERNAME/CodeGuard-AI.git)
cd CodeGuard-AI

2. Set Up Virtual Environment
Bash

python -m venv venv
venv\Scripts\activate     # For Windows

3. Install Dependencies
Bash

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the root directory and add your Groq API key:
Code snippet

GROQ_API_KEY=your_actual_groq_api_key_here

🚀 Running the Application

You need to run both the FastAPI backend and Streamlit frontend in separate terminals.
Terminal 1: Run FastAPI Backend
Bash

python -m uvicorn backend.main:app --reload

(Backend runs at: http://127.0.0.1:8000)
Terminal 2: Run Streamlit Frontend
Bash

streamlit run frontend/app.py

(Frontend runs at: http://localhost:8501)
💡 How to Use

    Open the Streamlit web dashboard in your browser.

    Paste any buggy Python or Java code snippet into the text input area.

    Click "🚀 Analyze & Fix Code".

    View detected bugs, detailed explanations, and the optimized fixed code instantly!

👨‍💻 Author

Ayush Kumar Singh
