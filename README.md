# LLM-Powered CI/CD Assistant

A lightweight, production-ready FastAPI service that integrates a **locally hosted Mistral LLM** with your CI/CD pipeline to automatically **summarize pull request diffs**. Designed for intelligent code review and automation of documentation within development workflows.

---

## ✨ Features

- Accepts code diffs via HTTP POST requests  
- Uses **Mistral-7B Instruct** (via `llama-cpp-python`) for summarization  
- Fast, local inference with no OpenAI or cloud dependency  
- Ready to integrate with GitHub Actions for PR workflows  

---

## 📂 Project Structure
llm-cicd-assistant/
├── backend/
│   ├── main.py               # FastAPI server
│   ├── llm_engine.py         # Mistral integration logic
├── models/
│   └── mistral-7b-instruct-v0.1.Q4_K_M.gguf  # Your local LLM file
├── .github/
│   └── workflows/
│       └── pr-review.yaml    # (To be added) GitHub Action
├── requirements.txt
├── README.md
└── .gitignore

## Duplicating this in your system:

### 1. Clone this repository
git clone https://github.com/YOUR_USERNAME/llm-cicd-assistant.git
cd llm-cicd-assistant

### 2. Set Up Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 3. Place the Mistral Model
Download mistral-7b-instruct-v0.1.Q4_K_M.gguf and place it in the models/ directory. I used Mistral here during the initial developments of this project but any model is recommended

### 4.  Run the Server
uvicorn backend.main:app --reload --port 8000


### 4. Example request:
curl -X POST http://localhost:8000/pr-review \
  -H "Content-Type: application/json" \
  -d '{"diff": "diff --git a/app.py b/app.py\n+ print(\"Hello World\")", "pr_number": "1"}'

### 5. Requirements
Python 3.8+

llama-cpp-python

FastAPI, uvicorn
