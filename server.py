""" Executing this function will initiate the app to be
    executed over the Flask channel and deployed on
    localhost:5000
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

PORT = 5000

app = Flask(__name__)

@app.route('/')
def render_home_page():
    """ This function initiate the rendering of the app
        page over the Flask channel
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emo_detector():
    """ This function receives the text from the HTML and
        run the 'emotion_detector' function from the module
        EmotionDetection. The output is a label formatted with
        the dominant emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    response_formatted = f"For the given statement, the system response is \
            'anger': {response['anger']}, 'disgust': {response['disgust']}, \
            'fear': {response['fear']}, 'joy': {response['joy']} and \
            'sadness': {response['sadness']}. \
            The dominant emotion is {response['dominant_emotion']}."

    return response_formatted

if __name__ == '__main__':
    app.run(port = PORT)
