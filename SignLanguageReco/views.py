from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

import cv2
import threading
import sys
import os
from .models import Gesture, GestureRecognitionResult

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'SLR')))

import gesture_recognition 
from . import views



def capture_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Preprocess frame and make prediction
        # preprocessed_frame = preprocess(frame)
        # prediction = model.predict(preprocessed_frame)
        # Display the frame with prediction
        cv2.imshow('Sign Language Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def video_feed(request):
    return StreamingHttpResponse(capture_video(), content_type='multipart/x-mixed-replace; boundary=frame')




# Create your views here.

def index(request):
    return render(request, 'index.html')


def start_gesture_recognition(request):
    threading.Thread(target=gesture_recognition.start_recognition).start()
    return HttpResponse('<img src="{% url \'video_feed\' %}" width="640" height="480">')

def store_gesture_recognition_result(request):
    gesture = Gesture.objects.get(name="wave")
    result = GestureRecognitionResult(gesture=gesture, result="recognized", confidence=0.8)
    result.save()
    return HttpResponse("Result stored")



