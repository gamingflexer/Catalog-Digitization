import gradio as gr
import pandas as pd
import os
import requests

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
SEVER_IP = os.environ.get("SEVER_IP")

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

def get_product_details_by_id(product_id):
    response = requests.get(f'{SEVER_IP}/api/product_details/{product_id}/')
    if response.status_code == 200:
        return response.json()  # Returns the product details as a dictionary
    else:
        return {"error": f"Product with ID {product_id} not found or error occurred."}

def sample_fun(voice_input, prodcut_id):
    print(prodcut_id)
    return

with gr.Blocks(theme=gr.themes.Default(primary_hue=gr.themes.colors.red, secondary_hue=gr.themes.colors.pink)) as demo:
    
    with gr.Tab("Add Your Image"):
        voice_input = gr.Audio(label="Upload Audio")
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