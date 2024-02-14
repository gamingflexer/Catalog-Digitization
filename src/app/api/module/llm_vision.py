import base64
import requests
from config import OPENAI_API_KEY
from openai import OpenAI
import os


""" 
openai_vision = OpenAIVision(api_key)
image_path = "path_to_your_image.jpg"
prompt = ""
response = openai_vision.get_image_description(prompt,image_path)
"""

class OpenAIVision:
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.base_url = "https://api.openai.com/v1/chat/completions"

    def __encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def get_image_description(self, image_path, prompt):
        base64_image = self.__encode_image(image_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "temperature": 0.0,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt,
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                        
                    ]
                  
                }
            ],
            "max_tokens": 1000,
            
        }

        response = requests.post(self.base_url, headers=headers, json=payload)
        return response.json()


    def getname(self , prompt):
        client = OpenAI()
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
        )

        return completion.choices[0].message

   



