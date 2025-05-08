from openai import OpenAI
import openai

# For DeepSeek API
client = OpenAI(api_key="sk-...", base_url="https://api.deepseek.com")

# For OpenAI API
#openai.api_key = 'sk-...'

def call_deepseek(prompt, system_prompt, model="deepseek-chat", max_tokens=512, temperature=0, stop='\n\n\n', n=1):
    try:
        ans = client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt}],
            temperature=temperature,
            stop=stop,
            top_p=1.0,
            n=n
            )
        #print([choice.message.content for choice in ans.choices])
        return [choice.message.content for choice in ans.choices]
    except Exception as e:
        print(e)
        return []

def call_gpt(prompt, system_prompt, model='gpt-3.5-turbo', max_tokens=512, temperature=0, stop='\n\n\n'):
    try:
        ans = openai.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            stop=stop,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt}],
            temperature=temperature,
            top_p=1.0,
            )
        #print([choice.message.content for choice in ans.choices])
        return [choice.message.content for choice in ans.choices]
    except Exception as e:
        print(e)
        return []

def call_reflection(prompt, model="deepseek-chat", max_tokens=512, temperature=0, stop='\n\n\n'):
    try:
        ans = client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {'role': 'user', 'content': prompt}],
            temperature=temperature,
            stop=stop,
            top_p=1.0
            )
        return [choice.message.content for choice in ans.choices]
    except Exception as e:
        print(e)
        return []