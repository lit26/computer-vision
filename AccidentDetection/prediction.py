import cv2
import os
import numpy as np
from keras.models import load_model
from skimage import io
from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input

predict_dir = 'predict'
CLASSES = ['Fire','Robbery','Safe']
model = load_model('inception.model')
for root, dirs, files in os.walk(predict_dir):
	for file in files:
	    img = io.imread(os.path.join(root, file))
	    img = image.img_to_array(img)
	    img = np.expand_dims(img, axis=0)
	    img = preprocess_input(img)
	    preds = model.predict(img)
	    j = np.argmax(preds)
	    print("Images: "+ file+", Predict: "+CLASSES[j])