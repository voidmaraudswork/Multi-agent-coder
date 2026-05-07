import os
from google import genai

def get_gemini_response(prompt, system_instruction="You are a lead developer."):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    # Change 'gemini-1.5-flash' to 'gemini-2.0-flash'
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=f"{system_instruction}\n\nTask: {prompt}"
    )
    return response.text
