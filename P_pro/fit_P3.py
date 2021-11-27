import numpy as np

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import csv
import math
def func_P3(G3,C0,C1,C2):
    '''
    :param G3: 自变量x
    :param C0: 待拟合参数
    :param C1:
    :param C2:
    :return:
    '''
    P3 = C0 + C1 * G3 + C2 * G3 * G3
    return P3

def calc_pre(G3,a,P3):
    P3_pre = a[0] + a[1] * G3 + a[2] * G3 * G3

    rat = abs(1-P3_pre/P3)
    mse = np.sum((P3_pre - P3) ** 2) / len(P3)
    return sum(rat)/len(rat),math.sqrt(mse)

if __name__ == '__main__':

    G3 = np.array([632,380,338,297,254])
    P3 = np.array([50,30.2,21.3,14.2,9.1])
    a,b  = curve_fit(func_P3, G3, P3)
    print(a)
    avg_error,rmse = calc_pre(G3,a,P3)
    print(avg_error)
    print(rmse)

