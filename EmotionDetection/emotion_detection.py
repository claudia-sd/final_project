from flask import Flask, request, json
import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return ('No text entered')

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url,headers=header,json=input_json)

    if response.status_code == 200:
        formatted_resp = json.loads(response.text)
        emotions = formatted_resp['emotionPredictions'][0]['emotion']
        max_emotion = max(emotions.values())
        max_index = [key for key in emotions if emotions[key] == max_emotion]
        emotions['dominant_emotion'] = max_index[0]
        return (emotions)
    else:
        return none