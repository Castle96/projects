import pygame
import sys
import pandas as pd

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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
PADDLE_COLOR = COLORS['green']
BALL_COLOR = COLORS['blue']
TEXT_COLOR = COLORS['text']

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# Game clock
clock = pygame.time.Clock()

# Font for displaying the score and messages
font = pygame.font.Font(None, 74)
message_font = pygame.font.Font(None, 48)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)
        self.speed = 5
        self.reaction_time = 0.02  # Reaction delay in seconds
        self.last_move_time = pygame.time.get_ticks()
    
    def move(self, up, down):
        keys = pygame.key.get_pressed()
        if keys[up] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
    
    def ai_move(self, ball):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time > self.reaction_time * 1000:
            if self.rect.centery < ball.rect.centery:
                self.rect.y += self.speed
            elif self.rect.centery > ball.rect.centery:
                self.rect.y -= self.speed
            self.last_move_time = current_time
    
    def draw(self, screen):
        pygame.draw.rect(screen, PADDLE_COLOR, self.rect)

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.speed_x = 4
        self.speed_y = 4
        self.base_speed = 4
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, BALL_COLOR, self.rect)
    
    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = self.base_speed
        self.speed_y = self.base_speed

    def increase_speed(self):
        self.speed_x *= 1.1
        self.speed_y *= 1.1

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
        df = pd.read_excel("pong_high_scores.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Score"])
    
    df =df.append({"Name": name, "Score": score}, ignore_index=True)
    df.to_excel("pong_high_scores.xlsx", index=False)

def draw_menu():
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 74)
    text = font.render("Press 1 for Normal Mode, 2 for Hard Mode", True, TEXT_COLOR)
    screen.blit(text, (100, SCREEN_HEIGHT // 2 - 50))
    pygame.display.flip()

def main():
    draw_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = 'normal'
                elif event.key == pygame.K_2:
                    mode = 'hard'
                else:
                    continue
                
                # Initialize paddles and ball
                player_paddle = Paddle(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - 50)
                opponent_paddle = Paddle(10, SCREEN_HEIGHT // 2 - 50)
                ball = Ball(SCREEN_WIDTH // 2 - 5, SCREEN_HEIGHT // 2 - 5)
                
                # Scores
                player_score = 0
                opponent_score = 0
                winning_score = 10
                
                paused = False
                
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                paused = not paused  # Toggle pause state
                    
                    if not paused:
                        # Move paddles
                        player_paddle.move(pygame.K_UP, pygame.K_DOWN)
                        opponent_paddle.ai_move(ball)  # Use AI movement for the opponent
                    
                        # Move ball
                        ball.move()
                    
                        # Check for collisions with paddles
                        if ball.rect.colliderect(player_paddle.rect) or ball.rect.colliderect(opponent_paddle.rect):
                            ball.speed_x *= -1
                            if mode == 'hard':
                                ball.increase_speed()
                    
                        # Check for out of bounds
                        if ball.rect.left <= 0:
                            player_score += 1
                            ball.reset()
                        elif ball.rect.right >= SCREEN_WIDTH:
                            opponent_score += 1
                            ball.reset()
                    
                        # Check for win condition
                        if player_score == winning_score:
                            display_message("Congratulations! You won!")
                            name = get_player_name()
                            save_high_score(name, player_score)
                            display_message("Press SPACE to play again.")
                            break
                        elif opponent_score == winning_score:
                            display_message("Sorry! You lost!")
                            name = get_player_name()
                            save_high_score(name, opponent_score)
                            display_message("Press SPACE to play again.")
                            break
                    
                    # Draw everything
                    screen.fill(BACKGROUND_COLOR)
                    player_paddle.draw(screen)
                    opponent_paddle.draw(screen)
                    ball.draw(screen)
                    
                    # Display scores
                    player_text = font.render(str(player_score), True, TEXT_COLOR)
                    screen.blit(player_text, (SCREEN_WIDTH // 2 + 20, 10))
                    opponent_text = font.render(str(opponent_score), True, TEXT_COLOR)
                    screen.blit(opponent_text, (SCREEN_WIDTH // 2 - 60, 10))
                    
                    # Update display
                    pygame.display.flip()
                    
                    # Frame rate
                    clock.tick(60)

if __name__ == '__main__':
    main()
