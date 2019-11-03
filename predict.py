from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

# app = Flask(__name__)
# LOG = create_logger(app)
# LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales Payload"""
    
    # LOG.info(f"Scaling Payload: \n{payload}")
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict

# @app.route("/")
# def home():
#     html = f"<h3>Sklearn Prediction Home</h3>"
#     return html.format(format)

def predict():
        
    input = jsonify({"CHAS":{  
      "0":0
   },
   "RM":{  
      "0":6.575
   },
   "TAX":{  
      "0":296.0
   },
   "PTRATIO":{  
      "0":15.3
   },
   "B":{  
      "0":396.9
   },
   "LSTAT":{  
      "0":4.98
   }})
    
    print(input)

    # Logging the input payload
    # json_payload = request.json
    # LOG.info(f"JSON payload: \n{input}")
    inference_payload = pd.DataFrame(input)
    # LOG.info(f"Inference payload DataFrame: \n{inference_payload}")

    # scale the input
    scaled_payload = scale(inference_payload)
    # LOG.info(f"Scaled Payload: \n{scaled_payload}")

    # get an output prediction from the pretrained model, clf

    clf = joblib.load("./model_data/boston_housing_prediction.joblib")

    prediction = list(clf.predict(scaled_payload))

    print(prediction)
    # LOG.info(f"Prediction: \n{prediction}")

    # TO DO:  Log the output prediction value
    # return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # load pretrained model as clf
    # clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    # app.run(host='127.0.0.1', port=80, debug=True) # specify port=80
    predict
