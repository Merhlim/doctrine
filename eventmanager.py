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
        print("options")
        return None
    def about(self):
        pygame.Surface.fill(self.screen,(0,0,0))
        titlefont = pygame.font.Font("./assets/Fonts/HELR45W.ttf",60)
        title = titlefont.render("DOCTRINE",False,(99,0,0))
        aboutfont = pygame.font.Font("./assets/Fonts/HELR45W.ttf",20)
        about_line1 = aboutfont.render("DOCTRINE - A strategy game where you create and develop your own cult to take over the world!",False, (255,255,255))
        about_line2 = aboutfont.render("Scripting - Joshua Ampstead and Tim Charters",False,(255,255,255))
        about_line3 = aboutfont.render("Art - Joshua Taylor",False,(255,255,255))
        about_line4 = aboutfont.render("Game written in Python3 using the Pygame library",False,(255,255,255))
        self.screen.blit(title,(0,0))
        self.screen.blit(about_line1,(0,60))
        self.screen.blit(about_line2,(0,90))
        self.screen.blit(about_line3,(0,120))
        self.screen.blit(about_line4,(0,150))
        pygame.display.flip()
        pygame.time.delay(5000)
        pygame.Surface.fill(self.screen, (0, 0, 0))
        pygame.display.flip()
        return None
    # methods
