import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from openai import OpenAI
import os
import datetime

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI()
log_file = "./history/chat_history_X.txt"

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(log_file, "a") as file:
    file.write(f" \n----------------- New Converstion -------------------\n")

def append_to_chat_history(user_input, gpt_response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"{timestamp} - user: {user_input}\n")
        file.write(f"{timestamp} - gpt: {gpt_response}\n\n")

window = tk.Tk()
window.title("OpenAI Chat")

chat_log = ScrolledText(window, state='disabled', wrap=tk.WORD)
chat_log.pack(padx=10, pady=10, expand=True, fill='both')

def send_message(event=None):
    user_input = user_entry.get()
    if user_input:
        try:
            chat_log.configure(state='normal')
            chat_log.insert(tk.END, f"\nUser: {user_input}\n")
            chat_log.configure(state='disabled')
            user_entry.delete(0, tk.END)

            completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"A user just typed in: {user_input}\nHow would you respond?"}
            ]
            )
            gpt_response = completion.choices[0].message.content.strip()

            chat_log.configure(state='normal')
            chat_log.insert(tk.END, f"Assistant: {gpt_response}\n")
            chat_log.configure(state='disabled')

            chat_log.yview(tk.END)

            append_to_chat_history(user_input, gpt_response)

        except Exception as e:
            print("An error occurred: ", e)
    

user_entry = tk.Entry(window)
user_entry.pack(padx=10, pady=5, fill='x')
user_entry.bind("<Return>", send_message)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

window.mainloop()