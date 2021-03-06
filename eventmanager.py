import pygame, game, configparser #Importing various modules required for the software to run


class error:
    pygame.init()
    def missing_file_error(screen,err):
        pygame.Surface.fill(screen, (0, 0, 0))
        font = pygame.font.Font(pygame.font.get_default_font(),20)
        text = font.render("Missing file(s) error, it appears: ",False,(255,255,255))
        text1 = font.render(str(err),False,(255,255,255))
        text2 = font.render("Are missing or corrupted", False, (255,255,255))
        text3 = font.render("Try redownloading the game to fix the problem", False, (255,255,255))
        text4 = font.render("Press any key to close", False, (255,255,255))
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()
                    exit("Files were missing from the games directories, try reinstalling\nTf that fails then contact:\n\njoshua.ampstead@hotmail.co.uk")
                if event.type == pygame.KEYDOWN:
                    pygame.quit()
                    exit("Files were missing from the games directories, try reinstalling\nTf that fails then contact:\n\njoshua.ampstead@hotmail.co.uk")
            screen.blit(text, (0,0))
            screen.blit(text1, (0,20))
            screen.blit(text2, (0,40))
            screen.blit(text3, (0,60))
            screen.blit(text4, (0,80))
            pygame.display.flip()

    def normie_error(screen):
        pygame.Surface.fill(screen, (0, 0, 0))
        font = pygame.font.Font(pygame.font.get_default_font(),20)
        text = font.render("GET OFF MY SUB NORMIE SCUM",False,(255,255,255))
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()
                    exit("BEGONE NORMIE")
                if event.type == pygame.KEYDOWN:
                    pygame.quit()
                    exit("BEGONE NORMIE")
            screen.blit(text, (0,0))
            pygame.display.flip()


class event: #Create the event class, accessible to any game script
    pygame.init() #Initialise the pygame libraries

    cfgpsr = configparser.ConfigParser()
    cfg = cfgpsr.read("./config.ini")

    def loadingscreen(self):  # Create a loading screen so to speak so that it can be used at any time
        try:
            loadtext = pygame.font.Font("./assets/Fonts/terminal.ttf", 20) #Creating a pygame font object
        except pygame.error as exc:
            error.missing_file_error(self.screen, exc)
            exit()
        load = loadtext.render("Loading...", False, (255, 255, 255)) #Creating the text using the pygame font object as previously mentioned
        pygame.Surface.fill(self.screen,(0,0,0)) #Clear the surface
        self.screen.blit(load,(self.size[0]/2,self.size[1]/2)) #Then blit the text
        pygame.display.flip() #Then render the blank frame with the text

    def startgame(self): #Function That will start the game once its called
        event.loadingscreen(self)
        game.game.startup(self)
        return None #Return to the main menu once complete

    def options(self): #Function that will open the options dialog once called
        pygame.Surface.fill(self.screen, (0, 0, 0))
        #This menu currently doesnt have anything, but stuff will be added once its needed
        return None #Return to the main menu once complete

    def about(self): #Function that will open the about menu once called
        pygame.Surface.fill(self.screen, (0, 0, 0))  #Clear the current screen so objects wont overlap
        try:
            titlefont = pygame.font.Font("./assets/Fonts/terminal.ttf",60) #Creating a pygame font object
            title = titlefont.render("DOCTRINE",False,(99,0,0)) #Using that font object to render the title text
            aboutfont = pygame.font.Font("./assets/Fonts/terminal.ttf",20) #Creating another font object thats a bit smaller
        except pygame.error as exc:
            error.missing_file_error(self.screen, exc)
            exit()

        about_line1 = aboutfont.render("DOCTRINE - A strategy game where you create and develop",False,(255,255,255)) #Then using that to render this text
        about_line1_5 = aboutfont.render("your own cult to take over the world!",False, (255,255,255)) #And this
        about_line2 = aboutfont.render("Scripting - Joshua Ampstead and Tim Charters",False,(255,255,255)) #And this...
        about_line3 = aboutfont.render("Art - Joshua Taylor",False,(255,255,255)) #And... Oh! you get the point
        about_line4 = aboutfont.render("Game written in Python3 using the Pygame library",False,(255,255,255)) #...
        self.screen.blit(title,(0,0)) #Actually blitting the text to the screen
        self.screen.blit(about_line1,(0,60))
        self.screen.blit(about_line1_5,(0,80))
        self.screen.blit(about_line2,(0,125))
        self.screen.blit(about_line3,(0,160))
        self.screen.blit(about_line4,(0,190))

        while True: #About main loop
            mouse = pygame.mouse.get_pos() #Getting the cursor position every time the loop restarts
            self.screen.blit(self.backbutton[0], self.backbutton[1]) #Blit the back button to the screen

            for event in pygame.event.get(): #Pygame event loop

                if event.type == pygame.QUIT: #If the user attempts to close the game, then quit
                    pygame.quit()
                    exit()

                if 10 + 200 > mouse[0] > 10 - 200 and 850 + 75 > mouse[1] > 850: #Checking if the button has been clicked
                    if event.type == pygame.MOUSEBUTTONDOWN: #Refer to the main.py script for information on how this works
                        self.screen.blit(self.backbutton_click[0],self.backbutton_click[1])
                        pygame.display.flip()
                        pygame.time.delay(100)
                        pygame.Surface.fill(self.screen, (0, 0, 0))
                        pygame.display.flip()
                        return None #Return to the main menu

            # Checking for when the mouse is over then button, if so then make it light up
            if 10 + 200 > mouse[0] > 10 - 200 and 850 + 75 > mouse[1] > 850:
                self.screen.blit(self.backbutton_hover[0], self.backbutton_hover[1])

            pygame.display.flip() #Render the current frame
        return None #Return to the main menu if the loop ends for any reason
    # methods
