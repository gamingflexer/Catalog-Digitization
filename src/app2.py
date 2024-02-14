import gradio as gr
import pandas as pd
import os
import requests
from audio_text import whisper_openai
from app_utils import voice_edit, extract_json_from_text, getname
import uuid
import soundfile as sf
import time

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
SEVER_IP = os.environ.get("SEVER_IP","http://34.122.223.224:9002")

def get_total_number_of_products():
    response = requests.get(f'{SEVER_IP}/api/total_number_of_products/')
    if response.status_code == 200:
        return response.json()['total_number_of_products']
    else:
        return "Error fetching total number of products"

def search_products(product_name):
    response = requests.get(f'{SEVER_IP}/api/search_products/', params={'name': product_name})
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return pd.DataFrame([])  # Return an empty DataFrame in case of an error

def update_product_details_by_id(product_id,payload):
    response = requests.put(f'{SEVER_IP}/api/update_product/{product_id}/',data=payload)
    if response.status_code == 200:
        return response.json()  # Returns the product details as a dictionary
    else:
        return {"error": f"Product with ID {product_id} not found or error occurred."}

def sample_fun(voice_input, product_id, progress=gr.Progress()):

    audio_path = str(uuid.uuid4().hex) + ".wav"
    print(voice_input)
    sample_rate,audio_data = voice_input
    progress(0.1, desc="Collecting audio data")
    # audio_data = audio_data.reshape(-1, 1) 
    audio_save_path = os.path.join(BASE_PATH,"audio",audio_path)
    sf.write(audio_save_path, audio_data, sample_rate)
    # print("Product ID:", product_id)
    time.sleep(2)
    transcription = whisper_openai(audio_save_path)
    # print("Transcription:", transcription)
    prompt = voice_edit.format(text = transcription)
    # print("Prompt:", prompt)
    name = getname(prompt)
    try:
        json_data = extract_json_from_text(name)
    except Exception as e:
        print(f"-->Exception occurred while extracting JSON: {str(e)}")
    # json_data['product_id'] = product_id
    json_data_to_add = {}
    progress(0.4, desc="Collecting Links")
    for key in json_data:
        if json_data[key] == "null" or json_data[key] == "" or json_data[key] == None:
            pass
        else:
            json_data_to_add[key] = json_data[key]
    print(json_data_to_add)
    progress(0.7, desc="Collecting Links")
    update_product_details_by_id(product_id,json_data)
    progress(0.9, desc="Collecting Links")
    return json_data


with gr.Blocks(theme=gr.themes.Default(primary_hue=gr.themes.colors.red, secondary_hue=gr.themes.colors.pink),title = "Edit Product by Voice") as demo:
    
    with gr.Tab("Add Your Image"):
        voice_input = gr.Audio(sources=["microphone"])
        prodcut_id = gr.Textbox(label="Enter Product ID")
        with gr.Row():
            submit_button_tab_1 = gr.Button("Start")
            
    with gr.Tab("Search Catalog"):
        with gr.Row():
            total_no_of_products = gr.Textbox(value=str(get_total_number_of_products()),label="Total Products")
        with gr.Row():
            embbed_text_search = gr.Textbox(label="Enter Product Name")
            submit_button_tab_4 = gr.Button("Start")
        dataframe_output_tab_4 = gr.Dataframe(headers=['id', 'barcode', 'brand', 'sub_brand', 'manufactured_by', 'product_name', 
                                               'weight', 'variant', 'net_content', 'price', 'parent_category', 
                                               'child_category', 'sub_child_category', 'images_paths', 'description', 
                                               'quantity', 'promotion_on_the_pack', 'type_of_packaging', 'mrp'])

    submit_button_tab_1.click(fn=sample_fun,inputs=[voice_input,prodcut_id])
    submit_button_tab_4.click(fn=search_products,inputs=[embbed_text_search] ,outputs= dataframe_output_tab_4)

demo.launch()