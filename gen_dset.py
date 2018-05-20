# -*- coding=utf-8 -*-

import os
import numpy as np
from PIL import Image
import h5py as hp

IMG_DIR="bg_img"
depth = hp.File("depth.h5","r")
seg_mask = hp.File("seg.h5","r")
seg = seg_mask[u'mask']

dset = hp.File("dset.h5","w")
dImage = dset.create_group("image")
dDepth = dset.create_group("depth")
dSeg = dset.create_group("seg")

if __name__ == "__main__":
    imgFiles = os.listdir(IMG_DIR)
    i = 0
    for file in imgFiles:
        imgFile = os.path.join(IMG_DIR,file)
        file = file.decode("utf-8")
        if os.path.isfile(imgFile):
            if file in depth.keys() and file in seg.keys():
                try:
                    img = Image.open(imgFile)
                    img_arr = np.array(img)
                    dImage.create_dataset(file,data=img_arr)
                    dDepth.create_dataset(file,data=depth[file][:])
                    dSeg.create_dataset(file,data=seg[file][:])
                    dSeg[file].attrs.create("label",seg[file].attrs["label"])
                    dSeg[file].attrs.create("area",seg[file].attrs["area"])
                    i += 1;
                    if i == 100:
                        break
                except:
                    continue;

depth.close()
seg_mask.close()
dset.close()


