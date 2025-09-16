from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")

def emotionDetector():
    # Retrieve the input text from request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Obtain emotion scores and dominant by passing input text to Emotion Detector 
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid text! Please try again!"
    else:
        return "For the given statement, the system response is 'anger': {}, 'disgust' : {},'fear': {},'joy' : {} and 'sadness': {}. The dominant emotion is {}".format(response['anger'], response['disgust'], response['fear'],response['joy'],response['sadness'],response['dominant_emotion'])
    

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
