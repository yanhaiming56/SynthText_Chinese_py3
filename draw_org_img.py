# -*- coding=utf-8 -*-

import h5py as hp
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import os

img_dir="org_img"

dset = hp.File("results/SynthText_cartoon_viz.h5", "r")
for k in dset['data'].keys():
    print(k)
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    fileName = k
    pos = fileName.find(".jpg_0")
    fileName = fileName[0:pos]

    imgFile = fileName + ".jpg"
    imgFile = os.path.join(img_dir,imgFile)
    img = Image.fromarray(dset['data'][k][:])
    img.save(imgFile)