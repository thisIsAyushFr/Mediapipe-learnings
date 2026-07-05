#Requirements
#Open the webcam.
#Create the Hands() detector.
#Convert each frame to RGB.
#Process the frame.
#If a hand is detected:
#Print:
#"Hand Found!"
#The number of landmarks detected.
#Display the webcam.
#Exit with Q.

import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)
temp = mp.solutions.hands
hands = temp.Hands()

while True:
    success,frame = camera.read()

    if not success:
        break

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        print("hand found")

        hand = results.multi_hand_landmarks[0]

        print("no of landmarks",len(hand.landmark))
    
    cv2.imshow("camera",frame)

    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
