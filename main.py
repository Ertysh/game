from pygame import *
import os

init()

window_width = 1000
window_height= 600

screen = display.set_mode((window_width, window_height))
display.set_caption("Game")
logo_path = os.path.join(os.path.dirname(__file__), 'src', 'images', 'logo.png')
display.set_icon(image.load(logo_path))
background_path = os.path.join(os.path.dirname(__file__), 'src', 'images', 'background.png')
background_img = transform.scale(image.load(background_path).convert() , (window_width, window_height))

running = True
while running:
    for e in event.get():
        if e.type == QUIT or (
            e.type == KEYDOWN and e.key == K_ESCAPE):
            running = False

    screen.blit(background_img, (0, 0))
    display.flip()


quit()