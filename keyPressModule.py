import pygame

def init():
    pygame.init()

    win = pygame.display.set_mode((400, 400))


speed = 100
rotate_speed = 30

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans





def main():
    if getKey("LEFT"):
        print('left key pressed')
    if getKey("RIGHT"):
        print('right key pressed')
    # if key == 27: # ESC
    #     break
    # elif key == ord('p'):
    #     tello.takeoff()
    # elif key == ord('w'):
    #     tello.move_forward(speed)
    # elif key == ord('s'):
    #     tello.move_back(speed)
    # elif key == ord('a'):
    #     tello.move_left(speed)
    # elif key == ord('d'):
    #     tello.move_right(speed)
    # elif key == '\x1b[C':
    #     tello.rotate_clockwise(rotate_speed)
    # elif key == '\x1b[D':
    #     tello.rotate_counter_clockwise(rotate_speed)
    # elif key == '\x1b[A':
    #     tello.move_up(rotate_speed)
    # elif key == '\x1b[B':
    #     tello.move_down(rotate_speed)
    # elif key == ord('i'):
    #     tello.land()



if __name__ == '__main__':
    init()
    while True:
        main()