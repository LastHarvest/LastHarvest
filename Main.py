import pygame
import sys
import time


from Disponibility import TRUE, FALSE, APPEARED
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
image4 = pygame.transform.scale(image4,(int(cell_size*0.8),int(cell_size*0.8)))
arme = pygame.image.load('Pictures/Arme.png')
arme = pygame.transform.scale(arme,(int(cell_size*0.8),int(cell_size*0.8)))

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

game_instance = Game()
# Set up font
font = pygame.font.Font(None, 27)


#Move to player class check_for_ressources(player)
# def check_for_resources(player):
#     for resource in game_instance.get_resources():
#         player.collect_resource(resource)


# def move_player_to_resource(player, resource):
#     """moves the player to the given resource"""
#     p = player.get_pos()
#     r = resource.get_position()
#     if p[0] < r[0]:
#       player.move_right()
#       draw_players()
#     elif p[0] > r[0]:
#        player.move_left()
#        draw_players()
#     else:
#         if p[1] < r[1]:
#            player.move_up()
#         elif p[1] > r[1]:
#            player.move_down()
#
#     player.check_for_resource(game_instance.get_resources())



#Resources spawning to make the game dynamic





#à quoi sert cette fonction ?
# def tuer(p1,p2):
#     if p1.get_arme() and p2.get_vivant():
#         pos = p1.get_pos()
#
#         tab = [(pos[0]+1,pos[1]),(pos[0]+1,pos[1]+1),(pos[0]+1,pos[1]-1),(pos[0],pos[1]+1),(pos[0],pos[1]-1),(pos[0]-1,pos[1]-1),
#                (pos[0]-1,pos[1]),(pos[0]-1,pos[1]+1)]
#
#         if p2.get_pos() in tab:
#             p2.update_vivant(False)



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

last_time = time.time()



while game_instance.get_running():

    for event in pygame.event.get():
        if event.type == pygame.QUIT: game_instance.stop_game()

    # Increment game time and move players every second
    current_time = time.time()

    if current_time - last_time >= 1:

        game_instance.increment_time()

        game_instance.action()





        #Savoir qui peut avoir l'arme
        # if players[0].has_arme() :
        #     playArme = players[0]
        #     playNotArme = players[1]
        # else :
        #     playArme = players[1]
        #     playNotArme = players[0]

        # Détermination des actions des joueurs
        # if not(playArme.has_arme()) and playArme.get_points()>30:
        #     resources[0].set_Free()
        #     playArme.move_player_to_resource(resources[0])
        #     playArme.check_for_resource(resources)
        #     if not(resources[0].get_isFree()):
        #         playArme.setArme()
        #     playNotArme.move_player_to_resource(player.get_best_resource(resources))
        #     playNotArme.check_for_resource(resources)
        #     if nb_Libre()<7 and nb_Resources<nb_ResourcesMax:
        #         nb_Resources+=1
        #         add_ressources(nb_Resources)
        #     draw_resources()

        # elif playArme.has_arme():
        #     playArme.move_player_to_player(playNotArme) # à ameliorer avec un for si on met plus de 2 players
        #     tuer(playArme,playNotArme)
        #     playNotArme.move_player_to_resource(player.get_best_resource(resources))
        #     playNotArme.check_for_resource(resources)
        #     if nb_Libre()<7 and nb_Resources<nb_ResourcesMax:
        #         nb_Resources+=1
        #         add_ressources(nb_Resources)
        #     draw_resources()
        #
        # else :
        #     for player in game_instance.get_players():
        #         player.move_player_to_resource(player.get_best_resource(resources))
        #     player.check_for_resource(resources)
        #     if nb_Libre()<7 and nb_Resources<nb_ResourcesMax:
        #         nb_Resources+=1
        #         add_ressources(nb_Resources)
        #     draw_resources()

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
    # for player in game_instance.get_players():
    #     if player.get_vivant():
    #         player_pos = player.get_pos()
            #pygame.draw.circle(screen, (0, 0, 255), (player_pos[0] * cell_size + cell_size // 2, player_pos[1] * cell_size + cell_size // 2), cell_size // 3)

    draw_resources()
    draw_player_points()
    draw_players()

    # Render the time text
    #time_text = font.render(f"Time: {game_instance.get_time()}", True, (0, 0, 0))
    #screen.blit(time_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()

