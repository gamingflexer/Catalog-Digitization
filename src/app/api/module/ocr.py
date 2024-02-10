from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from config import key, endpoint
import easyocr

def azure_ocr(image_path):
    try:
        # Create a DocumentAnalysisClient instance
        document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )

        # Open the image file and begin document analysis
        with open(image_path, "rb") as image_file:
            poller = document_analysis_client.begin_analyze_document(
                "prebuilt-read", document=image_file
            )
            result = poller.result()
            return result.content
    except Exception as e:
        print('Error occurred:', e)
        return ""
    
def easy_ocr(image_path):
    try:
        reader = easyocr.Reader(['en','hi','bn','mr','ta','te'])
        result = reader.readtext(image_path)
        return result
    except Exception as e:
        print('Error occurred:', e)
        return []