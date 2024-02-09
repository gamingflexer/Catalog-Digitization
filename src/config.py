from decouple import config
import os

OPENAI_API_KEY = config('OPENAI_API_KEY', default="")
emmbedding_model = "text-embedding-3-large"
