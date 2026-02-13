import requests
import json
def emotion_detector(text_to_analyze):   #This function takes the input as text_to_analyze to detect emotion
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion predict service
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    myobj= { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response=json.loads(response.text)
    #  Handle blank input (status_code = 400)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
    # Find dominant emotion
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
