import pygame, eztext
class game:
    pygame.init()
    def startup(self):
        txtbx = eztext.Input(maxlength=45, color=(255, 0, 0), prompt='',x=200 , y=400)
        font = pygame.font.Font("./assets/Fonts/HELR45W.ttf",60)
        textowo = font.render("Name your cult:",False,(99,0,0),(33,0,0))
        while pygame.mouse.get_pressed()[2] != 1:
            events = pygame.event.get()
            txtbx.update(events)
            pygame.Surface.fill(self.screen,(0,0,0))
            text = txtbx.draw(self.screen)
            self.screen.blit(textowo,(0,0))
            pygame.display.flip()
        pygame.Surface.fill(self.screen, (0,0,0))
        pygame.display.flip()
        return None