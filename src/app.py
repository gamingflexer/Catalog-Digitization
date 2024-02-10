from module.config import OPENAI_API_KEY
import gradio as gr
import pandas as pd

def sample_fun(first_image,voice_input, text_input):
    return

with gr.Blocks() as demo:
    
    with gr.Tab("Add Your Image"):
        with gr.Row():
            first_image = gr.Image(label="Upload Image")
            voice_input = gr.Audio(label="Upload Audio")
            text_input = gr.Textbox(label="Enter Text")
            submit_button_tab_1 = gr.Button("Start")
        with gr.Row():
            dataframe_output = gr.Dataframe(headers=['title','des','price'])

    with gr.Tab("Search Catalog"):
        with gr.Row():
            embbed_text_search = gr.Textbox(label="Enter Text")
        with gr.Row():
            top_k = gr.Number(label="Number of results - Min 2")
        with gr.Row():
            submit_button_tab_4 = gr.Button("Start")
            dataframe_output_tab_4 = gr.Dataframe(headers=['ID', 'Distance', 'Title', 'Authors', 'Source'])

    submit_button_tab_1.click(fn=sample_fun,inputs=[first_image,voice_input, text_input] ,outputs= dataframe_output)
    submit_button_tab_4.click(fn=sample_fun,inputs=[embbed_text_search, top_k] ,outputs= dataframe_output_tab_4)

demo.launch(server_name="0.0.0.0",server_port=9002)