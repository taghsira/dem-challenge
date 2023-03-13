import os
import numpy as np
from flask import Flask, jsonify, request
from PIL import Image
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('fashion_mnist_model.h5')
labels = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
          'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the request
    image = request.files.get('image')
    # Open and preprocess the image
    img = Image.open(image)
    img = img.resize((28, 28))
    img = np.array(img)
    img = img.reshape(-1, 28, 28, 1)
    img = img / 255.0
    # Predict the class of the image
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction[0])
    # Return the prediction
    result = {'class': labels[predicted_class]}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))