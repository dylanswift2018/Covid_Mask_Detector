# how to run the detector 
# py mask_detector_image.py --image  test/image.png

#imports 
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2
import os

# arguments parser 
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True,help="path to input image")
arg.add_argument("-f", "--face", type=str,default="face_detector",help="path to face detector model directory")
arg.add_argument("-m", "--model", type=str,default="mask_detector.model",help="path to trained face mask detector model")
arg.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(arg.parse_args())


