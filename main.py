import pygame
import eventmanager
import configparser

class main:
    pygame.init()
    Red = 99,00,00
    light_red = 99,22,22
    size = width, height = 1020, 940
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("DOCTRINE")
    burning_cross_1 = [pygame.image.load("./assets/Burning_Cross_1.bmp")]
    burning_cross_1.append(burning_cross_1[0].get_rect())
    burning_cross_1[0] = pygame.transform.scale(burning_cross_1[0], (300,492))
    burning_cross_1[1] = burning_cross_1[1].move(size[0]/2 - 300/2,20)
    burning_cross_2 = [pygame.image.load("./assets/Burning_Cross_2.bmp")]
    burning_cross_2.append(burning_cross_2[0].get_rect())
    burning_cross_2[0] = pygame.transform.scale(burning_cross_2[0], (300,492))
    burning_cross_2[1] = burning_cross_2[1].move(size[0]/2 - 300/2,20)
    doc = [pygame.image.load("./assets/Doc.bmp")]
    doc.append(doc[0].get_rect())
    doc[0] = pygame.transform.scale(doc[0],(350,180))
    doc[1] = doc[1].move(10,150)
    rine = [pygame.image.load("./assets/rine.bmp")]
    rine.append(rine[0].get_rect())
    rine[0] = pygame.transform.scale(rine[0],(350,180))
    rine[1] = rine[1].move(650,150)
    animate = pygame.USEREVENT + 1
    crossani = 0
    def __init__(self):
        pygame.time.set_timer(self.animate, 500)
        self.screen.blit(self.burning_cross_1[0], self.burning_cross_1[1])
        while True:
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(self.screen, self.Red, (self.size[0] / 2 - 200 / 2, 550, 200, 50))
            pygame.draw.rect(self.screen, self.Red, (self.size[0] / 2 - 200 / 2, 650, 200, 50))
            pygame.draw.rect(self.screen, self.Red, (self.size[0] / 2 - 200 / 2, 750, 200, 50))
            for event in pygame.event.get():
                if event.type == self.animate:
                    if self.crossani == 0:
                        self.screen.blit(self.burning_cross_1[0], self.burning_cross_1[1])
                        self.crossani = 1
                    else:
                        self.screen.blit(self.burning_cross_2[0], self.burning_cross_2[1])
                        self.crossani = 0
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if self.size[0]/2-200/2 + 200 > mouse[0] > self.size[0]/2-200/2 and 650 + 50 > mouse[1] > 650:
                pygame.draw.rect(self.screen, self.light_red, (self.size[0] / 2 - 200 / 2, 650, 200, 50))
            if self.size[0]/2-200/2 + 200 > mouse[0] > self.size[0]/2-200/2 and 750 + 50 > mouse[1] > 750:
                pygame.draw.rect(self.screen, self.light_red, (self.size[0] / 2 - 200 / 2, 750, 200, 50))
            if self.size[0]/2-200/2 + 200 > mouse[0] > self.size[0]/2-200/2 and 550 + 50 > mouse[1] > 550:
                pygame.draw.rect(self.screen, self.light_red, (self.size[0] / 2 - 200 / 2, 550, 200, 50))
            self.screen.blit(self.doc[0],self.doc[1])
            self.screen.blit(self.rine[0],self.rine[1])
            pygame.display.flip()

if __name__ == '__main__':
    main()

"""
------------- WUT --------------
So... were writing a game...

Make sure all functions in every class are under a strict private method (__) apart from the execution functions (game.startup)
in an attempt to prevent cheat engines from having an easy way in, of course there will always be cheats, but it is a singleplayer game so it doent matter that much

OwO Whats this???
--------------------------------
"""