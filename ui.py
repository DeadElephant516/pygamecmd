import pygame

import CONSTANTS
from CONSTANTS import COLORS

INPUT_HEIGHT = 50

INPUT_BOX = pygame.Rect(0,CONSTANTS.WINDOW_HEIGHT-50,CONSTANTS.WINDOW_WIDTH,INPUT_HEIGHT)
ROOM_INFO_BOX = pygame.Rect(0,0,CONSTANTS.WINDOW_WIDTH//2,CONSTANTS.WINDOW_HEIGHT//2)
IMAGE_BOX = pygame.Rect(CONSTANTS.WINDOW_WIDTH // 2, 0, CONSTANTS.WINDOW_WIDTH // 2, CONSTANTS.WINDOW_HEIGHT // 2)
RESPONSE_BOX = pygame.Rect(0,CONSTANTS.WINDOW_HEIGHT//2,CONSTANTS.WINDOW_WIDTH//2,CONSTANTS.WINDOW_HEIGHT//2-INPUT_HEIGHT)


def draw_input_box(surface):
    pygame.draw.rect(surface,COLORS["BLACK"],INPUT_BOX)
    pygame.draw.rect(surface, COLORS["WHITE"], INPUT_BOX, 2)

def draw_input_text(surface,text,font):
    text_surface = font.render(text,True,COLORS["WHITE"])
    text_rect = text_surface.get_rect(midleft=(INPUT_BOX.x + 10,INPUT_BOX.centery))
    surface.blit(text_surface,text_rect)

def draw_room_info_box(surface):
    pygame.draw.rect(surface,COLORS["BLACK"],ROOM_INFO_BOX)
    pygame.draw.rect(surface, COLORS["RED"], ROOM_INFO_BOX,2)

def draw_room_text(surface,text,font,y_pos,color):
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect(midleft=(ROOM_INFO_BOX.x + 10, ROOM_INFO_BOX.y + y_pos))
    surface.blit(text_surface, text_rect)

def draw_image_box(surface):
    pygame.draw.rect(surface, COLORS["BLACK"], IMAGE_BOX)
    pygame.draw.rect(surface, COLORS["BLUE"], IMAGE_BOX, 2)

def draw_area_image(surface, image):
    scaled_image = pygame.transform.scale(image, (IMAGE_BOX.width, IMAGE_BOX.height))
    surface.blit(scaled_image, IMAGE_BOX)

def draw_response_box(surface):
    pygame.draw.rect(surface,COLORS["BLACK"],RESPONSE_BOX)
    pygame.draw.rect(surface, COLORS["RED"], RESPONSE_BOX,2)

def draw_response_text(surface,text,font,y_pos,color):
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect(midleft=(RESPONSE_BOX.x+10, RESPONSE_BOX.y + y_pos))
    surface.blit(text_surface,text_rect)
