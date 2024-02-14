from api.module.llm_vision import OpenAIVision
from api.module.ocr import azure_ocr
from api.module.prompts.base import base_prompt, gpt3
from api.module.utils import  extract_json_from_text
# from vectorsearch import search , get_detail_df
import json

def get_details(image_path_list): 
    total_ocr = ""
    for image_path in image_path_list:
        details = azure_ocr(image_path)
        total_ocr += details
    print(total_ocr)
    prompt = base_prompt.format(text = total_ocr)
    # print(prompt)
    obj = OpenAIVision()
    if len(image_path_list) > 1:
        jsontext = obj.get_image_description(image_path_list[0],prompt)
    response =  extract_json_from_text(jsontext['choices'][0]['message']['content'])
    return response

def get_name(image_path): 
    details = azure_ocr(image_path)
    prompt = gpt3.format(text = details)
    obj = OpenAIVision()
    name = obj.getname(prompt)
    jsontext = json.loads(name.content)
    print(jsontext)
    # product_name = jsontext['product_name']
    # get_prod_name_db = search(product_name)
    # if name not in db:
    #     response = get_details(image_path, details)
    #     add_in_db(response)
    # else:
    #     add_in_db(get_prod_name_db)
