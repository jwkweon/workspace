import numpy as np
from scipy.misc import imread, imsave

def main():
  img = imread('./kpp.jpeg')
  gray_img = img.sum(axis = 2) / 3
  imsave('gray_kpp.jpeg', gray_img)

if __name__ == 'main':
  main()
