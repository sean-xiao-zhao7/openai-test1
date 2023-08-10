import os
import openai

openai.api_key = os.getenv('a')

messages_log = []

user_input = input('Enter prompt for ChatGPT: ')

while True:
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                "role": "user",
                "content": "Write me a haiku based on mountain"
            }
        ],
        temperature=0.2,
    )

    content = completion.choices[0].message.content
    print(content)
    messages_log.append(content)
