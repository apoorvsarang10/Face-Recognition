
'''
Description: Resize all images from a directory based on the path, img_path,
             with keeping the actual images frame size and save it as "filename"_dist
              
'''

from PIL import Image
from resizeimage import resizeimage
from glob import glob
import cv2
import numpy as np
import os

CONST_HEIGHT = 50;
CONST_WIDTH = 50;
CONST_PATH = "/Users/keonmin/Documents/Python/Face-Recognition-master/pictures/*.jpg"

img_names = glob(CONST_PATH)
for file in img_names:
    img = cv2.imread(file, 0)
    dimensions = img.shape
    height = img.shape[0]
    width = img.shape[1]
    #print('Image Height       : ',height)
    #print('Image Width        : ',width)
    blank_image = 48 * np.ones((height,width), np.uint8)
    img=cv2.resize(img,(CONST_HEIGHT, CONST_WIDTH))
    x_offset=y_offset=50
    blank_image[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img
    file = file + '_dist.jpg'
    cv2.imwrite(file,blank_image)
