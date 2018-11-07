from __future__ import print_function
import cv2

def frameBlender(path1, path2):
    alpha = 0.5
    # [load]
    src1 = cv2.imread(path1)
    src2 = cv2.imread(path2)
    # [load]
    if src1 is None: print("Error loading src1"); exit(-1)
    elif src2 is None: print("Error loading src2"); exit(-1)
    # resize
    size = (800, 800)
    frame1 = cv2.resize(src1, size)
    frame2 = cv2.resize(src2, size)
    # [blend_images]
    beta = (1.0 - alpha)
    dst = cv2.addWeighted(frame1, alpha, frame2, beta, 0.0)
    # [blend_images]
    # [display]
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    # [display]
    cv2.destroyAllWindows()

path1 = '/home/illy/gdrive/aniproj/media_archive/Ball.jpeg'
path2 = '/home/illy/gdrive/aniproj/media_archive/duffBeer.jpeg'

frameBlender(path1, path2)
