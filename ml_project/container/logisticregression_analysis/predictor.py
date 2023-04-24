# This is the file that implements a flask server to do inferences. It's the file that you will modify to
# implement the scoring for your own algorithm.

import os
import json
import joblib
import flask
import pandas as pd
import re
from bs4 import BeautifulSoup
from io import StringIO
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

#Define the path
prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')


# Load the model components
loaded_model = joblib.load(os.path.join(model_path, 'logistic_regression.pkl'))


# The flask app for serving predictions
app = flask.Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    # Check if the classifier was loaded correctly
    try:
        loaded_model
        status = 200
    except:
        status = 400
    return flask.Response(response= json.dumps(' '), status=status, mimetype='application/json' )

@app.route('/invocations', methods=['POST'])
def transformation():
    # # Get input JSON data and convert it to a DF

    input_json = flask.request.get_json(force=True)['input']
    print("data is :: " + format(input_json))

    # # Tokenize data and predict
    dont_remove = ['out','not','up','%','$']
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
    BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
    STOPWORDS = set(stopwords.words('english')).difference(dont_remove)

    def clean_text(text):
        """
            text: a string

            return: modified initial string
        """
        text = BeautifulSoup(text, "lxml").text  # HTML decoding
        text = text.lower()  # lowercase text
        text = REPLACE_BY_SPACE_RE.sub(' ', text)  # replace REPLACE_BY_SPACE_RE symbols by space in text
        text = BAD_SYMBOLS_RE.sub('', text)  # delete symbols which are in BAD_SYMBOLS_RE from text
        #     text = ' '.join(word for word in text.split() if word not in STOPWORDS)  # delete stopwors from text
        return text

    input_json = clean_text(input_json)
    prediction = loaded_model.predict(pd.read_csv(StringIO(input_json), sep='\t'))
    print(prediction[0])
    # # preparing a response object and storing the model's predictions
    # response = {}
    # response['predictions'] = pd.Series(prediction).to_json(orient='values')
    # return flask.jsonify(response)


    # Transform predictions to JSON
    result = {'prediction': prediction[0]}
    result = json.dumps(result)
    return flask.Response(response=result, status=200, mimetype='application/json')
    # return flask.jsonify(result)


