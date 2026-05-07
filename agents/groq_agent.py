import os
from groq import Groq

def get_groq_response(code_input):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a syntax auditor. Remove blunders and optimize this code."},
            {"role": "user", "content": code_input}
        ]
    )
    return response.choices[0].message.content
  
