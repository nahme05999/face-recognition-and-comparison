# Facial Recognition in Python using OpenCV
This web application leverages the power of face recognition to compare a live webcam stream with a database of 40 known faces. The application is built using Python and popular libraries such as OpenCV, Streamlit, face_recognition, and MTCNN.

# Features
Face Database Initialization:
Reads through a series of 40 images.
Detects faces in each image.
Computes face encodings.
Stores the results along with file names.

# Face Recognition:
Takes an image file, computes its face encoding.
Compares it with a list of known face encodings.
Returns the distances and file names of the top five closest matches.

# WebRTC Webcam Streaming:
Configures WebRTC connections.
Specifies an ICE server (STUN server) provided by Google.
Processes webcam video frames.
Detects faces using MTCNN.
Crops a sub-image around the detected face.
Draws a rectangle around the face in the original image.

# WebRTC Setup:
Sets up webcam streaming through WebRTC.
Supports both sending and receiving video.
Enables asynchronous processing of video frames.

# Face Comparison Trigger:
Creates a Streamlit app with a button to trigger face comparison.
Captures the detected face.
Performs face recognition.
Displays the extracted face image along with the top five most similar faces and their similarity score in percentage on the sidebar.

# Compatibility
The code is tested on Windows and Linux using Python 3.9 using Anaconda environment. The demo can be viewed here.
  
# Getting Started
Install the following packages in advance:
numpy
streamlit
streamlit_webrtc
Pillow
opencv-python
face_recognition
tensorflow
mtcnn
mtcnn-opencv
