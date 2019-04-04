import tensorflow as tf
import os
import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from scipy.misc import imread, imsave
import cv2

def load_datas():
    data = np.array(glob('./in/*.jpg'))
    
    sample = [imread(sample_file) for sample_file in data]
    sample_images = np.array(sample).astype(np.float32)
    
    return data, sample_images  
   
def load_sample_datas(batch_size):
    data = np.random.choice(glob('./in/*.jpg'), batch_size)
    sample = [imread(sample_file) for sample_file in data]
    sample_images = np.array(sample).astype(np.float32)
    
    return data, sample  

data, samples = load_datas()

print(samples,samples.shape)
print(data,data.shape)


#glob('./in/*.jpg')

data, samples = load_sample_datas(batch_size)

#print(data[:].shape)
print(data)

img = imread('./in/2.jpg')

print(img.shape)


plt.imshow(img)

x = 0
y = 0
img_resize = img[x : x + 256, y : y + 256]

img_resize = img_resize[:][:][:] + 255
#g = img_resize[:][:][1] + 100
#b = img_resize[:][:][2]  + 100

print(img_resize.shape)

plt.imshow(img_resize)
imsave('result.jpg',img_resize)

x = 0
y = 0
img_resize = img[x : x + 256, y : y + 256]

img_resize = img_resize[:][:][:] + 0
#g = img_resize[:][:][1] + 100
#b = img_resize[:][:][2]  + 100

print(img_resize.shape)

plt.imshow(img_resize)

    
