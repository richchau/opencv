#!/usr/bin/python2.7
import math

def LoG2d(x, y, sigma):
    xyp2 = x ** 2 + y ** 2
    LoG = ((xyp2 - 2 * sigma**2) /(math.sqrt(2 * math.pi) * math.pow(sigma, 5))) * math.exp(-xyp2 / (2 * sigma**2))
    return LoG

def KernelLoG(sigma, size, kernel):
    assert ((size % 2) != 0)
    for i in range(-(size/2), size/2 + 1):
        for j in range(-(size/2), size/2 + 1):
            kernel[i + size/2 ][j + size/2] = LoG2d(i, j, sigma)

if __name__ == "__main__":
    KernelSize = 3
    MyKernel = [[0 for x in range(KernelSize)] for y in range(KernelSize)]
    Sigma = 1.8
    KernelLoG(Sigma, KernelSize, MyKernel)
    print MyKernel

'''
3x3 LoG
[[-0.06946788034149066, -0.09915333938923544, -0.06946788034149066], 
 [-0.09915333938923544, -0.13681148161914702, -0.09915333938923544], 
 [-0.06946788034149066, -0.09915333938923544, -0.06946788034149066]]
5x5 LoG
 [[0.009337381455882096, -0.014444598966909878, -0.028243349976688703, -0.014444598966909878, 0.009337381455882096], 
 [-0.014444598966909878, -0.06946788034149066, -0.09915333938923544, -0.06946788034149066, -0.014444598966909878], 
 [-0.028243349976688703, -0.09915333938923544, -0.13681148161914702, -0.09915333938923544, -0.028243349976688703], 
 [-0.014444598966909878, -0.06946788034149066, -0.09915333938923544, -0.06946788034149066, -0.014444598966909878], 
 [0.009337381455882096, -0.014444598966909878, -0.028243349976688703, -0.014444598966909878, 0.009337381455882096]]

'''