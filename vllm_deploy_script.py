from openai import OpenAI
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Hello!"},
        ],
    )

    print(completion.choices[0].message.content)

if __name__ == "__main__":
    main()