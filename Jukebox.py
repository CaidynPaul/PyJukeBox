__author__ = "Caidyn Paul"
__copyright__ = "Copyright (C) 2023 Caidyn Paul"
__license__ = "MIT Licence"
__version__ = "1.0.8"

# import resource
import pygame, pygame.mixer
import os #Import to load all songs in Songs folder
import sys
import json
from tkinter import *
from tkinter import colorchooser

pygame.init()
pygame.mixer.init()

f = open("config.json",'r')
data = json.load(f)
f.close()

button_color = pygame.Color(data.get('button_color'))

def error5():
    pygame.display.set_caption("JukeBox!")
    AppIcon = pygame.image.load("AppIcon.ico")
    pygame.display.set_icon(AppIcon)

    SCREEN = pygame.display.set_mode((300,300))
    SCREEN_RECT = SCREEN.get_rect()

    running = True

    text = pygame.font.SysFont("Arial",16,True)
    errorMessage = text.render("Try adding a Song to the Songs Folder",True,('#ffffff'))

    open_icon = pygame.image.load('Folder.png')
    open_icon = pygame.transform.scale(open_icon,(64,64))

    while running:
        SCREEN.fill(('#000000'))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
            
                if mx >= 118 and mx <= 118+64: #Folder
                    if my >= 200 and my <= 200+64:
                        os.startfile('Songs')
                

        pygame.draw.rect(SCREEN,button_color,(118,200,64,64)) #Folder
        SCREEN.blit(open_icon,(118,200))
        SCREEN.blit(errorMessage,(SCREEN_RECT.left+30,SCREEN_RECT.centery))
        pygame.display.flip()

def Jukebox() -> None:
    pygame.display.set_caption("JukeBox!")
    AppIcon = pygame.image.load("AppIcon.ico")
    pygame.display.set_icon(AppIcon)

    folder_path = 'Songs'
    song_path_list = [] # Where the song paths are stored when app is launched

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


    for songname in os.listdir(folder_path): #Load all songs into above list
        song_path = os.path.join(folder_path,songname)

        if os.path.isfile(song_path):
            song_path_list.append(song_path)

    def Bubble(arr):
            n =  len(arr)
            swapped = True
            while n > 0 and swapped == True:
                swapped = False
                n -= 1
            
                for i in range(n):
                    if arr[i] > arr[i+1]:
                        arr[i],arr[i+1]=arr[i+1],arr[i]
                        swapped = True
            return arr

    song_path_list = Bubble(song_path_list)

    Clock = pygame.time.Clock()

    pos = 0 #Position in Queue

    try:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos])) #Play the First song in the queue when app is launched
        pygame.mixer.Channel(0).set_volume(0.3) #Set volume to 0.1
    except IndexError:
        error5()
        sys.exit()

    SCREEN = pygame.display.set_mode((1280,720)) #Enable Screen

    SCREEN_RECT = SCREEN.get_rect()

    image = pygame.image.load("background.png").convert() #Add Background image
    image = pygame.transform.scale(image,(1280,720)) #Convert to 1280x720

    Symfont = pygame.font.SysFont("Consolas",60)# Set Symbol Font

    skip_text = Symfont.render(">>",True,('#ffffff')) #Render Skip button text
    back_text = Symfont.render("<<",True,('#ffffff'))# Render Back button text

    volup_text = Symfont.render("^",True,('#ffffff'))# Render Volume up button text
    voldown_text = Symfont.render("v",True,('#ffffff'))# Render Volume down text

    Textfont = pygame.font.SysFont("Helvetica",25)# Set Font for text
    current_song_text = Textfont.render(song_path_list[pos],True,('#ffffff'))# Render the name of the current song playing
    current_song_text_rect = current_song_text.get_rect()

    pause_icon = pygame.image.load('Pause.png')
    pause_icon = pygame.transform.scale(pause_icon,(64,64))

    play_icon = pygame.image.load('Play.png')
    play_icon = pygame.transform.scale(play_icon,(64,64))

    open_icon = pygame.image.load('Folder.png')
    open_icon = pygame.transform.scale(open_icon,(64,64))

    mute_icon = pygame.image.load('Mute.png')
    mute_icon = pygame.transform.scale(mute_icon,(64,64))

    unmute_icon = pygame.image.load('Unmute.png')
    unmute_icon = pygame.transform.scale(unmute_icon,(64,64))

    reload_icon = pygame.image.load('Reload.png')
    reload_icon = pygame.transform.scale(reload_icon,(64,64))    


    running = True
    muted = False

    previous_vol = 0
    
    while running:
        SCREEN.blit(image,(0,0))
        # SCREEN.fill(('#00000000'))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
            if e.type == pygame.MOUSEBUTTONDOWN: #Mouse controls
                mx,my = pygame.mouse.get_pos()

                if mx >= 720 and mx <= 720+64: #Skip Button
                    if my >= 606 and my <= 606+64:
                        if pos == len(song_path_list)-1:
                            pygame.mixer.stop()
                            pos = 0
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
                        else:
                            pygame.mixer.stop()
                            pos += 1
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
                
                if mx >= 560 and mx <= 560+64: # Back Button
                    if my >= 606 and my <= 606+64:
                        if pos == 0:
                            pygame.mixer.stop()
                            pos = len(song_path_list)-1
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
                        else:
                            pygame.mixer.stop()
                            pos -= 1
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))

                if mx >= SCREEN_RECT.width//2 and mx <= (SCREEN_RECT.width//2) +64: #Volume Up
                    if my >= 556 and my <= 556+64:
                        vol = pygame.mixer.Channel(0)
                        if vol.get_volume() >= 0.7:
                            pass
                        else:
                            vol.set_volume(vol.get_volume()+0.01)

                if mx >= SCREEN_RECT.width//2 and mx <= (SCREEN_RECT.width//2) +64: #Volume Down
                    if my >= 640 and my <= 640+64:
                        vol = pygame.mixer.Channel(0)
                        if vol.get_volume() <= 0:
                            pass
                        else:
                            vol.set_volume(vol.get_volume()-0.01)
                
                if mx >= SCREEN_RECT.width-64 and mx <= SCREEN_RECT.width: #Play
                    if my >= SCREEN_RECT.height-64 and my <= SCREEN_RECT.height:
                        pygame.mixer.Channel(0).unpause()

                if mx >= SCREEN_RECT.width-128-10 and mx <= SCREEN_RECT.width-64:# Pause
                    if my >= SCREEN_RECT.height-64 and my <= SCREEN_RECT.height:
                        pygame.mixer.Channel(0).pause()
                
                if mx >= 1156 and mx <= 1156+64: #Folder
                    if my >= 90 and my <= 90+64:
                        os.startfile(folder_path)
                
                if mx >= SCREEN_RECT.left and mx <= SCREEN_RECT.left +64 and not muted: #Mute
                    if my >=SCREEN_RECT.bottom-64 and my <= SCREEN_RECT.bottom:
                        previous_vol = pygame.mixer.Channel(0).get_volume()
                        pygame.mixer.Channel(0).set_volume(0)
                        muted = True
                
                if mx >= SCREEN_RECT.left and mx <= SCREEN_RECT.left +64 and muted: #UnMute
                    if my >=SCREEN_RECT.bottom-128 and my <= SCREEN_RECT.bottom-64:
                        pygame.mixer.Channel(0).set_volume(previous_vol)
                        muted = False

                if mx >= 60 and mx <= 60+64:
                    if my >= 90 and my <= 90+64:
                        os.system("Reload.bat")
                    
            
            if e.type == pygame.KEYDOWN:  #Keyboard Controls
                if e.key == pygame.K_n or e.key == pygame.K_RIGHT:# Next Button KB
                    if pos == len(song_path_list)-1:
                        pygame.mixer.stop()
                        pos = 0
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
                    else:
                        pygame.mixer.stop()
                        pos += 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
                if e.key ==  pygame.K_b or e.key == pygame.K_LEFT:# Back Button KB
                    if pos == 0:
                        pygame.mixer.stop()
                        pos = len(song_path_list)-1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
                    else:
                        pygame.mixer.stop()
                        pos -= 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))

                if e.key == pygame.K_c: #Pause button
                    pygame.mixer.pause()                    
                
                if e.key == pygame.K_v:# Play Button
                    pygame.mixer.unpause()
                
                if e.key == pygame.K_UP: #Volume UP
                    vol = pygame.mixer.Channel(0)
                    if vol.get_volume() >= 0.7:
                        pass
                    else:
                        vol.set_volume(vol.get_volume()+0.01)
                
                if e.key == pygame.K_DOWN: #Volume Down
                    vol = pygame.mixer.Channel(0)
                    if vol.get_volume() <= 0:
                        pass
                    else:
                        vol.set_volume(vol.get_volume()-0.01)
                
                if e.key == pygame.K_o:
                    os.startfile(folder_path)
                
                if e.key == pygame.K_m and not muted:
                    previous_vol = pygame.mixer.Channel(0).get_volume()
                    pygame.mixer.Channel(0).set_volume(0)
                    muted = True
                
                if e.key == pygame.K_COMMA and muted:
                    pygame.mixer.Channel(0).set_volume(previous_vol)
                    muted = False
                
                if e.key == pygame.K_r:
                    os.system("Launcher.bat")                  

        if pygame.mixer.get_busy() == False: # Play next song automatically
            pos += 1
            if pos >= len(song_path_list):
                pos = 0
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
            
        
        pygame.draw.rect(SCREEN, (button_color), (720,606,64,64)) # Skip Button
        SCREEN.blit(skip_text,(720,608))

        pygame.draw.rect(SCREEN, (button_color), (560,606,64,64)) # Back Button
        SCREEN.blit(back_text,(560,608))

        current_song_text = Textfont.render((song_path_list[pos].removeprefix("Songs\\"))+f" @{pygame.mixer.Channel(0).get_volume()} Volume",True,('#ffffff')) #Render the current song that is being played
        SCREEN.blit(current_song_text,(0,0))

        pygame.draw.rect(SCREEN,(button_color),(SCREEN_RECT.width//2,556,64,64)) #Volup
        SCREEN.blit(volup_text,(SCREEN_RECT.width//2 +15,556))

        pygame.draw.rect(SCREEN,(button_color),(SCREEN_RECT.width//2,640,64,64))#Voldown
        SCREEN.blit(voldown_text,(SCREEN_RECT.width//2 +15,640+12))

        pygame.draw.rect(SCREEN,(button_color),(SCREEN_RECT.width-128-10,SCREEN_RECT.height-64,64,64))#Pause
        SCREEN.blit(pause_icon,(SCREEN_RECT.width-128-10,SCREEN_RECT.height-64))

        pygame.draw.rect(SCREEN,(button_color),(SCREEN_RECT.width-64,SCREEN_RECT.height-64,64,64))#Play
        SCREEN.blit(play_icon,(SCREEN_RECT.width-64,SCREEN_RECT.height-64))

        pygame.draw.rect(SCREEN,(button_color),(1156,90,64,64)) #Folder
        SCREEN.blit(open_icon,(1156,90))

        pygame.draw.rect(SCREEN,(button_color),(SCREEN_RECT.left,SCREEN_RECT.bottom-64,64,64)) # Mute
        SCREEN.blit(mute_icon,(SCREEN_RECT.left,SCREEN_RECT.bottom-64))

        pygame.draw.rect(SCREEN,(button_color),(SCREEN_RECT.left,SCREEN_RECT.bottom-128,64,64)) # Unmute
        SCREEN.blit(unmute_icon,(SCREEN_RECT.left,SCREEN_RECT.bottom-128))

        pygame.draw.rect(SCREEN,(button_color),(60,90,64,64)) # Reload
        SCREEN.blit(reload_icon,(60,90))

        pygame.display.flip()
        Clock.tick(10)

def configScreen():
    def pick_color():
        # Open color chooser dialog
        color_code = colorchooser.askcolor()[1]

        # Update the button color and save to config.json
        update_config(color_code)
        update_label(color_code)

    def update_config(color):
        # Load existing config or create a new one
        try:
            with open('config.json', 'r') as file:
                config = json.load(file)
        except FileNotFoundError:
            config = {"'button_color':'#1e2569'"}

        # Update the button color in the config
        config['button_color'] = color

        # Save the updated config to config.json
        with open('config.json', 'w') as file:
            json.dump(config, file, indent=4)
        
    def update_label(color):
        # Update the label's background color
        color_label.config(bg=color)
    
    def close_and_reload():
        root.destroy()

        os.system("Reload.bat")

    # Create the main window
    root = Tk()
    root.title("Color Picker")
    root.geometry("150x150")

    # Create a button to pick a color
    color_button = Button(root, text="Pick a Color", command=pick_color)
    color_button.pack(pady=20)

    color_label = Label(root, text = "Current Colour",width = 150,relief="solid")
    color_label.pack()

    close_button = Button(root, text="Close", command=root.destroy)
    close_button.pack()

    close_and_reload_button = Button(root, text="Close and Reload", command=close_and_reload)
    close_and_reload_button.pack()

    # Run the Tkinter event loop
    root.mainloop()

def titleChoice():
    pygame.init()
    pygame.display.set_caption("JukeBox!")
    AppIcon = pygame.image.load("AppIcon.ico")
    pygame.display.set_icon(AppIcon)

    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    SCREEN_RECT = SCREEN.get_rect()

    font = pygame.font.Font("Ubuntu.ttf", 100)

    # Button 1
    button1_text = font.render("Play", True, ('#d1d1d1'))
    button1_rect = button1_text.get_rect(center=(SCREEN_RECT.centerx, SCREEN_RECT.centery - 100))
    button1_hover = False

    # Button 2
    button2_text = font.render("Config", True, ('#d1d1d1'))
    button2_rect = button2_text.get_rect(center=(SCREEN_RECT.centerx, SCREEN_RECT.centery + 100))
    button2_hover = False

    clock = pygame.time.Clock()
    running = True

    while running:
        SCREEN.fill((10, 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if button1_rect.collidepoint(mx,my):
                    Jukebox()
                    running = False
                    sys.quit()
                
                if button2_rect.collidepoint(mx,my):
                    configScreen()

        # Check for button hover
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button1_hover = button1_rect.collidepoint(mouse_x, mouse_y)
        button2_hover = button2_rect.collidepoint(mouse_x, mouse_y)

        # Draw buttons with hover effect
        pygame.draw.rect(SCREEN, ('#2e2e2e') if button1_hover else ('#3a3a3a'), button1_rect,0,8)
        pygame.draw.rect(SCREEN, ('#2e2e2e') if button2_hover else ('#3a3a3a'), button2_rect,0,8)

        SCREEN.blit(button1_text, button1_rect)
        SCREEN.blit(button2_text, button2_rect)

        pygame.display.flip()
        clock.tick(60)

def titleScreen() -> None:
    pygame.display.set_caption("JukeBox!")
    AppIcon = pygame.image.load("AppIcon.ico")
    pygame.display.set_icon(AppIcon)

    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    SCREEN_RECT = SCREEN.get_rect()

    font = pygame.font.Font("Ubuntu.ttf", 200)
    text = font.render("Jukebox", True, (10, 10, 10))
    text_rect = text.get_rect(center=SCREEN_RECT.center)

    clock = pygame.time.Clock()
    running = True

    reveal_color = (button_color.r, button_color.g, button_color.b)  # Color for the reveal effect
    reveal_width = 0  # Initial width of the reveal effect

    while running:
        SCREEN.fill((10, 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Add color-revealing animation effect
        pygame.draw.rect(SCREEN, reveal_color, (0, 0, reveal_width, SCREEN_HEIGHT))
        reveal_width += 10  # Adjust the speed of the reveal effect

        # Draw the text on top
        SCREEN.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

        if reveal_width >= SCREEN_WIDTH:
            break  # Exit the loop once the screen is fully revealed
    
    titleChoice()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    titleScreen()
    
else:
    os.system("Reload.bat")