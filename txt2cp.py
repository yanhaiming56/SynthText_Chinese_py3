import pickle as pk
import numpy as np

if __name__ == "__main__":
    txtfile = open("cp_txt_cov/colors_new.txt")
    arr = []
    for line in txtfile.readlines():
        num = line.strip().split(",")
        arr.append(num)
    data = np.array(arr,np.float)
    with open("data/models/colors_new.cp",'wb') as f:
        pk.dump(data,f)

