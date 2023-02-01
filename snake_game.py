import pygame,sys,random
from pygame.math import Vector2

# Colors (R, G, B)
black = (0, 0, 0)              #black
cinnabar = (231, 71, 29)       #red
forest_green = (34,139,34)     #light green
japanese_laurel = (0,128,0)    #green
camarone = (0,100,0)           #dark green
dark_fern = (7, 72, 11)        #darker green
malibu = (98, 164, 250)        #blue

class SNAKE:
	def __init__(self):
		self.body = [Vector2(5,7), Vector2(4,7), Vector2(3,7)]
		self.direction = Vector2(1, 0)
		self.new_block = False

	def draw_snake(self):
		for block in self.body:
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
			pygame.draw.rect(screen, malibu, block_rect)
   
	def move_snake(self):
		if self.new_block == True:
			body_copy = self.body[:]
			body_copy.insert(0, body_copy[0] + self.direction)
			self.body = body_copy[:]
			self.new_block = False
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0, body_copy[0] + self.direction)
			self.body = body_copy[:]

	def add_block(self):
		self.new_block = True

class CORRECT:
	def __init__(self):
		self.randomize()

	def draw_correct(self):
		correct_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
		pygame.draw.rect(screen, dark_fern, correct_rect)

	def randomize(self):
		self.x = random.randint(0, cell_number - 1)
		self.y = random.randint(0, cell_number - 1)
		self.pos = Vector2(self.x, self.y)
class WRONG1:
	def __init__(self):
		self.randomize()

	def draw_wrong1(self):
		wrong1_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
		pygame.draw.rect(screen, cinnabar, wrong1_rect)

	def randomize(self):
		self.x = random.randint(0, cell_number - 1)
		self.y = random.randint(0, cell_number - 1)
		self.pos = Vector2(self.x, self.y)
class WRONG2:
	def __init__(self):
		self.randomize()

	def draw_wrong2(self):
		wrong2_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
		pygame.draw.rect(screen, cinnabar, wrong2_rect)

	def randomize(self):
		self.x = random.randint(0, cell_number - 1)
		self.y = random.randint(0, cell_number - 1)
		self.pos = Vector2(self.x, self.y)

class MAIN:
	def __init__(self):
		self.snake = SNAKE()
		self.correct = CORRECT()
		self.wrong1 = WRONG1()
		self.wrong2 = WRONG2()

	def update(self):
		self.snake.move_snake()
		self.check_collision()
		self.check_fail()
  
	def draw_elements(self):
		self.correct.draw_correct()
		self.wrong1.draw_wrong1()
		self.wrong2.draw_wrong2()
		self.snake.draw_snake()
		self.draw_score()

	def check_collision(self):
		if self.correct.pos == self.snake.body[0]:
			self.correct.randomize()
			self.wrong1.randomize()
			self.wrong2.randomize()
			self.snake.add_block()

	def check_fail(self):
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
			self.game_over()

		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.game_over()
	def game_over(self):
		pygame.quit()
		sys.exit()

	def draw_score(self):
		pygame.draw.rect(screen, camarone, pygame.Rect(0, 0, 140, 35))
		score_text = "Your Score: " + str(len(self.snake.body) - 3)
		score_surface = game_font.render(score_text, True, black)
		score_x = int(cell_size * cell_number - cell_size * cell_number * 0.9)
		score_y = int(cell_size * cell_number - cell_size * cell_number * 0.97)
		score_rect = score_surface.get_rect(center = (score_x, score_y))
		screen.blit(score_surface,score_rect)
     
pygame.init()

# Variables used for window size
cell_size = 40
cell_number = 15

# Initialise game window
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

# Main logic
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == SCREEN_UPDATE:
			main_game.update()
		# Whenever a key is pressed down
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if main_game.snake.direction.y != 1: # Making sure the snake cannot move in the opposite direction instantaneously
					main_game.snake.direction = Vector2(0, -1)
			if event.key == pygame.K_RIGHT:
				if main_game.snake.direction.x != -1: # Making sure the snake cannot move in the opposite direction instantaneously
					main_game.snake.direction = Vector2(1, 0)
			if event.key == pygame.K_DOWN:
				if main_game.snake.direction.y != -1: # Making sure the snake cannot move in the opposite direction instantaneously
					main_game.snake.direction = Vector2(0, 1)
			if event.key == pygame.K_LEFT:
				if main_game.snake.direction.x != 1: # Making sure the snake cannot move in the opposite direction instantaneously
					main_game.snake.direction = Vector2(-1,0)
			# Esc -> Create event to quit the game
			elif event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))

	screen.fill(japanese_laurel)
	main_game.draw_elements()
	pygame.display.update()
	clock.tick(60)