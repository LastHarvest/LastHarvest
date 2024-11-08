import pygame
import sys
import time
import random
from Game import Game
from Player1 import Player1
from Player2 import Player2
from Resource import Resource



# Initialize pygame
pygame.init()

# Set up display
window_size = 700  # Window size (700x700 pixels)
grid_size = 7  # 7x7 grid
cell_size = window_size // grid_size  # Size of each cell in the grid
#Import food and water images
image1= pygame.image.load('Pictures/food.png')
image1 = pygame.transform.scale(image1,(int(cell_size*0.5),int(cell_size*0.5)))
image2= pygame.image.load('Pictures/food2.png')
image2 = pygame.transform.scale(image2,(int(cell_size*0.5),int(cell_size*0.5)))
image3=pygame.image.load('Pictures/food3.png')
image3 = pygame.transform.scale(image3,(int(cell_size*0.5),int(cell_size*0.5)))
image4 = pygame.image.load('Pictures/water.png')
image4 = pygame.transform.scale(image4,(int(cell_size*0.5),int(cell_size*0.5)))

#Import players images
p1img1=pygame.image.load('Pictures/P1Run1.png')
p1img1 = pygame.transform.scale(p1img1,(int(cell_size*1.3),int(cell_size*1.3)))
p1img2=pygame.image.load('Pictures/P1Run2.png')
p1img2 = pygame.transform.scale(p1img2,(int(cell_size*1.3),int(cell_size*1.3)))
p1img3=pygame.image.load('Pictures/P1Run3.png')
p1img3 = pygame.transform.scale(p1img3,(int(cell_size*1.3),int(cell_size*1.3)))
p1img4 = pygame.image.load('Pictures/P1Run4.png')
p1img4 = pygame.transform.scale(p1img4,(int(cell_size*1.3),int(cell_size*1.3)))


screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Game Time Display')

# Create an instance of the Game class
players = [Player1(1, "Player1", (0, 0),"right"),
           Player2(2, "Player2", (6, 6),"left")]

resources = [
    Resource(2, 9, (3, 4), "Food", 1,True),
    Resource(3, 30, (2, 1), "Hydration",2, True),
    Resource(4, 15, (0, 4), "Food", 2,True),
    Resource(1, 10, (6, 0), "Food",3, True),
    Resource(6, 25, (1, 6), "Food",2, True),
    Resource(5, 20, (4, 0), "Hydration", 2,True)
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
    draw_players(move)
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
      draw_players()
    elif p[0] > r[0]:
       player.move_left()
       draw_players()
    else:
        if p[1] < r[1]:
           player.move_up()
        elif p[1] > r[1]:
           player.move_down()

     #update the player position
    check_for_resources(player)


def draw_resources():
    """Draw the resources on the grid."""
    for resource in game_instance.get_resources():
        if resource.get_isFree():
            resource_pos = resource.get_position()
            pixel_pos=(resource_pos[0]*cell_size, resource_pos[1]*cell_size)
            if resource.get_type()=="Food":
                listImg = [image1,image2,image3]
                image = listImg[resource.get_item()-1]
                screen.blit(image, pixel_pos)
            else: screen.blit(image4, pixel_pos)

def draw_players():
    """Draw the players on the grid."""
    for player in game_instance.get_players():
        direction=player.get_direction()
        player_pos = player.get_pos()
        pixel_pos=(player_pos[0]*cell_size, player_pos[1]*cell_size)
        if player_pos[0]%2==0:
            if direction=="right":
                screen.blit(p1img1, pixel_pos)
            else: screen.blit(p1img3, pixel_pos)
        else:
            if direction=="right":
                screen.blit(p1img2, pixel_pos)
            else: screen.blit(p1img4, pixel_pos)


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
        #for player in game_instance.get_players():
        #    move_player_to_resource(player,player.get_best_resource(resources))
        #    #move_player_randomly(player)
        #draw_resources()
        #last_time = current_time
        if game_instance.get_time() % 2 == 0:
            move_player_to_resource(players[0], players[0].get_best_resource(resources))
        else:
            move_player_to_resource(players[1], players[1].get_best_resource(resources))
        draw_resources()
        last_time = current_time



    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw the grid
    for x in range(0, window_size, cell_size):
        for y in range(0, window_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Draw the cell border
#
    # Draw the players

        #pygame.draw.circle(screen, (0, 0, 255), (player_pos[0] * cell_size + cell_size // 2, player_pos[1] * cell_size + cell_size // 2), cell_size // 3)

    draw_resources()
    draw_players()

    # Render the time text
    time_text = font.render(f"Time: {game_instance.get_time()}", True, (0, 0, 0))
    screen.blit(time_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()

