import cv2
import time
from djitellopy import Tello

class TelloImageCaptureAndFlying:
    
    def __init__(self, tello : Tello):
        self.tello = tello
        tello.streamon()
        self.frame_read = tello.get_frame_read()
        
        # Wait for startup
        time.sleep(3)
        print("Battery level: ", tello.get_battery())

    def capture_and_display_images(self):
        try:
            while True:
                # In reality you want to display frames in a seperate thread
                # Otherwise they will freeze while the drone moves
                img = self.frame_read.frame
                img = cv2.resize(img, (480,360))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                cv2.imshow("drone", img)
                
                cv2.waitKey(1) & 0xff
        except KeyboardInterrupt:
            pass
        
    def circle_movement_tello(self):
        self.tello.takeoff()
        self.tello.send_rc_control(0, 10, 0, -40)
        time.sleep(15)
        print("Battery level: ", self.tello.get_battery())

        self.tello.send_rc_control(0, 0, 0, 0)

        self.tello.land()
    
