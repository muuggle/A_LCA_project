import random
import pandas as pd
import docplex.mp.model as cpx

# I = [x for x in range(11)]
#
# s = 10.36
# h = 15.44
# t_lu = 4.10
# t_d = 0.051
#
# e_h = 160
# e_tr = 1.15
#
# g_h = 12.79
# g_tr = 0.119
#
# alpha = 0.0225
# beta = 0.144
#
# b_inv = 27993.4
# H = 230.88
#
# cij = 0
# for i in I:
#     # cij += (10.36 + 15.44 + 4.10 + 0.051 * d[i]) * q[i]
#     cij += (29.9 + 0.051 * d[i]) * q[i]
#
# eij = 0
# for i in I:
#     eij += (160 + 1.15 * d[j]) * q[i]
#
# gij = 0
# for i in I:
#     eij += (12.79 + 0.119 * d[i]) * q[i]
#
# c_inv_j = 6463116.2
#
# C = cij + 6463116.2 + eij * 0.0225 + gij * 0.144

opt_model = cpx.Model(name = "MINP Model")

n = 11  # 供应点
m = 6  # 选择点
set_I = range(1, n + 1)
set_J = range(1, m + 1)
list_obj = []
list_lb = []
list_ub = []
obj = {(i, j): list_obj.pop(0) for i in set_I for j in set_J}  # 目标函数的系数
lb = {(i, j): list_lb.pop(0) for i in set_I for j in set_J}  # 变量的约束条件下限
ub = {(i, j): list_ub.pop(0) for i in set_I for j in set_J}  # 变量的约束条件上限
a = {(i, j): random.normalvariate(0, 5) for i in set_I for j in set_J}  # 约束函数的系数
b = {j: random.randint(0, 30) for j in set_J}  # 约束函数的条件上限/下限

# 定义决策变量(上下界限)
# if x is Continuous
x_vars = {(i, j): opt_model.continuous_var(lb = lb[i, j], ub = ub[i, j],
                                           name = f"x_{i}_{j}")
          for i in set_I for j in set_J}

# 定义约束条件
constraints = {j: opt_model.add_constraint(ct = opt_model.sum(a[i, j] * x_vars[i, j] for i in set_I) <= b[j],
                                           ctname = f"constraint_{j}")
               for j in set_J}

# 目标函数
objective = opt_model.sum(x_vars[i, j] * obj[i, j] for i in set_I for j in set_J)

opt_model.minimize(objective)

# 求解
opt_model.solve()

# 获得结果
