import requests
import json


def emotion_detector(text_to_analyze):
    """
    Analyze the input text using the Watson Emotion Prediction API
    and return emotion scores along with the dominant emotion.

    Parameters:
    text_to_analyze (str): The text provided by the user for emotion analysis.

    Returns:
    dict: A dictionary containing the scores for anger, disgust, fear,
          joy, sadness, and the dominant_emotion.
          If the input text is blank, all values are returned as None.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    # Handle blank input (status_code = 400)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_response = json.loads(response.text)

    emotion_data = formatted_response["emotionPredictions"][0]["emotion"]

    anger_score = emotion_data["anger"]
    disgust_score = emotion_data["disgust"]
    fear_score = emotion_data["fear"]
    joy_score = emotion_data["joy"]
    sadness_score = emotion_data["sadness"]

    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }