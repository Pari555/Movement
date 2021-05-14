## Pygame
A set of python modules designed for writing video games.

## Coordinates in Pygame Window
- Top Left Corner of Screen is (0,0) and Bottom Right is (width, height).
- Positive x-Direction is to the Right and Negative x-Direction is to the left.
- Positive y-Direction is downwards and Negative y-Direction is upwards.

```python
#1. Import the Pygame Library
import pygame

#2. Initialize the Pygame
pygame.init()

#3. Create a Pygame Window with Size (width, height)
gameDisplay = pygame.display.set_mode((W, H))

#4. Accepting Key Inputs From the User
pygame.key.get_presses()

#5. Setup Delay Time (## in ms, (1s == 1000ms))
pygame.time.delay(##)

#6. Update Frames 
pygame.display.update()

#7. Terminate the Pygame at the End
pygame.quit()
```