import json
from google import genai
from google.genai import types
from google.genai import errors
import time
import os


os.environ['GEMINI_API_KEY'] = '...'
client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

# Gemini API
def call_gemini(prompt, model='gemini-2.5-pro-preview-03-25', temperature=0., top_p=1.0):

    try:
        ans = client.models.generate_content(
            model=model,
            contents=[prompt],
            config=types.GenerateContentConfig(
                system_instruction='You are an expert at categorizing mathematical problems based on their solution methods. I will provide you with a list of math problems. Your task is to read each problem and then group the problems into distinct categories (less than eight groups) based on these identified areas and sub-topics.',
                top_p=top_p,
                temperature=temperature
            ),
        )
        return ans.text
    except errors.APIError as e:
        time.sleep(1)
    raise RuntimeError('Failed to call GEMINI API')

def prompt_generate(path):
    instances = list(map(json.loads, open(path)))
    text_items = []
    for instance in instances:
        text_items.append(instance['original_text'])
    
    PROMPT = f'Here is the list of math problems:\n{text_items}\n\nPlease list the group name, short description, and one example for each group. The example should be a math problem from the list of questions I provided.'

    return PROMPT

if __name__ == '__main__':
    PROMPT = prompt_generate('dataset/math23k_test_new.jsonl')
    result = call_gemini(PROMPT)
    with open('dataset/Question_Categorization.txt', 'w') as f:
        f.write(result)
