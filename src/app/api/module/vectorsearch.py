import os
from config import OPENAI_API_KEY, file_Directory
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
import pandas as pd
import chromadb,uuid
from chromadb.utils import embedding_functions
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
db_path = os.path.join(file_Directory,"vectorstore")
client = chromadb.PersistentClient(path=db_path)

def generate_uuid():
    return str(uuid.uuid4())   

    
emmbedding_model = "text-embedding-3-large"
openai_ef = embedding_functions.OpenAIEmbeddingFunction(model_name=emmbedding_model,api_key=OPENAI_API_KEY)
collection = client.get_or_create_collection(name="products")


def add_document_chroma_collection(collection_object, document_list, embedding_list, metadata):   
    metadata_list = [metadata for i in range(len(document_list))]
    ids_gen = [generate_uuid() for i in range(len(document_list))]
    collection_object.add(embeddings = embedding_list,documents = document_list,metadatas = metadata_list , ids = ids_gen)
    if collection_object:
        return True
    

def create_vector():
    df = pd.read_csv(r"/home/vrush/Catalog-Digitization-/src/app/api/module/data/data.csv")
    for i , items in df.iterrows():
        print(items['name'])
        metadata = {"empty":""}
        doc_embed = openai_ef([items['name']])
        add_document_chroma_collection(collection_object = collection, document_list = [items["name"]], embedding_list = doc_embed ,metadata = metadata)







def search(query):
    embbed_text_search = openai_ef(query)
    data = collection.query(query_embeddings = embbed_text_search, n_results=10) 
    return data
 



def get_detail_df(name):
    print(name)
    df = pd.read_excel(r"/home/vrush/Catalog-Digitization-/src/app/api/module/data/Catalog/Data_Images/ONDCSampleData.xlsx")
    for i,item in df.iterrows():
        if str(item['name']) == str(name).split(":")[1].strip():
            return item
        else:
            continue
          

if __name__ == "__main__":
    # create_vector()
    name = search("Atta")
    print(name)
    # # # print(get_detail_df(name))
