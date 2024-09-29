import openai
import tiktoken

# Instantiate the OpenAI client with your project API key
openai.api_key = "your-api-key-here"


def count_tokens(text, selected_model):
    encoding = tiktoken.encoding_for_model(selected_model)
    num_tokens = encoding.encode(text)
    return len(num_tokens)


def generate_text_with_openai(user_prompt):
    # Use GPT-3.5-turbo model with the new client structure
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Correct model name based on your plan
        messages=[{"role": "user", "content": user_prompt}]
    )
    return completion.choices[0].message["content"]


prompt = "Generate 5 catchy YouTube titles about [email marketing tricks]"

num_token = count_tokens(prompt, "gpt-3.5-turbo")
print(f"Token Count {num_token}")

# Uncomment to generate the response
# response = generate_text_with_openai(prompt)
# print(response)
