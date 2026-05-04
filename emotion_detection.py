import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the Watson NLP Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Custom headers required by the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input data formatted as a JSON object
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a POST request to the API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Parsing the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extracting the emotion scores from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Returning the dictionary of emotions (anger, disgust, fear, joy, sadness)
    return emotions
