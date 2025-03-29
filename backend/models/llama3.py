# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer
# # from huggingface_hub import login

# # login(token="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")

# class Llama3Model:
#     def __init__(self, model_name="meta-llama/Llama-3.1-8B", device="cuda" if torch.cuda.is_available() else "cpu"):
#         self.device = device
#         self.tokenizer = AutoTokenizer.from_pretrained(model_name)
#         self.model = AutoModelForCausalLM.from_pretrained(
#             model_name, torch_dtype=torch.float16 if device == "cuda" else torch.float32
#         ).to(self.device)

#     def generate_text(self, prompt, max_length=200):
#         inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
#         with torch.no_grad():
#             outputs = self.model.generate(**inputs, max_length=max_length)
        
#         return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


# # Test the model (only runs when the script is executed directly)
# if __name__ == "__main__":
#     model = Llama3Model()
#     test_prompt = "Explain quantum physics in simple words."
#     print("Response:", model.generate_text(test_prompt))

from transformers import AutoModelForCausalLM, AutoTokenizer

class Llama3Model:
    def __init__(self):
        self.model_name = "meta-llama/Llama-3.1-8B"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

    def generate_response(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
