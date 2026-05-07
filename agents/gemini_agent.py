import os
import time
from google import genai
from google.genai import errors

def get_gemini_response(prompt, system_instruction="Lead dev"):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"{system_instruction}\n\nTask: {prompt}"
        )
        return response.text
    except errors.ClientError as e:
        if "429" in str(e):
            print("⚠️ Quota hit! Returning current code to prevent crash.")
            return prompt # Just return the code we already had
        raise e
