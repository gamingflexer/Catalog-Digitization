from textwrap import dedent
from openai import OpenAI
from decouple import config
import json,os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

voice_edit = dedent("""
        ### Instruction: 
        audio transcription starts here
        {text}
        audio transcription ends here
        
        I want you to provide the json format with all the details filled as mentioned below by getting information from the audio transcription.
        ( return "null" where you don't have a answer)
        
        "brand": sample_brand
        "mrp": 12, ##price of product
        "unit": per pack
        "Quantity": 1,  ##num of products visible
        "parent_category": from the above given list"
        "ingredients": "ingredient1", "ingredient2", "ingredient3" ##list of ingredients comma separated
        "calorie_count": 12 ##calorie count
        "marketed_by":  ##sample_marketer
        "manufactured_by": ##manufacturer
        "manufactured_in_country": India ##Country of manufacture
        "type_of_packaging": Box
        "promotion_on_the_pack": 
        "type_of_product":  ## give this your understanding of product
        "pack_of_or_no_of_units":  ##No. of Units
        "description": ##description of product
        "weight": ##weight of product
        
     
        Only return the output in the required json format with string in enclosed in double quotes.
        """)

def getname(prompt):
        client = OpenAI(api_key=OPENAI_API_KEY)
        completion = client.chat.completions.create(
        response_format={ "type": "json_object" },
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "user", "content": prompt , }
        ]
       
        )

        return completion.choices[0].message.content


def extract_json_from_text(text):
    text = str(text).lower()
    print(f"Extracting JSON from text: {text}")
    try:
        # Find the JSON part within the text
        start_index = text.find('{')
        end_index = text.rfind('}') + 1
        json_part = text[start_index:end_index]
        json_part = json.loads(json_part.strip())
        return json_part

    except Exception as e:
        print(f"\033[31m Exception occurred while loading JSON: {str(e)} [0m")
        return e