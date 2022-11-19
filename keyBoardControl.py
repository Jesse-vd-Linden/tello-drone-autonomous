import keyPressModule as kp
from djitellopy import tello
import time
import cv2

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()
frame_read = drone.get_frame_read()




 
while True:
    control = getKeyboardInput()
    drone.send_rc_control(control[0],control[1],control[2],control[3])
    time.sleep(0.05)