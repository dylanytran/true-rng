from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import hashlib
import requests

def index(request):
    return HttpResponse("Welcome to the Random Number Generator API: Django backend is active.")

llm = "openai-community/gpt2"
tokenizer = AutoTokenizer.from_pretrained(llm)
model = AutoModelForCausalLM.from_pretrained(llm)

def gen_text(prompt):
    input_text = prompt
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    
    # generate text with adjusted parameters
    outputs = model.generate(
        input_ids,
        max_length = 100,
        num_return_sequences = 1,
        temperature = 0.7,
        top_k = 50, 
        top_p = 0.95, 
        repetition_penalty = 1.2, 
        do_sample =True,
        pad_token_id = tokenizer.eos_token_id, 
        attention_mask = attention_mask 
    )

    # decode the generated text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# hash with SHA-256
def hash(text):
    hash_object = hashlib.sha256(text.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)


# call atmospheric noise api to get random number
API_KEY = '0f45c68a-3097-4388-875a-29ba60d6744a'

def get_atm_noise():
    url = f'https://www.random.org/integers/?num=1&min=1&max=100000000&col=1&base=10&format=plain&rnd=new&apiKey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return int(response.text.strip())
    else:
        print('Error:', response.status_code)
        return None


def gen_rand(request, min, max):
    if min > max:
        return JsonResponse({'error': 'Min value cannot be greater than max value'})
    
    # random number from GPT
    generated_text = gen_text("This is a")
    text_hash = hash(generated_text)
    small_hash = text_hash % 1000000000
    
    # random number from atmospheric noise
    atm_value = get_atm_noise()
    xor = small_hash ^ atm_value
    
    # final random number
    range = max - min + 1
    final_val = (xor % range) + min
    return JsonResponse({'random number': final_val})
