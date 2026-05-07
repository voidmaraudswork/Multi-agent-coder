import os
from groq import Groq

def get_groq_response(code_input):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768", # Using Mixtral here for a different perspective
        messages=[
            {"role": "system", "content": "You are a syntax auditor. Remove blunders."},
            {"role": "user", "content": code_input}
        ]
    )
    return response.choices[0].message.content
