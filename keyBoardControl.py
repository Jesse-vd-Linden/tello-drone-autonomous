import keyPressModule as kp
from djitellopy import tello
from time import sleep

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()
frame_read = drone.get_frame_read()


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

    if kp.getKey("t"): drone.takeoff()
    if kp.getKey("r"): drone.land()

    if kp.getKey("SPACE"): 
        drone.land()

    if kp.getKey("f"): drone.flip_forward()
    if kp.getKey("g"): drone.flip_back()
    if kp.getKey("b"): drone.flip_right()
    if kp.getKey("v"): drone.flip_left()


    return [lr, fb, up, yv]


 
while True:
    control = getKeyboardInput()
    drone.send_rc_control(control[0],control[1],control[2],control[3])
    sleep(0.05)