import pygame

from settings import setting

#子弹类
class Bullet(pygame.sprite.Sprite):
	def __init__(self, bullet_img, init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = bullet_img
		self.rect = self.image.get_rect()
		self.rect.midbottom = init_pos
		self.speed = 10

	def move(self):
		self.rect.top -= self.speed
		

# 玩家飞机类
class Player(pygame.sprite.Sprite):
	def __init__(self, plane_img, player_rect, init_pos):
		pygame.sprite.Sprite.__init__(self)
		#用来存储玩家飞机图片的列表
		self.image = []
		for i in range(len(player_rect)):
			self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
		
		# 初始化图片所在的矩形
		self.rect = player_rect[0]
		# 初始化矩形的左下角坐标
		self.rect.topleft = init_pos
		# 初始化玩家飞机速度
		self.speed = 8

		#玩家飞机所发射的子弹的集合
		self.bullets = pygame.sprite.Group()

		# 玩家飞机图片索引
		self.img_index = 0
		# 玩家是否被击中
		self.is_hit = False

	# 发射子弹
	def shoot(self, bullet_img):
		bullet = Bullet(bullet_img, self.rect.midtop)
		self.bullets.add(bullet)

	# 向上移动，需要判断边界
	def moveUp(self):
		if self.rect.top <= 0:
			self.rect.top = 0
		else:
			self.rect.top -= self.speed

	# 向下移动
	def moveDown(self):
		if self.rect.top >= setting.SCREEN_HEIGHT - self.rect.height:
			self.rect.top = setting.SCREEN_HEIGHT - self.rect.height
		else:
			self.rect.top += self.speed

	#向左移动
	def moveLeft(self):
		if self.rect.left <= 0:
			self.rect.left = 0
		else:
			self.rect.left -= self.speed

	# 向右移动
	def moveRight(self):
		if self.rect.left >= setting.SCREEN_WIDTH - self.rect.width:
			self.rect.left = setting.SCREEN_WIDTH - self.rect.width
		else:
			self.rect.left += self.speed

# 敌机类
class Enemy(pygame.sprite.Sprite):
	def __init__(self, enemy_img, enemy_down_imgs, init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = enemy_img
		self.rect = self.image.get_rect()
		self.rect.topleft = init_pos
		self.down_imgs = enemy_down_imgs
		self.speed = 2
		self.down_index = 0

	# 敌机移动，边界判断以及删除在游戏主循环里处理
	def move(self):
		self.rect.top += self.speed