__author__ = "Caidyn Paul"
__copyright__ = "Copyright (C) 2023 Caidyn Paul"
__license__ = "MIT Licence"
__version__ = "1.0.8"

# import resource
import pygame, pygame.mixer
import os #Import to load all songs in Songs folder
import sys
pygame.init()
pygame.mixer.init()

button_color = pygame.Color('#38374f')

def error5():
    pygame.display.set_caption("JukeBox!")
    AppIcon = pygame.image.load("AppIcon.ico")
    pygame.display.set_icon(AppIcon)

    SCREEN = pygame.display.set_mode((400,400))
    SCREEN_RECT = SCREEN.get_rect()

    background = pygame.image.load('Error_background.png')
    background_rect = background.get_rect()

    running = True

    text = pygame.font.SysFont("Arial",24,True)
    errorMessage = text.render("Try adding a Song to the Songs Folder",True,('#ffffff'))
    errorMessage_rect = errorMessage.get_rect(center = SCREEN_RECT.center)

    open_icon = pygame.image.load('Folder.png')
    open_icon = pygame.transform.scale(open_icon,(64,64))
    open_icon_rect = open_icon.get_rect(center = SCREEN_RECT.center,w = 64 , h = 64)
    open_icon_rect.y += 64

    reload_icon = pygame.image.load('Reload.png')
    reload_icon = pygame.transform.scale(reload_icon,(64,64))    
    reload_icon_rect = reload_icon.get_rect(center = SCREEN_RECT.center,w = 64,h = 64)
    reload_icon_rect.y -= 64

    
    while running:
        SCREEN.fill(('#000000'))
        SCREEN.blit(background,background_rect)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
            
                if open_icon_rect.collidepoint(mx,my):
                    os.startfile('Songs')
                
                if reload_icon_rect.collidepoint(mx,my): # Reload
                    os.system("Reload.bat")
                
        pygame.draw.rect(SCREEN,(button_color),reload_icon_rect) # Reload
        SCREEN.blit(reload_icon,reload_icon_rect)
                

        pygame.draw.rect(SCREEN,button_color,open_icon_rect) #Folder
        SCREEN.blit(open_icon,open_icon_rect)
        SCREEN.blit(errorMessage,errorMessage_rect)
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
    skip_text_rect = skip_text.get_rect(x = 720, y = 608, w = 64, h = 64)

    back_text = Symfont.render("<<",True,('#ffffff'))# Render Back button text
    back_text_rect = back_text.get_rect(x = 560,y = 606, w = 64, h = 64)

    volup_text = Symfont.render("^",True,('#ffffff'))# Render Volume up button text
    volup_text_rect = volup_text.get_rect(x = SCREEN_RECT.width//2,y = 556,w = 64,h = 64)

    voldown_text = Symfont.render("v",True,('#ffffff'))# Render Volume down text
    voldown_text_rect = voldown_text.get_rect(x = SCREEN_RECT.width//2,y = 640,w = 64, h = 64)

    Textfont = pygame.font.SysFont("Helvetica",25)# Set Font for text
    current_song_text = Textfont.render(song_path_list[pos],True,('#ffffff'))# Render the name of the current song playing
    current_song_text_rect = current_song_text.get_rect()

    pause_icon = pygame.image.load('Pause.png')
    pause_icon = pygame.transform.scale(pause_icon,(64,64))
    pause_icon_rect = pause_icon.get_rect(x = SCREEN_RECT.width, y = SCREEN_RECT.height,w = 64,h = 64)
    pause_icon_rect.x -= 128+10
    pause_icon_rect.y -= 64

    play_icon = pygame.image.load('Play.png')
    play_icon = pygame.transform.scale(play_icon,(64,64))
    play_icon_rect = play_icon.get_rect(x = SCREEN_RECT.width, y = SCREEN_RECT.height,w = 64,h = 64)
    play_icon_rect.x -= 64
    play_icon_rect.y -= 64

    open_icon = pygame.image.load('Folder.png')
    open_icon = pygame.transform.scale(open_icon,(64,64))
    open_icon_rect = open_icon.get_rect(x = 1156,y = 90,w = 64,h = 64)

    mute_icon = pygame.image.load('Mute.png')
    mute_icon = pygame.transform.scale(mute_icon,(64,64))
    mute_icon_rect = mute_icon.get_rect(bottomleft = SCREEN_RECT.bottomleft, w = 64 , h = 64)

    unmute_icon = pygame.image.load('Unmute.png')
    unmute_icon = pygame.transform.scale(unmute_icon,(64,64))
    unmute_icon_rect = unmute_icon.get_rect(bottomleft = SCREEN_RECT.bottomleft,w = 64,h = 64)
    unmute_icon_rect.y -= 64

    reload_icon = pygame.image.load('Reload.png')
    reload_icon = pygame.transform.scale(reload_icon,(64,64))    
    reload_icon_rect = reload_icon.get_rect(x = 60,y = 90,w = 64,h = 64)

    running = True
    muted = False

    previous_vol = 0
    volume_increment = 0.01
    
    while running:
        SCREEN.blit(image,(0,0))
        # SCREEN.fill(('#00000000'))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
            if e.type == pygame.MOUSEBUTTONDOWN: #Mouse controls
                mx,my = pygame.mouse.get_pos()

                if skip_text_rect.collidepoint(mx,my): # next
                    if pos == len(song_path_list)-1:
                        pygame.mixer.stop()
                        pos = 0
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
                    else:
                        pygame.mixer.stop()
                        pos += 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
            
                if back_text_rect.collidepoint(mx,my): # back
                    if pos == 0:
                        pygame.mixer.stop()
                        pos = len(song_path_list)-1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
                    else:
                        pygame.mixer.stop()
                        pos -= 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))

                if volup_text_rect.collidepoint(mx,my): #volume up
                    vol = pygame.mixer.Channel(0)
                    if vol.get_volume() >= 0.7:
                        pass
                    else:
                        vol.set_volume(vol.get_volume()+volume_increment)

                if voldown_text_rect.collidepoint(mx,my): # volume down
                    vol = pygame.mixer.Channel(0)
                    if vol.get_volume() <= 0:
                        pass
                    else:
                        vol.set_volume(vol.get_volume()-volume_increment)
                
                if play_icon_rect.collidepoint(mx,my): # Unpause / Play
                    pygame.mixer.Channel(0).unpause()

                if pause_icon_rect.collidepoint(mx,my): # Pause
                    pygame.mixer.Channel(0).pause()
                
                if open_icon_rect.collidepoint(mx,my): #Folder
                    os.startfile(folder_path)
                
                if mute_icon_rect.collidepoint(mx,my): #Mute
                    previous_vol = pygame.mixer.Channel(0).get_volume()
                    pygame.mixer.Channel(0).set_volume(0)
                    muted = True
                
                if unmute_icon_rect.collidepoint(mx,my): #Unmute
                    pygame.mixer.Channel(0).set_volume(previous_vol)
                    muted = False

                if reload_icon_rect.collidepoint(mx,my): # Reload
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
            
        
        pygame.draw.rect(SCREEN, (button_color), skip_text_rect) # Skip Button
        SCREEN.blit(skip_text,skip_text_rect)

        pygame.draw.rect(SCREEN, (button_color), back_text_rect) # Back Button
        SCREEN.blit(back_text,back_text_rect)

        current_song_text = Textfont.render((song_path_list[pos].removeprefix("Songs\\"))+f" @{pygame.mixer.Channel(0).get_volume()} Volume",True,('#ffffff')) #Render the current song that is being played
        SCREEN.blit(current_song_text,(0,0))

        pygame.draw.rect(SCREEN,(button_color),(volup_text_rect)) #Volup
        SCREEN.blit(volup_text,(volup_text_rect.x+15,volup_text_rect.y, volup_text_rect.w,volup_text_rect.h))

        pygame.draw.rect(SCREEN,(button_color),(voldown_text_rect))#Voldown
        SCREEN.blit(voldown_text,(voldown_text_rect.x + 15, voldown_text_rect.y,voldown_text_rect.w,voldown_text_rect.h))

        pygame.draw.rect(SCREEN,(button_color),(pause_icon_rect))#Pause
        SCREEN.blit(pause_icon,(pause_icon_rect))

        pygame.draw.rect(SCREEN,(button_color),(play_icon_rect))#Play
        SCREEN.blit(play_icon,(play_icon_rect))

        pygame.draw.rect(SCREEN,(button_color),(open_icon_rect)) #Folder
        SCREEN.blit(open_icon,open_icon_rect)

        pygame.draw.rect(SCREEN,(button_color),(mute_icon_rect)) # Mute
        SCREEN.blit(mute_icon,(mute_icon_rect))

        pygame.draw.rect(SCREEN,(button_color),(unmute_icon_rect)) # Unmute
        SCREEN.blit(unmute_icon,(unmute_icon_rect))

        pygame.draw.rect(SCREEN,(button_color),reload_icon_rect) # Reload
        SCREEN.blit(reload_icon,reload_icon_rect)

        pygame.display.flip()
        Clock.tick(10)


if __name__ == '__main__':
    error5()
    
else:
    os.system("Reload.bat")