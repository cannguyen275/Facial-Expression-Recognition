import numpy as np
import cv2
import keras
from keras.models import load_model
import os

facial_index = {0:"Angry",1 :"Disgust",2:"Fear",3:"Happy",4:"Sad",5:"Surprise",6:"Neutral"}
model = load_model(os.path.join('model',"facial_expression.h5"))

def draw_str(dst, x_y, s):
    x, y = x_y
    cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv2.LINE_AA)
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)

def predict(image):
    im = cv2.resize(image,(48,48),interpolation=cv2.INTER_AREA)
    im_reshape = im.reshape((1,48,48,1)).astype(np.float32)/255
    y = model.predict_classes(im_reshape)
    return facial_index[int(y)]

cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
cap = cv2.VideoCapture(0)
while cap.isOpened() :
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detection = cascade.detectMultiScale(frame_gray,scaleFactor=1.3,minNeighbors=5)
    for (x,y,w,h) in detection:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi = frame_gray[y:y+h,x:x+w]
        #cv2.imshow("frame", roi)
        if roi.shape[0]<48 or roi.shape[1]<48 :
            pass
        else :
            facial = predict(roi)
            #cv2.putText(frame,facial,(int(x),int(y-10)),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
            draw_str(frame, (x - 20, y - 20), facial)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()