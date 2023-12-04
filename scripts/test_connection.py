import cv2
import time
from djitellopy import Tello

tello = Tello()
    
tello.streamon()
frame_read = tello.get_frame_read()

# Wait for startup
time.sleep(3)
print("Battery level: ", tello.get_battery())

try:
    while True:
        # In reality you want to display frames in a seperate thread
        # Otherwise they will freeze while the drone moves
        img = frame_read.frame
        img = cv2.resize(img, (480,360))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("drone", img)
        
        cv2.waitKey(1) & 0xff
except KeyboardInterrupt:
    pass