#-----------------------------------module
import pygame
#-----------------------------------------
##########################################
##########################################
#################################### main program
def playSong(value='play'):
    if value=='play':
        pygame.mixer.init()
        pygame.mixer.music.load('external_modules/music/Music relax Musiceto (10).mp3')
        pygame.mixer.music.play(loops=2)
    else:
        pygame.mixer.music.stop()