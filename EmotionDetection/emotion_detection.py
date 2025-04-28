import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {'text':text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url,json=myobj,headers=header)
    formatted_response = json.loads(response.text)

    emotion = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotion['anger']
    disgust_score = emotion['disgust']
    fear_score = emotion['fear']
    joy_score = emotion['joy']
    sadness_score = emotion['sadness']
    dominant_key = max(emotion,key=emotion.get)

    if response.status_code == 200:
        return {
            'anger':anger_score,
            'disgust':disgust_score,
            'fear': fear_score,
            'joy':joy_score,
            'sadness':sadness_score,
            'dominant_emotion':dominant_key
        }
    elif response.status_code == 400:
        return {
            'anger':None,
            'disgust':None,
            'fear': None,
            'joy':None,
            'sadness':None,
            'dominant_emotion':None
        }