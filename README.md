# SynthText_Chinese_version from JarveeLee

Modify from https://github.com/JarveeLee/SynthText_Chinese_version.git to generate chinese character.

Due to SynthText_Chinese_version is writen by python2 and opencv2.So, I modify this program by python3 and opencv3.

My OS is Ubuntu18.01, python3.6, opencv3.4. But I am not sure whether it can run on other OS.

- **dset.h5**: For the "dset.h5" file,I have generated it which containts 99 images and corresponding to depth and seg 
infomation.If you don't want to genetate by yourself you can download from 
[dset.h5](https://pan.baidu.com/s/1-s7b_68O-GTK3dH4OJt6zw), password: fxtj

Of course,you can genetate the "dset.h5" file by yourself.You must download these files:
The 8,000 background images used in the paper, along with their segmentation and depth masks, 
have been uploaded here: http://zeus.robots.ox.ac.uk/textspot/static/db/<filename>, where, <filename> can be:

- **imnames.cp [180K]**: names of filtered files, i.e., those files which do not contain text
- **bg_img.tar.gz [8.9G]**: compressed image files (more than 8000, so only use the filtered ones in imnames.cp)
- **depth.h5 [15G]**: depth maps
- **seg.h5 [6.9G]**: segmentation maps

You can create a folder,such as "dataset" and put the files into this folder,and copying the "gen_dset.py" into this folder.
You also have to unzip the "bg_img.tar.gz" to this folder.You only run:
```
python gen_dset.py
```
The "gen_dset.py" file can generate 99 images infomation,if you want to generate more images infomation,You can modify the 
35th line of this file.Modify "i == 100" to "i == n",'n' denotes a number which is you want to generate quantity of image.
Then you just copy the generated file "dset.h5" to the folder "data".You only run:
```
python gen.py
```
If You want to visualize these synthtext images,you can run:
```
python gen.py --viz
```

Note: I do not own the copyright to these images.



More detail content,you can consult the https://github.com/ankush-me/SynthText.
