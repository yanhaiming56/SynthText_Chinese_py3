# Author: Ankush Gupta
# Date: 2015
"Script to generate font-models."

import pygame
from pygame import freetype
from text_utils import FontState
import numpy as np 
import matplotlib.pyplot as plt 
import pickle as cp
import os
pygame.init()

ys = np.arange(8,200)
A = np.c_[ys,np.ones_like(ys)]

xs = []
models = {} #linear model

font_dir = "data/fonts"

# FS = FontState()

ft = freetype.Font('data/fonts/more_font/方正隶书简体.ttf', size = 12)

fontfilelist = os.path.join(font_dir,"fontlist.txt")
fontfiles = open(fontfilelist,'r')
    	
for fontfile in fontfiles:
	fontfilepath = os.path.join(font_dir,fontfile)
	font = freetype.Font(fontfilepath.strip(), size=12)
	h = []
	for y in ys:
		h.append(font.get_sized_glyph_height(float(y)))
	h = np.array(h)
	m,_,_,_ = np.linalg.lstsq(A,h)
	models[font.name] = m
	xs.append(h)
	print(font.name)

with open('data/models/font_px2pt.cp','wb') as f:
	cp.dump(models,f)

