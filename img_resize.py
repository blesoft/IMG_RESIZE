import os
import cv2 as cv

SAVE_DIR = "./pic_resize_data/"

#　画像読み込み
img_origin = cv.imread("niku.jpg")
height_origin = img_origin.shape[0]
width_origin  = img_origin.shape[1]

#　圧縮して保存
comp_rate_array = [2,3,4,5,6,8,10,12,15,20]  #圧縮率
for i in comp_rate_array:
    height_rewrite = int(height_origin / i)
    width_rewrite  = int(width_origin / i)
    #  リサイズ
    img_rewrite = cv.resize(img_origin,(width_rewrite,height_rewrite))
    #  保存
    TITLE = "div" +str(i) + "_.jpg"
    cv.imwrite(os.path.join(SAVE_DIR,TITLE),img_rewrite)

