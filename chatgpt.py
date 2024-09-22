# pylint: disable=import-error

from openai import OpenAI

# Instantiate the OpenAI client with your project API key
client = OpenAI(api_key="your-api-key")


def generate_text_with_openai(user_prompt):
    # Use GPT-4o model with the new client structure
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Correct model name based on your plan
        messages=[{"role": "user", "content": user_prompt}]
    )
    return completion.choices[0].message.content


prompt = "Generate 5 catchy YouTube titles about [email marketing tricks]"

response = generate_text_with_openai(prompt)

print(response)
