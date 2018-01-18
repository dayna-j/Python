# Why should I blit a background onto the displace surface rather than
# drawing things directly on the screen surface?

# 1) EMBED GAME SCREEN INTO LARGER WINDOW WHICH CONTAINS SCORE INFO
# 2) ACCEPT USER INPUT IN ORDER TO PRINT USERNAME TO WINDOW WITH SCORE
# 3) BULLET INSTANCE ATTRIBUTE THAT KEEPS COUNT OF HOW MANY COLLISIONS 
#	 THAT PARTICULAR BULLET HAS HAD.  PRINT MESSAGES FOR COMBOS.




import pygame
import random
from sys import exit
import os

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

color_list = [red,green,blue]

#-----------------------RESOURCE HANDLING FUNCTIONS---------------------

def load_sound(name):
	
	class NoneSound:
		def play(self):
			pass
	
	if not pygame.mixer or not pygame.mixer.get_init():
		return NoneSound()
	soundpath = os.path.join('data', name)
	try:
		sound =  pygame.mixer.Sound(soundpath)
	except pygame.error, message:
		print 'Cannot load sound: ', soundpath
		raise SystemExit, message
	return sound

def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

#-----------------------------------------------------------------------

def makeWalls():
	
	wall = Wall(0,370,10,30)											# Instantiates 10px by 30px Wall object which will be drawn at (0,370)
	Container.wall_list.add(wall)										# Adds previously created Wall object to wall_list sprite container.
	Container.all_sprites_list.add(wall)
	wall = Wall(690,370,10,30)											# Instantiates 10px by 30px Wall object which will be drawn at (690,370)
	Container.wall_list.add(wall)										# Adds previously created Wall object to wall_list sprite container.
	Container.all_sprites_list.add(wall)
	wall = Wall(0,390,700,10)
	Container.wall_list.add(wall)
	Container.all_sprites_list.add(wall)


def makeBlocks():
	
	for i in range(20):												# Iterates through the nested statements 50 times.
	
		block = Block(blue)												# Instantiates 50 Block objects and points block variable to them.
	
		block.rect.x = random.randrange(10,screen_width-10)				# Assign the x coordinate of the block's rect attribute to a random number.
		block.rect.y = random.randrange(350)							# Assign the y coordinate o the block's rect attribute to a random number.
#		block.rect.inflate_ip(-15,-15,)
		
		Container.block_list.add(block)									# Add every block to block_list.
		Container.all_sprites_list.add(block)							# Add every block to all_sprites_list.


def scoreBoard():
	font = pygame.font.Font(None,26)
	fontHeight = font.get_height()
	
	scoreText = font.render("Score: " + str(score), True, green)
	
	shotsText = font.render("Shots Fired: " + str(player.shotsFired),
				True, green)
	
	
	return screen.blit(scoreText, [10,10]),screen.blit(shotsText, [10,10+fontHeight])

#--------------------------CLASS DEFINITIONS----------------------------

class Block(pygame.sprite.Sprite):										# Defines Block class as child of pygame.sprite.Sprite parent class.
	
	def __init__(self, color):											# Defines Block's constructor method.
		
		pygame.sprite.Sprite.__init__(self)								# Defines Block's parent's constructor method.
		
		self.color = color
		
		self.image = pygame.Surface([20,15])							# Creates a display surface object 20px wide by 15x high
		self.image.fill(self.color)											# Fills the previously created surface object and fills it with a given color.
		
		self.rect = self.image.get_rect()								# <rect(0, 0, 20, 15)>
		
	def update(self):                                                   # Update method is called every cycle through while loop.
		
		self.rect.x = self.rect.x + 4
		
		if self.rect.x >= 710:
			self.rect.x = random.randrange(-25,-10)
			self.rect.y = random.randrange(0, 350)


class Player(pygame.sprite.Sprite):									# Defines Player class
	
	change_x = 0
	change_y = 0
	
	def __init__(self,x,y):
		
		pygame.sprite.Sprite.__init__(self)
		
		self.x = x
		self.y = y
		
		self.image = pygame.Surface([x,y])								# Creates surface object (x px by y px) and points self.image instance variable to it
		self.image.fill(red)											# Fills the surface object with red color
		
		self.rect = self.image.get_rect()								#
		self.rect.x = ((screen_width) / 2)								# Initial position of the x coordinate of the rect object will be half the screen width
		self.rect.y = 370												# y coordinate of the Player rect object will remain constant at 370
		
		self.shotsFired = 0
		
	def changeSpeed(self,x,y):
		
		self.change_x = self.change_x + x
		self.change_y = self.change_y + y
		
	def update(self,walls):												# Defines update method. walls must be a sprite container containing Wall objects.
		
		old_x = self.rect.x												# When update method is called, the current x coordinate of the rect will be pointed to by old_x.
		
		new_x = old_x + self.change_x									# new_x will be the value of old_x + the change in x
		
		self.rect.x = new_x												# Assigns the x position of the upper left corner of the rect to the value of new_x calculated above.
		
																		
																		# spritecollide(sprite, group, dokill, collided = None) -> Sprite_list
																		# Returns a list of all Sprites in the indicated group which intersect with another Sprite.
																		# 
		collide = pygame.sprite.spritecollide(self, walls, False)		# collide method will return a list of all sprites in the walls_list which intersect with 
																		# the player object.  *NOTICE* that the dokill argument is False.  We do not want the walls to 
																		# disappear.
		
		if collide:														# Collide will be true when sprites are present in the collide list.  If collide is true, then...
			thud.play()
			self.rect.x = old_x											# returns the x position of the upper left corner of the Player object rect to it's original	
																		# value--old_x.  The old_x was determined when the update method was called.
		
		old_y = self.rect.y												# When update method is called, the current y coordinate of the rect will be pointed to by old_y.
		new_y = old_y + self.change_y									# new_x will be the value of old_x + the change in x
		self.rect.y = new_y												# Assigns the y position of the upper left corner of the rect to the value of new_y calculated above.
		
		collide = pygame.sprite.spritecollide(self, walls, False)
		
		if collide:														# Collide will be true when sprites are present in the collide list.  If collide is true, then...
			self.rect.y = old_y											# returns the y position of the upper left corner of the Player object rect to it's original
																		# value--old_y.  The old_y was determined when the update method was called.
	
	def shoot(self):
		
		self.shotsFired += 1
		bullet = Bullet(player.rect.x+8,player.rect.y)				# Instantiates bullet object
		Container.all_sprites_list.add(bullet)							# Add each bullet to all_sprites_list
		Container.bullet_list.add(bullet)								# Add each bullet to bullet_list


class Bullet(pygame.sprite.Sprite):									# Defines Bullet class.
	
#	count = 0
	
	def __init__(self,x,y):
#		self.__class__.count += 1
		
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface([4,5])
		self.image.fill(random.choice(color_list))
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.hits = 0
	
	#~ def update(self):
		#~ 
		#~ for eachBullet in Container.bullet_list:						# For every bullet in bullet_list, do the following..
		#~ 
			#~ eachBullet.rect.y = eachBullet.rect.y - 10					# Decreases y coordinate of the Bullet object's rect attribute by 5 pixels
																		#~ # ||Remember||,decreasing y will move the bullet towards the top of the screen.
																		#~ 
																		#~ 
																		#~ # spritecollide(sprite, group, dokill, collided = None) -> Sprite_list
																		#~ # Returns a list of all Sprites in the indicated group which intersect with another Sprite.
																		#~ # Intersection is determined by comparing the Sprite.rect attribute of each Sprite in the 
																		#~ # indicated group against the sprite indicated in the spritecolide argument
																		#~ # The dokill argument is a bool. If set to True, all Sprites that collide will be removed
																		#~ # from the indicated group.
			#~ block_hit_list = pygame.sprite.spritecollide(eachBullet,
													#~ Container.block_list, True)
		#~ 
			#~ for eachblock in block_hit_list:
				#~ explode.play()
				#~ #Container.bullet_list.remove(bullet)						# Remove the bullet from bullet_list
				#~ #Container.all_sprites_list.remove(bullet)
				#~ #score = score + 1
				#~ #print score
	#~ 
			#~ if eachBullet.rect.y < -10:											# If a bullet has gone off the top of the screen, remove it from bullet_list and all_sprites_list
			#~ 
				#~ Container.bullet_list.remove(eachBullet)
				#~ Container.all_sprites_list.remove(eachBullet)
		

class Wall(pygame.sprite.Sprite):										# Defines Wall class as child of pygame.sprite.Sprite parent class
	
	def __init__(self,x,y,width,height):								# Defines Wall's constructor's method.  Constructor initializes all of the
																		# Wall object's attributes--it's instance variables--and sets them to the
																		# values passed in when instantiated.  
																		# Constructor method requires 4 arguments when instantiated; x,y,width,height
																		
		
		pygame.sprite.Sprite.__init__(self)								# Calls constructor method for parent class.
		
		self.image = pygame.Surface([width, height])					# Creates a surface object width px by height px and points self.image instance variable to it.
		self.image.fill(green)											# Fills previously created surface object with blue color.
		
																		# get_rect() Surface method returns RECT OBJECT with the same rectangular area as
		self.rect = self.image.get_rect()								# the surface object; self.image.
																		# self.rect instance variable points to this rect object
																		
																		# self.rect=<rect(x, y, width, height)>
		
		self.rect.x = x													# Assigns to the x position of the upper left corner of the rect.
		self.rect.y = y													# Assigns to the y position of the upper left corner of the rect.


class Container:
	
	all_sprites_list = pygame.sprite.Group()							# Creates container object for all sprites.
	block_list = pygame.sprite.Group()									# Creates a container object for Block sprites.
	bullet_list = pygame.sprite.Group()									# Creates a container object for bullet sprites.
	wall_list = pygame.sprite.Group()



pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])

backImg = 'forest.jpg'
background = pygame.image.load('data/'+backImg)
background = background.convert()
#background.fill((255,255,255))


zap = load_sound('zap.wav')
zap.set_volume(0.2)
explode = load_sound('explode.wav')
explode.set_volume(0.2)
thud = load_sound('wallthud.wav')
thud.set_volume(0.7)

player = Player(20,20)													# Instantiates Player object and points player variable to it.
Container.all_sprites_list.add(player)									# Adds Player object to all_sprites_list.

pygame.mouse.set_visible(True)											# Causes the mouse cursor to be invisible.

clock = pygame.time.Clock()												


score = 0

makeBlocks()
makeWalls()

font = pygame.font.Font(None, 36)
title_page = 1

display_title = True

#--------------------TITLE PAGE EVENT LOOP------------------------------

while display_title:
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				title_page += 1
				if title_page == 2:
					display_title = False
	
	screen.blit(background,(0,0))
	
	if title_page == 1:
		
		text=font.render("Instructions:", True, white)
		screen.blit(text, [170, 150])
		text=font.render("Shoot the blocks", True, red)
		screen.blit(text, [170, 180])
		text=font.render("Press the SPACE BAR to continue..", True, white)
		screen.blit(text, [170, 210])
	
	clock.tick(20)
	
	pygame.display.flip()

#--------------------MAIN GAME EVENT LOOP-------------------------------

while True:
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			
			exit()
		
		if event.type == pygame.KEYDOWN:								# 
			
			if event.key == pygame.K_SPACE:
				
				zap.play()
				player.shoot()
			
			if event.key == pygame.K_LEFT:
				player.changeSpeed(-5,0)
			if event.key == pygame.K_RIGHT:
				player.changeSpeed(5,0)
			
			
		if event.type == pygame.KEYUP:									#KEYUP events will do the inverse of it's KEYDOWN partner.
			
			if event.key == pygame.K_LEFT:
				player.changeSpeed(5,0)
			if event.key == pygame.K_RIGHT:
				player.changeSpeed(-5,0)
	
	
	
	 
	for bullet in Container.bullet_list:								# For every bullet in bullet_list, do the following..
		
		bullet.rect.y = bullet.rect.y - 10								# Decreases y coordinate of the Bullet object's rect attribute by 10 pixels
																		# ||Remember||,decreasing y will move the bullet towards the top of the screen.
																		
																		
																		# spritecollide(sprite, group, dokill, collided = None) -> Sprite_list
																		# Returns a list of all Sprites in the indicated group which intersect with another Sprite.
																		
																		# Intersection is determined by comparing the Sprite.rect attribute of each Sprite in the 
																		# indicated group against the sprite indicated in the spritecolide argument
																		# The dokill argument is a bool. If set to True, all Sprites that collide will be removed
																		# from the indicated group.
		block_hit_list = pygame.sprite.spritecollide(bullet,
													Container.block_list, True)
		
		for eachblock in block_hit_list:
			bullet.hits += 1
			print bullet.hits
			explode.play()
			#Container.bullet_list.remove(bullet)						# Remove the bullet from bullet_list
			#Container.all_sprites_list.remove(bullet)
			score = score + 1
			print score
	
		if bullet.rect.y < -10:											# If a bullet has gone off the top of the screen, remove it from bullet_list and all_sprites_list
		
			Container.bullet_list.remove(bullet)
			Container.all_sprites_list.remove(bullet)
		
		
		
	screen.blit(background, (0,0))
	player.update(Container.wall_list)
	Container.bullet_list.update()
	
	Container.block_list.update()
	Container.all_sprites_list.draw(screen)
		
	scoreBoard()
	clock.tick(30)
	
	pygame.display.flip()


pygame.quit()


