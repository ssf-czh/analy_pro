import numpy as np

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import csv
import math

def func_P2(G2,A0,A1,A2):
    '''
    :param G2: 自变量x
    :param A0: 待拟合参数
    :param A1:
    :param A2:
    :return:
    '''
    P2 = A0 + A1 * G2 + A2 * G2 * G2
    return P2

def calc_pre(G2,a,P2):
    P2_pre = a[0] + a[1] * G2 + a[2] * G2 * G2

    rat = abs(1-P2_pre/P2)
    mse = np.sum((P2_pre-P2)**2)/len(P2)

    return sum(rat)/len(rat),math.sqrt(mse)

if __name__ == '__main__':

    G2 = np.array([533,498,442,387,331])
    P2 = np.array([78,56.8,39.9,26.8,16.8])
    a,b  = curve_fit(func_P2, G2, P2)
    print(a)
    avg_err, rmse = calc_pre(G2,a,P2)
    print(avg_err)
    print(rmse)