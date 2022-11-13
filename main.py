from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()


while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    img = frame_read.frame
    img = cv2.resize(img, (360,240))
    cv2.imshow("drone", img)
    cv2.waitKey(1) & 0xff
    
tello.land()