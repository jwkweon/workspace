import cv2
import numpy as np
import os
from scipy.misc import imread, imsave
import argparse
from sklearn.cluster import KMeans
from PIL import Image


def random_crop(img, rand, height, width):      #rand 1 : random 모드 이미지 내에서 랜덤하게 crop
    if rand == 1:
        randint = np.random.randint(0, 300, size=2)
        x, y = randint[0], randint[1]
        crop_img = img[x : x + 400 , y : y + 400]
    else:                                       #rand !1 : 이미지의 4분의 1(오른쪽 아래 이미지) crop
        x, y = width, height
        crop_img = img[x // 2 :  x, y // 2 : y]

    return crop_img

def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    return bar

def image_color_cluster(image, k = 4):
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    color_list = []

    clt = KMeans(n_clusters = k)
    clt.fit(image)

    hist = centroid_histogram(clt)
    bar = plot_colors(hist, clt.cluster_centers_)

    for i in range (300):
        if i == 0:
            temp_R=bar[0][i][0]
            temp_G=bar[0][i][1]
            temp_B=bar[0][i][2]
            #print(bar[0][i][:])
            color_list.append(bar[0][i][:])
        if temp_R != bar[0][i][0] or temp_G != bar[0][i][1] or temp_B != bar[0][i][2] and i != 0:
            temp_R=bar[0][i][0]
            temp_G=bar[0][i][1]
            temp_B=bar[0][i][2]
            #print(bar[0][i][:])
            color_list.append(bar[0][i][:])

    return color_list

def color2gray(img):
    img_Gray = img.copy()
    gray_img = img.sum(axis = 2) / 3
    height, width = gray_img.shape

    for i in range(width):
        for j in range(height):
            for k in range(3):
                img_Gray[i, j, k] = gray_img[i, j]

    return img_Gray

def rgb_mapping(img, c_list, g_list):
    recons_img = img.copy()
    height, width, _ = recons_img.shape

    k = 0
    for i in range(width):
        for j in range(height):
            temp = []
            for n in range(4):
                if recons_img[i, j, k] >= g_list[n][k] :
                    dif = abs(recons_img[i, j, k] - g_list[n][k])
                else:
                    dif = abs(g_list[n][k] - recons_img[i, j, k])
                temp.append(dif)

            for l, m in enumerate(temp):
                if m == min(temp):
                    recons_img[i, j, :] = c_list[l]
                    break

    return recons_img

def img_resize(h, w, color_img):
    a = np.zeros([640, 1100, 3])

    if w / h <= 25 / 16:
        res_h = 640
        res_w = w * res_h // h
        resized_img = cv2.resize(color_img, dsize=(res_w, res_h), interpolation=cv2.INTER_AREA)
        x = 600 - (res_w // 2)
        a[0:res_h , 1100 - res_w:1100] = resized_img / 255.0
    else:
        res_w = 1000
        res_h = h * res_w // w
        resized_img = cv2.resize(color_img, dsize=(res_w, res_h), interpolation=cv2.INTER_AREA)
        y = 320 - (res_h // 2)
        a[y:y + res_h, 100:100 + res_w] = resized_img / 255.0

    return a

def main():
    image_path = "./camo.jpg"
    img = imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_g = random_crop(img, 1, 0, 0)                  #random하게 crop

    img_Gray = color2gray(img_g)
    gray_color_list = image_color_cluster(img_Gray)    #처음 gray 영상의 4가지 색 추출 이후 컬러의 4가지 색과 mapping

    for i in os.listdir('./in_copy/'):
        img_g = random_crop(img, 1, 0, 0)              #random한 이미지 생성
        img_Gray = color2gray(img_g)

        color_img = imread("./in_copy/" + i)
        color_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)
        height, width, _ = color_img.shape

        dst = img_resize(height, width, color_img)

        #if height != 400:
        #    h = 400
        #    w = width * h // height
        #    dst = cv2.resize(color_img, dsize=(w, h), interpolation=cv2.INTER_AREA)

        color_img = random_crop(color_img, 0, height, width)    #4분의 1 crop : 하늘을 잘라내기위한 간단한 트릭
        color_list = image_color_cluster(color_img)

        result_img = rgb_mapping(img_Gray, color_list, gray_color_list)
        #result = img_concat = cv2.hconcat([result_img, dst])    #이미지 가로 방향으로 concat

        #a = np.zeros([1100,640,3])
        result_ = cv2.resize(result_img, dsize= (400, 400), interpolation=cv2.INTER_LINEAR)
        #a[200:400 , 0:200] = result_ / 255.0
        dst[240:640, 0:400] = result_ / 255.0



        cv2.destroyAllWindows()
        winname = 'result' + i
        cv2.namedWindow(winname)
        cv2.moveWindow(winname, 0, 0)
        cv2.imshow('result' + i , dst)
        cv2.waitKey(1000)



if __name__ == '__main__':
    main()
