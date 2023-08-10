import os
import openai

openai.api_key = os.getenv('a')

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            "role": "user",
            "content": "Test"
        }
    ]
)

print(completion.choices[0].message)
