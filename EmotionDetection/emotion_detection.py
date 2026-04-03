import requests
import json

def emotion_detector(text_to_analyze):
   
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send request to Watson API
    response = requests.post(url, headers=headers, json=input_json)

    # Convert the raw response text to dictionary
    data = json.loads(response.text)

    # Extract the main emotions from the first prediction
    emotions = data['emotionPredictions'][0]['emotion']

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Prepare formatted output
    formatted_output = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }

    return formatted_output