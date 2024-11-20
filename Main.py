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

window_size = 700
grid_size = 7
cell_size = window_size // grid_size

image1= pygame.image.load('Pictures/food.png')
image1 = pygame.transform.scale(image1,(int(cell_size*0.5),int(cell_size*0.5)))
image2= pygame.image.load('Pictures/food2.png')
image2 = pygame.transform.scale(image2,(int(cell_size*0.5),int(cell_size*0.5)))
image3=pygame.image.load('Pictures/food3.png')
image3 = pygame.transform.scale(image3,(int(cell_size*0.5),int(cell_size*0.5)))
image4 = pygame.image.load('Pictures/water.png')
image4 = pygame.transform.scale(image4,(int(cell_size*0.5),int(cell_size*0.5)))
image4 = pygame.transform.scale(image4,(int(cell_size*0.8),int(cell_size*0.8)))
arme = pygame.image.load('Pictures/Arme.png')
arme = pygame.transform.scale(arme,(int(cell_size*0.8),int(cell_size*0.8)))

p1img1=pygame.image.load('Pictures/P1Run1.png')
p1img1 = pygame.transform.scale(p1img1,(int(cell_size*1.3),int(cell_size*1.3)))
p1img2=pygame.image.load('Pictures/P1Run2.png')
p1img2 = pygame.transform.scale(p1img2,(int(cell_size*1.3),int(cell_size*1.3)))
p1img3=pygame.image.load('Pictures/P1Run3.png')
p1img3 = pygame.transform.scale(p1img3,(int(cell_size*1.3),int(cell_size*1.3)))
p1img4 = pygame.image.load('Pictures/P1Run4.png')
p1img4 = pygame.transform.scale(p1img4,(int(cell_size*1.3),int(cell_size*1.3)))

#Import player 2 images

p2img1=pygame.image.load('Pictures/P2Run1.png')
p2img1 = pygame.transform.scale(p2img1,(int(cell_size*1.3),int(cell_size*1.3)))
p2img2=pygame.image.load('Pictures/P2Run2.png')
p2img2 = pygame.transform.scale(p2img2,(int(cell_size*1.3),int(cell_size*1.3)))
p2img3=pygame.image.load('Pictures/P2Run3.png')
p2img3 = pygame.transform.scale(p2img3,(int(cell_size*1.3),int(cell_size*1.3)))
p2img4 = pygame.image.load('Pictures/P2Run4.png')
p2img4 = pygame.transform.scale(p2img4,(int(cell_size*1.3),int(cell_size*1.3)))


background=pygame.image.load('Pictures/grassbackground.jpg')
background_image = pygame.transform.scale(background, (window_size, window_size))
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Game Time Display')

game_instance = Game()
font = pygame.font.Font(None, 27)


def draw_player_points():
    """Draw the players' points on the screen."""
    y_offset = 40
    for player in game_instance.get_players():
        points_text = font.render(f"{player.name} Points: {player.get_points()}", True, (0, 0, 0))
        screen.blit(points_text, (10, y_offset))
        y_offset += 30

def draw_resources():
    """Draw the resources on the grid."""
    for resource in game_instance.get_resources():
        if resource.is_notTaken():
            resource_pos = resource.get_position()
            pixel_pos=(resource_pos[0]*cell_size, resource_pos[1]*cell_size)
            if resource.get_type()=="Food":
                listImg = [image1,image2,image3]
                image = listImg[resource.get_item()-1]
                screen.blit(image, pixel_pos)
            elif resource.get_type()=="Arme":
                screen.blit(arme, pixel_pos)
            else: screen.blit(image4, pixel_pos)

def draw_players():
    """Draw the players on the grid."""
    for player in game_instance.get_players():
        direction=player.get_direction()
        player_pos = player.get_pos()

        # Position in pixels for the cell's top-left corner
        cell_top_left = (player_pos[0] * cell_size, player_pos[1] * cell_size)

        # Calculate the size and offset for centering
        image_size = int(cell_size * 1.3)
        offset = (image_size - cell_size) // 2

    # Adjust position to center the image
        centered_position = (cell_top_left[0] - offset, cell_top_left[1] - offset)

        if player.get_id()==1:
            if player_pos[0]%2==0:
                image = p1img1 if direction == "right" else p1img3
            else:
                image = p1img2 if direction == "right" else p1img4
            screen.blit(image, centered_position)
        else:
            if player_pos[0]%2==0:
                image = p2img1 if direction == "right" else p2img3
            else:
                image = p2img2 if direction == "right" else p2img4
            screen.blit(image, centered_position)



last_time = time.time()


while game_instance.get_running():

    for event in pygame.event.get():
        if event.type == pygame.QUIT: game_instance.stop_game()

    current_time = time.time()

    if current_time - last_time >= 1:

        game_instance.increment_time()

        game_instance.action()


        last_time = current_time

    screen.fill((255, 255, 255))

    for x in range(0, window_size, cell_size):
        for y in range(0, window_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Draw the cell border


    draw_resources()
    draw_player_points()
    draw_players()


    # Render the time text
    time_text = font.render(f"Time: {game_instance.get_time()}", True, (0, 0, 0))
    screen.blit(time_text, (10, 10))

    # Update the display
    pygame.display.flip()


pygame.quit()
sys.exit()

