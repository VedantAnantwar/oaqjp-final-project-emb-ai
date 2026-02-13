import requests

def emotion_detector(text_to_analyze):   #This function takes the input as text_to_analyze to detect emotion
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion predict service
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    myobj= { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    return response.text  # Return the response text from the API