import numpy as np
import pygame
import sys
import cv2
import time
from threading import Thread
import queue
import audio_signal_energy

def basic_music_player(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(0) 


def playVid_pygmae(path, audioPath, duffTime):
    # initiate
    first = True
    windowSize = [1700, 1000]  # desired display window size
    duffPath = '/home/illy/gdrive/aniproj/media_archive/duffBeer.jpeg'
    duffFrame = cv2.imread(duffPath)
    # path = "/home/illy/gdrive/aniproj/codes/python/pygame_tests/sample.mkv"  # path to vid file
    vid = cv2.VideoCapture(path)  # read file with opencv
    fps = vid.get(cv2.CAP_PROP_FPS)  # find FPS

    # set display size, and set ratio for resizing video
    ret, frame = vid.read()
    frame = np.rot90(frame)
    frameSize = frame.shape
    if windowSize[0]/frameSize[0] < windowSize[1]/frameSize[1]:
        frameSizeRatio = windowSize[0]/frameSize[0]
    else:
        frameSizeRatio = windowSize[1]/frameSize[1]
    # set frme location in midle of the display 
    locx = int((windowSize[0]-frameSize[0]*frameSizeRatio)/2)
    locy = int((windowSize[1]-frameSize[1]*frameSizeRatio)/2)
    loc = (locx,locy)
    # initiate pygame, make display window, initiate game clock
    pygame.init()
    pygame.display.set_caption("OpenCV video stream on Pygame")
    screen = pygame.display.set_mode(windowSize)
    gameClock = pygame.time.Clock()
    # play music
    basic_music_player(audioPath)
    sTime = time.time() # count time from beginning of display 
    # main loop 
    i = 1
    while True:
        ## exit upon closing the display window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ret, frame = vid.read()
        # make sure has frame
        if not ret:
            break
        frame = cv2.resize(frame, (loc), fx=frameSizeRatio, fy=frameSizeRatio)  # resize frame
        if duffTime[int(i*44100/fps)]:
            if first:
                frameSize = frame.shape
                duffFrame = cv2.resize(duffFrame, (frameSize[1], frameSize[0]))
                first = False
            frame = cv2.addWeighted(frame, 1, duffFrame, 0.8, 0.0)
        # display
        # cv2 works with BGR while pygame with RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # for some resone the frame is rotated and fliped horizontally
        frame = np.rot90(frame)
        screen.fill([0, 0, 0])  # a black blink between frames
        frame = pygame.surfarray.make_surface(frame)  # pygame display frame
        screen.blit(frame, (loc))  # update disply frame
        pygame.display.flip()  # display new frame
        # control FPS. a more acurate, yet expensive method
        gameClock.tick_busy_loop(fps)
        if not q.empty():
            print('got')
            j = q.get()
            print(j)
        i += 1

    print(time.time()-sTime) # calculate video playtime
# # #

def basic_producer():
    i = 0
    while True:
        if i==20 or i==5:
            q.put(i)
        i +=1
        if i > 100:
            exit()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

q = queue.Queue()
path = "/home/illy/gdrive/aniproj/codes/python/pygame_tests/sample.mkv"  # path to vid file
audioPath = '/home/illy/gdrive/aniproj/media_archive/BASS_DRUMS.mp3'
# audioPath = '/home/illy/gdrive/aniproj/media_archive/50_BPM_Metronome.mp3'
duffPath = '/home/illy/gdrive/aniproj/media_archive/duffBeer.jpeg'
duffTime = audio_signal_energy.audio_signal_energy(audioPath)
t = Thread(target=basic_producer, args=())
t.daemon = True
t.start()
playVid_pygmae(path, audioPath, duffTime)
