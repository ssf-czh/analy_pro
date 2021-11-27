import numpy as np

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import csv
import math

def func_H(T,F0,F1,F2):
    '''
    T相当于自变量X
    B相当于参数W
    拟合F0-F2
    '''
    # TS,G = T
    T3,T4,TS,G = T
    a = 2500 * G
    b = F0 * np.power((G/3.6),F2)* (T4-TS)
    c = (T4-T3)*(7/6)*G
    d = (b/c)-1
    # print(d/F1)
    # print(1/F2)
    # e = 3 * np.power(d/F1,1/F2)
    e = 3 * d/F1
    H = a/e
    return H

    # P4 = (E0/TS) +(E1/TS)*G +(E2/TS)*G*G
    # P4 = E0 + E1 * G * (np.power(TS , f0)) + E2 * np.power(G , 2) * (np.power(TS , f1)) + f2 * TS + f3 * np.power(TS , 2)
    # P4 = E0*(G) +E1*TS+E2 * G/(TS*TS)
    # P4 = E0 + E1 * np.power(G , (f0 * TS)) + E2 * np.power(G , (f1 * TS)) + f2 * TS + f3 * np.power(TS , 2)
    # *(G / TS) * (G / TS) * (G / TS)
    # P4 = E0 * (TS * G) + E1 *(TS * G) * (TS * G) + E2 * (TS * G) *(TS * G) * (TS * G)




    return H

def calc_pre(H,W):
    '''

    :param H:  实际值，观测值
    :param W: 自变量X值
    :return:
    '''
    predict_H= func_H(W,-1.28446176 ,-1.79390413  ,1.17601112)
    rat = abs(1-predict_H/H)

    mse = np.sum((predict_H - H)**2)/len(H)
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
    # print(func_H((66,2,3,4),1,2,3))
    a, b = curve_fit(func_H, (T3,T4,TS,G), H)
    print(a)
    print("==="*20)
    print(b)
    avg_err, rmse = calc_pre(H,(T3,T4,TS,G))
    print(avg_err)
    print(rmse)

    # for i in range(len(H)):
    #     PRE = func_H((T3[i],T4[i],TS[i],G[i]),5.18, 3.787, 7.53049)
    #     print("真实值：{:s},预测值{:s}".format(str(P4[i]),str(PRE)))