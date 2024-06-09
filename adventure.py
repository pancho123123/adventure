
import pygame, random
from random import randint

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

def draw_hp_bar1(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 900
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BROWN, border, 2)

def draw_hp_bar3(surface, x, y, percentage):
	BAR_LENGHT = 80
	BAR_HEIGHT = 7
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar4(surface, x, y, percentage):
	BAR_LENGHT = 30
	BAR_HEIGHT = 7
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

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
		bullet = Bullet(self.rect.centerx, self.rect.centery)
		all_sprites.add(bullet)
		bullets.add(bullet)
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
	if radio != 0:
		x, y = (dx/radio, dy/radio)
	else:
		x, y = (0, 0)
	return x, y

class Boss(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/centaur.png").convert(),(100,125))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.choice([300,400, 500, 600, 700, 800, 900,1000])
		self.rect.y = random.choice([100,200,300,400,500])
		self.hp = 21875
		self.atack = 21875
		self.armor = 20
		self.speed = 3
	
	def update(self):
		if distance(self, player1) < distance(self, player2):
			target = player1
		elif distance(self, player1) > distance(self, player2):
			target = player2
		else:
			target = random.choice([player1, player2])
			
		x,y = direction(self, target)
		self.rect.centerx += self.speed*x
		self.rect.centery += self.speed*y
		if self.hp > 21875:
			self.hp = 21875
		if self.hp <= 0:
			self.hp = 0
			self.kill()
		
class Creep_melee(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.set_image()
		self.rect.x = random.choice([300,400, 500, 600, 700, 800, 900,1000])
		self.rect.y = random.choice([100,200,300,400,500])
		self.speed = 2
		self.set_hp_and_armor()

	def set_image(self):
		self.image = pygame.transform.scale(pygame.image.load("img/creep_melee1.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()

	def set_hp_and_armor(self):
		self.max_hp = 550
		self.hp = self.max_hp
		self.armor = 2
	
	def update(self):
		if distance(self, player1) < distance(self, player2):
			target = player1
		elif distance(self, player1) > distance(self, player2):
			target = player2
		else:
			target = random.choice([player1, player2])
			
		x,y = direction(self, target)
		self.rect.centerx += self.speed*x
		self.rect.centery += self.speed*y
		
		if self.hp > self.max_hp:
			self.hp = self.max_hp
		if self.hp <= 0:
			self.hp = 0
			self.kill()

class Creep_range1(Creep_melee):
	def set_image(self):
		self.image = pygame.transform.scale(pygame.image.load("img/creep_ranged1.png").convert(),(25,50))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		
	def set_hp_and_armor(self):
		self.max_hp = 300
		self.hp = self.max_hp
		self.armor = 0

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

score = 0
counter2 = False
wave = False
waveca = False
game_over = False
running = True
counter1 = True
counter = False
show_go_screen()
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
boss_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player1 = Player1()
player2 = Player2()
all_sprites.add(player1, player2)
players.add(player1, player2)

creeps = pygame.sprite.Group([Creep_melee() for _ in range(4)])

creep_ranged1 = Creep_range1()
creeps.add(creep_ranged1)
all_sprites.add(creeps)
while running:
	if game_over:
		show_game_over_screen()
		game_over = False
		all_sprites = pygame.sprite.Group()
		player_list = pygame.sprite.Group()
		bullets = pygame.sprite.Group()
		player1 = Player1()
		player2 = Player2()
		all_sprites.add(player1, player2)
		player_list.add(player1, player2)
		creeps = pygame.sprite.Group([Creep_melee() for _ in range(4)])
		creep_ranged1 = Creep_range1()
		creeps.add(creep_ranged1)
		all_sprites.add(creeps)
		score = 0

	if counter1:
		if len(creeps) == 0:
			if len(boss_list) ==0:
				counter = True

	if counter2:
		if len(boss_list) == 0:
			score += 2000*2
			creeps = pygame.sprite.Group([Creep_melee() for _ in range(4)])
			creep_ranged1 = Creep_range1()
			creeps.add(creep_ranged1)
			all_sprites.add(creeps)
			counter2 = False
			counter = True

	if counter:
		if len(creeps) == 0:
			score += 36*5
			boss1 = Boss()
			boss2 = Boss()
			all_sprites.add(boss1, boss2)
			boss_list.add(boss1, boss2)
			counter = False
			counter2 = True
			
	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				if player2.hp > 0:
					player2.shoot()
				else:
					pass
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_f:
				if player1.hp > 0:
					player1.shoot()
				else:
					pass
					
	if player1.hp <= 0:
		if player1.lifes > 0:
			player1.lifes -= 1
			player1.hp = 500
			player1.rect.x = 50
			player1.rect.y = HEIGHT//3
		else:
			player1.kill()
				
	if player2.hp <= 0:
		if player2.lifes > 0:
			player2.lifes -=1
			player2.hp = 500
			player2.rect.x = 50
			player2.rect.y = HEIGHT * 2/3
		else:
			player2.kill()
				
	if len(players) == 0:
		game_over = True	
		
	# Checar colisiones - boss - bullets
	for bullet in bullets:
		for boss in boss_list:
			if pygame.sprite.collide_rect(boss, bullet):
				boss.hp -= 10
				bullet.kill()

	# Checar colisiones - players - creeps
	for player in players:
		for creep in creeps:
			if pygame.sprite.collide_rect(player, creep):
				player.hp -= 1

	# Checar colisiones - boss - players
	for boss in boss_list:
		for player in players:
			if pygame.sprite.collide_rect(boss, player):
				player.hp -= 1
	
	# Checar colisiones - bullets - creeps
	for bullet in bullets:
		for creep in creeps:
			if pygame.sprite.collide_rect(creep, bullet):
				creep.hp -= 25
				bullet.kill()
	
	all_sprites.update()
				
	"""
	# dtención del juego en t = () en mlseg	
	now = pygame.time.get_ticks()
	if now > 16000:
		game_over = True"""
	
	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	draw_text2(screen, str(score), 25, WIDTH // 2, 10)

	# Escudo.
	draw_text2(screen, "P1", 20, 210, 6)
	draw_text2(screen, "P2", 20, 740, 6)

	draw_text2(screen, str(player1.lifes) + "/7", 20, 180, 6)
	draw_text2(screen, str(player2.lifes) + "/7", 20, 700, 6)

	draw_hp_bar1(screen, 220, 5, player1.hp/5)
	draw_text2(screen, str(int(player1.hp)) + "/500", 10, 270, 6)

	draw_hp_bar1(screen, 750, 5, player2.hp/5)
	draw_text2(screen, str(int(player2.hp))+ "/500", 10, 800, 6)

	for p in players:
		if p.hp > 0:
			draw_hp_bar(screen, p.rect.x, p.rect.y - 10, p.hp/5)
	
	draw_mana_bar(screen, 220, 15, player1.mana)
	draw_text2(screen, str(int(player1.mana))+ "/100", 10, 270, 16)

	draw_mana_bar(screen, 750, 15, player2.mana)
	draw_text2(screen, str(int(player2.mana))+ "/100", 10, 800, 16)

	try:
		if boss1.hp > 0:
			draw_hp_bar(screen, 0, 115, boss1.hp/218.75)
			draw_text2(screen, str(int(boss1.hp)) + "/21875", 10, 25, 116)
		if boss2.hp > 0:
			draw_hp_bar(screen, 1000, 115, boss2.hp/218.75)
			draw_text2(screen, str(int(boss2.hp)) + "/21875", 10, 1025, 116)
	except(NameError):
		pass

	for boss in boss_list:
		if boss.hp > 0:
			draw_hp_bar3(screen, boss.rect.x, boss.rect.y, boss.hp/218.75)
	
	try:
		draw_hp_bar2(screen, 150, 80, (boss1.hp + boss2.hp)/437.50)
	except(NameError):
		pass
	
	for creep in creeps:
		try:
			if creep.hp > 0:
				draw_hp_bar4(screen, creep.rect.x, creep.rect.y, creep.hp/5.5)
		except(NameError):
			pass

	#reloj
	draw_text2(screen, str(pygame.time.get_ticks()//1000), 30, 600, 50)

	pygame.display.flip()
