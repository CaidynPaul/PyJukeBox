import pygame
import math
import pyaudio
pygame.init()

screen_width = 1280
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Audio Initialization
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100 # Hz

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT,
                channels=CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer=CHUNK)

def set_audio(data):
    stream.write(data)

def get_microphone_input_level():
    data = stream.read(CHUNK)
    rms = 0 # root mean squared
    for i in range(0,len(data),2):
        sample = int.from_bytes(data[i:i+2], byteorder = 'little', signed = True)
        rms += sample * sample
    rms = math.sqrt(rms / (CHUNK / 2))
    return rms


def draw_sine_wave(amplitude:float):
    points = []
    if amplitude > 10:
        for x in range(screen_width):
            y = screen_height / 2 + int(amplitude * math.sin(x * 0.02))
            points.append((x,y))
        
    else:
        points.append((0,screen_height/2))
        points.append((screen_width,screen_height/2))
    
    return pygame.draw.lines(screen,(255,255,255), False, points, 2)

running = True
amplitude = 100
while running:
    screen.fill((0,0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    amplitude_adjustment = get_microphone_input_level() / 20
    amplitude = max(10 , amplitude_adjustment)
    draw_sine_wave(amplitude)

    pygame.display.flip()