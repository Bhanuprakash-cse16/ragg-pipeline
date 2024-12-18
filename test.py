import openai

# Set your API key
openai.api_key = "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"

# Generate a response using GPT-4oaa
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",  # Correct model name
    messages=[
        {"role": "user", "content": "write a haiku about AI"}
    ]
)

# Print the response
print(response['choices'][0]['message']['content'])
