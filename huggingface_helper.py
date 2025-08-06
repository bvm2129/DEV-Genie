# huggingface_helper.py
from huggingface_hub import InferenceClient, login
# Cache clients per model
client_cache = {}

def generate_response(prompt, model, huggingface_token):
    # If not cached, create a new InferenceClient
    if model not in client_cache:
        client_cache[model] = InferenceClient(model=model, token=huggingface_token)

    client = client_cache[model]
    model = model
    
    # Text generation
    response = client.text_generation(prompt, model=model, max_new_tokens=100, do_sample=True)
    return response