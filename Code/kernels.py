import numpy as np

simple = [-1,0,1]

prewittY = [[-1,-1,-1],[0,0,0],[1,1,1]]
prewittX = [[-1,0,1],[-1,0,1],[-1,0,1]]

sobelY = [[-1,-2,-1],[0,0,0],[1,2,1]]
sobelX = [[-1,0,1],[-2,0,2],[-1,0,1]]

sobelDF = [[-2,-1,0],[-1,0,1],[0,1,2]]
sobelDA = [[0,-1,-2],[1,0,-1],[2,1,0]]

extendedSobel = [np.asarray(sobelY), np.asarray(sobelDF), np.asarray(sobelX), np.flip(sobelDA), np.flip(sobelY), np.flip(sobelDF),np.flip(sobelX),np.asarray(sobelDA)]

kirschX = [[-5,3,3],[-5,0,3],[-5,3,3]]
kirschY = [[-5,-5,-5],[3,0,3],[3,3,3]]