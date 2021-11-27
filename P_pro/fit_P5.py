import numpy as np

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import csv
import math



def func_T3(T,D0,D1,D2,D3):
    '''
    T相当于自变量X
    B相当于参数W
    '''
    T4,TS,Q,G = T
    T3 = D0*TS+D1*T4+D2*np.power((Q/G),D3)
    return T3

def calc_pre(T3,W):
    '''

    :param P:  实际值，观测值
    :param W: 自变量X值
    :return:
    '''
    predict_T3 = func_T3(W,-1.45108938e-09,1.00000000e+00,-4.99999996e+00,3.28629844e-09)
    rat = abs(1-predict_T3/T3)

    mse = np.sum((predict_T3 - T3)**2)/len(T3)
    # print(mse)
    # print("===")

    rmse = math.sqrt(mse)

    return (sum(rat)/len(rat)),rmse

if __name__ == '__main__':
    data = []

    df = pd.read_excel("./设备5.xlsx").astype(float)
    T3 = np.array(df["出水温度T3"]).astype(float)
    T4 = np.array(df["进水温度T4"]).astype(float)
    TS = np.array(df["湿球温度Ts"]).astype(float)
    Q = np.array(df["风量Q,m3/h"]).astype(float)
    G = np.array(df["水量G,m3/h"]).astype(float)
    #
    # print(T3)
    # print(T4)
    # print(TS)
    # print(Q)
    # print(G)
    # print(len(Q))



    # print(len(T3),len(T4),len(TS),len(Q),len(G))
    #
    a, b = curve_fit(func_T3, (T4, TS, Q, G), T3)
    print(a)
    print("==="*20)
    print(b)
    avg_err, rmse = calc_pre(T3,(T4, TS, Q, G))
    print(avg_err)
    print(rmse)

    # for i in range(len(Q)):
    #     print("真实值：{:s},预测值{:s}".format(str(T3[i]),str(func_T3((T4[i], TS[i], Q[i], G[i]),-1.45108938e-09,1.00000000e+00,-4.99999996e+00 ,3.28629844e-09))))