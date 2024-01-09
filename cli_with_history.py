from openai import OpenAI
import os
import datetime

USER_COLOR = "\033[1;32m"
GPT_COLOR = "\033[1;34m"
RESET_COLOR = "\033[0m"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    exit(1)

client = OpenAI()
HistoryPath = "./history/"


def append_to_chat_history(user_input, gpt_response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HistoryFile, "a") as file:
        file.write(f"{timestamp} - user: {user_input}\n")
        file.write(f"{timestamp} - gpt: {gpt_response}\n\n")

print(f"{GPT_COLOR}Welcome to the OpenAI Playground! {RESET_COLOR}Enter your message (or 'exit' to quit): ")
HistoryFile = input("What's history file name? ")
HistoryFile = HistoryPath + HistoryFile + ".txt"
input("Press Enter to continue...")
while True:
    user_input = input(f"\n{USER_COLOR}user: {RESET_COLOR}").strip()
    
    if user_input.lower() == "exit":
        print(f"{GPT_COLOR}Goodbye!{RESET_COLOR}")
        break

    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"A user just typed in: {user_input}\nHow would you respond?"}
            ]
        )

        gpt_response = completion.choices[0].message.content.strip()
        print(f"{GPT_COLOR}gpt: {RESET_COLOR}{gpt_response}")

        append_to_chat_history(user_input, gpt_response)

    except Exception as e:
        print("An error occurred: ", e)