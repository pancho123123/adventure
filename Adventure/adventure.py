
import pygame, random
from random import randint
from pathlib import Path

WIDTH = 1300
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0,0,255)
PLOMO = (122,122,122)
BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure Boss")
clock = pygame.time.Clock()


def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text3(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, PLOMO)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 900
	BAR_HEIGHT = 20
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BROWN, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/sniper.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.hp = 500
		self.mana = 100
		self.armor = 2
		self.lifes = 7

class Player1(Player):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT//3
		
	def update(self):
		self.hp += 1/40
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.lifes < 0:
			self.lifes = 0
					
		if self.hp > 500:
			self.hp = 500
		if self.hp < 0:
			self.hp = 0
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -7
		if keystate[pygame.K_d]:
			self.speed_x = 7
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -7
		if keystate[pygame.K_s]:
			self.speed_y = 7
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700

	def shoot(self):
		bullet = Bullet(self.rect.right, self.rect.centery)
		all_sprites.add(bullet)
		bullets.add(bullet)

		laser_sound.play()

class Player2(Player):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT * 2 // 3
		
	def update(self):
		self.hp += 1/40
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.lifes < 0:
			self.lifes = 0
		if self.hp > 500:
			self.hp = 500
		if self.hp < 0:
			self.hp = 0
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -7
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 7
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -7
		if keystate[pygame.K_DOWN]:
			self.speed_y = 7
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700

	def shoot(self):
		bullet2 = Bullet2(self.rect.centerx, self.rect.centery)
		all_sprites.add(bullet2)
		bullets2.add(bullet2)

		laser_sound.play()

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("img/bullet.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedx = 10

	def update(self):
		self.rect.x += self.speedx
		if self.rect.left > 1300:
			self.kill()

class Bullet2(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("img/bullet.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedx = 10

	def update(self):
		self.rect.x += self.speedx
		if self.rect.left > 1300:
			self.kill()

def distance(a,b):
	#pitagoras distancia entre a y b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	return (dx**2 + dy**2)**(1/2)

def direction(a,b):
	#vector unitario desde a a b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	radio = (dx**2 + dy**2)**(1/2)
	return dx/radio, dy/radio

class Boss(pygame.sprite.Sprite):
	def __init__(self,target):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/centaur.png").convert(),(100,125))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = HEIGHT//2
		self.hp = 21875
		self.atack = 21875
		self.armor = 20
		self.speed = 3
		self.target = target

class Boss1(Boss):
	def __init__(self,target):
		super().__init__(target)
		self.rect.x = 900
		self.target = target
		
	def update(self):
		alist = [player1, player2]
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) < 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player1
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) > 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player2
		
		try:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
		except(UnboundLocalError):
			pass
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) ==
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = random.choice(alist)
		if self.hp > 21875:
			self.hp = 21875
		if self.hp < 0:
			self.hp = 0
		if self.hp <= 0:
			self.kill()
		

class Boss2(Boss):
	def __init__(self,target):
		super().__init__(target)
		self.rect.x = 1000
		self.target = target
		
	def update(self):
		alist = [player1, player2]
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) < 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player1
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) > 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player2
		
		try:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction( self, self.target)
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
		except(UnboundLocalError):
			pass
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) ==
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = random.choice(alist)
		if self.hp > 21875:
			self.hp = 21875
		if self.hp < 0:
			self.hp = 0
		if self.hp <= 0:
			self.kill()

class Creep_melee(pygame.sprite.Sprite):
	def __init__(self,target):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee1.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.alist = [100,200,300,400,500]
		self.rect.y = random.choice(self.alist)
		self.speed = 2
		self.target = target
		self.hp = 550
		self.armor = 2
		
class Creep_melee1(Creep_melee):
	def __init__(self,target):
		super().__init__(target)
		self.rect.x = 800
		self.target = target
		
	def update(self):
		alist = [player1, player2]
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) < 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player1
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) > 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player2
		
		try:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
		except(UnboundLocalError):
			pass
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) ==
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = random.choice(alist)
		
		if self.hp > 550:
			self.hp = 550
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		

class Creep_melee2(Creep_melee):
	def __init__(self,target):
		super().__init__(target)
		self.rect.x = 900
		self.target = target

	def update(self):
		alist = [player1, player2]
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) < 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player1
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) > 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player2
		
		try:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
		except(UnboundLocalError):
			pass
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) ==
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = random.choice(alist)
		if self.hp > 550:
			self.hp = 550
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		

class Creep_melee3(Creep_melee):
	def __init__(self, target):
		super().__init__(target)
		self.rect.x = 900
		self.target = target

	def update(self):
		alist = [player1, player2]
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) < 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player1
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) > 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player2
		
		try:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
		except(UnboundLocalError):
			pass
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) ==
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = random.choice(alist)
		
		if self.hp > 550:
			self.hp = 550
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()	


class Creep_range1(pygame.sprite.Sprite):
	def __init__(self, target):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_ranged1.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 900
		self.alist = [100,200,300,400,500]
		self.rect.y = random.choice(self.alist)
		self.speed = 2
		self.hp = 300
		self.armor = 0
		self.target = target

	def update(self):
		alist = [player1, player2]
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) < 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player1
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) > 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player2
		
		try:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
		except(UnboundLocalError):
			pass
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) ==
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = random.choice(alist)
		
		if self.hp > 300:
			self.hp = 300
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # how long to wait for the next frame VELOCITY OF THE EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill() # if we get to the end of the animation we don't keep going.
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

def show_go_screen():
	
	screen.blit(background, [0,0])
	draw_text2(screen, "Adventure", 65, WIDTH // 2, HEIGHT // 4)
	draw_text2(screen, "Destruye los enemigos", 20, WIDTH // 2, HEIGHT // 2)
	draw_text2(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	#draw_text(screen, "Created by: Francisco Carvajal", 10,  60, 500)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screen():
	screen.blit(background, [0,0])
	draw_text2(screen, "Game Over", 60, WIDTH  // 2, HEIGHT * 1/4)
		#draw_text(screen, "score: "+str(score), 30, WIDTH // 2, HEIGHT // 2)
	draw_text2(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 4/5)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

## --------------- CARGAR IMAGENES EXPLOSIÓN -------------------------- ##
explosion_anim = []
for i in range(9):
	file = "img/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(BLACK)
	img_scale = pygame.transform.scale(img, (70, 70))
	explosion_anim.append(img_scale)

# Cargar imagen de fondo
background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(1300,700))

laser_sound = pygame.mixer.Sound("sound/laser5.ogg")
explosion_sound = pygame.mixer.Sound("sound/explosion.wav")

wave = False
waveca = False
game_over = False

running = True
start = True
counter = True
while running:
	if game_over:

		show_game_over_screen()
		game_over = False
		all_sprites = pygame.sprite.Group()
		team1p_list = pygame.sprite.Group()
		team2p_list = pygame.sprite.Group()
		team1cr_list = pygame.sprite.Group()
		team1cma_list = pygame.sprite.Group()
		team1cmb_list = pygame.sprite.Group()
		team1cmc_list = pygame.sprite.Group()
		
		bullets = pygame.sprite.Group()
		bullets2 = pygame.sprite.Group()
		
		player1 = Player1()
		player2 = Player2()
		all_sprites.add(player1, player2)
		team1p_list.add(player1)
		team2p_list.add(player2)
		
		creep_melee1 = Creep_melee1(any)
		creep_melee2 = Creep_melee2(any)
		creep_melee3 = Creep_melee3(any)
		all_sprites.add(creep_melee1, creep_melee2, creep_melee3)
		team1cma_list.add(creep_melee1)
		team1cmb_list.add(creep_melee2)
		team1cmc_list.add(creep_melee3)

		creep_ranged1 = Creep_range1(any)
		
		team1cr_list.add(creep_ranged1)
		
		all_sprites.add(creep_ranged1)
		
	if start:
		show_go_screen()
		start = False

		all_sprites = pygame.sprite.Group()
		team1p_list = pygame.sprite.Group()
		team2p_list = pygame.sprite.Group()
		team1cr_list = pygame.sprite.Group()
		
		team1cma_list = pygame.sprite.Group()
		team1cmb_list = pygame.sprite.Group()
		team1cmc_list = pygame.sprite.Group()
		
		bullets = pygame.sprite.Group()
		bullets2 = pygame.sprite.Group()
		
		player1 = Player1()
		player2 = Player2()
		team1p_list.add(player1)
		team2p_list.add(player2)
		all_sprites.add(player1, player2)
		
		creep_melee1 = Creep_melee1(any)
		creep_melee2 = Creep_melee2(any)
		creep_melee3 = Creep_melee3(any)
		all_sprites.add(creep_melee1, creep_melee2, creep_melee3)
		team1cma_list.add(creep_melee1)
		team1cmb_list.add(creep_melee2)
		team1cmc_list.add(creep_melee3)

		creep_ranged1 = Creep_range1(any)
		
		team1cr_list.add(creep_ranged1)
		
		all_sprites.add(creep_ranged1)
		
	if counter:
		
		if len(team1cma_list) == 0 and len(team1cmb_list) == 0 and len(team1cmc_list) == 0 and len(team1cr_list) == 0:
			boss1 = Boss1(any)
			boss2 = Boss2(any)
			all_sprites.add(boss1, boss2)
			counter = False

	try:
		if boss1.hp == 0 and boss2.hp == 0:
		
			creep_melee1 = Creep_melee1(any)
			creep_melee2 = Creep_melee2(any)
			creep_melee3 = Creep_melee3(any)
		
			team1cma_list.add(creep_melee1)
			team1cmb_list.add(creep_melee2)
			team1cmc_list.add(creep_melee3)
		
			all_sprites.add(creep_melee1, creep_melee2, creep_melee3)
			
			creep_ranged1 = Creep_range1(any)
		
			team1cr_list.add(creep_ranged1)
		
			all_sprites.add(creep_ranged1)
			counter = True
	except(NameError):
		pass
	
	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_p:
				print("p")
				if player2.hp > 0:
					player2.shoot()
					#print("p")
				else:
					pass
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_f:
				if player1.hp > 0:
					player1.shoot()
				else:
					pass
					
	if player1.hp <= 0:
		player1.lifes -= 1
		if player1.lifes > 0:
			player1.hp = 500
			player1.rect.x = 50
			player1.rect.y = HEIGHT//3
		else:
			player1.kill()
				
	if player2.hp <= 0:
		player2.lifes -=1
		if player2.lifes > 0:
			player2.hp = 500
			player2.rect.x = 50
			player2.rect.y = HEIGHT * 2/3
		else:
			player2.kill()
				
	if len(team1p_list) == 0 and len(team2p_list) == 0:

		game_over = True	
		
	# Checar colisiones - boss1 - bullets
	try:
		hits = pygame.sprite.spritecollide(boss1, bullets, True)
		for hit in hits:
		
			boss1.hp -= 10
	except(NameError):
		pass	
	# Checar colisiones - boss2 - bullets
	try:
		hits = pygame.sprite.spritecollide(boss2, bullets, True)
		for hit in hits:
		
			boss2.hp -= 10
	except(NameError):
		pass	

	# Checar colisiones - boss1 - bullets2
	try:
		hits = pygame.sprite.spritecollide(boss1, bullets2, True)
		for hit in hits:
		
			boss1.hp -= 10
	except(NameError):
		pass	
	# Checar colisiones - boss2 - bullets2
	try:
		hits = pygame.sprite.spritecollide(boss2, bullets2, True)
		for hit in hits:
		
			boss2.hp -= 10
	except(NameError):
		pass	
	# Checar colisiones - player1 - creep melee 1
	try:
		hits = pygame.sprite.spritecollide(player1, team1cma_list, False)
		for hit in hits:
		
			player1.hp -= 1
	except(NameError):
		pass
	# Checar colisiones - player2 - creeps melee 1
	try:
		hits = pygame.sprite.spritecollide(player2, team1cma_list, False)
		for hit in hits:
		
			player2.hp -= 1	
	except(NameError):
		pass	
	# Checar colisiones - player1 - creeps melee 2
	try:
		hits = pygame.sprite.spritecollide(player1, team1cmb_list, False)
		for hit in hits:
		
			player1.hp -= 1
	except(NameError):
		pass	
	# Checar colisiones - player2 - creeps melee 2
	try:
		hits = pygame.sprite.spritecollide(player2, team1cmb_list, False)
		for hit in hits:
		
			player2.hp -= 1
	except(NameError):
		pass
	# Checar colisiones - player1 - creeps melee 3
	try:
		hits = pygame.sprite.spritecollide(player1, team1cmc_list, False)
		for hit in hits:
		
			player1.hp -= 1
	except(NameError):
		pass
	# Checar colisiones - player2 - creeps melee 3
	try: 
		hits = pygame.sprite.spritecollide(player2, team1cmc_list, False)
		for hit in hits:
		
			player2.hp -= 1
	except(NameError):
		pass
	# Checar colisiones - player1 - creeps ranged
	try:
		hits = pygame.sprite.spritecollide(player1, team1cr_list, False)
		for hit in hits:
		
			player1.hp -= 1
	except(NameError):
		pass
	# Checar colisiones - player2 - creeps ranged
	try:
		hits = pygame.sprite.spritecollide(player2, team1cr_list, False)
		for hit in hits:
		
			player2.hp -= 1
	except(NameError):
		pass
	# Checar colisiones - boss1 - player2
	try:
		hits = pygame.sprite.spritecollide(boss1, team2p_list, False)
		for hit in hits:
		
			player2.hp -= 1
	except(NameError):
		pass	
	# Checar colisiones - boss2 - player1
	try:
		hits = pygame.sprite.spritecollide(boss2, team1p_list, False)
		for hit in hits:
		
			player1.hp -= 1
	except(NameError):
		pass
	# Checar colisiones - boss1 - player1
	try:
		hits = pygame.sprite.spritecollide(boss1, team1p_list, False)
		for hit in hits:
		
			player1.hp -= 1
	except(NameError):
		pass
	# Checar colisiones - boss2 - player2
	try:
		hits = pygame.sprite.spritecollide(boss2, team2p_list, False)
		for hit in hits:
		
			player2.hp -= 1
	except(NameError):
		pass

	# Checar colisiones - player1 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee1, bullets, True)
	for hit in hits:
		
		creep_melee1.hp -= 25
			
	# Checar colisiones - player1 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee2, bullets, True)
	for hit in hits:
		
		creep_melee2.hp -= 25
			
	# Checar colisiones - player1 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee3, bullets, True)
	for hit in hits:
		
		creep_melee3.hp -= 25

	# Checar colisiones - player1 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_ranged1, bullets, True)
	for hit in hits:
		
		creep_ranged1.hp -= 25


	# Checar colisiones - player1 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee1, bullets2, True)
	for hit in hits:
		
		creep_melee1.hp -= 25
			
	# Checar colisiones - player1 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee2, bullets2, True)
	for hit in hits:
		
		creep_melee2.hp -= 25
			
	# Checar colisiones - player1 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee3, bullets2, True)
	for hit in hits:
		
		creep_melee3.hp -= 25

	# Checar colisiones - player1 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_ranged1, bullets2, True)
	for hit in hits:
		
		creep_ranged1.hp -= 25

	all_sprites.update()
				
	"""
	# dtención del juego en t = () en mlseg	
	now = pygame.time.get_ticks()
	if now > 16000:
		game_over = True"""
	
	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	#draw_text(screen, str(score), 25, WIDTH // 2, 10)

	# Escudo.
	draw_text2(screen, "P1", 20, 210, 6)
	draw_text2(screen, "P2", 20, 740, 6)

	draw_text2(screen, str(player1.lifes) + "/7", 20, 180, 6)
	draw_text2(screen, str(player2.lifes) + "/7", 20, 700, 6)

	draw_hp_bar(screen, 220, 5, player1.hp/5)
	draw_text2(screen, str(int(player1.hp)) + "/500", 10, 270, 6)

	draw_hp_bar(screen, 750, 5, player2.hp/5)
	draw_text2(screen, str(int(player2.hp))+ "/500", 10, 800, 6)

	draw_mana_bar(screen, 220, 15, player1.mana)
	draw_text2(screen, str(int(player1.mana))+ "/100", 10, 270, 16)

	draw_mana_bar(screen, 750, 15, player2.mana)
	draw_text2(screen, str(int(player2.mana))+ "/100", 10, 800, 16)

	try:
		draw_hp_bar(screen, 0, 115, boss1.hp/218.75)
		draw_text2(screen, str(int(boss1.hp)) + "/21875", 10, 50, 116)
	except(NameError):
		pass
	try:
		draw_hp_bar(screen, 1100, 115, boss2.hp/218.75)
		draw_text2(screen, str(int(boss2.hp))+ "/21875", 10, 1145, 116)
	except(NameError):
		pass

	try:
		draw_hp_bar2(screen, 150, 80, (boss1.hp + boss2.hp)/437.50)
		draw_text2(screen, str(int(boss1.hp + boss2.hp)) + "/43750", 19, 580, 81)
	except(NameError):
		pass
	#reloj
	draw_text2(screen, str(pygame.time.get_ticks()//1000), 30, 600, 50)

	pygame.display.flip()