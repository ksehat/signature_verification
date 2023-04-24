import os
from flask import Flask, render_template, request, redirect, url_for
import cv2
from PIL import Image
import numpy as np
from io import BytesIO
import base64
import tensorflow as tf
# from signature_verification import SignatureVerificationModel

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Load the trained model
# model = SignatureVerificationModel()
# model.load_weights("path/to/your/trained/model")

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        national_id = request.form["national_id"]
        signature_data = request.form["signature"]
        mouse_data = request.form["mouse_data"]

    #
        # Decode the signature image from base64
        signature_image = base64.b64decode(signature_data.split(",")[-1])
        signature_image = Image.open(BytesIO(signature_image))
    #
        # Save the signature image
        signature_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{first_name}_{last_name}_{national_id}.png")
        signature_image.save(signature_path)
    #
    #     # Check the authenticity of the signature
    #     result = model.verify_signature(name, family_name, signature_path)
    #
    #     if result["is_authenticated"]:
    #         return "Authenticated"
    #     else:
    #         return "Not authenticated"
    # return render_template("index.html")

if __name__ == "__main__":
    app.run(host='http://127.0.0.1',port=8080)
