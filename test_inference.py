from huggingface_helper import generate_response

prompt = "What is the capital of France?"
model = "tiiuae/falcon-7b-instruct"  # or any model you've set in MODEL_NAMES

try:
    response = generate_response(prompt, model)
    print(response)
except Exception as e:
    print(f"❌ Error during inference: {e}")
