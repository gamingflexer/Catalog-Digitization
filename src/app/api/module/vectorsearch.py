import os
from config import OPENAI_API_KEY, file_Directory
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
import pandas as pd

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY


# df = pd.read_excel(r"/home/vrush/Catalog-Digitization-/src/module/data/Catalog Digitization/ONDC Test Data _ Images/ONDCSampleData.xlsx")
# df_new = pd.DataFrame(columns=["id", "name"])
# df_new =  df['name']
# df_new.to_csv(r"data/data.csv", index=False)

def create_vector():
    loader = CSVLoader(file_path="data/data.csv")
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(docs)
    db_path = os.path.join(file_Directory,"vectorstore")
    embeddings = OpenAIEmbeddings()
    os.makedirs(db_path, exist_ok=True)      
    Chroma.from_documents(docs, embeddings, persist_directory= db_path)
    
def search(query):
    embeddings = OpenAIEmbeddings()
    db_path = os.path.join(file_Directory,"vectorstore")
    db = Chroma(persist_directory= db_path, embedding_function= embeddings)
    embedding_vector = OpenAIEmbeddings().embed_query(query)
    docs = db.similarity_search_by_vector(embedding_vector)
    print(docs[0].page_content)
    return docs[0].page_content


def get_detail_df(name):
    df = pd.read_excel(r"/home/vrush/Catalog-Digitization-/src/module/data/Catalog Digitization/ONDC Test Data _ Images/ONDCSampleData.xlsx")
    for item in df.iterrows():
        if item['name'] == name:
            return item
        else:
            return None

if __name__ == "__main__":
    create_vector()
    name = search("Choco Creme Wafers")
    print(get_detail_df(name))
