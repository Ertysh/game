from pygame import *
import os

init()
mixer.init()
font.init()

window_width = 1000
window_height= 800

screen = display.set_mode((window_width, window_height))
display.set_caption("Game")
logo_path = os.path.join(os.path.dirname(__file__), 'src', 'images', 'logo.png')
display.set_icon(image.load(logo_path))

background_path = os.path.join(os.path.dirname(__file__), 'src', 'images', 'background.png')
optinons_background_path = os.path.join(os.path.dirname(__file__), 'src', 'images', 'option_background.png')
background_img = transform.scale(image.load(background_path).convert() , (window_width, window_height))

main_font = font.SysFont('PixelArt Fantasy Font',50)
main_menu_button_quit =  os.path.join(os.path.dirname(__file__), 'src', 'images', 'button_quit.png')
main_menu_button_play = os.path.join(os.path.dirname(__file__), 'src', 'images', 'button_play.png')
main_menu_button_options = os.path.join(os.path.dirname(__file__), 'src', 'images', 'button_option.png')

option_menu_button_return = os.path.join(os.path.dirname(__file__), 'src', 'images', 'option_menu_button_return.png')


music_path = os.path.join(os.path.dirname(__file__), 'src', 'musik', 'main_menu_musik.mp3')

try:
    mixer.music.load(music_path)
    mixer.music.play(-1)
except error as e:
    print(f"Помилка завантаження музики: {e}")


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
button_quit = SingleSpriteButton(main_menu_button_quit, window_width // 2 - 225, 500 , action="quit")
# Створення кнопки "Грати"
button_play = SingleSpriteButton(main_menu_button_play, window_width // 2 - 225, 200 , action="start")
# Створення кнопки "Опції"
button_options = SingleSpriteButton(main_menu_button_options, window_width // 2 - 225, 350 , action="options")
# Створення кнопки "Повернутися до меню"
button_return = SingleSpriteButton(option_menu_button_return, window_width // 2 - 225, 500 , action="back_to_menu")

main_menu_buttons = sprite.Group()
main_menu_buttons.add(button_quit, button_play , button_options)
options_buttons = sprite.Group()
options_buttons.add(button_return)

# Змінна для відстеження поточного стану гри
game_state = "main_menu"

# Функція для відображення головного меню
def draw_main_menu():
    screen.blit(transform.scale(image.load(background_path).convert(), (window_width, window_height)), (0, 0))
    main_menu_buttons.draw(screen)

# Функція для відображення екрана опцій
def draw_options_screen():
    screen.blit(transform.scale(image.load(optinons_background_path).convert(), (window_width, window_height)), (0, 0))
    text = main_font.render("Settings", True, (255, 255, 255))
    text_rect = text.get_rect(center=(window_width // 2, 100))
   
    screen.blit(text, text_rect)
    options_buttons.draw(screen)

    

running = True


while running:
    for e in event.get():
        if e.type == QUIT or (
            e.type == KEYDOWN and e.key == K_ESCAPE):
            running = False
            

        if e.type == MOUSEBUTTONDOWN:
                for button in main_menu_buttons:
                    if button.is_clicked():
                        print(f"Натиснуто кнопку в області: {button.rect}")
                        print(f"Позиція миші: {mouse.get_pos()}")
                        if button.action == "options":
                            game_state = "options"
                        elif button.action == "start":
                            print("Запуск гри!")
                            game_state = "playing" # Перехід до стану гри
                        elif button.action == "quit":
                            running = False
        
        elif game_state == "options":
            for button in options_buttons:
                if button.is_clicked():
                    if button.action == "back_to_menu":
                        game_state = "main_menu"
         

    if game_state == "main_menu":
        draw_main_menu()
    elif game_state == "options":
        draw_options_screen()
    elif game_state == "playing":
        screen.fill((0, 0, 0))
        text = main_font.render("Гра запущена!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        screen.blit(text, text_rect)         

    display.flip()
  

quit()