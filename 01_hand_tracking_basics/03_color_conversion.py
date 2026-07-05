#Task
#Open the webcam.
#Read frames continuously.
#Convert each frame from BGR to RGB.
#Print the shape of both frame and rgb_frame.
#Display the original frame.
#Exit when Q is pressed

import cv2

camera = cv2.VideoCapture(0)

while True:
    success,frame=camera.read()
    if not success:
        break

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("Camera",frame)
    print("frame shape",frame.shape)
    print("rgb shape",rgb.shape)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()