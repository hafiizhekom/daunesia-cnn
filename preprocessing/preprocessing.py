import cv2
import numpy as np
from os import walk
import os
sensitivity = 20
gauss_win_size = 5
gauss_sigma = 3
th_window_size = 15
th_offset = 2

def crop_rotate(img):
    height, width = img.shape[:2]

    img_resize_result = cv2.resize(img, (width / 10, height / 10), interpolation=cv2.INTER_CUBIC)
    img = img_resize_result
    if (height < width) and (height != width):
        dst = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    else:
        dst = img
    crop_img = dst[55:355, 0:300]
    return crop_img

def get_biggest_scracth(img):
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(img)

    sizes = stats[1:, -1];
    if len(sizes) < 1:
        return img
    else:
        nb_components = nb_components - 1
        min_size = max(sizes) - 1

        img2 = np.zeros((output.shape))
        for i in range(0, nb_components):
            if sizes[i] >= min_size:
                img2[output == i + 1] = 255

        return img2

def denoising(img):
    height, width = img.shape[:2]
    real = img
    img = cv2.medianBlur(img, 5)

    return img

def brigtning(img):
    height, width = img.shape[:2]
    image = img

    new_image = np.zeros(image.shape, image.dtype)

    alpha = 1.0  # Simple contrast control
    beta = 0  # Simple brightness control

    try:
        alpha = float(1.5)
        beta = int(50)
    except ValueError:
        print('Error, not a number')

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y, x, c] = np.clip(alpha * image[y, x, c] + beta, 0, 255)

    return new_image


def binarize(img):
    ret, binarize_otsu = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

    return binarize_otsu

def replaceWhite(img,new_img):
    height, width = img.shape[:2]

    blank = np.zeros([height, width, 3], dtype=np.uint8)
    blank.fill(0)  # or img[:] = 255

    for x in range(0, width):
        for y in range(0, height):
            if (img[y, x] >= 200) and (img[y, x] <= 255):
                #print img[y, x]
                blank[y, x] = new_img[y, x]
            else:
                a = 0
                # print "hitam"

    return blank


def preprocessing():
    mypath = "/home/hafiizhekom/Documents/Dataset Daun/test_dracaena"
    destinationpath = "/home/hafiizhekom/Documents/Dataset Daun/result_dracaena"

    for (dirpath, dirnames, filenames) in walk(mypath):

        if not os.path.exists(destinationpath + "/BRIGHT/" + dirpath[-1]):
            os.makedirs(destinationpath + "/BRIGHT/" + dirpath[-1])

            if not os.path.exists(destinationpath + "/DENOISING/" + dirpath[-1]):
                os.makedirs(destinationpath + "/DENOISING/" + dirpath[-1])

        if not os.path.exists(destinationpath + "/BIN/" + dirpath[-1]):
            os.makedirs(destinationpath + "/BIN/" + dirpath[-1])

        for index, names in enumerate(filenames):
            img = cv2.imread(dirpath+"/"+names, cv2.IMREAD_COLOR)
            img = crop_rotate(img)
            imgcolor = brigtning(img)
            cv2.imwrite(destinationpath+"/BRIGHT/"+dirpath[-1]+"/"+names,img)
            img = denoising(imgcolor)
            cv2.imwrite(destinationpath+"/DENOISING/"+dirpath[-1]+"/"+names,img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = binarize(img)
            img = cv2.bitwise_not(img)
            img = get_biggest_scracth(img)


            img = replaceWhite(img, imgcolor)


            print index
            #cv2.imshow('as', img)
            #cv2.waitKey(0)

            cv2.imwrite(destinationpath+"/BIN/"+dirpath[-1]+"/"+names,img)

    print "Finish"

preprocessing()