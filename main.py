import os
from dotenv import load_dotenv
from agents.gemini_agent import get_gemini_response
from agents.deepseek_agent import get_deepseek_response
from agents.groq_agent import get_groq_response
from debate.engine.py import start_debate

load_dotenv()

def main():
    user_prompt = input("Describe the code you want: ")
    
    # 1. Initial Gemini Draft
    v1 = get_gemini_response(user_prompt)
    
    # 2. DeepSeek Refine
    v2 = get_deepseek_response(v1)
    
    # 3. Groq Blunder Removal
    v3 = get_groq_response(v2)
    
    # 4. The 20-Second Debate
    final_code = start_debate(v3, get_gemini_response, get_deepseek_response)
    
    print("\n--- FINAL OUTPUT ---\n")
    print(final_code)

if __name__ == "__main__":
    main()
  
