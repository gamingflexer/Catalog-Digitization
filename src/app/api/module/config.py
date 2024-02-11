from decouple import config
import os

OPENAI_API_KEY = config('OPENAI_API_KEY', default="")
key = config("AZURE")
emmbedding_model = "text-embedding-3-large"

file_Directory= os.path.join(os.getcwd(), "data")