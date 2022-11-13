import keyPressModule as kp
from djitellopy import tello
from time import sleep
import cv2, math, time


kp.init()
drone = tello.Tello()
drone.connect()
print("BATTERY: ", drone.get_battery())

drone.streamon()
frame_read = drone.get_frame_read()


def getKeyboardInput():
    lr, fb, up, yv, flip = 0, 0, 0, 0, 0

    speed = 200

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): up = speed
    elif kp.getKey("s"): up = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("t"): flip = drone.takeoff()
    if kp.getKey("r"): flip = drone.land()

    if kp.getKey("f"): flip = drone.flip_forward()
    if kp.getKey("g"): flip = drone.flip_back()
    if kp.getKey("v"): flip = drone.flip_left()
    if kp.getKey("b"): flip = drone.flip_right()


    if kp.getKey("SPACE"): drone.get_video_capture()

    return [lr, fb, up, yv]


 
while True:
    control = getKeyboardInput()
    print("Battery level: ", drone.get_battery())

    drone.send_rc_control(control[0],control[1],control[2],control[3])
    img = frame_read.frame
    img = cv2.resize(img, (720,480))
    cv2.imshow("drone", img)
    cv2.waitKey(1)