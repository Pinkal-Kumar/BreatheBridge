# llm_utils.py
from langchain_ollama import OllamaLLM

# MODEL_NAME = "deepseek-r1:1.5b"  # or "deepseek-chat" or your custom model name
MODEL_NAME = "deepseek-llm:7b-chat"
# MODEL_NAME = "deepseek-coder:6.7b-instruct"
# Initialize Ollama LLM once
llm = OllamaLLM(
    model=MODEL_NAME,
    temperature=0.7,
    num_predict=128,
)

def deepseek_call(prompt: str) -> str:
    """
    Uses the Ollama-hosted DeepSeek model to generate a string response.
    """
    print(f"[🔍 Prompt to DeepSeek-Ollama]: {prompt}")
    response = llm.invoke(prompt)
    return response.strip()
