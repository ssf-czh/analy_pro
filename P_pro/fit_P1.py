import numpy as np

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import csv
import math

def data_clean(str_num):
    flg = 0
    num = ''
    for i in str_num:
        if i != '.' and i!=' ':
            num +=i
        if i =='.'and flg ==0:
            num+= i
            flg = 1
    return float("".join(num.split()))


def func_P1(T,B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17,B18,B19,B20,B21,B22,B23):
    '''
    T相当于自变量X
    B相当于参数W
    '''
    T1,T2,T3,T4,Q = T
    P1 = B0 + B1 * T1 + B2 * T2 + B3 * Q + B4 * Q * Q + B5 * T1 * T1 + B6 * T2 * T2 + B7 * Q * T1 + B8 * Q * T2 + B9 * T1 * T2 + B10 * T3 + B11 * T4 + B12 * T3 * T3 + B13 * T4 * T4 + B14 * Q * T3 + B15 * Q * T4 + B16 * T3 * T4 + B17 * (
                T2 - T1) + B18 * (T4 - T3) + B19 * (T2 - T1) * (T2 - T1) + B20 * (T4 - T3) * (T4 - T3) + B21 * Q * (
                T2 - T1) + B22 * Q * (T4 - T3) + B23 * (T2 - T1) * (T4 - T3)
    return P1

def calc_pre(P,W):
    '''

    :param P:  实际值，观测值
    :param W: 自变量X值
    :return:
    '''
    predict_P = func_P1(W, 1.25592470e+02, 5.39445250e+01, -5.22395970e+01,6.29397302e-02,-2.06962469e-05, -3.33850530e+01, -3.30937615e+01,  1.13915116e+02
 ,-1.13920754e+02 , 6.62996700e+01, -5.43024482e+01,  4.63683510e+01
 ,-2.01032174e+03 ,-2.00895336e+03 , 1.97466857e+02, -1.97464621e+02
 , 4.01945845e+03  ,5.63936524e+01 ,-9.05705574e+01 , 3.25980615e+01
  ,2.00722896e+03 , 1.13929510e+02  ,1.97486520e+02 ,-3.39669822e+00)
    rat = abs(1-predict_P/P)

    mse = np.sum((predict_P - P)**2)/len(P)
    # print(mse)
    # print("===")

    rmse = math.sqrt(mse)

    return (sum(rat)/len(rat)),rmse

if __name__ == '__main__':
    # data = []
    # with open(r"C:\Users\ssf\Desktop\水泵性能分析需求文档\数据拟合数据表B0--B23.csv", encoding='utf-8') as f:
    #     f_csv = csv.reader(f)
    #     headers = next(f_csv)
    #     k = 1
    #     for row in f_csv:
    #         #         print(row)
    #         k += 1
    #         temp = []
    #         if k % 2 == 1:
    #             P1 = data_clean(row[3])
    #             T1 = data_clean(row[4])
    #             T2 = data_clean(row[5])
    #             T3 = data_clean(row[6])
    #             T4 = data_clean(row[7])
    #             Q = data_clean(row[1])
    #             temp.append(P1)
    #             temp.append(T1)
    #             temp.append(T2)
    #             temp.append(T3)
    #             temp.append(T4)
    #             temp.append(Q)
    #             data.append(np.array(temp))
    # data = np.array(data)
    # print(len(data))
    #
    # P1 = data[:, 0]
    # T1 = data[:, 1]
    # T2 = data[:, 2]
    # T3 = data[:, 3]
    # T4 = data[:, 4]
    # Q  = data[:,5]

    df = pd.read_excel(r"./20211111主机数据拟合数据表B0--B23.xlsx").astype(float)

    T1 = df["T1"]
    T2 = df["T2"]
    T3 = df["T3"]
    T4 = df["T4"]
    Q = df["Q"]
    P1 = df["P1"]
    # print(P1)
    # print(T2)
    a, b = curve_fit(func_P1, (T1, T2, T3, T4,Q), P1)
    print(a)
    print("==="*20)
    # print(b)
    avg_err, rmse = calc_pre(P1,(T1, T2, T3, T4,Q))
    print(avg_err)
    print(rmse)

    temp = func_P1((9.78183461, 18.18283916, 23.5893269,  29.32993893
,281.4), 1.25592470e+02, 5.39445250e+01, -5.22395970e+01, 6.29397302e-02, -2.06962469e-05, -3.33850530e+01,
            -3.30937615e+01, 1.13915116e+02
            , -1.13920754e+02, 6.62996700e+01, -5.43024482e+01, 4.63683510e+01
            , -2.01032174e+03, -2.00895336e+03, 1.97466857e+02, -1.97464621e+02
            , 4.01945845e+03, 5.63936524e+01, -9.05705574e+01, 3.25980615e+01
            , 2.00722896e+03, 1.13929510e+02, 1.97486520e+02, -3.39669822e+00)
    print("p1::" ,temp)