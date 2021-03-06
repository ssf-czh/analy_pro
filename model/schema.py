class InitialParameters:
    def __init__(self):
        self.calcType = 0 #计算类型
        self.lengque_maxn = 4 #冷却水泵最大台数
        self.q = 2814.0
        self.n = 3
        self.efficiency_range = 80.0
        self.t3_min = 21.0
        self.h = 41.0
        self.p2 = 90.0
        # t2-t1
        self.delta_t1_range = (4.0, 10.0)
        # t4-t3
        self.delta_t2_range = (4.0, 10.0)
        self.q_min = 422.0
        self.p20 = 90.0
        self.mu = 0.6
        self.lamb = 0.65
        self.load_rat = [100, 95, 90, 85, 80, 75, 70, 65, 60]
        self.t1_range = []
        self.P0 = 22.0
        self.G20 = 533.0
        self.G30 = 650.0
        self.yuzhi= 5

class MainFitting:
    def __init__(self):
        self.load_percentage = 100.0
        self.q = 0.0
        self.p1 = 0.0
        self.t1 = 0.0
        self.t2 = 0.0
        self.t3 = 0.0
        self.t4 = 0.0
        self.cop = 0.0


class Pump2Fitting:
    def __init__(self):
        self.g2 = 0.0
        self.p2 = 0.0


class Pump3Fitting:
    def __init__(self):
        self.g3 = 0.0
        self.p3 = 0.0


class WetBulbFitting_1to1:
    def __init__(self):
        self.temp = 0.0
        # 冷幅
        self.amplitude = 0.0

class WetBulbFitting_2to1:
    def __init__(self):
        self.temp = 0.0
        # 冷幅
        self.amplitude = 0.0

class WetBulbFitting_3to1:
    def __init__(self):
        self.temp = 0.0
        # 冷幅
        self.amplitude = 0.0

class WetBulbFitting_4to1:
    def __init__(self):
        self.temp = 0.0
        # 冷幅
        self.amplitude = 0.0

class WetBulbFitting_3to2:
    def __init__(self):
        self.temp = 0.0
        # 冷幅
        self.amplitude = 0.0

class WetBulbFitting_4to3:
    def __init__(self):
        self.temp = 0.0
        # 冷幅
        self.amplitude = 0.0


class P4Fitting:
    def __init__(self):
        self.g = 0.0
        self.p4 = 0.0


class FittingCoefficients:
    def __init__(self):
        self.a = []  # 0-2
        self.b = []  # 0-23
        self.c = []  # 0-2
        self.d_1to1 = []  # 0-2
        self.d_2to1 = []  # 0-2
        self.d_3to1 = []  # 0-2
        self.d_4to1 = []  # 0-2
        self.d_3to2 = []  # 0-2
        self.d_4to3 = []  # 0-2
        self.e = []  # 0-3


class OptimizeResult:
    def __init__(self):
        self.q = 0.0
        self.ts = 0.0
        self.load_percentage = None
        self.system_load_percentage =None
        self.t1 = None
        self.t2 = None
        self.G2_lendong = None
        self.fluency_lendong = None

        self.t3 = None
        self.t4 = None
        self.G3_lenque = None
        self.fluency_lenque = None
        self.delta_t = None
        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.p = None
        self.cop = None
        # 开启台数
        self.n = 0
        self.year = ""
        self.mon = ""
        self.day = ""
        self.hour = ""


class QDeltaEntry:
    def __init__(self):
        self.year = "2021"
        self.mon = "1"
        self.day = "1"
        self.hour = "1"
        self.Q = "1"
        self.Ts = "1"
        self.T = "1"
