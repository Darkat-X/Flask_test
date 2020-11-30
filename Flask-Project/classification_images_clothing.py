# Flask
from flask import Flask, render_template, request, redirect, url_for
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
# Mongo DB
import dns
from pymongo import MongoClient
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
# Image
from PIL import Image
import cv2
import io

# part of MongoDB


try:
    print("good")
    connect = MongoClient(
        "mongodb+srv://Bohui_Xia:XBH123123@clothes.6avbf.mongodb.net/<dbname>?retryWrites=true&w=majority")
    print("Connected successfully!!")
except:
    print("Could not connect to MongoDB")

db = connect.clothes
collection = db.photos

print("good")

# part of tensorflow
print(tf.__version__)

app = Flask(__name__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])

model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=20)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])


# part of flask

@app.route('/')
def index():
    return render_template('classification_images_clothing.html')


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        #uploaded_file.save(uploaded_file.filename)
        img = cv2.imread(uploaded_file.filename, 0)
        img_resize = cv2.resize(img, (28, 28))
        final_img = (np.expand_dims(img_resize, 0))
        prediction = probability_model.predict(final_img)
        clothes_type = np.argmax(prediction[0])
        print("result is")
        print(clothes_type)
        # send picture to mongo DB
        image_file = Image.open(uploaded_file.filename)

        imgByteArr = io.BytesIO()
        image_file.save(imgByteArr, format='PNG')
        imgByteArr = imgByteArr.getvalue()
        rec = {
            "image": imgByteArr,
            "tag": class_names[clothes_type]
        }
        try:
            rec = collection.insert_one(rec)
            print("Insert successfully!")
        except:
            print("Fail to insert")
        # -------------------------
    else:
        print('error')
    return render_template('result.html', result=class_names[clothes_type])
# return redirect(url_for('index'))
