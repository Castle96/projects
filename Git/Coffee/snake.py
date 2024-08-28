import pygame
import sys
import random
import pandas as pd


# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20

# Colors from Catppuccin Macchiato color scheme
COLORS = {
    'rosewater': (245, 224, 220),
    'flamingo': (242, 205, 205),
    'pink': (245, 194, 231),
    'mauve': (203, 166, 247),
    'red': (243, 139, 168),
    'maroon': (235, 160, 172),
    'peach': (250, 179, 135),
    'yellow': (249, 226, 175),
    'green': (166, 227, 161),
    'teal': (148, 226, 213),
    'sky': (137, 220, 235),
    'sapphire': (116, 199, 236),
    'blue': (137, 180, 250),
    'lavender': (180, 190, 254),
    'text': (205, 214, 244),
    'subtext1': (186, 194, 222),
    'subtext0': (166, 173, 200),
    'overlay2': (147, 153, 178),
    'overlay1': (127, 132, 156),
    'overlay0': (108, 112, 134),
    'surface2': (88, 91, 112),
    'surface1': (69, 71, 90),
    'surface0': (49, 50, 68),
    'base': (30, 30, 46),
    'mantle': (24, 24, 37),
    'crust': (17, 17, 27)
}

BACKGROUND_COLOR = COLORS['base']
SNAKE_COLOR = COLORS['green']
FOOD_COLOR = COLORS['red']
ENEMY_COLOR = COLORS['mauve']
TEXT_COLOR = COLORS['text']

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')

# Game clock
clock = pygame.time.Clock()

# Font for displaying the score and messages
font = pygame.font.Font(None, 74)
message_font = pygame.font.Font(None, 48)

class Snake:
    def __init__(self):
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.grow = False

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = cur
        if self.direction == pygame.K_UP:
            y -= CELL_SIZE
        elif self.direction == pygame.K_DOWN:
            y += CELL_SIZE
        elif self.direction == pygame.K_LEFT:
            x -= CELL_SIZE
        elif self.direction == pygame.K_RIGHT:
            x += CELL_SIZE

        new_position = (x, y)
        if new_position in self.positions:
            self.reset()
        else:
            self.positions.insert(0, new_position)
            if not self.grow:
                self.positions.pop()
            else:
                self.grow = False

    def reset(self):
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

    def change_direction(self, key):
        if (key == pygame.K_UP and not self.direction == pygame.K_DOWN) or \
           (key == pygame.K_DOWN and not self.direction == pygame.K_UP) or \
           (key == pygame.K_LEFT and not self.direction == pygame.K_RIGHT) or \
           (key == pygame.K_RIGHT and not self.direction == pygame.K_LEFT):
            self.direction = key

    def draw(self, screen):
        for position in self.positions:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

class Enemy:
    def __init__(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
    
    def move_towards(self, target_position):
        target_x, target_y = target_position
        x, y = self.position
        if x < target_x:
            x += CELL_SIZE
        elif x > target_x:
            x -= CELL_SIZE
        if y < target_y:
            y += CELL_SIZE
        elif y > target_y:
            y -= CELL_SIZE
        self.position = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, ENEMY_COLOR, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

def display_message(message):
    text = message_font.render(message, True, TEXT_COLOR)
    rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, rect)
    pygame.display.flip()

def get_player_name():
    pygame.display.flip()
    name = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        
        screen.fill(BACKGROUND_COLOR)
        prompt = message_font.render("Enter your name: " + name, True, TEXT_COLOR)
        screen.blit(prompt, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        pygame.display.flip()

def save_high_score(name, score):
    try:
        df = pd.read_excel("snake_high_scores.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Score"])
    
    df = df.append({"Name": name, "Score": score}, ignore_index=True)
    df.to_excel("snake_high_scores.xlsx", index=False)

def main():
    while True:
        snake = Snake()
        food = Food()
        enemy = Enemy()
        score = 0
        paused = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                    else:
                        snake.change_direction(event.key)

            if not paused:
                snake.move()
                if snake.get_head_position() == food.position:
                    snake.grow = True
                    score += 1
                    food.randomize_position()

                if snake.get_head_position() == enemy.position:
                    display_message(f'Game Over! Score: {score}')
                    name = get_player_name()
                    save_high_score(name, score)
                    display_message("Press SPACE to play again.")
                    break

                enemy.move_towards(food.position)

                if enemy.position == food.position:
                    food.randomize_position()

                if snake.get_head_position()[0] not in range(SCREEN_WIDTH) or \
                   snake.get_head_position()[1] not in range(SCREEN_HEIGHT):
                    display_message(f'Game Over! Score: {score}')
                    name = get_player_name()
                    save_high_score(name, score)
                    display_message("Press SPACE to play again.")
                    break

            # Draw everything
            screen.fill(BACKGROUND_COLOR)
            snake.draw(screen)
            food.draw(screen)
            enemy.draw(screen)

            # Display score
            score_text = font.render(str(score), True, TEXT_COLOR)
            screen.blit(score_text, (10, 10))

            # Update display
            pygame.display.flip()

            # Frame rate
            clock.tick(10)

if __name__ == '__main__':
    main()
