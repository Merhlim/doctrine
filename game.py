import pygame, eztext
class game:
    pygame.init()
    def startup(self):

        nyc = [pygame.image.load("./assets/Name_Your_Cult.bmp")]
        nyc.append(nyc[0].get_rect())
        nyc[0] = pygame.transform.scale(nyc[0], (525, 185))
        nyc[1] = nyc[1].move(10, 25)
        txtbx = eztext.Input(maxlength=20, color=(88, 0, 0), prompt='',x=10 , y=225, font=pygame.font.Font("./assets/Fonts/terminal.ttf",60))
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
        okbutton = [pygame.image.load("./assets/ok_static.bmp")]
        okbutton.append(okbutton[0].get_rect())
        okbutton[1] = okbutton[1].move(800, 850)
        okbutton[0] = pygame.transform.scale(okbutton[0], (200, 75))
        okbutton_hover = [pygame.image.load("./assets/ok_hover.bmp")]
        okbutton_hover.append(okbutton_hover[0].get_rect())
        okbutton_hover[1] = okbutton_hover[1].move(800, 850)
        okbutton_hover[0] = pygame.transform.scale(okbutton_hover[0], (200, 75))
        okbutton_click = [pygame.image.load("./assets/ok_active.bmp")]
        okbutton_click.append(okbutton_click[0].get_rect())
        okbutton_click[1] = okbutton_click[1].move(800, 850)
        okbutton_click[0] = pygame.transform.scale(okbutton_click[0], (200, 75))
        self.screen.blit(nyc[0], nyc[1])
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