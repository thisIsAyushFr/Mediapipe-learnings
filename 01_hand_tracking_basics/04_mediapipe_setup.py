#Requirements:
#Import OpenCV and MediaPipe.
#Open the webcam.
#Create a Hands() detector before the loop.
#Read and display webcam frames.
#Print:
#Hand detector initialized!

import cv2
import mediapipe as mp

camera=cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
print("hand detector initialised")

while True:
    success,frame = camera.read()

    if not success:
        break
    
    cv2.imshow("camera",frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()