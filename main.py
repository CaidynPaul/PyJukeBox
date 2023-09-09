import pygame, pygame.mixer
import os #Import to load all songs in Songs folder

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("JukeBox!")
AppIcon = pygame.image.load("AppIcon.ico")
pygame.display.set_icon(AppIcon)

folder_path = 'Songs'
song_path_list = [] # Where the song paths are stored when app is launched

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

pos = 0 #Position in Queue

pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos])) #Play the First song in the queue when app is launched
pygame.mixer.Channel(0).set_volume(0.5) #Set volume to 0.5

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


running = True
muted = False

Clock = pygame.time.Clock()

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
                    if vol.get_volume() >= 1:
                        pass
                    else:
                        vol.set_volume(vol.get_volume()+0.05)

            if mx >= SCREEN_RECT.width//2 and mx <= (SCREEN_RECT.width//2) +64: #Volume Down
                if my >= 640 and my <= 640+64:
                    vol = pygame.mixer.Channel(0)
                    if vol.get_volume() <= 0:
                        pass
                    else:
                        vol.set_volume(vol.get_volume()-0.05)
            
            if mx >= SCREEN_RECT.width-64 and mx <= SCREEN_RECT.width: #Play
                if my >= SCREEN_RECT.height-64 and my <= SCREEN_RECT.height:
                    pygame.mixer.Channel(0).unpause()

            if mx >= SCREEN_RECT.width-128-10 and mx <= SCREEN_RECT.width-64:# Pause
                if my >= SCREEN_RECT.height-64 and my <= SCREEN_RECT.height:
                    pygame.mixer.Channel(0).pause()
            
            if mx >= 1196 and mx <= 1196+64:
                if my >= 50 and my <= 50+64:
                    os.startfile(folder_path)
            
            if mx >= SCREEN_RECT.left and mx <= SCREEN_RECT.left +64 and not muted: #Mute
                if my >=SCREEN_RECT.bottom-64 and my <= SCREEN_RECT.bottom:
                    pygame.mixer.Channel(0).set_volume(0)
                    muted = True
            
            if mx >= SCREEN_RECT.left and mx <= SCREEN_RECT.left +64 and muted: #Mute
                if my >=SCREEN_RECT.bottom-128 and my <= SCREEN_RECT.bottom-64:
                    pygame.mixer.Channel(0).set_volume(0.5)
                    muted = False


        
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
                if vol.get_volume() >= 1:
                    pass
                else:
                    vol.set_volume(vol.get_volume()+0.05)
            
            if e.key == pygame.K_DOWN: #Volume Down
                vol = pygame.mixer.Channel(0)
                if vol.get_volume() <= 0:
                    pass
                else:
                    vol.set_volume(vol.get_volume()-0.05)
            
            if e.key == pygame.K_o:
                os.startfile(folder_path)
            
            if e.key == pygame.K_m and not muted:
                pygame.mixer.Channel(0).set_volume(0)
                muted = True
            
            if e.key == pygame.K_COMMA and muted:
                pygame.mixer.Channel(0).set_volume(0.5)
                muted = False
                

    
    if pygame.mixer.get_busy() == False: # Play next song automatically
        pos += 1
        if pos >= len(song_path_list):
            pos = 0
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(song_path_list[pos]))
        
    
    pygame.draw.rect(SCREEN, ('#383838'), (720,606,64,64)) # Skip Button
    SCREEN.blit(skip_text,(720,608))

    pygame.draw.rect(SCREEN, ('#383838'), (560,606,64,64)) # Back Button
    SCREEN.blit(back_text,(560,608))

    current_song_text = Textfont.render((song_path_list[pos].removeprefix("Songs\\"))+f" @{pygame.mixer.Channel(0).get_volume()} Volume",True,('#ffffff')) #Render the current song that is being played
    SCREEN.blit(current_song_text,(0,0))

    pygame.draw.rect(SCREEN,('#383838'),(SCREEN_RECT.width//2,556,64,64)) #Volup
    SCREEN.blit(volup_text,(SCREEN_RECT.width//2 +15,556))

    pygame.draw.rect(SCREEN,('#383838'),(SCREEN_RECT.width//2,640,64,64))#Voldown
    SCREEN.blit(voldown_text,(SCREEN_RECT.width//2 +15,640+12))

    pygame.draw.rect(SCREEN,('#383838'),(SCREEN_RECT.width-128-10,SCREEN_RECT.height-64,64,64))#Pause
    SCREEN.blit(pause_icon,(SCREEN_RECT.width-128-10,SCREEN_RECT.height-64))

    pygame.draw.rect(SCREEN,('#383838'),(SCREEN_RECT.width-64,SCREEN_RECT.height-64,64,64))#Play
    SCREEN.blit(play_icon,(SCREEN_RECT.width-64,SCREEN_RECT.height-64))

    pygame.draw.rect(SCREEN,('#383838'),(1196,50,64,64))
    SCREEN.blit(open_icon,(1196,50))

    pygame.draw.rect(SCREEN,('#383838'),(SCREEN_RECT.left,SCREEN_RECT.bottom-64,64,64)) # Mute
    SCREEN.blit(mute_icon,(SCREEN_RECT.left,SCREEN_RECT.bottom-64))

    pygame.draw.rect(SCREEN,('#383838'),(SCREEN_RECT.left,SCREEN_RECT.bottom-128,64,64)) # Unmute
    SCREEN.blit(unmute_icon,(SCREEN_RECT.left,SCREEN_RECT.bottom-128))

    pygame.display.flip()
    Clock.tick(10)