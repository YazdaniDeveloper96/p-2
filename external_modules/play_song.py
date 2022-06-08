#-----------------------------------module
import pygame     # ok
#-----------------------------------------
##########################################
##########################################
#################################### main program
def playSong(value='play'):
    if value=='play':
        pygame.mixer.init()
        pygame.mixer.music.load('external_modules/music/0bikalam download1music.ir (1).mp3')
        pygame.mixer.music.play(loops=2)
    else:
        pygame.mixer.music.stop()