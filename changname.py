import cv2
import os
lst_name=[]
for i in range(1,45):
    pat=str(i)+'\\name.txt'
    f = open(pat, "r")
    s = f.read()
    lst_name.append(str(i)+','+s)
    f.close()

with open(r'lst_name.csv', 'w') as fp:
    for item in lst_name:
        # write each item on a new line
        fp.write("%s" % item)
    print('Done')