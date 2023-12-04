from djitellopy import Tello
from threading import Thread
from tello_modules.camera_capture import TelloImageCaptureAndFlying

if __name__ == "__main__":
    tello = Tello()
    tello_capture_flying = TelloImageCaptureAndFlying(tello)

    t1 = Thread(target=tello_capture_flying.capture_and_display_images)
    # t2 = Thread(target=tello_capture_flying.circle_movement_tello)

    t1.start()
    # t2.start()
    
    t1.join()
    # t2.join()