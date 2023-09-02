from flask import Flask, request
from flask_restx import Api, Resource, fields
import base64
import os
import json
from PIL import Image
from io import BytesIO

app = Flask(__name__)
api = Api(app)

input_model = api.model('InputModel', {
    'base64': fields.String(required=True, description='The acronym of the name of airport')
})


@api.route('/insert-image')
class insert_image(Resource):
    @api.expect(input_model)
    def post(self):
        base64_data = json.loads(request.data)['base64'].split(',')[1]
        # image_data = data.get('image')
        if not base64_data:
            return {'message': 'No image data provided'}, 400
        decoded = base64.b64decode(base64_data)
        path = os.path.join('data2', 'image.png')
        img = Image.open(BytesIO(decoded))
        img.save(path)
        return {'message': 'Image saved successfully'}

if __name__ == '__main__':
    app.run()
