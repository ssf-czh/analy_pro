import base64

from model.schema import *
from typing import List
from template import template_file_base64
import openpyxl
import os

init_params = InitialParameters()
main_fittings: List[MainFitting] = list()
pump2_fittings: List[Pump2Fitting] = list()
pump3_fittings: List[Pump3Fitting] = list()
wet_bulb_fittings: List[WetBulbFitting] = list()
p4_fittings: List[P4Fitting] = list()
fitting_coefficients = FittingCoefficients()
optimize_result: List[OptimizeResult] = list()


def load(path: str):
    global init_params, main_fittings, pump2_fittings, pump3_fittings, wet_bulb_fittings, p4_fittings, \
        fitting_coefficients, optimize_result
    if not os.path.exists(path):
        save_default(path)
    wb = openpyxl.load_workbook(path, read_only=True)
    for sheet in wb:
        if sheet.title == "参数初始值设定":
            init_params.q = float(sheet["B4"].value)
            init_params.n = int(sheet["B5"].value)
            init_params.efficiency_range = (float(sheet["B6"].value), float(sheet["C6"].value))
            init_params.t3_min = float(sheet["B7"].value)
            init_params.g = float(sheet["B9"].value)
            init_params.h = float(sheet["B10"].value)
            init_params.p2 = float(sheet["B11"].value)
            init_params.delta_t1_range = (float(sheet["B24"].value), float(sheet["C24"].value))
            init_params.delta_t2_range = (float(sheet["B25"].value), float(sheet["C25"].value))
        elif sheet.title == "主机参数拟合":
            main_fittings = list()
            i = 3
            while sheet.cell(i, 1).value is not None:
                entry = MainFitting()
                entry.load_percentage = float(sheet.cell(i, 1).value)
                entry.q = float(sheet.cell(i, 2).value)
                entry.p1 = float(sheet.cell(i, 3).value)
                entry.t1 = float(sheet.cell(i, 4).value)
                entry.t2 = float(sheet.cell(i, 5).value)
                entry.t3 = float(sheet.cell(i, 6).value)
                entry.t4 = float(sheet.cell(i, 7).value)
                entry.cop = float(sheet.cell(i, 8).value)
                main_fittings.append(entry)
                i += 1
        elif sheet.title == "水泵性能参数拟合":
            pump2_fittings = list()
            for i in range(5):
                entry = Pump2Fitting()
                entry.g2 = float(sheet.cell(4, 3 + i * 2).value)
                entry.p2 = float(sheet.cell(4, 4 + i * 2).value)
                pump2_fittings.append(entry)

            pump3_fittings = list()
            for i in range(5):
                entry = Pump3Fitting()
                entry.g3 = float(sheet.cell(11, 3 + i * 2).value)
                entry.p3 = float(sheet.cell(11, 4 + i * 2).value)
                pump3_fittings.append(entry)
        elif sheet.title == "冷却塔拟合":
            i = 0
            wet_bulb_fittings = list()
            while sheet.cell(3 + i, 1).value is not None:
                entry = WetBulbFitting()
                entry.temp = float(sheet.cell(3 + i, 1).value)
                entry.amplitude = float(sheet.cell(3 + i, 2).value)
                wet_bulb_fittings.append(entry)
                i += 1

            i = 0
            p4_fittings = list()
            while sheet.cell(3 + i, 4).value is not None:
                entry = P4Fitting()
                entry.g = float(sheet.cell(3 + i, 4).value)
                entry.p4 = float(sheet.cell(3 + i, 5).value)
                p4_fittings.append(entry)
                i += 1
        elif sheet.title == "拟合系数表":
            # TODO 需要读入吗？
            pass
        elif sheet.title == "优化计算结果":
            optimize_result = list()
            i = 0
            while sheet.cell(2 + i, 1).value is not None:
                entry = OptimizeResult()
                entry.q = float(sheet.cell(2 + i, 1).value)
                entry.ts = float(sheet.cell(2 + i, 2).value)
                optimize_result.append(entry)
                i += 1


def save_default(path: str):
    with open(path, "wb") as f:
        data = base64.decodebytes(bytes(template_file_base64, "utf-8"))
        f.write(data)
        f.close()
