import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import csv
import math
import xgboost as xgb


def calc_pre(P4,predict_P4):
    '''

    :param P:  实际值，观测值
    :param W: 自变量X值
    :return:
    '''
    # predict_P4 = func_P4(W,-2.07832029e+00,  6.22291728e-02, -1.82160034e-04,  2.52676063e-07)
    rat = abs(1-predict_P4/P4)

    mse = np.sum((predict_P4 - P4)**2)/len(P4)
    # print(mse)
    # print("===")

    rmse = math.sqrt(mse)

    return (sum(rat)/len(rat)),rmse

if __name__ == '__main__':
    data = []

    df_p4 = pd.read_excel("./设备5_p4.xlsx").astype(float)
    # T3 = np.array(df["出水温度T3"]).astype(float)
    # T4 = np.array(df["进水温度T4"]).astype(float)
    # TS = np.array(df["湿球温度Ts"]).astype(float)
    TS = np.array(df_p4["湿球温度Ts"]).astype(float)
    G = np.array(df_p4["水量G,m3/h"]).astype(float)
    y = np.array(df_p4["风机功率P4，Kw"]).astype(float)
    # print(G)
    # print(TS.shape)
    X =  np.hstack((TS.reshape((-1,1)),G.reshape((-1,1))))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)



    model_c = xgb.XGBRegressor()
    model_c.fit(X, y)  # 使用训练数据训练
    y_pre = model_c.predict(X)
    # print(model_c.score(X_test, y_test))
    print(calc_pre(y,y_pre))

    temp= list()
    temp.append([28,-120.33202896588189])
    print(model_c.predict(temp))

    # print(y)
    # print(y_pre)
    # print(len(T3),len(T4),len(TS),len(Q),len(G))
    #
    # a, b = curve_fit(func_P4, (G), P4)
    # print(a)
    # print("==="*20)
    # print(b)
    # avg_err, rmse = calc_pre(P4,(G))
    # print(avg_err)
    # print(rmse)

    # for i in range(len(P4)):
    #     PRE = func_P4((TS[i],G[i]),2.72281437e-02, -1.21740608e-05, -8.18525579e-09,  8.07740271e-03)
    #     print("真实值：{:s},预测值{:s}".format(str(P4[i]),str(PRE)))