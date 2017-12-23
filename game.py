import pygame, pygame_textinput, eventmanager  # Importing various modules required for the software to run


class game:  # Creating the class for the game
    pygame.init()  # Initialise the pygame libraries

    def startup(self):
        txtbx = pygame_textinput.TextInput(font_family="./assets/Fonts/terminal.ttf",  # Creating a text box object for the user to input text that they desire for their cult name
                                           font_size=40,
                                           text_color=(88,0,0),
                                           cursor_color=(255,255,255)
                                           )
        while True:  # NYC screen loop
            pygame.Surface.fill(self.screen,(0,0,0))  # Clear the window
            self.screen.blit(self.nyc[0], self.nyc[1])  # Blit the title to the screen
            mouse = pygame.mouse.get_pos()  # Get the position of the mouse
            self.screen.blit(self.backbutton[0], self.backbutton[1])  # Blit the buttons to the screen
            self.screen.blit(self.okbutton[0],self.okbutton[1])

            events = pygame.event.get() #Get the window events
            for event in events: #A diffrent take on the pygame event loop, for the input box

                if event.type == pygame.QUIT:  # If the user attempts to close the game, then quit
                    pygame.quit()
                    exit()

                if 10 + 200 > mouse[0] > 10 - 200 and 850 + 75 > mouse[1] > 850:  # Checking if the users mouse is over the button object
                    if event.type == pygame.MOUSEBUTTONDOWN:  # Then if they click while its over that object
                        self.screen.blit(self.backbutton_click[0],self.backbutton_click[1])  # Replace the button image with the clicked state
                        pygame.display.flip()  # Render the frame
                        pygame.time.delay(100)  # Wait for 100
                        pygame.Surface.fill(self.screen, (0, 0, 0))  # Clear the frame
                        pygame.display.flip()  # Render the frame
                        return None  # Return to the main menu
                        # This is the same for the rest of the button checks

                if 800 + 200 > mouse[0] > 800 - 200 and 850 + 75 > mouse[1] > 850:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(self.okbutton_click[0], self.okbutton_click[1])
                        pygame.display.flip()
                        pygame.time.delay(100)
                        pygame.Surface.fill(self.screen, (0, 0, 0))
                        pygame.display.flip()
                        return None

            if 800 + 200 > mouse[0] > 800 - 200 and 850 + 75 > mouse[1] > 850:  # Checking if the users mouse is over the button object
                self.screen.blit(self.okbutton_hover[0], self.okbutton_hover[1])  # Update the buttons image to the "button hover" asset

            if 10 + 200 > mouse[0] > 10 - 200 and 850 + 75 > mouse[1] > 850:
                self.screen.blit(self.backbutton_hover[0], self.backbutton_hover[1])
            txtbx.update(events)  # Send the text box the current pygame events
            self.screen.blit(txtbx.get_surface(), (10, 255))  # Blit the text box to the frame
            pygame.display.flip()  # Render the current frame
            self.clock.tick(30)  # Tick the pygame clock be 30
