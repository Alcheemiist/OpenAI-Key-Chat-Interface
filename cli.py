from openai import OpenAI
import os
import sys

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()

if not OPENAI_API_KEY:
    print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

def clear_screen():
        _ = os.system('clear')

print("Welcome to the OpenAI Playground! Enter your message (or 'exit' to quit): ")
while True:
    user_input = input("\n\033[1;32m" + "user: "+ "\033[0m")
    if user_input.lower() == "exit":
        clear_screen()
        break

    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"A user just typed in: {user_input}\nHow would you respond?"}
            ]
        )

        clear_screen()
        print("Assistant: ", completion.choices[0].message.content.strip())
    except Exception as e:
        print("An error occurred: ", e)