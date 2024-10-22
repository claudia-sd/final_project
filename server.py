from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_analizer():
    text = request.args.get('textToAnalyze')
    emotion = emotion_detector(text)
    emotion_output = (f"For the given statement, the system response is 'anger': {emotion['anger']}, 'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, 'joy': {emotion['joy']} and 'sadness': {emotion['sadness']}. The dominant emotion is <strong>{emotion['dominant_emotion']}</strong>.")
    return emotion_output


if __name__ == "__main__":
    app.run(port=5000)
