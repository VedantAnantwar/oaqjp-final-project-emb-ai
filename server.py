"""
Flask server for Emotion Detection Web Application.

This module handles routing, user input processing,
and communication with the emotion_detector function
to display emotion analysis results.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Render the main index page of the Emotion Detection web application.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_emotion():
    """
    Handle emotion detection requests.

    Retrieves user input text, processes it using emotion_detector,
    and returns formatted emotion analysis results.
    """

    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return output


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
