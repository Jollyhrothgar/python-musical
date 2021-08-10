from . import encode
import pygame
import numpy
import sounddevice as sd


def play(data, rate=44100):
    ''' Send audio array to pygame for playback
    '''
    pygame.mixer.init(rate, -16, 1, 1024)
    sound = pygame.sndarray.make_sound(encode.as_int16(data))
    length = sound.get_length()
    sound.play()
    # Blocks return until sound has completed.
    pygame.time.wait(int(length * 1000))
    pygame.mixer.quit()

def play_sd(data, rate=44100):
    sd.play(data, rate)
    sd.wait()