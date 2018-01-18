import pygame
from pygame.draw import circle
import random

pygame.init()                                                           # initializes all pygame module

black = [0,0,0]                                                         # creates 3 variables pointing to lists holding RGB values
white = [255,255,255]
green = [0,255,0]

size = [700,500]                                                        # size will control the screen size in pixels.  700x500

screen = pygame.display.set_mode(size)                                  # Returns display surface.
pygame.display.set_caption('Falling snow..')

circle_list = []
circle_list2 = []
circle_list3 = []
blinking_list = []
click_list = []

for i in range(50):                                                    # adds 50 random pairs of [x,y] to circle_list
	x = random.randrange(0,700)                                         
	y = random.randrange(0,500)                                         
	circle_list.append([x,y])                                             

for i in range(12):                                                    # adds 12 random pairs of [x,y] to circle_list2
	x = random.randrange(0,700)
	y = random.randrange(0,500)
	circle_list2.append([x,y])

for i in range(3):                                                     # adds 3 random pairs of [x,y] to circle_list3
	x = random.randrange(0,700)
	y = random.randrange(0,500)
	circle_list3.append([x,y])

for i in range(3):                                                     # adds 3 random pairs of [x,y] to blinking_list
	x = random.randrange(0,700)
	y = random.randrange(0,500)
	blinking_list.append([x,y])


clock = pygame.time.Clock()

done = False

while done == False:                                                   #Event loop
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True
		
		if event.type == pygame.MOUSEBUTTONDOWN:                       # get new (x,y) pair at position of mouseclick
			pos = pygame.mouse.get_pos()                                #
			
			click_list.append(pos)                                      # append pos to click_list
			
	screen.fill(black)

	for i in range(len(circle_list)):                                 # iterates through a range of values for i which is equal to the length
		                                                                # of circle_list
		
		circle(screen, [127,127,127], circle_list[i], 5,1)				# circle(Surface, color, pos, radius, width=0) -> Rect
		
		                                                                # THIS IS WHAT MAKES THE CIRCLES MOVE DOWNWARDS
		circle_list[i][1] = circle_list[i][1] + 1                       # adds 1 to y value of ith circle in circle_list each time through the loop.  
		
		if circle_list[i][1] > 500:
			y = random.randrange(-50,-10)
			circle_list[i][1] = y
			x = random.randrange(0, 700)
			circle_list[i][0] = x
		
	for i in range(len(circle_list2)):
		
		circle(screen, [35,193,205], circle_list2[i], 10,2)
		
		circle_list2[i][1] = circle_list2[i][1] + 2                     # adds 2 to y value of ith circle in circle_list2
		
		if circle_list2[i][1] > 500:
			y = random.randrange(-50,-10)
			circle_list2[i][1] = y
			x = random.randrange(0,700)
			circle_list2[i][0] = x
		
	for i in range(len(circle_list3)):
																		#circle(Surface, color, pos, radius, width=0) -> Rect
		circle(screen, [162,101,48], circle_list3[i],
		               random.randrange(22,25),
					   random.randrange(1,2)
					   )
		
		circle_list3[i][1] = circle_list3[i][1] + 3                     # adds 2 to the y value of the ith circle in circle_list3
		
		if circle_list3[i][1] > 525:
			y = random.randrange(-50,-10)
			circle_list3[i][1] = y
			x = random.randrange(0,700)
			circle_list3[i][0] = x
	
	for i in range(len(blinking_list)):
		
		circle(screen, white, blinking_list[i], 2,
				random.randrange(0,3)
				)
				
		blinking_list[i][1] =  blinking_list[i][1] + 1
		#blinking_list[i][0] = blinking_list[i][0] + 2
		
		if blinking_list[i][1] > 500:
			y = random.randrange(-50,-10)
			blinking_list[i][1] = y
			x = random.randrange(0,700)
			blinking_list[i][0] = x
	
	for i in range(len(click_list)):
		
		circle(screen, white, click_list[i], 1,0)
	
	pygame.display.flip()
	clock.tick(20)

pygame.quit()

