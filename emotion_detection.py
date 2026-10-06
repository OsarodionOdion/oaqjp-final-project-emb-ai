import json
import requests

def emotion_detector(text_to_analyze):
    """ Function to decipher the emotion associated with a text using the 
    emotion predict function of the Watson NLP library.

    Args:
        text_to_analyze (str): text to be analyzed

    returns:
        str: text attribute of the response object

    """
    # URL of the emtion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # header required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # send a post request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header, timeout=5)

    return response.text
    