import h5py as hp
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import os

result_dir = "render_img"
label_dir = "label_txt"

dset = hp.File("results/SynthText_cartoon_viz.h5", "r")

for k in dset['data'].keys():
    print(k)
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)

    fileName = k
    pos = fileName.find(".jpg_0")
    fileName = fileName[0:pos]

    labelFile = fileName + "_charBB" + ".txt"
    labelFile = os.path.join(label_dir, labelFile)
    label_file = open(labelFile, 'w')
    im_arr = dset['data'][k][:]
    # wordBB = dset['data'][k].attrs["wordBB"]
    charBB = dset['data'][k].attrs['charBB']
    txt = dset['data'][k].attrs["txt"]
    texts = ''
    for text in txt:
        lines = text.split("\n")
        for line in lines:
            words = line.strip().split("　")
            for word in words:
                ws = word.strip().split(" ")
                for w in ws:
                    if w != '':
                        texts += w
    texts = texts.strip()
    txts = texts
    img = Image.fromarray(im_arr)
    draw = ImageDraw.Draw(img)

    for i in range(charBB.shape[2]):
        left_top = (charBB[0, 0, i], charBB[1, 0, i])
        right_top = (charBB[0, 1, i], charBB[1, 1, i])
        right_bottom = (charBB[0, 2, i], charBB[1, 2, i])
        left_bottom = (charBB[0, 3, i], charBB[1, 3, i])
        draw.polygon([left_top, right_top, right_bottom,
                      left_bottom], outline=(255, 0, 0))
        # draw.text(left_top, txts[i], fill=(0, 0, 255), font=font)
        # l = np.array([charBB[0, 0, i], charBB[1, 0, i], charBB[0, 1, i], charBB[1, 1, i], charBB[0, 2, i], charBB[1, 2, i], charBB[0, 3, i], charBB[1, 3, i]], np.int32)
        strPts = "%d,%d,%d,%d,%d,%d,%d,%d" % (charBB[0, 0, i], charBB[1, 0, i], charBB[0, 1, i], charBB[1, 1, i],
                                              charBB[0, 2, i], charBB[1, 2, i], charBB[0, 3, i], charBB[1, 3, i])
        strL = strPts + " " + txts[i]
        label_file.write(strL)
        label_file.write("\n")

    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    imgFile = fileName + "_charBB" + ".jpg"
    imgFile = os.path.join(result_dir, imgFile)
    img.save(imgFile)
    # pts = np.array([left_top,right_top,right_bottom,left_bottom],np.int32)
    # cv2.fillPoly(im_arr,[pts],(0,0,255))
    # cv2.imwrite("results/new.jpg",im_arr)
