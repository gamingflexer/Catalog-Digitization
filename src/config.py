from decouple import config
import os

OPENAI_API_KEY = config('OPENAI_API_KEY', default="")
SQL_URL = config('SQL_URL', default="sqlite:///./db.sqlite3")
emmbedding_model = "text-embedding-3-large"

key = "f375d6130d4d4c518d69fe4716b5a6de"
endpoint = "https://bintix-ocr.cognitiveservices.azure.com/"