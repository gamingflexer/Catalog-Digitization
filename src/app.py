import gradio as gr
import pymysql
import pandas as pd

def get_total_number_of_products():
    connection = connect_to_db()
    cursor = connection.cursor()

    # Execute SQL query to count total number of products
    sql = "SELECT COUNT(*) AS total_products FROM api_database"
    cursor.execute(sql)
    result = cursor.fetchone()
    total_products = result['total_products']

    connection.close()

    return total_products

def search_products(search_query):
    search_query = " " + search_query.lower() + " "
    connection = connect_to_db()
    cursor = connection.cursor()
    sql = """
        SELECT * FROM api_database 
        WHERE product_name LIKE %s OR description LIKE %s
    """
    cursor.execute(sql, ('%' + search_query + '%', '%' + search_query + '%'))
    search_results = cursor.fetchall()

    connection.close()
    search_results_formatted = []
    for result in search_results:
        search_results_formatted.append(list(result.values()))
    return search_results_formatted

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

demo.launch(server_name="0.0.0.0",server_port=9003)