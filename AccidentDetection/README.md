# AccidentDetection (Ongoing project)
Detecting fire, robbery and safe using deep neural network Keras Inception v3
- DataProcessing.ipynb: split the dataset into training directory and testing directory which contains each classes.
- AccidentDetectionV1.ipynb: using Keras Inception V3 model to train the dataset. 
  - Result: After 10 epoches, training accuracy is about 93.2%, testing accuracy is about 92.0%
- inception.model: keras model for future prediction
- prediction.py: separate prediction script for predicting image classes

**Dataset:**

Accident Images: from Google Search Images

Safe Images: https://people.csail.mit.edu/torralba/code/spatialenvelope/

Predict Images: from Google Search Images

**Model:**

AccidentDetectionV1: using Keras Inception v3

**Use Case:**
- Security Camera

- Internet of Things (IoT)
