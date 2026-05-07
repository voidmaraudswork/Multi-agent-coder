import time

def start_debate(code, gemini_func, deepseek_func):
    print("⚖️ STARTING AI DEBATE (2 ROUNDS)...")
    curr = code
    
    # We do exactly 2 rounds instead of a timed loop
    for i in range(2):
        print(f"💬 Round {i+1}: DeepSeek critiquing...")
        curr = deepseek_func(f"Find one logical flaw and fix it: {curr}")
        time.sleep(10)  # 👈 10 seconds is the 'magic number' for Free Tier safety
        
        print(f"💬 Round {i+1}: Gemini improving...")
        curr = gemini_func(f"Make this better based on feedback: {curr}")
        time.sleep(10)  # 👈 10 seconds break
        
    return curr
