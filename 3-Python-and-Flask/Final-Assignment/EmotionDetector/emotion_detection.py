import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        returned_response = {
            'anger': float(anger_score),
            'disgust': float(disgust_score),
            'fear': float(fear_score),
            'joy': float(joy_score),
            'sadness': float(sadness_score),
        }
        dom = max(returned_response, key=returned_response.get)
        returned_response["dominant_emotion"] = dom

    if response.status_code == 400:
        returned_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return  returned_response

    # # If the response status code is 200, extract the label and score from the response
    # if response.status_code == 200:
    #     label = formatted_response['documentSentiment']['label']
    #     score = formatted_response['documentSentiment']['score']
    # # If the response status code is 500, set label and score to None
    # elif response.status_code == 500:
    #     label = None
    #     score = None

    # Returning a dictionary containing sentiment analysis results
    # return {'label': label, 'score': score}