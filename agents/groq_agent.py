import os
from groq import Groq

def get_groq_response(code_input):
    """
    This function handles the 'Syntax Auditing' and 'Blunder Removal' 
    using the Groq API.
    """
    # Initialize the Groq client using the environment variable
    # Ensure 'GROQ_API_KEY' is set in your Render Settings
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        return "Error: GROQ_API_KEY is missing from environment variables."

    client = Groq(api_key=api_key)

    try:
        # We use Llama 3.3 70B for high-quality code analysis
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "You are a Senior Syntax Auditor. Your job is to take the provided code, "
                        "remove any logical blunders, optimize the performance, and ensure "
                        "the code is clean and production-ready. Return only the improved code."
                    )
                },
                {
                    "role": "user", 
                    "content": f"Please audit and refine this code:\n\n{code_input}"
                }
            ],
            temperature=0.2, # Lower temperature for more consistent coding results
            max_tokens=4096
        )
        
        return response.choices[0].message.content

    except Exception as e:
        # If there is a rate limit or auth error, return a helpful message
        return f"Groq Agent Error: {str(e)}"
