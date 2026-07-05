#Requirements
#Open the webcam.
#Create a Hands() detector.
#Convert each frame to RGB.
#Call:
#results = hands.process(rgb_frame)
#Print:
#Processing frame...
#every loop..
#Print the type of results using:
#print(results)
#Display the webcam.
#Exit on Q.

import cv2
import mediapipe as mp

camera= cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands= mp_hands.Hands()
while True:
    success,frame=camera.read()

    if not success:
        break

    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)
    print("processing frame")

    print(results)

    cv2.imshow("camera",frame)

    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
