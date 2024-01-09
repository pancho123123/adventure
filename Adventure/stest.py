
import pygame, random
from random import randint
from pathlib import Path

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
PLOMO = (122,122,122)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monedas")
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

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)





class Tower1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/tower1.png").convert(),(100,125))
		#self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 25
		self.rect.y = 25
		self.hp = 2000
		self.armor = 12

	def update(self):
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 2000:
			self.hp = 2000

	

class Tower2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/tower2.png").convert(),(100,125))
		#self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1100
		self.rect.y = 575
		self.hp = 2000
		self.armor = 12

	def update(self):
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 2000:
			self.hp = 2000
		
		

class Creep_melee1a(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 40
		self.rect.y = 70
		self.speedy = 1
		self.speedx = 2
		self.hp = 550
		self.armor = 2

	def update(self):

		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if abs(self.rect.x - creep_melee2a.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee2b.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee2c.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_ranged2.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
			
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 550:
			self.hp = 550

class Creep_melee1b(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 60
		self.rect.y = 77
		self.speedy = 1
		self.speedx = 2
		self.hp = 550
		self.armor = 2

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if abs(self.rect.x - creep_melee2a.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee2b.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee2c.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_ranged2.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 550:
			self.hp = 550

class Creep_melee1c(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 80
		self.rect.y = 81
		self.speedy = 1
		self.speedx = 2
		self.hp = 550
		self.armor = 2

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if abs(self.rect.x - creep_melee2a.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee2b.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee2c.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_ranged2.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 550:
			self.hp = 550
		
class Creep_melee2a(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1190
		self.rect.y = 674
		self.speedy = -1
		self.speedx = -2
		self.hp = 550
		self.armor = 2

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if abs(self.rect.x - creep_melee1a.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee1b.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee1c.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_ranged1.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 550:
			self.hp = 550

class Creep_melee2b(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1170
		self.rect.y = 672
		self.speedy = -1
		self.speedx = -2
		self.hp = 550
		self.armor = 2

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if abs(self.rect.x - creep_melee1a.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee1b.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee1c.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_ranged1.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 550:
			self.hp = 550

class Creep_melee2c(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1150
		self.rect.y = 670
		self.speedy = -1
		self.speedx = -2
		self.hp = 550
		self.armor = 2

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if abs(self.rect.x - creep_melee1a.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee1b.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee1c.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_ranged1.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 550:
			self.hp = 550

class Creep_range1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_ranged.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 75
		self.speedy = 1
		self.speedx = 2
		self.hp = 300
		self.armor = 0

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if abs(self.rect.x - creep_melee2a.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee2b.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee2c.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_ranged2.rect.x) < 10:
			self.speedx = 0
			self.speedy = 0
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 300:
			self.hp = 300

class Creep_range2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_ranged.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1175
		self.rect.y = 675
		self.speedy = -1
		self.speedx = -2
		self.hp = 300
		self.armor = 0

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if abs(self.rect.x - creep_melee1a.rect.x) < 7:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee1b.rect.x) < 7:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_melee1c.rect.x) < 7:
			self.speedx = 0
			self.speedy = 0
		if abs(self.rect.x - creep_ranged1.rect.x) < 7:
			self.speedx = 0
			self.speedy = 0
		
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 300:
			self.hp = 300

class Creep_asedio1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_asedio.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 75
		self.speedy = 1
		self.speedx = 2
		self.hp = 935
		self.armor = 0

		
	def update(self):
		self.rect.y += self.speedy
		self.rect.y += self.speedy
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 935:
			self.hp = 935

class Creep_asedio2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/creep_asedio.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1175
		self.rect.y = 675
		self.speedy = -1
		self.speedx = -2
		self.hp = 935
		self.armor = 0

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 935:
			self.hp = 935

def show_go_screen():
	
	screen.blit(background, [0,0])
	draw_text2(screen, "Tower", 65, WIDTH // 2, HEIGHT // 4)
	draw_text2(screen, "Destruye la torre enemiga", 20, WIDTH // 2, HEIGHT // 2)
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



def show_game_over_screen1():
	screen.blit(background, [0,0])
	draw_text2(screen, "Radiant victory", 60, WIDTH  // 2, HEIGHT * 1/4)
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

def show_game_over_screen2():
	screen.blit(background, [0,0])
	draw_text2(screen, "Dire victory", 60, WIDTH  // 2, HEIGHT * 1/4)
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

# Cargar imagen de fondo
background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(1200,700))

wave = False
running = True
start = True
while running:
	
	if start:
		show_go_screen()
		start = False

		all_sprites = pygame.sprite.Group()
		team1p_list = pygame.sprite.Group()
		team2p_list = pygame.sprite.Group()
		team1cr_list = pygame.sprite.Group()
		team2cr_list = pygame.sprite.Group()
		team1cma_list = pygame.sprite.Group()
		team1cmb_list = pygame.sprite.Group()
		team1cmc_list = pygame.sprite.Group()
		team2cma_list = pygame.sprite.Group()
		team2cmb_list = pygame.sprite.Group()
		team2cmc_list = pygame.sprite.Group()
		
				
		tower1 = Tower1()
		tower2 = Tower2()
		all_sprites.add(tower1, tower2)
		
		creep_melee1a = Creep_melee1a()
		creep_melee1b = Creep_melee1b()
		creep_melee1c = Creep_melee1c()
		creep_melee2a = Creep_melee2a()
		creep_melee2b = Creep_melee2b()
		creep_melee2c = Creep_melee2c()
		team1cma_list.add(creep_melee1a)
		team1cmb_list.add(creep_melee1b)
		team1cmc_list.add(creep_melee1c)
		team2cma_list.add(creep_melee2a)
		team2cmb_list.add(creep_melee2b)
		team2cmc_list.add(creep_melee2c)

		all_sprites.add(creep_melee1a, creep_melee2a, creep_melee1b, creep_melee2b, creep_melee1c, creep_melee2c)
			
		
		for i in range(1):
			creep_ranged1 = Creep_range1()
			creep_ranged2 = Creep_range2()
			team1cr_list.add(creep_ranged1)
			team2cr_list.add(creep_ranged2)
			all_sprites.add(creep_ranged1, creep_ranged2)
		

	if wave:
		wave = False
		creep_melee1a = Creep_melee1a()
		creep_melee1b = Creep_melee1b()
		creep_melee1c = Creep_melee1c()
		creep_melee2a = Creep_melee2a()
		creep_melee2b = Creep_melee2b()
		creep_melee2c = Creep_melee2c()
		team1cma_list.add(creep_melee1a)
		team1cmb_list.add(creep_melee1b)
		team1cmc_list.add(creep_melee1c)
		team2cma_list.add(creep_melee2a)
		team2cmb_list.add(creep_melee2b)
		team2cmc_list.add(creep_melee2c)

		all_sprites.add(creep_melee1a, creep_melee2a, creep_melee1b, creep_melee2b, creep_melee1c, creep_melee2c)
			
		
		for i in range(1):
			creep_ranged1 = Creep_range1()
			creep_ranged2 = Creep_range2()
			team1cr_list.add(creep_ranged1)
			team2cr_list.add(creep_ranged2)
			all_sprites.add(creep_ranged1, creep_ranged2)
		
		
		
		

		

	
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	anow = pygame.time.get_ticks()


	if (anow//1000) % 30 == 0:
		wave = True
		
	

	if tower1.hp == 0:
		game_over2 = True
	if tower2.hp == 0:
		game_over1 = True

	
		
	

	

	
	# Checar colisiones - torre1 - creeps meleea
	hits = pygame.sprite.spritecollide(tower1, team2cma_list, False)
	for hit in hits:
		
		tower1.hp -= 1/70
		creep_melee2a.hp -= 1
		creep_melee2a.speedx = 0
		creep_melee2a.speedy = 0
		
		
	# Checar colisiones - torre2 - creeps meleea
	hits = pygame.sprite.spritecollide(tower2, team1cma_list, False)
	for hit in hits:
		
		tower2.hp -= 1/70
		creep_melee1a.hp -= 1
		creep_melee1a.speedx = 0
		creep_melee1a.speedy = 0
		

	# Checar colisiones - torre1 - creeps meleeb
	hits = pygame.sprite.spritecollide(tower1, team2cmb_list, False)
	for hit in hits:
		
		tower1.hp -= 1/70
		creep_melee2b.hp -= 1
		creep_melee2b.speedx = 0
		creep_melee2b.speedy = 0
		
	# Checar colisiones - torre2 - creeps meleeb
	hits = pygame.sprite.spritecollide(tower2, team1cmb_list, False)
	for hit in hits:
		
		tower2.hp -= 1/70
		creep_melee1b.hp -= 1
		creep_melee1b.speedx = 0
		creep_melee1b.speedy = 0
		

	# Checar colisiones - torre1 - creeps meleec
	hits = pygame.sprite.spritecollide(tower1, team2cmc_list, False)
	for hit in hits:
		
		tower1.hp -= 1/70
		creep_melee2c.hp -= 1
		creep_melee2c.speedx = 0
		creep_melee2c.speedy = 0
		
	# Checar colisiones - torre2 - creeps meleec
	hits = pygame.sprite.spritecollide(tower2, team1cmc_list, False)
	for hit in hits:
		
		tower2.hp -= 1/70
		creep_melee1c.hp -= 1
		creep_melee1c.speedx = 0
		creep_melee1c.speedy = 0
		
	
	# Checar colisiones - torre1 - creeps ranged
	hits = pygame.sprite.spritecollide(tower1, team2cr_list, False)
	for hit in hits:
		
		tower1.hp -= 1/70
		creep_ranged2.hp -= 1
		creep_ranged2.speedx = 0
		creep_ranged2.speedy = 0
		
		
	# Checar colisiones - torre2 - creeps ranged
	hits = pygame.sprite.spritecollide(tower2, team1cr_list, False)
	for hit in hits:
		
		tower2.hp -= 1/70
		creep_ranged1.hp -= 1
		creep_ranged1.speedx = 0
		creep_ranged1.speedy = 0

	# Checar colisiones - creeps meleea - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee1a, team2cma_list, False)
	for hit in hits:
		
		creep_melee1a.hp -= 1/10
		creep_melee2a.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee2a, team1cma_list, False)
	for hit in hits:
		
		creep_melee2a.hp -= 1/10
		creep_melee1a.hp -= 1/10
		

	# Checar colisiones - torre1 - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee1a, team2cmb_list, False)
	for hit in hits:
		
		creep_melee1a.hp -= 1/10
		creep_melee2b.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee2a, team1cmb_list, False)
	for hit in hits:
		
		creep_melee2a.hp -= 1/10
		creep_melee1b.hp -= 1/10
		

	# Checar colisiones - torre1 - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee1a, team2cmc_list, False)
	for hit in hits:
		
		creep_melee1a.hp -= 1/10
		creep_melee2c.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee2a, team1cmc_list, False)
	for hit in hits:
		
		creep_melee2a.hp -= 1/10
		creep_melee1c.hp -= 1/10
		
	
	# Checar colisiones - torre1 - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee1a, team2cr_list, False)
	for hit in hits:
		
		creep_melee1a.hp -= 1/10
		creep_ranged2.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee2a, team1cr_list, False)
	for hit in hits:
		
		creep_melee2a.hp -= 1/10
		creep_ranged1.hp -= 1/10
	
	# Checar colisiones - creeps meleea - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee1b, team2cma_list, False)
	for hit in hits:
		
		creep_melee1b.hp -= 1/10
		creep_melee2a.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee2b, team1cma_list, False)
	for hit in hits:
		
		creep_melee2b.hp -= 1/10
		creep_melee1a.hp -= 1/10
		

	# Checar colisiones - torre1 - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee1b, team2cmb_list, False)
	for hit in hits:
		
		creep_melee1b.hp -= 1/10
		creep_melee2b.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee2b, team1cmb_list, False)
	for hit in hits:
		
		creep_melee2b.hp -= 1/10
		creep_melee1b.hp -= 1/10
		

	# Checar colisiones - torre1 - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee1b, team2cmc_list, False)
	for hit in hits:
		
		creep_melee1b.hp -= 1/10
		creep_melee2c.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee2b, team1cmc_list, False)
	for hit in hits:
		
		creep_melee2b.hp -= 1/10
		creep_melee1c.hp -= 1/10
		
	
	# Checar colisiones - torre1 - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee1b, team2cr_list, False)
	for hit in hits:
		
		creep_melee1b.hp -= 1/10
		creep_ranged2.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee2b, team1cr_list, False)
	for hit in hits:
		
		creep_melee2b.hp -= 1/10
		creep_ranged1.hp -= 1/10

	# Checar colisiones - creeps meleea - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee1c, team2cma_list, False)
	for hit in hits:
		
		creep_melee1c.hp -= 1/10
		creep_melee2a.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_melee2c, team1cma_list, False)
	for hit in hits:
		
		creep_melee2c.hp -= 1/10
		creep_melee1a.hp -= 1/10
		

	# Checar colisiones - torre1 - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee1c, team2cmb_list, False)
	for hit in hits:
		
		creep_melee1c.hp -= 1/10
		creep_melee2b.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_melee2c, team1cmb_list, False)
	for hit in hits:
		
		creep_melee2c.hp -= 1/10
		creep_melee1b.hp -= 1/10
		

	# Checar colisiones - torre1 - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee1c, team2cmc_list, False)
	for hit in hits:
		
		creep_melee1c.hp -= 1/10
		creep_melee2c.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleec
	hits = pygame.sprite.spritecollide(creep_melee2c, team1cmc_list, False)
	for hit in hits:
		
		creep_melee2c.hp -= 1/10
		creep_melee1c.hp -= 1/10
		
	
	# Checar colisiones - torre1 - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee1c, team2cr_list, False)
	for hit in hits:
		
		creep_melee1c.hp -= 1/10
		creep_ranged2.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps ranged
	hits = pygame.sprite.spritecollide(creep_melee2c, team1cr_list, False)
	for hit in hits:
		
		creep_melee2c.hp -= 1/10
		creep_ranged1.hp -= 1/10
		
	# Checar colisiones - creeps meleea - creeps meleea
	hits = pygame.sprite.spritecollide(creep_ranged1, team2cma_list, False)
	for hit in hits:
		
		creep_ranged1.hp -= 1/10
		creep_melee2a.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleea
	hits = pygame.sprite.spritecollide(creep_ranged2, team1cma_list, False)
	for hit in hits:
		
		creep_ranged2.hp -= 1/10
		creep_melee1a.hp -= 1/10
		

	# Checar colisiones - torre1 - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_ranged1, team2cmb_list, False)
	for hit in hits:
		
		creep_ranged1.hp -= 1/10
		creep_melee2b.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleeb
	hits = pygame.sprite.spritecollide(creep_ranged2, team1cmb_list, False)
	for hit in hits:
		
		creep_ranged2.hp -= 1/10
		creep_melee1b.hp -= 1/10
		

	# Checar colisiones - torre1 - creeps meleec
	hits = pygame.sprite.spritecollide(creep_ranged1, team2cmc_list, False)
	for hit in hits:
		
		creep_ranged1.hp -= 1/10
		creep_melee2c.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps meleec
	hits = pygame.sprite.spritecollide(creep_ranged2, team1cmc_list, False)
	for hit in hits:
		
		creep_ranged2.hp -= 1/10
		creep_melee1c.hp -= 1/10
		
	
	# Checar colisiones - torre1 - creeps ranged
	hits = pygame.sprite.spritecollide(creep_ranged1, team2cr_list, False)
	for hit in hits:
		
		creep_ranged1.hp -= 1/10
		creep_ranged2.hp -= 1/10
		
		
	# Checar colisiones - torre2 - creeps ranged
	hits = pygame.sprite.spritecollide(creep_ranged2, team1cr_list, False)
	for hit in hits:
		
		creep_ranged2.hp -= 1/10
		creep_ranged1.hp -= 1/10
	

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

	

	draw_hp_bar(screen, 25, 135, tower1.hp/20)
	draw_text2(screen, str(int(tower1.hp)) + "/2000", 10, 75, 136)

	draw_hp_bar(screen, 1100, 690, tower2.hp/20)
	draw_text2(screen, str(int(tower2.hp))+ "/2000", 10, 1145, 691)

	#reloj
	draw_text2(screen, str(pygame.time.get_ticks()//1000), 30, 600, 50)

	pygame.display.flip()