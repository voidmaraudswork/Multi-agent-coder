import os
from groq import Groq

def get_deepseek_response(code_to_fix):
    # We use Groq's Llama-3 model as a FREE replacement for DeepSeek
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # A very powerful free model on Groq
        messages=[
            {"role": "system", "content": "You are a logic expert. Refine this code and fix mistakes."},
            {"role": "user", "content": code_to_fix}
        ]
    )
    return response.choices[0].message.content
