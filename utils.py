import pygame
pygame.font.init()

FPS = 60
PATH = [(169, 124), (52, 127), (71, 488), (299, 717), (406, 637), (430, 519), (590, 531), 
        (611, 698), (734, 677), (728, 410), (455, 367), (476, 261), (685, 250), (690, 87), 
        (340, 81), (280, 239), (276, 369), (173, 349), (166, 223)]


def scale_image(img,factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft = top_left).center)
    win.blit(rotated_image, new_rect.topleft)
    
def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width()/2,
                    win.get_height()/2 - render.get_height()/2))