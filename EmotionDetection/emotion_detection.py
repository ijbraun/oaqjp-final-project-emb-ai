import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {'text':text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url,json=myobj,headers=header)
    formatted_response = json.loads(response.text)
    
    emotion = formatted_response['emotionPredictions']['emotion']

    anger_score = emotion['anger']
    disgust_score = emotion['disgust']
    fear_score = emotion['fear']
    joy_score = emotion['joy']
    sadness_score = emotion['sadness']
    dominant_score = max(emotion.values,key=emotion.get)


    return {
        'anger':anger_score,
        'disgust':disgust_score,
        'fear': fear_score,
        'joy':joy_score,
        'sadness':sadness_score,
        'dominant_emotion':dominant_score
    }