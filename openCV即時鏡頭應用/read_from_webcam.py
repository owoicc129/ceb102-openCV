'''
原理：OpenCV 取出影片中的"每張"影格

打開terminal-cd到檔案目錄
輸入python read_from_webcam.py 開啟
'''


import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)  # 0 代表要用筆電上的webcam 他會用你的鏡頭照 ，原本是寫路徑
 
while True:
    ret, frame = cap.read()  #frame 是一張照片
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #把照片轉灰階
     
    cv2.imshow("gray scale", gray_frame) 
    cv2.imshow("frame", frame)
 
    key = cv2.waitKey(1)
    if key == 27:  # 按Esc關閉
        break
 
 
cap.release() #釋放所有資源
cv2.destroyAllWindows()