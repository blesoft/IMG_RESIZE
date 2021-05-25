from img_resize import TITLE
import os
import cv2 as cv

DATA_DIR = "./pic_resize_data/"
SAVE_DIR = "./pic_comparise_data/"

#  オリジナル画像読み込み
img_origin = cv.imread("niku.jpg")
height_origin = img_origin.shape[0]
width_origin  = img_origin.shape[1]

#　圧縮画像読み込み
NUM = 0
comp_rate = [4,9,16,25,36,64,100,144,225,400]
for img_name in os.listdir(DATA_DIR):
    img_div = cv.imread(os.path.join(DATA_DIR,img_name))
    if not img_div is None:
        #  リサイズ
        img_rest = cv.resize(img_div,(width_origin,height_origin))
        TITLE = "comp_rate_" + str(comp_rate[NUM]) + ".jpg"
        cv.imwrite(os.path.join(SAVE_DIR,TITLE),img_rest)
    NUM += 1