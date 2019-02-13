import cv2
import time
import winsound as ws

beep_flag = 0
fname = 'kimpurple.jpg'
tic = time.time()

original = cv2.imread(fname, cv2.IMREAD_COLOR)
resize = cv2.resize(original, dsize = (600, 900), interpolation=cv2.INTER_AREA)
cv2.imshow('Original', resize)

while True:
    toc = time.time()
    t = toc - tic
    k = cv2.waitKey(1)

    if k == ord('q'):
        beep_flag = 1
    elif t > 7.5 and beep_flag == 0:
        ws.Beep(2000, 3000)
    elif t > 20:
        cv2.destroyAllWindow()
