# Modules
import pygame
import os


# Search for files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
pygame.mixer.init()


# -----------------------------------
# Constants

# Screen size
WIDTH = 800
HEIGHT = 650

# Colors
BLACK = (0,0,0)


# -----------------------------------
# Displays the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# -----------------------------------
# Background 
# Checks to see if background image is present
try:
                                        # Enter background image here! 
    background_image = pygame.image.load("IMAGE HERE").convert()

    # If present, transforms the image to be able to fit in the game window
    background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    # If not, sets background to a single color
except Exception:
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((150,150,150)) # RGB Color Code
    print("Missing file for background...")


# -----------------------------------
# Music

# Checks if the audio for background music is present
try:
    # The mp3 file is a test to see if this code works
    pygame.mixer.music.load("AUDIO HERE") # <--- Enter the audio file (.mp3 / .ogg) here!

    # Plays the music (-1 plays it endlessly)
    pygame.mixer.music.play(-1)

    # Adjusts the volume
    pygame.mixer.music.set_volume(1)

# If not, plays silently
except Exception:
    print("Missing file for background music...")

# -----------------------------------
# Game Title 
pygame.display.set_caption("Solum")

# -----------------------------------
# Fonts
#           <CUSTOM>

# Checks if custom fonts are present
try:
    title_font = pygame.font.Font("FONT HERE", 90)
    option_font = pygame.font.Font("FONT HERE", 35)

# If not found, use a backup font 'Arial'
except FileNotFoundError:
    print("Font file(s) missing, using backup...")
    title_font = pygame.font.SysFont("Arial", 90)
    option_font = pygame.font.SysFont("Arial", 35)


#           <DEFAULT>
game_font = pygame.font.SysFont("Arial", 25) 


# -----------------------------------
#           <BUTTONS>
# Class
class Button():                                                 # Paste audios files for button hover / press (.wav files) !
    def __init__(self, x, y, width, height, text, color, button_hover = "AUDIO HERE", button_press = "AUDIO HERE"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color

        self.rect = pygame.Rect(x, y, width, height)

        # Lower the button's color by -35 on all numbers (x , y, z) AND reverts when no longer hovered
        self.hover = tuple(max(0,i-35) for i in color)

        # Set state for button hovering, set to False
        self.hovered = False


        # Checks if audio for hovering buttons is present
        try:
            self.sound = pygame.mixer.Sound(button_hover)
        # If not, use no audio
        except Exception:
            self.sound = None
            print("Missing audio file for button hover...")


        # Checks if audio for pressing buttons is present
        try:
            self.pressed = pygame.mixer.Sound(button_press)
        # If not, use no audio
        except Exception:
            self.pressed = None
            print("Missing audio file for button press...")



    # Function to create the button
    def draw(self, mouse_pos):

        # Checks if the mouse is hovering a button
        if self.rect.collidepoint(mouse_pos):

            # Triggers the 'self.hover' in the 'Button' class
            pygame.draw.rect(screen, self.hover, self.rect)


            # Plays the audio file when a button is hovered
            if not self.hovered:
                if self.sound:
                    self.sound.play()
                self.hovered = True


            # If mouse is not hovering on the button anymore
        else:
            pygame.draw.rect(screen, self.color, self.rect)

            # Resets state so audio file can be played again
            self.hovered = False

        # Creates a border around the button
        pygame.draw.rect(screen, BLACK, self.rect, 3)


        # Creates the text for button
        text_surface = option_font.render(self.text, True, (0,0,0))

        # Sets the text to the center of the button
        text_center = text_surface.get_rect(center=self.rect.center)

        # Displays on the game window
        screen.blit(text_surface, text_center)


    # Function to make the player able to interact with them
    def press(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.pressed:
                # Plays the audio "audio_press"
                self.pressed.play()
            return True
        return False
    

# -----------------------------------
# Variables for buttons

button_width = 250
button_height = 50

# -----------------------------------
# Creating buttons

# Main Menu buttons
playbutton = Button(WIDTH // 2 - button_width // 2, 285, button_width, button_height, "Play", (34, 156, 65))
settingsbutton = Button(WIDTH // 2 - button_width // 2, 357, button_width, button_height, "Settings", (150,150,150))
exitbutton = Button(WIDTH // 2 - button_width // 2,430, button_width, button_height, "Exit", (128, 9, 29))

# -----------------------------------
# Back buttons
backbutton2 = Button(WIDTH // 2 - button_width // 2,550, button_width, button_height, "Back", (150,150,150))

# -----------------------------------
# Others

# Mute Music
mutemusic = Button(WIDTH // 2 - button_width // 2,285, button_width, button_height, "Mute Music: OFF", (150,150,150))




# -----------------------------------
#           <GAME LOOP>

running = True

clock = pygame.time.Clock()

mainmenu = "Main Menu"
muted_music = False

while running:

    # Gets the position of the mouse
    mouse_pos = pygame.mouse.get_pos()


    # Allows the player to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            running = False


        # Checks for mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  

                # If the user clicks the 'Play' Button
                if mainmenu == "Main Menu":
                    if playbutton.press(mouse_pos):
                        print("Entering the game...")

                        # Add start screen here! ! !

                        mainmenu = "Solum Game"

                    elif settingsbutton.press(mouse_pos):
                        print("Displaying settings...")
                        mainmenu = "Settings"

                    # If the user clicks the 'Exit' Button
                    elif exitbutton.press(mouse_pos):
                        # Closes the game
                        print("Closing the game...")
                        running = False  


                # If the player is on 'Settings'
                elif mainmenu == "Settings":

                    # Back button to return to Main Menu
                    if backbutton2.press(mouse_pos):
                        print("Returning to Main Menu...")
                        mainmenu = "Main Menu"

                    # If the mute music button was pressed
                    elif mutemusic.press(mouse_pos):
                        muted_music = not muted_music

                        # If muted
                        if muted_music:

                            # Sets music volume to zero
                            pygame.mixer.music.set_volume(0)
                            print("Music has been muted")

                        # If unmuted / playing
                        else:
                            # Reverts the volume to normal
                            pygame.mixer.music.set_volume(1)
                            print("Music is now playing")    


    # Drawing

    # Creates the screen
    screen.blit(background, (0,0))

    # Main Menu screen
    if mainmenu == "Main Menu":
           
        # Title Font
        menu_title = title_font.render("< Solum >", True, (0, 105, 250))
        screen.blit(menu_title,((WIDTH-menu_title.get_width())//2, 75))
 
        # Creates the buttons on the game window
        playbutton.draw(mouse_pos)
        settingsbutton.draw(mouse_pos)
        exitbutton.draw(mouse_pos)


    # Game screen
    elif mainmenu == "Solum Game":
        screen.fill(BLACK)

        # This is where the game will start...
        start = game_font.render("Game here...", True, (255,255,255))
        screen.blit(start,((WIDTH-start.get_width())//2, 280))

    # Settings screen
    elif mainmenu == "Settings":
        # Title Font
        setting = title_font.render("< Settings >", True, (0, 105, 250))
        screen.blit(setting,((WIDTH-setting.get_width())//2, 75))

        # Changes the text of the 'mute music' button depending on current state
        # If muted
        if muted_music:
            mutemusic.text = "Music: OFF"
            mutemusic.color = (92, 92, 92)
        # If unmuted / playing
        else:
            mutemusic.text = "Music: ON"
            mutemusic.color = (150,150,150)

        # Buttons (In 'Settings')
        backbutton2.draw(mouse_pos)
        mutemusic.draw(mouse_pos)

    # --------------------------------------------------------------------------------
    # NOTE !!
    # !!! NOTHING FOR 'EXIT' AS THE GAME IS CLOSED WHEN THAT BUTTON IS PRESSED !!!
    # --------------------------------------------------------------------------------


    pygame.display.update()
    # FPS
    clock.tick(60)

pygame.quit()