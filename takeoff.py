import CoDrone
import pygame
import sys
#from CoDrone import Direction


pygame.init()
display = pygame.display.set_mode((300, 300))



drone = CoDrone.CoDrone()
drone.pair("0457")
pygame.event.set_grab(True)

# creating a running loop
while True:

    # creating a loop to check events that
    # are occurring

    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                drone.takeoff()
                drone.set_arm_led(CoDrone.Color.Green, CoDrone.Mode.BLINK)




            if event.key == pygame.K_w:
                drone.move(1)

                drone.set_arm_led(CoDrone.Color.Green, CoDrone.Mode.BLINK)
                #drone.go(Direction.FORWARD, 1, 25)
                print("Key w has been pressed")


            if event.key == pygame.K_a:
                drone.set_yaw(-100)
                #drone.go(Direction.LEFT, 1, 25)
                drone.set_arm_led(CoDrone.Color.Blue, CoDrone.Mode.BLINK)
                print("Key a has been pressed and yaw should be -100")


            if event.key == pygame.K_s:
                drone.set_yaw(0)
                drone.set_arm_led(CoDrone.Color.Orange, CoDrone.Mode.BLINK)
                print("Key s has been pressed and yaw should be 0")


            if event.key == pygame.K_d:
                drone.set_yaw(100)
                #drone.go(Direction.RIGHT, 1, 25)
                drone.set_arm_led(CoDrone.Color.Purple, CoDrone.Mode.BLINK)
                print("Key d has been pressed and yaw should be 100")


            if event.key == pygame.K_SPACE:
                drone.set_arm_led(CoDrone.Color.Red, CoDrone.Mode.SOLID)
                #drone.set_arm_led(CoDrone.Color.Red, CoDrone.Mode.BLINK)
                drone.land()
                drone.close()
                pygame.quit()
                sys.exit()







#drone = CoDrone.CoDrone()
#drone.pair("0457")
#drone.set_arm_led(CoDrone.Color.Green, CoDrone.Mode.BLINK, 45)
#drone.takeoff()
#drone.hover(2)
#drone.land()
#drone.close()






#drone #457