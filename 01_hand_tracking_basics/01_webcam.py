#TASK:
#Import OpenCV.
#Open your laptop webcam.
#Continuously read frames.
#Display the webcam feed.
#Print "Frame Captured" every time a frame is successfully read.
#Exit when the user presses Q.
#Properly release the webcam and close all windows.
import cv2

camera = cv2.VideoCapture(0)

while True:
    success,frame = camera.read() # success is bool and frame is the current img
    if not success: 
        break
    if success:
        cv2.imshow("cam",frame)
        print("frame Captured")
        print(frame.shape)
    #closing cam
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()