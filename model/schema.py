class InitialParameters:
    q = 2814.0
    n = 3
    efficiency_range = (30.0, 80.0)
    t3_min = 21.0
    g = 533.0
    h = 41.0
    p2 = 90.0
    # t2-t1
    delta_t1_range = (4.0, 10.0)
    # t4-t3
    delta_t2_range = (4.0, 10.0)


class MainFitting:
    load_percentage = 100.0
    q = 0.0
    p1 = 0.0
    t1 = 0.0
    t2 = 0.0
    t3 = 0.0
    t4 = 0.0


class Pump2Fitting:
    g2 = 0.0
    p2 = 0.0


class Pump3Fitting:
    g3 = 0.0
    p3 = 0.0


class WetBulbFitting:
    temp = 0.0
    # 冷幅
    amplitude = 0.0


class P4Fitting:
    g = 0.0
    p4 = 0.0


class FittingCoefficients:
    a = []  # 0-2
    b = []  # 0-23
    c = []  # 0-2
    d = []  # 0-2
    e = []  # 0-3


class OptimizeResult:
    q = 2814.0
    ts = 0.0
    load_percentage = 0.0
    t1 = 0.0
    t2 = 0.0
    t3 = 0.0
    t4 = 0.0
    delta_t = 0.0
    p1 = 0.0
    p2 = 0.0
    p3 = 0.0
    p4 = 0.0
    p = 0.0
    cop = 0.0
    # 开启台数
    n = 0
