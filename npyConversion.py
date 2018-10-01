import csv
import os
import numpy as np
import cv2 as cv

def load_data(n_x,n_y,n):
    images=np.zeros((n, n_x,n_y,3))
    i=0
    
    for i in range(n):
        images[i] = cv.imread("/home/yash/AGV/Data/"+str(i)+'.jpg',1)
        i=i+1
    
    
    return images
X=load_data(200,200,1424)
Y=[]
with open('annotations.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for (i, row) in enumerate(reader):
        x = row['bumpPresent']
        if (i<1424):
            Y.append(x)
Y=np.array(Y)
print("Y shape")
print(Y.shape)
Y=Y.reshape((Y.shape[0],1))
X=X.reshape((1424,200*200*3))
Z=np.zeros((X.shape[0],X.shape[1]+1))
print(Z.shape,Y.shape)
Z[:,0]=Y.reshape(Y.shape[0])
Z[:,1:X.shape[1]+1]=X
np.save("test1",Z)
