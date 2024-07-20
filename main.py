#%%
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import os
import cv2
#%%设置位置的读取文职
train_path = './DataSet/train/'
val_path = './DataSet/val/'
save_path = 'AdvPic'

#%%预备工作，创建文件夹
root = os.listdir('./')
if not(save_path in 'AdvPic'):
    os.mkdir(save_path)
#%%os读取文件
train_files = os.listdir(train_path)
print(train_files)
val_files = os.listdir(val_path)
for folder in train_files:
    print(folder)
    pic_path = train_path + folder
    pics = os.listdir(pic_path)
    #检测文件夹是否存在并且进行创建

    for pic in pics:
        print(pic)
        img = cv2.imread(pic_path + '/' + pic, cv2.IMREAD_GRAYSCALE)
        h=img.shape[0]
        w=img.shape[1]
        for i in range(h):
            for j in range(w):
                img[i][j] = 255 - img[i][j]

        cv2.imwrite(save_path+folder+pic, img)

