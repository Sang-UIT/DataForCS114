import cv2
for i in range(36,37):
    for j in range(1,101):
        path=str(i)+'\\' +str(i)+"_" + str(j) + '.jpg'
        print(path)
        img=cv2.imread(path)
        img_66=cv2.resize(img, (600,600))
        cv2.imwrite(path,img_66)