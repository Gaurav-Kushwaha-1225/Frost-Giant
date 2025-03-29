# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

# def evaluate_model(model_dir, test_prompts, max_length=100):
#     # Load the tokenizer and fine-tuned model
#     tokenizer = AutoTokenizer.from_pretrained(model_dir)
#     model = AutoModelForCausalLM.from_pretrained(model_dir)

#     # Ensure model is in evaluation mode
#     model.eval()
    
#     results = []
    
#     for prompt in test_prompts:
#         # Tokenize the input prompt
#         inputs = tokenizer(prompt, return_tensors="pt")

#         # Generate response from the model
#         with torch.no_grad():
#             output = model.generate(
#                 **inputs,
#                 max_length=max_length,
#                 temperature=0.7,  # Adjusts randomness of predictions
#                 top_k=50,  # Keeps top 50 words with the highest probability
#                 top_p=0.9,  # Nucleus sampling
#                 do_sample=True  # Enables sampling for variability
#             )

#         # Decode generated output
#         generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
#         results.append({"prompt": prompt, "response": generated_text})
    
#     return results


# # Example Usage
# if __name__ == "__main__":
#     test_prompts = [
#         "Explain the theory of relativity.",
#         "How does a neural network work?",
#         "Write a short story about a space adventure."
#     ]

#     model_directory = "user_models/xyz/"
#     responses = evaluate_model(model_directory, test_prompts)

#     for res in responses:
#         print(f"Prompt: {res['prompt']}")
#         print(f"Response: {res['response']}\n")

from models.llama3 import Llama3Model
from user_models.trained import TrainedModel

def evaluate_model(model_path, prompt):
    model = TrainedModel.load_model(Llama3Model, model_path)
    return model.generate_response(prompt)

if __name__ == "__main__":
    model_path = "user_models/llama3_finetuned.pth"
    print(evaluate_model(model_path, "Explain AI fine-tuning"))
