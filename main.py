import pygame, eventmanager, configparser   # Importing various modules required for the software to run


# Create the main class that will be running the program
class __main__:

    pygame.init()    # Initialise the pygame libraries
    Red = 99,00,00    # Default game colors e.t.c.
    light_red = 99,22,22

    # Setting up the pygame window
    size = width, height = 1020, 940
    screen = pygame.display.set_mode(size)   # Window resolution
    pygame.display.set_caption("DOCTRINE")   # Window name
    pygame.display.set_icon(pygame.image.load("./assets/icon.ico"))   # Window icon

    # Creating a simple loading screen while the game loads its assets
    loadtext = pygame.font.Font("./assets/Fonts/HELR45W.ttf", 20)
    load = loadtext.render("Loading...", False, (255, 255, 255))
    pygame.Surface.fill(screen, (0, 0, 0))
    trect = load.get_rect()
    screen.blit(load, (0, 0))
    pygame.display.flip()

    # Loading ALL assets for the game, allowing any screen to use them at any time, slowing down the startup, but speeding up the actual runtime and speed of the game
    burning_cross_1 = [pygame.image.load("./assets/Burning_Cross_1.bmp")]   # Load the burning cross image
    burning_cross_1.append(burning_cross_1[0].get_rect())   # Will get the location object of the image allowing it to be manipulated
    burning_cross_1[0] = pygame.transform.scale(burning_cross_1[0], (300,492))   # Changing the size of the image to allowing it to fit the constraints we want
    burning_cross_1[1] = burning_cross_1[1].move(size[0]/2 - 300/2,20)   # Moving the image to the location on the screen
    burning_cross_2 = [pygame.image.load("./assets/Burning_Cross_2.bmp")]   # loading the second frame for the animation
    burning_cross_2.append(burning_cross_2[0].get_rect())   # Performing the same operations as the first frame
    burning_cross_2[0] = pygame.transform.scale(burning_cross_2[0], (300,492))
    burning_cross_2[1] = burning_cross_2[1].move(size[0]/2 - 300/2,20)
    # The rest of the image loading follows the same format

    doc = [pygame.image.load("./assets/Doc.bmp")]   # Loading the first half of the title
    doc.append(doc[0].get_rect())
    doc[0] = pygame.transform.scale(doc[0],(300,180))
    doc[1] = doc[1].move(10,150)
    rine = [pygame.image.load("./assets/rine.bmp")]   # Loading the second half of the title
    rine.append(rine[0].get_rect())
    rine[0] = pygame.transform.scale(rine[0],(350,180))
    rine[1] = rine[1].move(size[0]-360,150)

    startbutton = [pygame.image.load("./assets/button_static.bmp")]   # Loading the startgame button
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

    optionsbutton = [pygame.image.load("./assets/options_static.bmp")]   # Loading the options button
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

    aboutbutton = [pygame.image.load("./assets/about_static.bmp")]   # Loading the About button
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

    exitbutton = [pygame.image.load("./assets/exit_static.bmp")]   # Loading the exit button
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

    backbutton = [pygame.image.load("./assets/back_static.bmp")]   # Loading the back button
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

    okbutton = [pygame.image.load("./assets/ok_static.bmp")]   # Loading the Ok button
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

    clock = pygame.time.Clock()    # Setup the clock object for tick counting

    nyc = [pygame.image.load("./assets/Name_Your_Cult.bmp")]   # Loading the "name your cult" image
    nyc.append(nyc[0].get_rect())
    nyc[0] = pygame.transform.scale(nyc[0], (525, 185))
    nyc[1] = nyc[1].move(10, 25)

    animate = pygame.USEREVENT + 1   # Setting up the check for the burning cross animation
    crossani = 0

    pygame.Surface.fill(screen,(0,0,0))  # Clear the screen from the loading text

    def __init__(self):   # main function for the game
        pygame.time.set_timer(self.animate, 250)   # start the animation timer
        self.screen.blit(self.burning_cross_1[0], self.burning_cross_1[1])   # Blit the first frame of the burning cross
        while True:   # Menu main loop
            mouse = pygame.mouse.get_pos()   # getting events for buttons
            clicc = pygame.mouse.get_pressed()

            self.screen.blit(self.startbutton[0],self.startbutton[1])   # Loading the images for the buttons
            self.screen.blit(self.optionsbutton[0],self.optionsbutton[1])
            self.screen.blit(self.aboutbutton[0],self.aboutbutton[1])
            self.screen.blit(self.exitbutton[0],self.exitbutton[1])

            # Checking for when the mouse is over one of the buttons, if so then make them light up
            if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 650 + 75 > mouse[1] > 650:
                self.screen.blit(self.optionsbutton_hover[0], self.optionsbutton_hover[1])
            if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 750 + 75 > mouse[1] > 750:
                self.screen.blit(self.aboutbutton_hover[0], self.aboutbutton_hover[1])
            if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 550 + 75 > mouse[1] > 550:
                self.screen.blit(self.startbutton_hover[0], self.startbutton_hover[1])
            if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 850 + 75 > mouse[1] > 850:
                self.screen.blit(self.exitbutton_hover[0], self.exitbutton_hover[1])

            for event in pygame.event.get():   # Menu event loop

                if event.type == self.animate:   # Change the frame for the animation accordingly
                    if self.crossani == 0:
                        self.screen.blit(self.burning_cross_1[0], self.burning_cross_1[1])
                        self.crossani = 1
                    else:
                        self.screen.blit(self.burning_cross_2[0], self.burning_cross_2[1])
                        self.crossani = 0

                if event.type == pygame.QUIT:   # If the user attempts to close the game, then quit
                    pygame.quit()
                    exit()

                    # Checking if a button has been clicked
                if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 650 + 75 > mouse[1] > 650:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(self.optionsbutton_click[0],self.optionsbutton_click[1])   # Load the clicked image for the button
                        pygame.display.flip()   # Render the frame
                        pygame.time.delay(100)   # Allow the frame to be visible for 100
                        eventmanager.event.options(self)   # Change the current program event
                        # The rest of the button click checks will follow the same format
                if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 750 + 75 > mouse[1] > 750:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(self.aboutbutton_click[0],self.aboutbutton_click[1])
                        pygame.display.flip()
                        pygame.time.delay(100)
                        eventmanager.event.about(self)
                if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 550 + 75 > mouse[1] > 550:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(self.startbutton_click[0],self.startbutton_click[1])
                        pygame.display.flip()
                        pygame.time.delay(100)
                        eventmanager.event.startgame(self)
                if self.size[0] / 2 - 200 / 2 + 200 > mouse[0] > self.size[0] / 2 - 200 / 2 and 850 + 75 > mouse[1] > 850:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.blit(self.exitbutton_click[0],self.exitbutton_click[1])
                        pygame.display.flip()
                        pygame.time.delay(100)
                        try:   # If the exit button is pressed then close the game
                            pygame.quit()
                            exit()
                        except:
                            exit()

            # Blit both of the title images
            self.screen.blit(self.doc[0], self.doc[1])
            self.screen.blit(self.rine[0], self.rine[1])

            pygame.display.flip()   # Render the current frame

if __name__ == '__main__':
    __main__()   # Start the game if its run directly from the script

"""
------------- WUT --------------
So... were writing a game...

Make sure all functions in every class are under a strict private method (__) apart from the execution functions (game.startup)
in an attempt to prevent cheat engines from having an easy way in, of course there will always be cheats, but it is a singleplayer game so it doent matter that much

OwO Whats this???
--------------------------------
"""