import numpy as np
import numpy_financial as npf


# eq = 100000
# DC = DirectCosts(eq)
# IDC = IndirectCosts(eq)
# CI = CapitalInvestment(eq)
# print(DC.TDC_Totaldirectcosts())f
# print(IDC.TIC_Totalindirectcosts())
# print(CI.TCI_Totalcapitalinvestment())

# 现金流量折现分析 discount cash  flow analysis
# NPV:净现值
# IRR：内部收益率
# AD：摊销期限
# T:运行寿命(30)
# I0:t0时的投资成本
# i：贴现率
# datalist:初始资本支出+每一年的(Et-At)(收入-支出)：[-100, 20, 30, 40, 50, 60]

class NPV_Cal:
    def __init__(self, i, datalist = None):
        if datalist is None:
            datalist = []
        self.i = i
        self.datalist = datalist

    def NPV(self):
        npv = npf.npv(self.i, self.datalist)
        print(f"净现值NPV：{npv}")
        return npv

    def AD(self):
        n = 1
        y = self.datalist[0]
        for x in self.datalist[1:]:
            y += x / (1 + self.i) ** n
            if y < 0:
                n += 1
            else:
                break
        print(f"摊销期限AD：第{n}年")
        return n

    def IRR(self):
        irr = npf.irr(self.datalist)
        print(f"内部收益率IRR：{irr}")
        return irr


proj = NPV_Cal(0.08, [-100, 20, 30, 40, 50, 60])
proj.NPV()
proj.AD()
proj.IRR()
