import os
import pickle
from random import randint
from flask_cors import CORS, cross_origin

import cv2
from PIL.Image import Image
from flask import Flask, request, jsonify
from skimage import feature
import numpy as np
from datetime import datetime

app = Flask('cataract_predict')

cors = CORS(app,  resources={
    r"/*": {
        "origins": "*"
    }
})

app.config['CORS_HEADERS'] = 'Content-Type'

UPLOAD_FOLDER = os.path.join(os.curdir,"Imagem")
ALLOWED_EXTENSIONS = set(['png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST'])
@cross_origin()

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        file = request.files['image']

        now = datetime.now()
        dt_string = now.strftime("%H_%M_%S_%MS")
        print("time =", dt_string)

        filename = dt_string+"_"+str(randint(0, 100000))+".png"
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        #write your function that loads the model
        model = get_model() #you can use pickle to load the trained model

        print(os.path.join(os.curdir,"Imagem",filename))

        file.save(os.path.join(os.curdir,"Imagem",filename))

        imArray = cv2.imread(os.path.join(os.curdir,"Imagem",filename))

        # img = cv2.resize(image, (800, 800))
        gray = cv2.cvtColor(imArray, cv2.COLOR_BGR2GRAY)
        hist = describe(24,3,gray)

        predict = model.predict(hist.reshape(1, -1))
        os.remove(os.path.join(os.curdir,"Imagem",filename))

    return jsonify(predict[0])

def get_model():
    mainDir = os.getcwd()

    os.chdir(os.path.join(os.curdir, "Modelo"))

    fileLucas = 'finalized_model.sav'
    loaded_model_Lucas = pickle.load(open(fileLucas, 'rb'))

    os.chdir(mainDir)

    return loaded_model_Lucas

def describe(numPoints, radius, image, eps=1e-7):
    # compute the Local Binary Pattern representation
    # of the image, and then use the LBP representation
    # to build the histogram of patterns
    lbp = feature.local_binary_pattern(image, numPoints,
        radius, method="uniform")
    (hist, _) = np.histogram(lbp.ravel(),
        bins=np.arange(0, numPoints + 3),
        range=(0, numPoints + 2))
    # normalize the histogram
    hist = hist.astype("float")
    hist /= (hist.sum() + eps)
    # return the histogram of Local Binary Patterns
    return hist


if __name__== '__main__':
    port = int(os.environ.get("PORT", 9999))
    app.run(host='localhost', port=port)