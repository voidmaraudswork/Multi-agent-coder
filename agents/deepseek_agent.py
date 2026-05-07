import os
from openai import OpenAI

def get_deepseek_response(code_to_fix):
    client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a logic expert. Refine this code and fix mistakes."},
            {"role": "user", "content": code_to_fix}
        ]
    )
    return response.choices[0].message.content
  
