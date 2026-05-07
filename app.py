import sys
import os
import time

# 1. RENDER PATH FIX: Ensure subfolders are discoverable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import gradio as gr
from dotenv import load_dotenv

# 2. IMPORT AGENTS: Make sure agents/__init__.py exists!
from agents.gemini_agent import get_gemini_response
from agents.deepseek_agent import get_deepseek_response # This now uses Groq internally
from agents.groq_agent import get_groq_response
from debate.engine import start_debate

# Load API keys from Render Environment Variables
load_dotenv()

def ai_coding_process(user_prompt):
    """The main pipeline logic with status updates for the UI."""
    try:
        # Step 1: Draft
        yield "🏗️ Phase 1: Gemini is drafting...", ""
        v1 = get_gemini_response(user_prompt)
        time.sleep(2) # Brief pause for rate-limit safety
        
        # Step 2: Refine (Using our 'DeepSeek' agent which now runs on Groq)
        yield "🔍 Phase 2: Llama (Groq) is refining logic...", v1
        v2 = get_deepseek_response(v1)
        time.sleep(2)
        
        # Step 3: Audit
        yield "⚡ Phase 3: Mixtral (Groq) is removing blunders...", v2
        v3 = get_groq_response(v2)
        time.sleep(2)
        
        # Step 4: The Debate (Safety-limited to 2 rounds)
        yield "⚖️ Phase 4: Starting AI Consensus Debate (Fixed Rounds)...", v3
        final_code = start_debate(v3, get_gemini_response, get_deepseek_response)
        
        yield "✅ Success: Final Code Generated!", final_code

    except Exception as e:
        yield f"❌ Error: {str(e)}", "An error occurred during the pipeline. Check logs."

# 3. GRADIO INTERFACE DESIGN
with gr.Blocks(theme=gr.themes.Ocean(), title="AI Consensus Coder") as demo:
    gr.Markdown("# 🤖 AI Consensus Coder")
    gr.Markdown("A multi-agent pipeline using **Gemini 2.0** and **Groq (Llama/Mixtral)** to build high-quality code.")
    
    with gr.Row():
        with gr.Column(scale=4):
            user_input = gr.Textbox(
                label="Describe your project", 
                placeholder="e.g., Create a Python script for a Pomodoro timer with a GUI",
                lines=3
            )
            submit_btn = gr.Button("Build My Code", variant="primary")
        
        with gr.Column(scale=1):
            status_label = gr.Label(label="Pipeline Status", value="Ready")

    output_display = gr.Code(
        label="Final Refined Code", 
        language="python", 
        interactive=False,
        show_label=True
    )

    # Wire up the button
    submit_btn.click(
        fn=ai_coding_process,
        inputs=user_input,
        outputs=[status_label, output_display]
    )

# 4. RENDER DEPLOYMENT CONFIG
# app = demo.app is used if running with Gunicorn
app = demo.app

if __name__ == "__main__":
    # demo.queue() is critical for long-running AI processes like ours
    demo.queue().launch(
        server_name="0.0.0.0", 
        server_port=10000,
        share=False
    )
