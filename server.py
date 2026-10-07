''' Executing this function initiates the application of emotion detection to be
    executed ove the Flask channel and deployed on localhost:5000.
''' 
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    ''' This function receives the text from the HTML interface and runs
        and detects the associated emotions. The output shows the emotion label 
        and confidence score for the provided text.
    '''
    # Retrieve text from the request arguments
    text_To_Analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_To_Analyze)

    # Extract the dominant and sadness emotions for the return statement
    dominant_emotion = response.pop('dominant_emotion', None)
    sadness_emotion = response.pop('sadness', None)

    return f"For the given statement, the system response is {str(response)[1:-1]} \
        and 'sadness': {sadness_emotion}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application page over the 
        Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
