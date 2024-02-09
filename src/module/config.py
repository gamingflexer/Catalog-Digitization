from decouple import config
import os

OPENAI_API_KEY = config('OPENAI_API_KEY')

file_Directory= os.path.join(os.getcwd(), "data")