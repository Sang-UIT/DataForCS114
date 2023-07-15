import os
for i in range(5,6):    
    for j in range(1,16):
        os.rename('test'+str(i)+'\\'+'test'+str(i)+'_'+str(j)+'.txt','labels\\'+'test'+str(i)+'_'+str(j)+'.txt')
        os.rename('test'+str(i)+'\\'+'test'+str(i)+'_'+str(j)+'.jpg','images\\'+'test'+str(i)+'_'+str(j)+'.jpg')