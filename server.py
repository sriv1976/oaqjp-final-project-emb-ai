'''
This application will be acccessed from localhost:5000 and provides user ability to enter text
and responds with scores for different emotions and also the dominant emotion for the text
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")

def emotion_detect():
    '''
    This function takes the input of the user and performs emotion detection analysis
    '''
    # Retrieve the input text from request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Obtain emotion scores and dominant by passing input text to Emotion Detector
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"""
    For the given statement, the system response is 
    'anger': {response['anger']},
    'disgust' : {response['disgust']},
    'fear': {response['fear']},
    'joy' : {response['joy']} and 
    'sadness': {response['sadness']}
    . The dominant emotion is {response['dominant_emotion']}
    """

@app.route("/")
def render_index_page():
    '''
    This renders the default page for user entry 
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
