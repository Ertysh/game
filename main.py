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
menu_button_image =  os.path.join(os.path.dirname(__file__), 'src', 'images', 'button_quit.png')


class SingleSpriteButton(sprite.Sprite):
    def __init__(self, image_path, x, y, action=None):
        super().__init__()
        self.image = image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action

    def is_clicked(self):
        mouse_pos = mouse.get_pos()
        mouse_click = mouse.get_pressed()
        return self.rect.collidepoint(mouse_pos) and mouse_click[0]

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Створення кнопки "Вихід"
button_quit = SingleSpriteButton(menu_button_image, window_width // 2 - 225, 400)

all_sprites = sprite.Group()
all_sprites.add(button_quit)

running = True
while running:
    for e in event.get():
        if e.type == QUIT or (
            e.type == KEYDOWN and e.key == K_ESCAPE):
            running = False

        if e.type == MOUSEBUTTONDOWN:
            if button_quit.is_clicked():
                running = False

    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)  # Відображення кнопки
    display.flip()
  


quit()