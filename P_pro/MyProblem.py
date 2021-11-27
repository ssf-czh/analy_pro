# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""

    目标：max f = 21.5 + x1 * np.sin(4 * np.pi * x1) + x2 * np.sin(20 * np.pi * x2)
    约束条件：
        x1 != 10
        x2 != 5
        x1 ∈ [-3, 12.1] # 变量范围是写在遗传算法的参数设置里面

————————————————
版权声明：本文为CSDN博主「Strong_wind」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_37790882/article/details/84034956
"""

# import numpy as np
# import geatpy as ea
#
# class MyProblem(ea.Problem): # 继承Problem父类
#     def __init__(self):
#         name = 'MyProblem' # 初始化name（函数名称，可以随意设置）
#         M = 1 # 初始化M（目标维数）
#         maxormins = [-1] # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
#         Dim = 2 # 初始化Dim（决策变量维数）
#         varTypes = [0] * Dim # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
#         lb = [-3, 4.1] # 决策变量下界
#         ub = [12.1, 5.8] # 决策变量上界
#         lbin = [1] * Dim # 决策变量下边界
#         ubin = [1] * Dim # 决策变量上边界
#         # 调用父类构造方法完成实例化
#         ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
#
#     def aimFunc(self, pop): # 目标函数
#         x1 = pop.Phen[:, [0]] # 获取表现型矩阵的第一列，得到所有个体的x1的值
#         x2 = pop.Phen[:, [1]]
#         f = 21.5 + x1 * np.sin(4 * np.pi * x1) + x2 * np.sin(20 * np.pi * x2)
#         exIdx1 = np.where(x1 == 10)[0] # 因为约束条件之一是x1不能为10，这里把x1等于10的个体找到
#         exIdx2 = np.where(x2 == 5)[0]
#         pop.CV = np.zeros((pop.sizes, 2))
#         pop.CV[exIdx1, 0] = 1
#         pop.CV[exIdx2, 1] = 1
#         pop.ObjV = f # 计算目标函数值，赋值给pop种群对象的ObjV属性


# ============================================================================

import numpy as np
import geatpy as ea

class MyProblem(ea.Problem): # 继承Problem父类
    def __init__(self):
        name = 'MyProblem' # 初始化name（函数名称，可以随意设置）
        M = 1 # 初始化M（目标维数）
        maxormins = [-1] # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = 3 # 初始化Dim（决策变量维数）
        varTypes = [0] * Dim # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [0, 0,0] # 决策变量下界
        ub = [1, 1,2] # 决策变量上界
        lbin = [1,1,0]  # 决策变量下边界
        ubin = [1,1,0]  # 决策变量上边界
        # 调用父类构造方法完成实例化




        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop): # 目标函数
        Vars = pop.Phen
        x1 = pop.Phen[:, [0]] # 获取表现型矩阵的第一列，得到所有个体的x1的值
        x2 = pop.Phen[:, [1]]
        x3 = pop.Phen[:, [2]]
        f = 4*x1+2*x2+x3

        pop.CV = np.hstack([2*x1 + x2 - 1,x1 + 2*x3 - 2,np.abs(x1 + x2 + x3 - 1)])#第三个约束
        pop.ObjV = f # 计算目标函数值，赋值给pop种群对象的ObjV属性