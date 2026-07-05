#Requirements:
#Open webcam.
#Create Hands().
#Create:
#mp_draw = mp.solutions.drawing_utils
#Process each RGB frame.
#If a hand is detected:
#Draw the landmarks.
#Display the webcam.
#Exit with Q.

import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

while True:
    success,frame = camera.read()
    if not success:
        break

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_marks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_marks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("camera",frame)

    if cv2.waitKey(1)& 0xFF==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()