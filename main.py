import pygame

class Ball:
	def __init__(self):
		self.image = pygame.image.load("TENNISBALL.jpeg")
		self.speed = (0,1)
		self.rect = self.image.get_rect()

def main():
	pygame.init()
	screen = pygame.display.set_mode((500, 500))
	ball = Ball()

	while True:
		screen.fill((0, 0, 0)) #RGB Value
		screen.blit(ball.image, ball.rect)

if __name__ == "__main__":
	main()