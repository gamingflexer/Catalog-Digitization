import gradio as gr

def sample_fun(first_image,voice_input, text_input):
    return

with gr.Blocks(theme=gr.themes.Default(primary_hue=gr.themes.colors.red, secondary_hue=gr.themes.colors.pink)) as demo:
    
    with gr.Tab("Add Your Image"):
        voice_input = gr.Audio(label="Upload Audio")
        prodcut_id = gr.Textbox(label="Enter Product ID")
        with gr.Row():
            submit_button_tab_1 = gr.Button("Start")

    with gr.Tab("Search Catalog"):
        with gr.Row():
            embbed_text_search = gr.Textbox(label="Enter Product Name")
            submit_button_tab_4 = gr.Button("Start")
        dataframe_output_tab_4 = gr.Dataframe(headers=['ID', 'Distance', 'Title', 'Authors', 'Source'])

    submit_button_tab_1.click(fn=sample_fun,inputs=[voice_input,prodcut_id])
    submit_button_tab_4.click(fn=sample_fun,inputs=[embbed_text_search] ,outputs= dataframe_output_tab_4)

demo.launch(server_name="0.0.0.0",server_port=9003)