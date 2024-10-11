import pygame
import sys
import time
import random
from Game import Game
from Player import player
from Resource import Resource



# Initialize pygame
pygame.init()

# Set up display
window_size = 700  # Window size (700x700 pixels)
grid_size = 7  # 7x7 grid
cell_size = window_size // grid_size  # Size of each cell in the grid

screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Game Time Display')

# Create an instance of the Game class
players = [player(1, "Player1", (0, 0), [], 0),
           player(2, "Player2", (6, 6), [], 0)]

resources = [
    Resource(2, 9, (3, 4), "Food", True),
    Resource(3, 30, (2, 1), "Hydration", True),
    Resource(4, 15, (0, 4), "Food", True),
    Resource(1, 10, (6, 0), "Food", True),
    Resource(6, 25, (1, 6), "Food", True),
    Resource(5, 20, (4, 0), "Hydration", True)
]

game_instance = Game(1, players, resources)

# Set up font
font = pygame.font.Font(None, 27)

def check_for_resources(player):
    for resource in game_instance.get_resources():
        player.collect_resource(resource)

def move_player_randomly(player):
    """Move the player randomly in one of the four directions."""
    directions = ['up', 'down', 'left', 'right']
    move = random.choice(directions)
    if move == 'up':
        player.move_up()
    elif move == 'down':
        player.move_down()
    elif move == 'left':
        player.move_left()
    elif move == 'right':
        player.move_right()
    check_for_resources(player)


def move_player_to_resource(player, resource):
    """moves the player to the given resource"""
    p = player.get_pos()
    r = resource.get_position()
    if p[0] < r[0]:
      player.move_right()
    elif p[0] > r[0]:
       player.move_left()
     if p[1] < r[1]:
       player.move_up()
     elif p[1] > r[1]:
       player.move_down()
           
     #update the player position
     p = player.get_pos()
     check_for_resources(player)





def draw_resources():
    """Draw the resources on the grid."""
    for resource in game_instance.get_resources():
        if resource.get_isFree():
            resource_pos = resource.get_position()
            pygame.draw.rect(screen, (0, 255, 0), (resource_pos[0] * cell_size, resource_pos[1] * cell_size, cell_size, cell_size))

# Main loop
running = True
last_time = time.time()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Increment game time and move players every second
    current_time = time.time()
    if current_time - last_time >= 1:
        game_instance.increment_time()
        for player in game_instance.get_players():
            move_player_to_resource(player,player.get_best_resource(resources))
            #move_player_randomly(player)
        draw_resources()
        last_time = current_time

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw the grid
    for x in range(0, window_size, cell_size):
        for y in range(0, window_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Draw the cell border

    # Draw the players
    for player in game_instance.get_players():
        player_pos = player.get_pos()
        pygame.draw.circle(screen, (0, 0, 255), (player_pos[0] * cell_size + cell_size // 2, player_pos[1] * cell_size + cell_size // 2), cell_size // 3)

    draw_resources()
    # Render the time text
    time_text = font.render(f"Time: {game_instance.get_time()}", True, (0, 0, 0))
    screen.blit(time_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()

