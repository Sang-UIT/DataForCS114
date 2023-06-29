import cv2
for i in range(1,45):
    for j in range(1,101):
        path=i+'\\' + j + '.jpg'
        img=cv2.imread(path)
        img_66=cv2.resize(img, (600,600))
        cv2.imwrite(path,img_66)