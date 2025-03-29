from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login

login(token="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")

def download_model(model_name, model_dir):
    """
    Downloads the specified model and tokenizer from Hugging Face and saves them locally.
    """
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model.save_pretrained(model_dir)
    tokenizer.save_pretrained(model_dir)

# Example usage:
download_model("meta-llama/Llama-3.1-8B", "llama/")
download_model("mistralai/Mistral-7B-v0.1", "mistral/")
# download_model("smol-ai/SmolLM", "models/smollm/")
