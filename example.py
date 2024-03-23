import os

if __name__ == "__main__":
    from openai import OpenAI
    client = OpenAI(
        base_url=os.getenv('OPENAI_BASE_URL')
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion.choices[0].message.content)
