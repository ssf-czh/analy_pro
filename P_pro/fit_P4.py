import numpy as np

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import csv
import math

def func_P4(T,N0,N1,N2):
    '''
    T相当于自变量X
    B相当于参数W
    拟合N0-N2
    '''
    # TS,G = T
    H = T
    P0 = 18000
    H0 = 8.47

    # P4 = (E0/TS) +(E1/TS)*G +(E2/TS)*G*G
    # P4 = E0 + E1 * G * (np.power(TS , f0)) + E2 * np.power(G , 2) * (np.power(TS , f1)) + f2 * TS + f3 * np.power(TS , 2)
    # P4 = E0*(G) +E1*TS+E2 * G/(TS*TS)
    # P4 = E0 + E1 * np.power(G , (f0 * TS)) + E2 * np.power(G , (f1 * TS)) + f2 * TS + f3 * np.power(TS , 2)
    # *(G / TS) * (G / TS) * (G / TS)
    # P4 = E0 * (TS * G) + E1 *(TS * G) * (TS * G) + E2 * (TS * G) *(TS * G) * (TS * G)
    P4 = P0 * (N0+N1*(H/H0)+N2*(H/H0)*(H/H0))



    return P4

def calc_pre(P4,W):
    '''

    :param P:  实际值，观测值
    :param W: 自变量X值
    :return:
    '''
    predict_P4 = func_P4(W,5.18666064e-05, 3.78739038e-09, 7.53049515e-13)
    rat = abs(1-predict_P4/P4)

    mse = np.sum((predict_P4 - P4)**2)/len(P4)
    # print(mse)
    # print("===")

    rmse = math.sqrt(mse)

    return (sum(rat)/len(rat)),rmse

if __name__ == '__main__':
    data = []

    df = pd.read_excel("./冷却塔5_p4.xlsx").astype(float)
    T3 = np.array(df["出水温度T3"]).astype(float)
    T4 = np.array(df["进水温度T4"]).astype(float)
    TS = np.array(df["湿球温度Ts"]).astype(float)
    H = np.array(df["风量H,m3/h"]).astype(float)
    G = np.array(df["水量G,m3/h"]).astype(float)
    P4 = np.array(df["风机功率P4，Kw"]).astype(float)




    # print(len(T3),len(T4),len(TS),len(Q),len(G))
    #
    a, b = curve_fit(func_P4, (H), P4)
    print(a)
    print("==="*20)
    print(b)
    avg_err, rmse = calc_pre(P4,(H))
    print(avg_err)
    print(rmse)

    for i in range(len(P4)):
        PRE = func_P4((H[i]),5.18666064e-05, 3.78739038e-09, 7.53049515e-13)
        print("真实值：{:s},预测值{:s}".format(str(P4[i]),str(PRE)))