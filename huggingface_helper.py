# huggingface_helper.py
from huggingface_hub import InferenceClient, login
# Cache clients per model
client_cache = {}

def generate_response(prompt, model, huggingface_token):
    # If not cached, create a new InferenceClient
    if model not in client_cache:
        client_cache[model] = InferenceClient(model=model, token=huggingface_token)

    client = client_cache[model]

    # ❌ DON'T pass model again — it's already baked into the client
    try:
        response = client.text_generation(prompt, max_new_tokens=100, do_sample=True)
    except Exception as e:
        print("Error during generation:", e)
        response = "Oops! Something went wrong on Genie’s side."

    return response
