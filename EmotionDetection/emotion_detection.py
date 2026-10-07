# Function for detecting emotions using the emotion predict function of the Watson NLP library

'''
URL, headers, and input json format for accessing the emotion predict function in the embedded Watson NLP libraries

URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyze } }

'''
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

    # Parsing the json response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotions and their scores
    emotions_scores = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = {'emotion': None, 'score':0}
    for k,v in emotions_scores.items():
        if v > dominant_emotion['score']:
            dominant_emotion['emotion'] = k
            dominant_emotion['score'] = v

    return emotions_scores | {'dominant_emotion': dominant_emotion['emotion']}
