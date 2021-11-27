def aimFunc(pop):  # 目标函数
    # Vars = pop.Phen
    T1 = pop[0]
    T2 = pop[1]
    T3 = pop[2]
    T4 = pop[3]


    # =================================================
    Q = 281.4

    B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23 = 7.94539444e+01, 8.52049211e+06, -5.42344834e+01, 8.59864857e-02, 6.95046641e-06, 2.23510625e+00, 8.22659631e+01, -8.59345634e+01, -1.41233523e+01, -4.56373684e+00, -8.52048947e+06, 5.03213748e+01, -2.95697716e+01, -1.07953074e+02, 7.07085892e+01, 2.93456023e+01, 5.75888681e+01, 8.52048827e+06, -8.52053335e+06, -2.16722512e+00, 2.90316804e+01, -8.59289244e+01, 7.07100121e+01, -1.71110243e-01
    A0, A1, A2 = 1.05105606e+02, -6.08574731e-01, 1.03989940e-03
    C0, C1, C2 = -5.40003853e+01, 2.96859204e-01, -2.09088412e-04

    P1 = B0 + B1 * T1 + B2 * T2 + B3 * Q + B4 * Q * Q + B5 * T1 * T1 + B6 * T2 * T2 + B7 * Q * T1 + B8 * Q * T2 + B9 * T1 * T2 + B10 * T3 + B11 * T4 + B12 * T3 * T3 + B13 * T4 * T4 + B14 * Q * T3 + B15 * Q * T4 + B16 * T3 * T4 + B17 * (
                T2 - T1) + B18 * (T4 - T3) + B19 * (T2 - T1) * (T2 - T1) + B20 * (T4 - T3) * (T4 - T3) + B21 * Q * (
                     T2 - T1) + B22 * Q * (T4 - T3) + B23 * (T2 - T1) * (T4 - T3)
    # print("P1 value ")
    # print(P1)

    G2 = Q / (4.2 * (T2 - T1) * 1000)
    P2 = A0 + A1 * G2 + A2 * G2 * G2
    # print("P2 value ")
    # print(P2)

    G3 = (Q + P1) / (4.2 * (T4 - T3) * 1000)
    P3 = C0 + C1 * G3 + C2 * G3 * G3
    # print("P3 value ")
    # print(P3)

    P4 = 69.8978 * (P1 + Q) / (T4 - T3) * (P1 + Q) / (T4 - T3) + 83.7279 * (P1 + Q) / (T4 - T3) + 0.1554
    # print("P4 value ")
    # print(P4)

    P = P1 + P2 + P3 + P4
    return P

    # print("Sum P value ")
    # print(P)

    # pop.CV = np.hstack([T1-T2+4,T2-T1-10,T3-T4+4,T4-T3+6])

    # pop.CV = np.hstack([2*x1 + x2 - 1,x1 + 2*x3 - 2,np.abs(x1 + x2 + x3 - 1)])#第三个约束


    # pop.ObjV[exIdx] = max(P)+1
    # print("objV")
    # print(pop.ObjV)
    # print(min(P))


# print(aimFunc([9, 19, 21, 26]))
# 通过1.txt来画图=======================
#
# y = list()
# with open("./1.txt", "r") as f:
#     s = f.readline()
#     while s:
#         y.append(float(s.split('|')[4]))
#         s = f.readline()
# print(y)
# print(len(y))
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# #
# x = np.arange(30)
# # # y = [4.27824e+18, 3.81878e+18, 3.51498e+18, 2.73494e+18, 2.41945e+18, 2.22736e+18, 1.61373e+18, 5.9276e+17, 2.74581e+17, 4.35701e+16, 2.73185e+16, 2.47586e+16, 2.35074e+16, 2.1242e+16, 1.80536e+16, 1.67301e+16, 1.49954e+16, 1.37986e+16, 1.26886e+16, 1.12019e+16, 9743720000000000.0, 8421840000000000.0, 7783300000000000.0, 7554860000000000.0, 7282390000000000.0, 6926590000000000.0, 6906000000000000.0, 6847280000000000.0, 6841610000000000.0, 6839390000000000.0]
#
# plt.title("Q = 2814")
# plt.xlabel("Number of Generation")
# plt.ylabel("Average P Value")
# plt.plot(x,y)
# plt.show()

# ============
# 测试P4等式是否成立
# import pandas as pd
#
# df = pd.read_excel("./冷却塔5_p4.xlsx").astype(float)
# T3 = np.array(df["出水温度T3"]).astype(float)
# T4 = np.array(df["进水温度T4"]).astype(float)
# TS = np.array(df["湿球温度Ts"]).astype(float)
# H = np.array(df["风量H,m3/h"]).astype(float)
# G = np.array(df["水量G,m3/h"]).astype(float)
# P4 = np.array(df["风机功率P4，Kw"]).astype(float)
#
# print(len(T3))
# print(len(T4))
# print(len(TS))
# print(len(H))
# print(len(G))
# C1 = (T4-T3)*(7/6)*G
# C2 =
#
# a = np.array([8,8])
# print(np.sqrt(a))
# 计算P1,P2,P3,P4==============
from fit_P1 import func_P1
import pandas as pd
import numpy as np
import pandas as pd
import csv
import math
import xgboost as xgb
from sklearn.model_selection import train_test_split

def calc_p4(p4g, ts):
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
    X = np.hstack((TS.reshape((-1, 1)), G.reshape((-1, 1))))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

    model_c = xgb.XGBRegressor()
    model_c.fit(X, y)  # 使用训练数据训练
    y_pre = model_c.predict(X)
    # print(model_c.score(X_test, y_test))
    # print(calc_pre(y, y_pre))

    temp = list()
    temp.append([ts, p4g])
    return model_c.predict(temp)


T1,T2,T3,T4 = 7.61760841, 17.59148718 ,29.8754903 , 34.18393378
Q = 562.8
TS = 10

P1 = func_P1((T1,	T2,	T3, T4
,Q), 1.25592470e+02, 5.39445250e+01, -5.22395970e+01, 6.29397302e-02, -2.06962469e-05, -3.33850530e+01,
            -3.30937615e+01, 1.13915116e+02
            , -1.13920754e+02, 6.62996700e+01, -5.43024482e+01, 4.63683510e+01
            , -2.01032174e+03, -2.00895336e+03, 1.97466857e+02, -1.97464621e+02
            , 4.01945845e+03, 5.63936524e+01, -9.05705574e+01, 3.25980615e+01
            , 2.00722896e+03, 1.13929510e+02, 1.97486520e+02, -3.39669822e+00)
print("p1::" ,P1)

A0,A1,A2 = 1.05105606e+02,-6.08574731e-01,1.03989940e-03

G1=6*Q/(7*(T2-T1))
P2 = A0+A1*G1+A2*G1*G1
print("p2:",P2)

# 10,	16.43171636,	21, 25
C0,C1,C2 = -5.40003853e+01,2.96859204e-01,-2.09088412e-04
# P1 = -146.63113336006293
G3=6*(Q+P1)/(7*(T4-T3))
print("P3的G3：", G3)
P3 = C0+C1*G3+C2*G3*G3

print("p3",P3)
P4G = 0.85714*(P1+Q)/(T4-T3)
# print("P4G:",P4G)
P4 = calc_p4(P4G,TS)
print("p4:",P4)

print(str(P1)+"、"+str(P2)+"、"+str(P3)+"、"+str(P4[0]))
print("MINP:",P1+P2+P3+P4)

