import av
import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer,WebRtcMode, RTCConfiguration,VideoProcessorBase
from mtcnn_cv2 import MTCNN
import face_recognition as fr
from PIL import Image

#This section reads through the series of 40 images,
#detects faces in each image, computes their face encodings and
#stores the results along with file names in a cache for speed
@st.cache_data
def get_faces_encs():
    faces_encs=[]
    file_name=[]
    for i in range(1,42):
        img=cv2.imread("faces/{}.jpeg".format(i))
        rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        try:
            img_enc=fr.face_encodings(rgb_img)[0]
            faces_encs.append(img_enc)
            file_name.append("faces/{}.jpeg".format(i))
        except IndexError:
            continue
    return [faces_encs,file_name]

#Takes the image file, computes its face encoding,
#compares it with a list of known face encodings, and
#returns the distances and file names of the top five closest matches.    
def face_rec(file,faces_encs,file_name):
    img=cv2.imread(file)
    rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=None
    try:
        img_enc=fr.face_encodings(rgb_img)[0]
    except IndexError:
        print('index error')
    result=fr.face_distance(faces_encs,img_enc)
    dist=np.sort(result)[:5]
    inx=np.argsort(result)[:5]
    files=[file_name[i] for i in inx]
    return [dist,files]

#Preparing for face recognition by obtaining face encodings,
#initializing a variable for recognition data, and
#creating a face detector using the MTCNN algorithm
fen=get_faces_encs()
rec_data=None
detector = MTCNN()

#Configuring WebRTC connections, specifying an ICE server (STUN server) provided by Google
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

#Processes the webcam video frames,
#detects faces using an object detector,
#opencv converts the captured frame into a matrix and mtcnn returns the sub-matrix box of the face, 
#draws a rectangle around the face in the original image, and returns the modified video frame
class VideoProcessor(VideoProcessorBase):
    def __init__(self) -> None:
        self.sub_face=False
        
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        rgb_frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        try:
            face=detector.detect_faces(rgb_frame)[0]['box']
        except IndexError:
            return None
        self.sub_face=img[face[1]-18:face[1]+face[3]+18,face[0]-18:face[0]+face[2]+18] 
        #cv2.putText(img,"face",(face[0],face[1]-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
        cv2.rectangle(img,(face[0]-20,face[1]-20),(face[0]+face[2]+20,face[1]+face[3]+20),(0,0,255),2)        
        return av.VideoFrame.from_ndarray(img, format="bgr24")

#Setting up webcam streaming through webrtc
stream=webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True,)

# Creates a Streamlit app with a button to trigger face comparison.
# When the button is clicked, it captures the detected face,
# performs face recognition
# displays the extracted face image along with the top five most similar faces and the similarity score in percentage on the sidebar
if st.button('Click to compare'):
    cv2.imwrite("face.jpg",stream.video_processor.sub_face)
    rec_data=face_rec('face.jpg',fen[0],fen[1])
    st.sidebar.image(Image.open('face.jpg'),"Extracted face image")
    for i in range(len(rec_data[0])):
        st.sidebar.image(Image.open(rec_data[1][i]),str(rec_data[0][i]*100))
        
    
    