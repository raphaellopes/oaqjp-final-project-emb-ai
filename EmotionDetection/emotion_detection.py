import requests
import json

def emotion_detector(text_to_analyze):
    """
    This function returns the emotion data based on the arg 'text_to_analyze'
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { 'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock' }
    data = { 'raw_document': { 'text': text_to_analyze } }
    response = requests.post(url, json = data, headers = headers)

    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotion = response_dict['emotionPredictions'][0]['emotion']

        anger_score = emotion['anger']
        disgust_score = emotion['disgust']
        fear_score = emotion['fear']
        joy_score = emotion['joy']
        sadness_score = emotion['sadness']
        dominant_emotion = max(emotion, key=emotion.get)

    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    else:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
