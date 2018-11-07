#  "/home/illy/gdrive/aniproj/media_archive/illy.mp3"
import numpy as np
import pygame
import sys
import cv2
import time
from threading import Thread
import queue

pygame.mixer.init()
pygame.mixer.music.load('/home/illy/gdrive/aniproj/media_archive/illy.mp3')
pygame.mixer.music.play(0)
i=0
while True:
    i = 2
