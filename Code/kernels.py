import numpy as np

simple = [-1,0,1]

prewittY = [[-1,-1,-1],[0,0,0],[1,1,1]]
prewittX = [[-1,0,1],[-1,0,1],[-1,0,1]]

sobelY = [[-1,-2,-1],[0,0,0],[1,2,1]]
sobelX = [[-1,0,1],[-2,0,2],[-1,0,1]]
sobelDF = [[-2,-1,0],[-1,0,1],[0,1,2]] # DF = Diagonals Falling
sobelDR = [[0,-1,-2],[1,0,-1],[2,1,0]] # DR = Diagonals Rising
#Order is important! Needs to be clockwise. Where to start is random
extendedSobel = [np.asarray(sobelY), np.asarray(sobelDF), np.asarray(sobelX), np.flip(sobelDR), np.flip(sobelY), np.flip(sobelDF),np.flip(sobelX),np.asarray(sobelDR)]

kirschX = [[-5,3,3],[-5,0,3],[-5,3,3]]
kirschY = [[-5,-5,-5],[3,0,3],[3,3,3]]
kirschDF= [[-5,-5,3],[-5,0,3],[3,3,3]]
kirschDR= [[3,3,3],[-5,0,3],[-5,-5,3]]
#Order is important! Needs to be clockwise. Where to start is random
kirsch = [np.asarray(kirschY), np.asarray(kirschDF), np.asarray(kirschX), np.flip(kirschDR), np.flip(kirschY), np.flip(kirschDF),np.flip(kirschX),np.asarray(kirschDR)]


laplacian = [[1,1,1],[1,-8,1],[1,1,1]]

max1 = [[0,1,0],[0,0,0],[0,-1,0]]
max2 = [[1,0,0],[0,0,0],[0,0,-1]]
max3 = [[0,0,0],[1,0,-1],[0,0,0]]
max4 = [[0,0,1],[0,0,0],[-1,0,0]]
max5 = [[0,-1,0],[0,0,0],[0,1,0]]
max6 = [[-1,0,0],[0,0,0],[0,0,1]]
max7 = [[0,0,0],[-1,0,1],[0,0,0]]
max8 = [[0,0,-1],[0,0,0],[1,0,0]]
maxCompass = [max1,max2,max3,max4,max5,max6,max7,max8]