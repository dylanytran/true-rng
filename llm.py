from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import hashlib
import requests

# Specify the model name from Hugging Face model hub
model_name = "openai-community/gpt2"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Encode input text
input_text = "This is a"
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
text_hash = int(hex_dig, 16)  # Convert the hexadecimal digest to an integer

# Random.org atmospheric noise
API_KEY = '0f45c68a-3097-4388-875a-29ba60d6744a'

def generate_atmosphere():
    url = f'https://www.random.org/integers/?num=1&min=1&max=100000000&col=1&base=10&format=plain&rnd=new&apiKey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return int(response.text.strip())
    else:
        print('Error:', response.status_code)
        return None

# Generate a random number
atmospheric_value = generate_atmosphere()

print(generated_text)
print('Text hash: ', text_hash)
small_hash = text_hash % 1000000000
print('small hash: ', small_hash)
print('Atmospheric noise:', atmospheric_value)

sum = small_hash + atmospheric_value
xor = small_hash ^ atmospheric_value
print('sum: ', sum)
print('xor: ', xor)
