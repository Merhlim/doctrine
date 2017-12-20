import pygame, pygame_textinput
class game:
    pygame.init()
    def startup(self):

        nyc = [pygame.image.load("./assets/Name_Your_Cult.bmp")]
        nyc.append(nyc[0].get_rect())
        nyc[0] = pygame.transform.scale(nyc[0], (525, 185))
        nyc[1] = nyc[1].move(10, 25)
        txtbx = pygame_textinput.TextInput(font_family="./assets/Fonts/terminal.ttf",font_size=40,text_color=(88,0,0),cursor_color=(255,255,255))
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
        clock = pygame.time.Clock()

        while True:
            pygame.Surface.fill(self.screen,(0,0,0))
            self.screen.blit(nyc[0], nyc[1])
            mouse = pygame.mouse.get_pos()
            self.screen.blit(backbutton[0], backbutton[1])
            self.screen.blit(okbutton[0],okbutton[1])
            events = pygame.event.get()
            for event in events:
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
                if 800 + 200 > mouse[0] > 800 - 200 and 850 + 75 > mouse[1] > 850:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(okbutton_click[0], okbutton_click[1])
                        pygame.display.flip()
                        pygame.time.delay(100)
                        pygame.Surface.fill(self.screen, (0, 0, 0))
                        pygame.display.flip()
                        return None
            if 800 + 200 > mouse[0] > 800 - 200 and 850 + 75 > mouse[1] > 850:
                self.screen.blit(okbutton_hover[0], okbutton_hover[1])

            if 10 + 200 > mouse[0] > 10 - 200 and 850 + 75 > mouse[1] > 850:
                self.screen.blit(backbutton_hover[0], backbutton_hover[1])
            txtbx.update(events)
            print(txtbx.get_text())  # FIXME Text wont clear on backspace and text cursor not clearing
            self.screen.blit(txtbx.get_surface(), (10, 255))
            pygame.display.flip()
            clock.tick(30)