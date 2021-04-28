import numpy as np
import random as rd
 
X = np.array(([0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]), dtype=float)
Y = np.array(([1], [0], [0], [0], [0],[0], [0], [1]), dtype=float)

xPredicted = np.array(([0,0,1]), dtype=float)
X = X/np.amax(X, axis=0) 
xPredicted = xPredicted/np.amax(xPredicted, axis=0)

lossFile = open("SumSquaredLossList.csv", "w")

class Neural(object):
    def __init__(self):
        self.input = 3
        self.hidden = 4
        self.ouput = 1
        self.input = np.random.rand(3,1)
        self.hidden = np.random.rand(4,1)
        self.output = np.random.rand(1,1)
        self.s = 0
    def Sigmoid_squish(self,s):
        return 1/(1+np.exp(-s))
        
    def Forward(self,X):
        self.w1 = np.dot(X,self.input)
        self.bias = np.random.rand(len(self.w1),1)
        self.active1 = self.w1 + self.bias
        print(self.active1)

        '''
        for i in range(len(self.active1)):
            self.s = self.s + self.active1[i]
        self.n1 = self.Sigmoid_squish(self.s) # here n1 is just one singular neuron in the ML code !!

        print("First layer of activation is:",self.n1)

        self.w2 = np.dot(self.active1,self.hidden)
        for i in range(len(self.w2)):
            self.bias = np.random.rand()
        self.active2 = self.w2 + self.bias
        for i in range(len(self.active2)):
            self.s = self.s + self.active2[i]
        self.n2 = self.Sigmoid_squish(self.s) # here n2 is just one singular neuron of the second layer !! we need a whole set of such neurons with the size of the respective layer each.
        
        print("Second layer is:",self.n2)
        '''
        
nobj = Neural()
nobj.Forward(X)
