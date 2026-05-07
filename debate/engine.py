import time

def start_debate(code, gemini_func, deepseek_func):
    print("\n⚖️ STARTING 20-SECOND AI DEBATE...")
    start_time = time.time()
    current_version = code
    
    # Loop for roughly 20 seconds
    while time.time() - start_time < 20:
        print("💬 DeepSeek is critiquing Gemini...")
        current_version = deepseek_func(f"Find one flaw in this and fix it: {current_version}")
        
        print("💬 Gemini is defending and improving...")
        current_version = gemini_func(f"Make this even better based on feedback: {current_version}")
        
    return current_version
  
