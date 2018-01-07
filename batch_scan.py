# USAGE
# python batch_scan.py -p images
# This script need argument for path of directory
# When windows appear you can see the green line for edge Detection
# If edge detection is currect, press to 'space key' to continue
# If not, press 'esc key' to save original picture
# Modified picture will saved in the directory that python script in it

# TODO
# 1. print [number/totalnumber]

# import the necessary packages
from pyimagesearch.transform import four_point_transform
from pyimagesearch import imutils
from skimage.filters import threshold_adaptive
import numpy as np
import argparse
import cv2
import glob
from os.path import basename

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
                help="Path to the image to be scanned")
args = vars(ap.parse_args())

# load the image
file_list = glob.glob("%s/*.jpg" % (args["path"]))

# make function


def save_ori(name):
    image = cv2.imread(name)
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height=500)
    cv2.imshow('Original', image)
    cv2.waitKey(0)
    cv2.imwrite(basename(name), orig)
    cv2.destroyAllWindows()


def auto_canny(x, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(x)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(x, lower, upper)
    # return the edged image
    return edged


def warp(name):
    image = cv2.imread(name)
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height=500)
    # convert the image to grayscale, blur it, and find edges in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    edged = auto_canny(gray)
    # edged = cv2.Canny(gray, 75, 200)
    # how the original image and the edge detected image
    # print "{} STEP 1: Edge Detection".format(basename(name))
    (cnts, _) = cv2.findContours(edged.copy(),
                                 cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            # print "{} STEP 2: Find contours of paper".format(basename(name))
            cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
            cv2.imshow("Outline", image)
            k = cv2.waitKey(0) & 0xFF
            if k == 27:  # esc key
                cv2.destroyAllWindows()
                cv2.imwrite(basename(name), orig)
            elif k == 32:  # space key
                # apply the four point transform to obtain a top-down
                # view of the original image
                warped = four_point_transform(
                    orig, screenCnt.reshape(4, 2) * ratio)
                # show the original and scanned images
                print " {} : Apply transform!".format(basename(name))
                cv2.imshow("Scanned", imutils.resize(warped, height=650))
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                # warped = increase_contrast(warped)
                cv2.imwrite(basename(name), warped)
                break
        else:
            cv2.imwrite(basename(name), orig)


def increase_contrast(x):
    img = x
    # cv2.imshow("Original image",img)
    # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8, 8))
    # convert from BGR to LAB color space
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)  # split on 3 different channels
    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
    lab = cv2.merge((l2, a, b))  # merge channels
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
    # cv2.imshow('Increased contrast', img2)
    # cv2.imwrite('sunset_modified.jpg', img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img2


if __name__ == '__main__':
    for i in file_list:
        try:
            warp(i)
        except:
            print "ERROR in {}".format(i)
            # save original pic
            save_ori(i)
    print "DONE!"
