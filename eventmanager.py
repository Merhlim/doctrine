import pygame
from time import sleep
import game


class event:
    pygame.init()

    def startgame(self):
        print("startgame")
        loadtext = pygame.font.Font("./assets/Fonts/HELR45W.ttf", 20)
        load = loadtext.render("Loading...", False, (255, 255, 255))
        pygame.Surface.fill(self.screen,(0,0,0))
        self.screen.blit(load,(0,0))
        pygame.display.flip()
        game.game.startup(self)
        return None
    def options(self):
        pygame.surface.fill(self.screen, (0, 0, 0))
        backbutton = [pygame.image.load("./assets/back_static.bmp")]
        backbutton.append(backbutton[0].get_rect())
        backbutton[1] = backbutton[1].move(10, 850)
        backbutton[0] = pygame.transform.scale(backbutton[0], (200, 75))
        backbutton_hover = [pygame.image.load("./assets/back_hover.bmp")]
        backbutton_hover.append(backbutton_hover[0].get_rect())
        backbutton_hover[1] = backbutton_hover[1].move(10, 850)
        backbutton_hover[0] = pygame.transform.scale(backbutton_hover[0], (200, 75))
        backbutton_click = [pygame.image.load("./assets/back_active.bmp")]
        backbutton_click.append(backbutton_click[0].get_rect())
        backbutton_click[1] = backbutton_click[1].move(10, 850)
        backbutton_click[0] = pygame.transform.scale(backbutton_click[0], (200, 75))

        return None
    def about(self):
        pygame.Surface.fill(self.screen, (0, 0, 0))
        backbutton = [pygame.image.load("./assets/back_static.bmp")]
        backbutton.append(backbutton[0].get_rect())
        backbutton[1] = backbutton[1].move(10, 850)
        backbutton[0] = pygame.transform.scale(backbutton[0], (200, 75))
        backbutton_hover = [pygame.image.load("./assets/back_hover.bmp")]
        backbutton_hover.append(backbutton_hover[0].get_rect())
        backbutton_hover[1] = backbutton_hover[1].move(10, 850)
        backbutton_hover[0] = pygame.transform.scale(backbutton_hover[0], (200, 75))
        backbutton_click = [pygame.image.load("./assets/back_active.bmp")]
        backbutton_click.append(backbutton_click[0].get_rect())
        backbutton_click[1] = backbutton_click[1].move(10, 850)
        backbutton_click[0] = pygame.transform.scale(backbutton_click[0], (200, 75))
        pygame.Surface.fill(self.screen,(0,0,0))
        titlefont = pygame.font.Font("./assets/Fonts/terminal.ttf",60)
        title = titlefont.render("DOCTRINE",False,(99,0,0))
        aboutfont = pygame.font.Font("./assets/Fonts/terminal.ttf",20)
        about_line1 = aboutfont.render("DOCTRINE - A strategy game where you create and develop",False,(255,255,255))
        about_line1_5 = aboutfont.render("your own cult to take over the world!",False, (255,255,255))
        about_line2 = aboutfont.render("Scripting - Joshua Ampstead and Tim Charters",False,(255,255,255))
        about_line3 = aboutfont.render("Art - Joshua Taylor",False,(255,255,255))
        about_line4 = aboutfont.render("Game written in Python3 using the Pygame library",False,(255,255,255))
        self.screen.blit(title,(0,0))
        self.screen.blit(about_line1,(0,60))
        self.screen.blit(about_line1_5,(0,80))
        self.screen.blit(about_line2,(0,125))
        self.screen.blit(about_line3,(0,160))
        self.screen.blit(about_line4,(0,190))
        while True:
            mouse = pygame.mouse.get_pos()
            self.screen.blit(backbutton[0], backbutton[1])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if 10 + 200 > mouse[0] > 10 - 200 and 850 + 75 > mouse[1] > 850:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(backbutton_click[0],backbutton_click[1])
                        pygame.display.flip()
                        pygame.time.delay(100)
                        pygame.Surface.fill(self.screen, (0, 0, 0))
                        pygame.display.flip()
                        return None
            if 10 + 200 > mouse[0] > 10 - 200 and 850 + 75 > mouse[1] > 850:
                self.screen.blit(backbutton_hover[0], backbutton_hover[1])
            pygame.display.flip()
        return None
    # methods
