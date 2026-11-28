import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).with_name('.env.local'), override=True)
api_key = os.getenv('DEEPSEEK_API_KEY')
if not api_key:
    raise ValueError('Set DEEPSEEK_API_KEY in .env.local before running')

client = OpenAI(
    api_key=api_key,
    base_url='https://api.deepseek.com',
)

response = client.chat.completions.create(
    model='deepseek-flash',
    messages=[
        {'role': 'system', 'content': '你是一个善于写文章的的小助手！'},
        {'role': 'user', 'content': '你好' },
    ],
    stream=False,
    reasoning_effort='low',
    extra_body={'thinking': {'type': 'enabled'}},
)

print(response.choices[0].message.content)
