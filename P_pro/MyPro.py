# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""

    目标：max f = 21.5 + x1 * np.sin(4 * np.pi * x1) + x2 * np.sin(20 * np.pi * x2)
    约束条件：
        6<T1<10
        10<T2<20
        21<T3<33
        25<T4<39

            # 4 < T2 - T1 < 10       （4）
            # 4 < T4 - T3 < 6；    （5）

        P1=B0+B1*T1+B2*T2+B3*Q+B4*Q*Q+B5*T1*T1+B6*T2*T2+B7*Q*T1+B8*Q*T2+B9*T1*T2+B10*T3+B11*T4+B12*T3*T3+B13*T4*T4+B14*Q*T3+B15*Q*T4+B16*T3*T4+B17*(T2-T1)+B18*(T4-T3)+B19*(T2-T1)*(T2-T1)+B20*(T4-T3)*(T4-T3)+B21*Q*(T2-T1)+B22*Q*(T4-T3)+B23*(T2-T1)*(T4-T3)。

        G2=Q/(4.2*(T2-T1)*1000)
        P2=A0+A1*G2+A2*G2*G2。

        G3=(Q+P1)/(4.2*(T4-T3)*1000)
        P3=C0+C1*G3+C2*G3*G3

        P4=69.8978*(P1+Q)/(T4-T3)*(P1+Q)/(T4-T3)+83.7279*(P1+Q)/(T4-T3)+0.1554。

        Minf(P)=P1+P2+P3+P4；
————————————————
版权声明：本文为CSDN博主「Strong_wind」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_37790882/article/details/84034956
"""


import numpy as np
import geatpy as ea
import pandas as pd
import xgboost as xgb

class MyProblem(ea.Problem): # 继承Problem父类
    def __init__(self, Q,TS):
        self.Q = Q #热量
        self.TS = TS
        B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17,B18,B19,B20,B21,B22,B23 =  1.25592470e+02,  5.39445250e+01, -5.22395970e+01,  6.29397302e-02, -2.06962469e-05, -3.33850530e+01, -3.30937615e+01,  1.13915116e+02, -1.13920754e+02,  6.62996700e+01, -5.43024482e+01,  4.63683510e+01, -2.01032174e+03, -2.00895336e+03,  1.97466857e+02, -1.97464621e+02,  4.01945845e+03,  5.63936524e+01, -9.05705574e+01,  3.25980615e+01,  2.00722896e+03,  1.13929510e+02,  1.97486520e+02, -3.39669822e+00
        A0,A1,A2 = 1.05105606e+02,-6.08574731e-01,1.03989940e-03
        C0,C1,C2 = -5.40003853e+01,2.96859204e-01,-2.09088412e-04

        name = 'MyProblem' # 初始化name（函数名称，可以随意设置）
        M = 1 # 初始化M（目标维数）
        maxormins = [1] # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = 4 # 初始化Dim（决策变量维数）
        varTypes = [0] * Dim # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [6,10,21,25] # 决策变量下界
        ub = [10,20,33,39] # 决策变量上界
        lbin = [1,1,1,1]  # 决策变量下边界
        ubin = [1,1,1,1]  # 决策变量上边界
        # 调用父类构造方法完成实例化

        # 计算P4 xgboost模型=============================
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
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

        self.model_p4 = xgb.XGBRegressor()
        self.model_p4.fit(X, y)  # 使用训练数据训练
        # print(model_c.score(X_test, y_test))


        # ===========================

        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop): # 目标函数
        Vars = pop.Phen
        T1 = pop.Phen[:, [0]] # 获取表现型矩阵的第一列，得到所有个体的x1的值
        T2 = pop.Phen[:, [1]]
        T3 = pop.Phen[:, [2]]
        T4 = pop.Phen[:, [3]]
        # ==========================================
        # 6 < T1 < 10
        # 10 < T2 < 20
        # 21 < T3 < 33
        # 25 < T4 < 39
        # T1_x = sum(T1<6)+sum(T1>10)
        # T2_x = sum(T2<10)+sum(T2>20)
        # T3_x = sum(T3<21)+sum(T3>33)
        # T4_x = sum(T4<25)+sum(T4>39)
        #
        #
        # if T1_x > 0:
        #     print("T1定义域出错")
        # if T2_x > 0:
        #     print("T2定义域出错")
        # if T3_x > 0:
        #     print("T3定义域出错")
        # if T4_x > 0:
        #     print("T4定义域出错")
        #
        #     # 4 < T2 - T1 < 10       （4）
        #     # 4 < T4 - T3 < 6；    （5）
        # constr1 = T2-T1
        # constr2 = T4-T3
        #
        # constr1_x = sum(constr1<4)+sum(constr1>10)
        # constr2_x = sum(constr1<4)+sum(constr1>6)
        # if constr1_x > 0:
        #     print("T2-T1定义域出错{:s}".format(str(constr1_x)))
        # if constr2_x > 0:
        #     print("T4-T3定义域出错{:s}".format(str(constr2_x)))



        exIdx1 = np.where(T2 - T1 > 10)[0]  # 找到违反约束条件1的个体索引exIdx2 = np.where(x1+2*x3>2)[0]#找到违反约束条件2的个体索引exIdx3 = np.where(x1+x2+x3!=1)
        exIdx2 = np.where(T2 - T1 < 4)[0]  # 找到违反约束条件1的个体索引exIdx2 = np.where(x1+2*x3>2)[0]#找到违反约束条件2的个体索引exIdx3 = np.where(x1+x2+x3!=1)
        exIdx3 = np.where(T4 - T3 < 4)[0]  # 找到违反约束条件1的个体索引exIdx2 = np.where(x1+2*x3>2)[0]#找到违反约束条件2的个体索引exIdx3 = np.where(x1+x2+x3!=1)
        exIdx4 = np.where(T4 - T3 > 6)[0]  # 找到违反约束条件1的个体索引exIdx2 = np.where(x1+2*x3>2)[0]#找到违反约束条件2的个体索引exIdx3 = np.where(x1+x2+x3!=1)


        # ok_edIdx = ~ exIdx

        # =================================================
        Q = self.Q
        B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17,B18,B19,B20,B21,B22,B23 =  1.25592470e+02,  5.39445250e+01, -5.22395970e+01,  6.29397302e-02, -2.06962469e-05, -3.33850530e+01, -3.30937615e+01,  1.13915116e+02, -1.13920754e+02,  6.62996700e+01, -5.43024482e+01,  4.63683510e+01, -2.01032174e+03, -2.00895336e+03,  1.97466857e+02, -1.97464621e+02,  4.01945845e+03,  5.63936524e+01, -9.05705574e+01,  3.25980615e+01,  2.00722896e+03,  1.13929510e+02,  1.97486520e+02, -3.39669822e+00
        A0,A1,A2 = 1.05105606e+02,-6.08574731e-01,1.03989940e-03
        C0,C1,C2 = -5.40003853e+01,2.96859204e-01,-2.09088412e-04

        P1=B0+B1*T1+B2*T2+B3*Q+B4*Q*Q+B5*T1*T1+B6*T2*T2+B7*Q*T1+B8*Q*T2+B9*T1*T2+B10*T3+B11*T4+B12*T3*T3+B13*T4*T4+B14*Q*T3+B15*Q*T4+B16*T3*T4+B17*(T2-T1)+B18*(T4-T3)+B19*(T2-T1)*(T2-T1)+B20*(T4-T3)*(T4-T3)+B21*Q*(T2-T1)+B22*Q*(T4-T3)+B23*(T2-T1)*(T4-T3)
        # print("P1 value ")
        # print(P1)
        edIdx_P1 = np.where(P1<0)[0]
        # print(P1)
        # print(edIdx_P1)
        print("P1>0的决策变量：", pop.Phen[np.where(P1>0)[0][:5]])
        print("P1<0的决策变量：",pop.Phen[edIdx_P1[:5]])
        print("P1<0: ",len(edIdx_P1))


        G2=6*Q/(7*(T2-T1))
        P2 = A0 + A1 * G2 + A2 * G2 * G2
        # print("P2 value ")
        # print(P2)
        edIdx_P2 = np.where(P2<0)[0]
        print("P2<0: ",len(edIdx_P2))

        # A0, A1, A2 = 1.05105606e+02, -6.08574731e-01, 1.03989940e-03
        # C0, C1, C2 = -5.40003853e+01, 2.96859204e-01, -2.09088412e-04
        G3=6*(Q+P1)/(7*(T4-T3))
        P3 = C0 + C1 * G3 + C2 * G3 * G3
        edIdx_P3 = np.where(P3<0)[0]
        print("P3<0: ",len(edIdx_P3))

        # print("P3 value ")
        # print(P3)

        G = 0.85714*(P1+Q)/(T4-T3)
        TS = np.ones(len(T4))* self.TS



        temp = np.hstack((TS.reshape(-1,1),G))
        # print("======")
        # print(temp)
        P4 = self.model_p4.predict(temp)


        # print(P1)
        # print(P2.shape)
        # print(len(P3))
        # print(len(P4))
        # print("P4 value ")
        # print(P4)
        P4 = P4.reshape((-1,1))
        edIdx_P4 = np.where(P4 < 0)[0]
        print("P4<0: ",len(edIdx_P4))

        # print(np.hstack([exIdx1, exIdx2, exIdx3, exIdx4, edIdx_P1, edIdx_P2, edIdx_P3, edIdx_P4]))
        # exIdx = np.unique(np.hstack([exIdx1, exIdx2, exIdx3, exIdx4, edIdx_P1, edIdx_P2, edIdx_P3, edIdx_P4]))
        # print(len(exIdx))
        exIdx = np.unique(np.hstack([exIdx1, exIdx2, exIdx3, exIdx4]))
        print("违反定义域约束条件的：",len(np.unique(np.hstack([exIdx1, exIdx2, exIdx3, exIdx4]))))
        print("违反P>0约束条件的：",len(np.unique(np.hstack([edIdx_P1, edIdx_P2, edIdx_P3, edIdx_P4]))))
        print("违反所有约束条件的：",len(exIdx))
        print("=="*15)
        P = P1+P2+P3+P4

        # print(min(P[ok_edIdx]))
        # print("Sum P value ")
        # print(P.size)

        # pop.CV = np.hstack([T1-T2+4,T2-T1-10,T3-T4+4,T4-T3+6])


        # pop.CV = np.hstack([2*x1 + x2 - 1,x1 + 2*x3 - 2,np.abs(x1 + x2 + x3 - 1)])#第三个约束
        alpha = 100 # 惩罚缩放因子
        beta = 1# 惩罚最小偏移量
        P[exIdx] += self.maxormins[0] * alpha * (np.max(P) - np.min(P) + beta)
        pop.ObjV = P



        # pop.ObjV[exIdx] = max(P)+1
        # print("objV")
        # print(pop.ObjV)
        # print(min(P))
