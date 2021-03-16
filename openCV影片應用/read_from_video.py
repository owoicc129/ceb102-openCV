'''
原理：OpenCV 取出影片中的"每張"影格

打開terminal-cd到檔案目錄
輸入python read_from_video.py 開啟
'''

import cv2
import numpy as np
 
cap = cv2.VideoCapture("Ben.mp4") #改成你要開的影片檔名
 
fourcc = cv2.VideoWriter_fourcc(*"XVID") #影片的編碼

out = cv2.VideoWriter("video.avi", fourcc, 25, (640, 360))  #跑完影片後會生成這個檔案 (長,寬)
 
while True:
    ret, frame = cap.read()  #frame 一張照片
    frame2 = cv2.flip(frame, 1)  #.flip 左右對換
  
    cv2.imshow("frame2", frame2)  #顯示 翻轉過的
    cv2.imshow("frame", frame)  #顯示 原版
 
    out.write(frame2) # 寫檔 翻轉過的
 
    key = cv2.waitKey(25)
    if key == 27:  #如果按Esc 就跳出
        break

out.release() #釋放所有資源
cap.release()
cv2.destroyAllWindows()