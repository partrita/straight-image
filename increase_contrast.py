# import the necessary packages
import numpy as np
import argparse
import glob
import cv2
from os.path import basename

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to input dataset of images")
args = vars(ap.parse_args())

# loop over the images
for imagePath in glob.glob(args["images"] + "/*.*"):
    img = cv2.imread(imagePath)
    cv2.imshow("Original image",img)
    # CLAHE contrast limited adaptive histogram equalization
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels
    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
    lab = cv2.merge((l2,a,b))  # merge channels
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
    cv2.imshow('Increased contrast', img2)
    cv2.waitKey(0)
    cv2.imwrite(basename(imagePath), img2)
    cv2.destroyAllWindows()

# TODO
# make function and do error control
