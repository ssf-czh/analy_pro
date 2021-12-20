import numpy as np

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import csv
import math
from model import schema


class PumpFitting():
    def __init__(self):
# ======================拟合结果
        self.B = [1]*24
        self.A = [1]*3
        self.C = [1]*3
        self.D = [1]*3
        self.E = [1]*4

    def func_P1(self,T,B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17,B18,B19,B20,B21,B22,B23):
        '''
            T相当于自变量X
            B相当于参数W
            '''
        T1, T2, T3, T4, Q = T
        P1 = B0 + B1 * T1 + B2 * T2 + B3 * Q + B4 * Q * Q + B5 * T1 * T1 + B6 * T2 * T2 + B7 * Q * T1 + B8 * Q * T2 + B9 * T1 * T2 + B10 * T3 + B11 * T4 + B12 * T3 * T3 + B13 * T4 * T4 + B14 * Q * T3 + B15 * Q * T4 + B16 * T3 * T4 + B17 * (
                T2 - T1) + B18 * (T4 - T3) + B19 * (T2 - T1) * (T2 - T1) + B20 * (T4 - T3) * (T4 - T3) + B21 * Q * (
                     T2 - T1) + B22 * Q * (T4 - T3) + B23 * (T2 - T1) * (T4 - T3)
        return P1

    def fit_P1(self,P1_data):
        temp_T1 = []
        temp_T2 = []
        temp_T3 = []
        temp_T4 = []
        temp_Q = []
        temp_P = []
        for i in P1_data:
            temp_T1.append(i.t1)
            temp_T2.append(i.t2)
            temp_T3.append(i.t3)
            temp_T4.append(i.t4)
            temp_Q.append(i.q)
            temp_P.append(i.p1)
        T1 = np.array(temp_T1)
        T2 = np.array(temp_T2)
        T3 = np.array(temp_T3)
        T4 = np.array(temp_T4)
        Q = np.array(temp_Q)
        P1 = np.array(temp_P)
        a, b = curve_fit(self.func_P1, (T1, T2, T3, T4, Q), P1)
        for i in range(len(a)) :
            a[i] = round(a[i],4)
        self.B = list(a)
        return a

    def func_P2(self,G2,A0,A1,A2):
        '''
            :param G2: 自变量x
            :param A0: 待拟合参数
            :param A1:
            :param A2:
            :return:
            '''
        P2 = A0 + A1 * G2 + A2 * G2 * G2
        return P2


    def fit_P2(self,P2_data):
        temp_G2 = []
        temp_P2 = []
        for i in P2_data:
            temp_G2.append(i.g2)
            temp_P2.append(i.p2)
        G2 = np.array(temp_G2)
        P2 = np.array(temp_P2)
        a, b = curve_fit(self.func_P2, G2, P2)
        for i in range(len(a)):
            a[i] = round(a[i], 4)
        self.A = a
        return a


    def func_P3(self,G3,C0,C1,C2):
        '''
            :param G3: 自变量x
            :param C0: 待拟合参数
            :param C1:
            :param C2:
            :return:
            '''
        P3 = C0 + C1 * G3 + C2 * G3 * G3
        return P3

    def fit_P3(self,P3_data):
        temp_P3 = []
        temp_G3 = []
        for i in P3_data:
            temp_P3.append(i.p3)
            temp_G3.append(i.g3)
        G3 = np.array(temp_G3)
        P3 = np.array(temp_P3)

        a, b = curve_fit(self.func_P3, G3, P3)
        for i in range(len(a)) :
            a[i] = round(a[i],4)
        self.C = a
        return a


    def func_Tdelta(self,T,D0,D1,D2):
        '''
        T相当于自变量X
        B相当于参数W
        拟合D0-D2
        '''
        # TS,G = T
        TS = T
        Tdelta = D0+D1*TS+D2*TS*TS
        return Tdelta

    def fit_Tdelta(self,WetBulb_data):
        temp_Tdelta = []
        temp_TS = []
        for i in WetBulb_data:
            temp_Tdelta.append(i.amplitude)
            temp_TS.append(i.temp)
        TS = np.array(temp_TS)
        Tdelta = np.array(temp_Tdelta)
        a, b = curve_fit(self.func_Tdelta, (TS), Tdelta)
        for i in range(len(a)) :
            a[i] = round(a[i],4)
        self.D = a
        return a

    def func_P4(self,T, E0, E1, E2, E3):
        '''
        T相当于自变量X
        B相当于参数W
        拟合E0-E3
        '''
        # TS,G = T
        G3 = T
        P4 = E0 + E1 * G3 + E2 * G3 * G3 + E3 * G3 * G3 * G3
        return P4

    def fit_P4(self,P4_data):
        temp_G3_P4 = []
        temp_P4 = []
        for i in P4_data:
            temp_G3_P4.append(i.g)
            temp_P4.append(i.p4)
        G3_P4 = np.array(temp_G3_P4)
        P4 = np.array(temp_P4)
        a, b = curve_fit(self.func_P4, (G3_P4), P4)
        for i in range(len(a)) :
            a[i] = round(a[i],4)
        self.E = a
        return a




