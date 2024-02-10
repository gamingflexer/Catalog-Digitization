import cv2
import os
import matplotlib.pyplot as plt 
import numpy as np 
from llm_vision import OpenAIVision
from ocr import azure_ocr
from prompts.base import base_prompt, gpt3
from utils import  extract_json_from_text
from vectorsearch import search , get_detail_df
import json

def get_details(image_path , details):   ### If product is not in database
    prompt = base_prompt.format(text = details)
    obj = OpenAIVision()
    jsontext = obj.get_image_description(image_path,prompt)
    response =  extract_json_from_text(jsontext['choices'][0]['message']['content'])
    ##add 
    return response

def get_name(image_path):   ### If product is in database
    details = azure_ocr(image_path)
    prompt = gpt3.format(text = details)
    obj = OpenAIVision()
    name = obj.getname(prompt)
    jsontext = json.loads(name.content)
    print(jsontext)
    product_name = jsontext['product_name']
    get_prod_name_db = search(product_name)
    # if name not in db:
    #     response = get_details(image_path, details)
    #     add_in_db(response)
    # else:
    #     add_in_db(get_prod_name_db)


def add_in_db(response):
    pass


if __name__ == "__main__":
    image_path = r"data/remove_flash.jpg"
    get_name(image_path)