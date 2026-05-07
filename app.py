import gradio as gr
import os
from dotenv import load_dotenv
from agents.gemini_agent import get_gemini_response
from agents.deepseek_agent import get_deepseek_response
from agents.groq_agent import get_groq_response
from debate.engine import start_debate

load_dotenv()

def ai_coding_process(user_prompt):
    # Phase 1: Draft
    yield "🏗️ Gemini is drafting...", ""
    v1 = get_gemini_response(user_prompt)
    
    # Phase 2: Refine
    yield "🔍 DeepSeek is refining...", v1
    v2 = get_deepseek_response(v1)
    
    # Phase 3: Upgrade
    yield "⚡ Groq is removing blunders...", v2
    v3 = get_groq_response(v2)
    
    # Phase 4: Debate
    yield "⚖️ Starting 20s AI Debate...", v3
    final = start_debate(v3, get_gemini_response, get_deepseek_response)
    
    yield "✅ Final Result Ready!", final

# Create the UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 AI Consensus Coder")
    gr.Markdown("Gemini, DeepSeek, and Groq will now debate to write your code.")
    
    with gr.Row():
        input_text = gr.Textbox(label="What do you want to build?", placeholder="e.g. A snake game in Python")
        submit_btn = gr.Button("Start Process", variant="primary")
    
    status = gr.Label(label="Current Status")
    output_code = gr.Code(label="Refined Code Output", language="python")

    submit_btn.click(
        fn=ai_coding_process, 
        inputs=input_text, 
        outputs=[status, output_code]
    )

# share=True creates a public link you can open on any phone
demo.launch(share=True)
