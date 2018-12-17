import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption("Draw primit")
clock = pygame.time.Clock()
White =  (255,255,255,255)
done = False
while not done:
    	# --- Main event loop
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
		done = True # Flag that we are done so we exit this loop
	
pygame.draw.rect(screen, White, (20,20,100,75))
pygame.draw.rect(screen, (64,128,255), (150,20,100,75), 8)
	
	pygame.display.update()
	clock.tick(60)

