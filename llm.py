
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import hashlib

# Specify the model name from Hugging Face model hub
model_name = "openai-community/gpt2"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Encode input text
input_text = "This is a "
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Create attention mask
attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

# Generate text with adjusted parameters
outputs = model.generate(
    input_ids,
    max_length=100,
    num_return_sequences=1,
    temperature=0.7,  # Adjust the temperature to add randomness
    top_k=50,  # Use top-k sampling
    top_p=0.95,  # Use top-p sampling
    repetition_penalty=1.2,  # Apply a repetition penalty
    do_sample=True,  # Enable sampling
    pad_token_id=tokenizer.eos_token_id,  # Set pad token to eos token
    attention_mask=attention_mask  # Pass attention mask
)

# Decode the generated text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
hash_object = hashlib.sha256(generated_text.encode())
hex_dig = hash_object.hexdigest()
hash_value = int(hex_dig, 16)  # Convert the hexadecimal digest to an integer

print(generated_text)
print(hash_value)
