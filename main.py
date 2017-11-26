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
    pygame.display.set_icon(pygame.image.load("./assets/icon.ico"))
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

    startbutton = [pygame.image.load("./assets/button_static.bmp")]
    startbutton.append(startbutton[0].get_rect())
    startbutton[1] = startbutton[1].move(size[0] / 2 - 200 / 2, 550)
    startbutton[0] = pygame.transform.scale(startbutton[0],(200,75))
    startbutton_hover = [pygame.image.load("./assets/button_hover.bmp")]
    startbutton_hover.append(startbutton_hover[0].get_rect())
    startbutton_hover[1] = startbutton_hover[1].move(size[0] / 2 - 200 / 2, 550)
    startbutton_hover[0] = pygame.transform.scale(startbutton_hover[0],(200,75))
    startbutton_click = [pygame.image.load("./assets/button_active.bmp")]
    startbutton_click.append(startbutton_click[0].get_rect())
    startbutton_click[1] = startbutton_click[1].move(size[0] / 2 - 200 / 2, 550)
    startbutton_click[0] = pygame.transform.scale(startbutton_click[0],(200,75))

    optionsbutton = [pygame.image.load("./assets/options_static.bmp")]
    optionsbutton.append(optionsbutton[0].get_rect())
    optionsbutton[1] = optionsbutton[1].move(size[0] / 2 - 200 / 2, 650)
    optionsbutton[0] = pygame.transform.scale(optionsbutton[0],(200,75))
    optionsbutton_hover = [pygame.image.load("./assets/options_hover.bmp")]
    optionsbutton_hover.append(optionsbutton_hover[0].get_rect())
    optionsbutton_hover[1] = optionsbutton_hover[1].move(size[0] / 2 - 200 / 2, 650)
    optionsbutton_hover[0] = pygame.transform.scale(optionsbutton_hover[0],(200,75))
    optionsbutton_click = [pygame.image.load("./assets/options_active.bmp")]
    optionsbutton_click.append(optionsbutton_click[0].get_rect())
    optionsbutton_click[1] = optionsbutton_click[1].move(size[0] / 2 - 200 / 2, 650)
    optionsbutton_click[0] = pygame.transform.scale(optionsbutton_click[0],(200,75))

    aboutbutton = [pygame.image.load("./assets/about_static.bmp")]
    aboutbutton.append(aboutbutton[0].get_rect())
    aboutbutton[1] = aboutbutton[1].move(size[0] / 2 - 200 / 2, 750)
    aboutbutton[0] = pygame.transform.scale(aboutbutton[0],(200,75))
    aboutbutton_hover = [pygame.image.load("./assets/about_hover.bmp")]
    aboutbutton_hover.append(aboutbutton_hover[0].get_rect())
    aboutbutton_hover[1] = aboutbutton_hover[1].move(size[0] / 2 - 200 / 2, 750)
    aboutbutton_hover[0] = pygame.transform.scale(aboutbutton_hover[0],(200,75))
    aboutbutton_click = [pygame.image.load("./assets/about_active.bmp")]
    aboutbutton_click.append(aboutbutton_click[0].get_rect())
    aboutbutton_click[1] = aboutbutton_click[1].move(size[0] / 2 - 200 / 2, 750)
    aboutbutton_click[0] = pygame.transform.scale(aboutbutton_click[0],(200,75))

    exitbutton = [pygame.image.load("./assets/exit_static.bmp")]
    exitbutton.append(exitbutton[0].get_rect())
    exitbutton[1] = exitbutton[1].move(size[0] / 2 - 200 / 2, 850)
    exitbutton[0] = pygame.transform.scale(exitbutton[0],(200,75))
    exitbutton_hover = [pygame.image.load("./assets/exit_hover.bmp")]
    exitbutton_hover.append(exitbutton_hover[0].get_rect())
    exitbutton_hover[1] = exitbutton_hover[1].move(size[0] / 2 - 200 / 2, 850)
    exitbutton_hover[0] = pygame.transform.scale(exitbutton_hover[0],(200,75))
    exitbutton_click = [pygame.image.load("./assets/exit_active.bmp")]
    exitbutton_click.append(exitbutton_click[0].get_rect())
    exitbutton_click[1] = exitbutton_click[1].move(size[0] / 2 - 200 / 2, 850)
    exitbutton_click[0] = pygame.transform.scale(exitbutton_click[0],(200,75))

    backbutton = [pygame.image.load("./assets/back_static.bmp")]
    backbutton.append(backbutton[0].get_rect())
    backbutton[1] = backbutton[1].move(size[0] / 2 - 200 / 2, 750)
    backbutton[0] = pygame.transform.scale(backbutton[0],(200,75))
    backbutton_hover = [pygame.image.load("./assets/back_hover.bmp")]
    backbutton_hover.append(backbutton_hover[0].get_rect())
    backbutton_hover[1] = backbutton_hover[1].move(size[0] / 2 - 200 / 2, 750)
    backbutton_hover[0] = pygame.transform.scale(backbutton_hover[0],(200,75))
    backbutton_click = [pygame.image.load("./assets/back_active.bmp")]
    backbutton_click.append(backbutton_click[0].get_rect())
    backbutton_click[1] = backbutton_click[1].move(size[0] / 2 - 200 / 2, 750)
    backbutton_click[0] = pygame.transform.scale(backbutton_click[0],(200,75))

    animate = pygame.USEREVENT + 1
    crossani = 0
    def __init__(self):
        pygame.time.set_timer(self.animate, 250)
        self.screen.blit(self.burning_cross_1[0], self.burning_cross_1[1])
        while True:
            mouse = pygame.mouse.get_pos()
            clicc = pygame.mouse.get_pressed()

            self.screen.blit(self.startbutton[0],self.startbutton[1])
            self.screen.blit(self.optionsbutton[0],self.optionsbutton[1])
            self.screen.blit(self.aboutbutton[0],self.aboutbutton[1])
            self.screen.blit(self.exitbutton[0],self.exitbutton[1])
            #pygame.draw.rect(self.screen, self.Red, (self.size[0] / 2 - 200 / 2, 550, 200, 50))
            #pygame.draw.rect(self.screen, self.Red, (self.size[0] / 2 - 200 / 2, 650, 200, 50))
            #pygame.draw.rect(self.screen, self.Red, (self.size[0] / 2 - 200 / 2, 750, 200, 50))
            if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 650 + 75 > mouse[1] > 650:
                self.screen.blit(self.optionsbutton_hover[0], self.optionsbutton_hover[1])
            if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 750 + 75 > mouse[1] > 750:
                self.screen.blit(self.aboutbutton_hover[0], self.aboutbutton_hover[1])
            if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 550 + 75 > mouse[1] > 550:
                self.screen.blit(self.startbutton_hover[0], self.startbutton_hover[1])
            if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 850 + 75 > mouse[1] > 850:
                self.screen.blit(self.exitbutton_hover[0], self.exitbutton_hover[1])
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
                if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 650 + 75 > mouse[1] > 650:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(self.optionsbutton_click[0],self.optionsbutton_click[1])
                        pygame.display.flip()
                        eventmanager.event.options(self)
                if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 750 + 75 > mouse[1] > 750:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(self.aboutbutton_click[0],self.aboutbutton_click[1])
                        pygame.display.flip()
                        eventmanager.event.about(self)
                if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 550 + 75 > mouse[1] > 550:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(self.startbutton_click[0],self.startbutton_click[1])
                        pygame.display.flip()
                        eventmanager.event.startgame(self)
                if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 850 + 75 > mouse[1] > 850:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(self.exitbutton_click[0],self.exitbutton_click[1])
                        pygame.display.flip()
                        try:
                            pygame.quit()
                            exit()
                        except:
                            exit()
            self.screen.blit(self.doc[0], self.doc[1])
            self.screen.blit(self.rine[0], self.rine[1])

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