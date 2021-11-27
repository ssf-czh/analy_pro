# -*- coding: utf-8 -*-
"""main.py"""
import geatpy as ea # import geatpy
from MyPro import MyProblem # 导入自定义问题接口
import numpy as np
import random as rd
"""===============================实例化问题对象================================"""
problem = MyProblem(562.8,10) # 生成问题对象

# 2814
# 2532.6
# 2251.2
# 1969.8
# 1688.4
# 1407
# 1125.6
# 844.2
# 562.8
# 281.4

"""==================================种群设置=================================="""
# Encoding = 'BG'       # 编码方式
Encoding = 'RI'       # 编码方式
NIND = 100           # 种群规模
Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) # 创建区域描述器
population = ea.Population(Encoding, Field, NIND) # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
"""================================算法参数设置================================="""
# myAlgorithm = ea.soea_EGA_templet(problem, population) # 实例化一个算法模板对象
# myAlgorithm = ea.soea_studGA_templet(problem, population) # 实例化一个算法模板对象
# myAlgorithm = ea.soea(problem, population) # 实例化一个算法模板对象
# myAlgorithm = ea.soea_DE_best_1_bin_templet(problem, population) # 实例化一个算法模板对象
myAlgorithm = ea.soea_DE_best_1_L_templet(problem, population) # 实例化一个算法模板对象
myAlgorithm.mutOper.F = 0.5 #差分进化中的参数F
myAlgorithm.mutOper.pm = 0.2
myAlgorithm.recOper.XOVR = 0.7  #设置交叉概率

myAlgorithm.MAXGEN = 1 # 最大进化代数
myAlgorithm.logTras = 2  # 设置每隔多少代记录日志，若设置成0则表示不记录日志
myAlgorithm.verbose = True  # 设置是否打印输出日志信息
myAlgorithm.drawing = 1  # 设置绘图方式（0：不绘图；1：绘制结果图；2：绘制目标空间过程动画；3：绘制决策空间过程动画）

# ============启发式初始化种群==========
# 6 < T1 < 10
# 10 < T2 < 20
# 21 < T3 < 33
# 25 < T4 < 39

# 4 < T2 - T1 < 10       （4）
# 4 < T4 - T3 < 6；    （5）
initial_chrome = np.zeros((NIND,4))
for i in range(NIND):
    T1 = rd.uniform(6,10)
    T2_MIN =  max(4+T1,10)
    T2_MAX =  min(10+T1,20)
    T2 = rd.uniform(T2_MIN,T2_MAX)
    T3 = rd.uniform(21,33)
    T4_MIN = max(4+T3,25)
    T4_MAX = min(6+T3,39)
    T4 = rd.uniform(T4_MIN,T4_MAX)
    initial_chrome[i][0]=T1
    initial_chrome[i][1]=T2
    initial_chrome[i][2]=T3
    initial_chrome[i][3]=T4

# print(initial_chrome)
popPhet = ea.Population(Encoding, Field, NIND, initial_chrome)
myAlgorithm.call_aimFunc(popPhet)
# ======================================
"""===========================调用算法模板进行种群进化==============--==========="""
[BestIndi, population] = myAlgorithm.run(popPhet)  # 执行算法模板，得到最优个体以及最后一代种群
# [BestIndi, population] = myAlgorithm.run()  # 执行算法模板，得到最优个体以及最后一代种群
BestIndi.save()  # 把最优个体的信息保存到文件中
"""==================================输出结果=================================="""
print('用时：%f 秒' % myAlgorithm.passTime)
print('评价次数：%d 次' % myAlgorithm.evalsNum)
if BestIndi.sizes != 0:
    # print(BestIndi.sizes)
    print('最优的目标函数值为：%s' % BestIndi.ObjV[0][0])
    print('最优的控制变量值为：')
    for i in range(BestIndi.sizes):
        print(BestIndi.Phen[i,:])

else:
    print('没找到可行解。')