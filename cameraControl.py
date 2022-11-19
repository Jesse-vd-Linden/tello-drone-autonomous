import keyPressModule as kp
from djitellopy import tello
from time import sleep
import cv2, math, time

global img

kp.init()
drone = tello.Tello()
drone.connect()
print("BATTERY: ", drone.get_battery())
drone.streamon()

def getKeyboardInput():
    lr, fb, up, yv = 0, 0, 0, 0

    speed = 200

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): up = speed
    elif kp.getKey("s"): up = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("e"): drone.takeoff()
    if kp.getKey("q"): drone.land()

    if kp.getKey("f"): drone.flip(direction='b')
    # if kp.getKey("g"): drone.flip_back()
    # if kp.getKey("b"): drone.flip_right()
    # if kp.getKey("v"): drone.flip_left()

    if kp.getKey("z"):
        cv2.imwrite(f'resources/images/{time.time()}.jpg', img)
        time.sleep(0.3)


    return [lr, fb, up, yv]

 
while True:
    control = getKeyboardInput()
    print("Battery level: ", drone.get_battery())

    drone.send_rc_control(control[0],control[1],control[2],control[3])
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (480,360))
    cv2.imshow("drone", img)
    cv2.waitKey(40)