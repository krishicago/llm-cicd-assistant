# backend/llm_engine.py
import os
from llama_cpp import Llama

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(base_dir, "models", "mistral-7b-instruct-v0.1.Q4_K_M.gguf")

llm = Llama(
    model_path=model_path,
    n_ctx=2048,
    n_threads=8,
    temperature=0.2,
)

def summarize_diff(diff_text):
    prompt = f"[INST] Summarize this pull request diff:\n{diff_text} [/INST]"
    output = llm(prompt, max_tokens=300, stop=["</s>"])
    return output["choices"][0]["text"].strip()
