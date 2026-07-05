#Task
#Open the webcam.
#Print the frame shape every frame.
#Print the value of the top-left pixel (frame[0][0]).
#Display the webcam.
#Press Q to exit.

import cv2

camera = cv2.VideoCapture(0)

while True:
    success,frame = camera.read()

    if not success:
        break
    cv2.imshow("Camera",frame)

    print(frame.shape)
    print("Top left Pixel",frame[0][0])

    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
camera.release()
cv2.destroyAllWindows