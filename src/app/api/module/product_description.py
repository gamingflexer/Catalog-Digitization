import cv2
import os
import matplotlib.pyplot as plt 
import numpy as np 
from llm_vision import OpenAIVision
from ocr import azure_ocr
from prompts.base import base_prompt
from utils import  extract_json_from_text
from vectorsearch import search , get_detail_df



def get_product_description(image_path):
    details = azure_ocr(image_path)
    prompt = base_prompt.format(text = details)
    obj = OpenAIVision()
    json = obj.get_image_description(image_path,prompt)
    response =  extract_json_from_text(json['choices'][0]['message']['content'])
   
    return response

def add_in_db(response):
    name = response['brand'] + " " + response['type_of_product']
    get_prod_name_db = search(name)
    name = get_detail_df(get_prod_name_db)
    ### Add things into database
