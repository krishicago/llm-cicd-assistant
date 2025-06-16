# backend/main.py
from fastapi import FastAPI, Request
from backend.llm_engine import summarize_diff

app = FastAPI()

@app.post("/pr-review")
async def pr_review(request: Request):
    data = await request.json()
    diff = data.get("diff", "")
    pr_number = data.get("pr_number", "N/A")

    summary = summarize_diff(diff)
    return {"pr_number": pr_number, "summary": summary}
