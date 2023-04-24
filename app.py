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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # Get the user's name, family name, and signature
        return render_template("index.html")
    #     name = request.form["name"]
    #     family_name = request.form["family_name"]
    #     signature_data = request.form["signature"]
    #
    #     # Decode the signature image from base64
    #     signature_image = base64.b64decode(signature_data.split(",")[-1])
    #     signature_image = Image.open(BytesIO(signature_image))
    #
    #     # Save the signature image
    #     signature_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{name}_{family_name}.png")
    #     signature_image.save(signature_path)
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
