import gradio as gr
import pandas as pd
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
SEVER_IP = os.environ.get("SEVER_IP")

def sample_fun(voice_input, prodcut_id):
    print(prodcut_id)
    return

with gr.Blocks(theme=gr.themes.Default(primary_hue=gr.themes.colors.red, secondary_hue=gr.themes.colors.pink)) as demo:
    
    with gr.Tab("Add Your Image"):
        voice_input = gr.Audio(label="Upload Audio")
        prodcut_id = gr.Textbox(label="Enter Product ID")
        with gr.Row():
            submit_button_tab_1 = gr.Button("Start")


    submit_button_tab_1.click(fn=sample_fun,inputs=[voice_input,prodcut_id])

demo.launch(server_name="0.0.0.0",server_port=9003)