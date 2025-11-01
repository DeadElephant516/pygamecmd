import pygame
import ui
from CONSTANTS import COLORS, WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from game import game
import commands
import utils

pygame.init()



screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Adventure")
clock = pygame.time.Clock()


input_text = ""
input_font = pygame.font.Font(None,24)
room_font = pygame.font.Font(None,32)
history = []
result = ""


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #BASIC INPUT HANDLING
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                history.append(input_text)
                print(f"Command entered: {input_text}")
                print(history)
                cmd = input_text.lower()
                result = commands.process_cmd(cmd,game)


                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    screen.fill(COLORS["BLACK"])
    current_room_data = game["areas"][game["current_area"]]
    room_text = current_room_data["description"]
    exits = list(current_room_data["exits"].keys())
    exits_text = ", ".join(exits)
    area_items = utils.show_nearby_items(game)

    # Draw the image box background
    ui.draw_image_box(screen)
    ui.draw_area_image(screen, current_room_data["image"])


    ui.draw_input_box(screen)
    ui.draw_room_info_box(screen)
    ui.draw_input_text(screen,input_text,input_font)
    ui.draw_room_text(screen, f"You are in {game['current_area']}", room_font, 20,COLORS["WHITE"])
    ui.draw_room_text(screen,room_text,room_font,50,COLORS["WHITE"])
    ui.draw_room_text(screen,f"Exits: {exits_text}",room_font,120,COLORS["YELLOW"])
    ui.draw_room_text(screen, f"{area_items}", room_font, 150, COLORS["YELLOW"])
    ui.draw_response_box(screen)
    ui.draw_response_text(screen,result,room_font,20,COLORS["YELLOW"])




    pygame.display.flip()

    clock.tick(FPS)
pygame.quit()