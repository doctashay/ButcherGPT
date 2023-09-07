import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize GPT-3.5-turbo engine
model = "gpt-3.5-turbo-16k"

# Pre-prompt
pre_prompt = "You're ButcherGPT! You talk like Billy Butcher from The Boys. Use lots of Australian slang and a condescending tone."

# Function for chatting with GPT-3.5-turbo
def chat_with_gpt3(prompt):
    messages = [
        {"role": "system", "content": pre_prompt},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=1000,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

# Main loop for user interaction
if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ButcherGPT: Right, then. I'm out.")
            break
        else:
            gpt3_response = chat_with_gpt3(user_input)
            print(f"ButcherGPT: {gpt3_response}")