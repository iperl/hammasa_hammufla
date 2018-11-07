import numpy as np
import pygame
import sys
import cv2
import time
from threading import Thread
import queue
import audio_signal_energy

class bucket:
    def __init__(self, clipPath, interval=np.ndarray, frameCounter=0):
        Path = clipPath
        clip = cv2.VideoCapture(path)
        length = int(clip.get(cv2.CAP_PROP_FRAME_COUNT))
        self.clip = clip
        self.interval = np.ones(length)
        self.length = length
        self.frameCounter = frameCounter
##################################################################
def basic_music_player(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(0)    
##################################################################
def frameBlender(frame, buckets):
    newBuckets = []
    i=0
    for bucket in buckets:
        bucketFrame = bucket.clip.read()
        frame = cv2.addWeighted(frame, 1, bucketFrame, bucket.interval[bucket.frameCounter], 0.0)
        bucket.frameCounter += 1
        if framCounter < len(interval):
            newBuckets.append(bucket)
        i+=1
    return(frame, newBuckets) # not sure it works. chack!
        
    
##################################################################
def hamasa_vid_player(firstBucket, audioPath):
    # initiate
    buckets = []
    frameCount = 1
    clip = firstBucket.clip
    fps = 24
    windowSize = [1700, 1000]  # desired display window size
    loc = (0,0)
    # initiate pygame, make display window, initiate game clock
    pygame.init()
    pygame.display.set_caption("Hamasa Hamufla")
    screen = pygame.display.set_mode(windowSize)
    gameClock = pygame.time.Clock()
    # play music
    basic_music_player(audioPath)
    sTime = time.time() # count time from beginning of display 
    # main loop 
    while True:
        # exit upon closing the display window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # read frame, make sure retrived
        ret, frame = clip.read()
        if not ret:
            break
        if frameCount == bucket.length:
            frameCount = 0 
            clip.set(cv2.CAP_PROP_POS_FRAMES, 0)
        if buckets:
            frame, buckets = frameBlender(frame, buckets)
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
            print('there is a new bucket')
            bucket = q.get()
            print('got a new bucket')
            buckets.append(bucket)
            frameCount = 0
        frameCount += 1

################################################################
def video_feeder():
    path = "/home/illy/gdrive/aniproj/codes/python/pygame_tests/sample.mkv"
    Qbuck = bucket(path)
    sTime = time.time()
    while True:
        time.sleep(1)
        if time.time() > sTime+5:
            q.put(Qbuck)
            return
################################################################
################################################################
if __name__ == "__main__":
    q = queue.Queue()
    path = "/home/illy/gdrive/aniproj/codes/python/pygame_tests/sample.mkv"
    audioPath = '/home/illy/gdrive/aniproj/media_archive/BASS_DRUMS.mp3'
    buck = bucket(path)
    t = Thread(target=video_feeder, args=())
    t.daemon = True
    t.start()
    hamasa_vid_player(buck, audioPath)