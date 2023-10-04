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
The code is tested on Windows OS using Python 2.0. The demo can be viewed here.
  
Getting Started
Clone the Repository:

Begin by cloning this repository to your local machine. Open a terminal or command prompt and run the following command:
bash
Copy code
git clone https://github.com/your-username/face-recognition-web-app.git
Replace "your-username" with your GitHub username if you forked the repository.
Install Dependencies:

Navigate to the project directory using the terminal or command prompt:
bash
Copy code
cd face-recognition-web-app
Install the required Python dependencies using pip:
bash
Copy code
pip install -r requirements.txt
Run the Streamlit App:

With the dependencies installed, you can now run the Streamlit app. Use the following command:
bash
Copy code
streamlit run your_app.py
Replace "your_app.py" with the actual name of the Python script containing your application code.
Access the Web Application:

Once the app is running, you should see output indicating that the app is available on a specific address (e.g., http://localhost:8501/). Open your web browser and navigate to this address to access the face recognition web application.
Interact with the Application:

Follow the on-screen instructions to interact with the application. This may involve clicking buttons, allowing webcam access, and triggering face comparison.
Explore and Enhance:

Feel free to explore the application's functionality and experiment with the code. If you have specific use cases or improvements in mind, you can customize the code to suit your requirements.
