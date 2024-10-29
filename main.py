# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# import pandas as pd
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-p", "--prompt", help="prompt to send to ai")
# parser.add_argument("-f", "--file", help="path to write the response to")

# # parse_args will turn terminal flags into python dictionary
# args = parser.parse_args()
# prompt = args.prompt
# file = args.file

# load_dotenv()

# api_key = os.getenv("API_KEY")

# print(api_key)

# os.environ['API_KEY'] = api_key
# genai.configure(api_key=os.environ['API_KEY'])


# # generic prompt
# def get_completion(file, prompt, model="gemini-1.5-flash", **kwargs):
#     model = genai.GenerativeModel(model)
    
#     generation_config = {
#         "temperature": 0.8,
#         "max_output_tokens": 200
#     }
    
#     generation_config.update(kwargs)
    
#     response = model.generate_content(prompt, generation_config=generation_config)
    
#     # Write response to ai.md
#     with open(file if file else "ai.md", 'a') as f:
#         f.write(f"\n\nPrompt: {prompt}\n")
#         f.write(f"Response: {response.text}\n")
    
#     return response.text

# # prompt = "tell me about climate change, specifcally what it is, it;'s causes, whats observable efects it has on the enviorment ( like temp change ) and possible solutions"
# # After parsing arguments

# prompt = input("Please enter a prompt: ")
# if not prompt.strip():  # Check if prompt is empty or only whitespace
#     raise ValueError("Prompt must not be empty. Please provide a valid prompt.")

# # Existing code...
# response = get_completion(
#     file,
#     prompt,
#     temperature=0.9,
#     max_output_tokens=1000
# )

# # response = get_completion(
# #     file,
# #     prompt,
# #     temperature=0.9,
# #     max_output_tokens=1000
# # )

# print(response)

from dotenv import load_dotenv
import os
import google.generativeai as genai
import argparse

# Load environment variables from .env file
load_dotenv()

# Set up argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--prompt", help="prompt to send to AI")
parser.add_argument("-f", "--file", help="path to write the response to")
args = parser.parse_args()

# Retrieve and set the API key
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set.")

genai.configure(api_key=api_key)

# Define the function to get AI completion
def get_completion(file, prompt, model="gemini-1.5-flash", **kwargs):
    model_instance = genai.GenerativeModel(model)
    
    generation_config = {
        "temperature": 0.8,
        "max_output_tokens": 200
    }
    
    generation_config.update(kwargs)
    
    response = model_instance.generate_content(prompt, generation_config=generation_config)
    
    # Write response to the specified file or default to "ai.md"
    with open(file if file else "ai.md", 'a') as f:
        f.write(f"\n\nPrompt: {prompt}\n")
        f.write(f"Response: {response.text}\n")
    
    return response.text

# Use the prompt from arguments or ask for user input
prompt = args.prompt or input("Please enter a prompt (default: 'Hello'): ") or 'Hello'

# Ensure prompt is not empty
if not prompt.strip():
    raise ValueError("Prompt must not be empty. Please provide a valid prompt.")

# Get the response from the AI
response = get_completion(
    args.file,
    prompt,
    temperature=0.9,
    max_output_tokens=1000
)

print(response)