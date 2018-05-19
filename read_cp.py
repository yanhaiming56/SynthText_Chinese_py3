import pickle as pk
import numpy as np

with open("data/models/colors_new.cp",'rb') as f:
    color = pk.load(f)
    print(np.random.randint(0,color.shape[0]))
    print(color[np.mod(100000,4941),:])

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

# print_format_table()