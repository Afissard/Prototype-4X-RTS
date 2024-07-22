import pygame, sys, random
from sprite import Sprite

# VARIABLES
# Tiles and Window setting
TILE_SIZE = 16
scr_width = TILE_SIZE * 64
scr_height = TILE_SIZE * 48

COLOR = [
    (23,14,0),      # Black
    (255,241,232),  # White
]


# CLASSE
class Game():
    def __init__(self):
        # pygame setup
        self.screen = pygame.display.set_mode((scr_width, scr_height))
        pygame.display.set_caption("Prototype 4X/RTS [v0.01]")
        self.clock = pygame.time.Clock()
        #pygame.event.set_grab(False) # set to True if the game use the mouse

        # game variable
        self.show_debug = False
        self.font = pygame.font.Font("./assets/font/BigBlueTerm437NerdFont-Regular.ttf", 16)

        self.run_sprite_benchmark = False
        self.sprite_list = []


    def show_debug_info(self):
        debug_str = ""
        debug_str += str(int(self.clock.get_fps())) + " FPS"
        debug_str += "\n" + str(len(self.sprite_list)) + " sprites"

        debug_disp = self.font.render(debug_str, False, COLOR[1])
        self.screen.blit(debug_disp, (0, 0))


    def __sprite_benchmark(self): ### TESTS ###
        if self.clock.get_fps() > 30 :
            new_sprite = Sprite(random.randint(0, scr_width), random.randint(0, scr_height), "assets/sprite/mage.png")
            self.sprite_list.append(new_sprite)
        else :
            self.run_sprite_benchmark = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_F3:
                    self.show_debug = not self.show_debug
                if event.key == pygame.K_F12:
                    running = False
                    pygame.quit()
                    sys.exit()
                # TESTS
                if event.key == pygame.K_F1:
                    self.run_sprite_benchmark = not self.run_sprite_benchmark
                    #print("benchmark is runing :", self.run_sprite_benchmark)
                if event.key == pygame.K_F2:
                    self.sprite_list = []

        if self.run_sprite_benchmark :
            self.__sprite_benchmark()

    def display(self):
        self.screen.fill(COLOR[0]) # Clear the screen

        for i in self.sprite_list :
            i.display(self.screen)

        if self.show_debug: self.show_debug_info()

        pygame.display.update()

    def run(self):
        """
        Game loop
        """
        running = True
        while running:
            # UPDATE
            self.update()
            # DISPLAY
            self.display()

            self.clock.tick(60)
