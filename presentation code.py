from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import hashlib
import requests

model_name = "openai-community/gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def gen_text(prompt):

    input_text = prompt
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    
    # generate text with adjusted parameters
    outputs = model.generate(
        input_ids,
        max_length=100,
        num_return_sequences=1,
        temperature=0.7, 
        top_k=50, 
        top_p=0.95,  
        repetition_penalty=1.2,  
        do_sample=True, 
        pad_token_id=tokenizer.eos_token_id,  
        attention_mask=attention_mask  
    )

    # decode the generated text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def gen_hash(text):
    hash_object = hashlib.sha256(text.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)


# Random.org atmospheric noise
API_KEY = '0f45c68a-3097-4388-875a-29ba60d6744a'

def gen_atmosphere():
    url = f'https://www.random.org/integers/?num=1&min=1&max=100000000&col=1&base=10&format=plain&rnd=new&apiKey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return int(response.text.strip())
    else:
        print('Error:', response.status_code)
        return None


def rand_gen(min, max):
    # AI
    generated_text = gen_text("This is a")
    print("\nRandom sentence: ", generated_text)

    text_hash = gen_hash(generated_text)
    print("\nSHA-256 hash: ", text_hash)

    small_hash = text_hash % 1000000000
    print("\nShortened hash: ", small_hash)

    
    # atmospheric noise
    atmospheric_value = gen_atmosphere()
    print("\nAtmospheric noise: ", atmospheric_value)

    xor = small_hash ^ atmospheric_value
    print("\nXOR value: ", xor)
    
    rang = max - min + 1
    final_val = (xor % rang) + min
    return final_val

print("\nPlease enter a minimum value.")
min = int(input())

print("\nPlease enter a maxmimum value.")
max = int(input())

print("\nYour random number is : ", rand_gen(min, max), "\n")