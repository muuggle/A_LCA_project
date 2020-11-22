#########################################
# import cplex
# from cplex.exceptions import CplexError
#
# my_obj = [1, 2, 3, 1]
# my_ub = [40, cplex.infinity, cplex.infinity, 3]
# my_lb = [0.0, 0.0, 0.0, 2.0]
# my_ctype = "CCCI"
# my_colnames = ["x1", "x2", "x3", "x4"]
# my_rhs = [20.0, 30.0, 0.0]
# my_rownames = ["r1", "r2", "r3"]
# my_sense = "LLE"
#
#
# def populatebyrow(prob):
#     prob.objective.set_sense(prob.objective.sense.maximize)
#
#     prob.variables.add(obj = my_obj, lb = my_lb, ub = my_ub, types = my_ctype,
#                        names = my_colnames)
#     rows = [[["x1", "x2", "x3", "x4"], [-1.0, 1.0, 1.0, 10.0]],
#             [["x1", "x2", "x3"], [1.0, -3.0, 1.0]],
#             [["x2", "x4"], [1.0, -3.5]]]
#     prob.linear_constraints.add(lin_expr = rows, senses = my_sense,
#                                 rhs = my_rhs, names = my_rownames)
#
#
# try:
#     my_prob = cplex.Cplex()
#     handle = populatebyrow(my_prob)
#     my_prob.solve()
# except CplexError as exc:
#     print(exc)
#
# print()
# # solution.get_status() returns an integer code
# print("Solution status = ", my_prob.solution.get_status(), ":", end=' ')
# # the following line prints the corresponding string
# print(my_prob.solution.status[my_prob.solution.get_status()])
# print("Solution value  = ", my_prob.solution.get_objective_value())
#
# numcols = my_prob.variables.get_num()
# numrows = my_prob.linear_constraints.get_num()
#
# slack = my_prob.solution.get_linear_slacks()
# x = my_prob.solution.get_values()
#
# print('x: ')
# print(x)

#########################################
# 导入cplex
# import cplex
# from cplex.exceptions import CplexError
#
# my_obj = [3.0, 1.0, 3.0]  # 目标函数系数
# my_ctype = 'ICI'  # 目标函数变量的类型，一般就是C,整数类型就是I就是integer
# my_ub = [cplex.infinity, cplex.infinity, 1]  # 变量的约束条件上限
# my_lb = [0, 0, 0]  # 变量的约束条件下限
# my_colnames = ['x1', 'x2', 'x3']  # column names列向量的名字
# my_rhs = [4.0, 2.0, 3.0]  # 约束条件的值相当于b
# my_rownames = ['r1', 'r2', 'r3']  # row names行向量的名字
# # 是约束条件的形式，L为小于号“less-than”,大于号是‘G’，即'greater than'
# my_sense = 'LLL'
#
#
# def populatebyrow(prob):
#     # 设置目标函数类型：求max or min
#     prob.objective.set_sense(prob.objective.sense.maximize)
#     # 设置（增加）变量，明确目标函数，约束条件上限、下限，变量类型，还有变量名称
#     prob.variables.add(obj = my_obj, lb = my_lb, ub = my_ub, types = my_ctype,
#                        names = my_colnames)
#     # 对应的约束方程
#     rows = [[['x1', 'x2', 'x3'], [-1.0, 2.0, 1.0]],
#             [['x2', 'x3'], [4.0, -3.0]],
#             [['x1', 'x2', 'x3'], [1.0, -3.0, 2.0]]]
#     # 设置（增加）约束条件
#     prob.linear_constraints.add(lin_expr = rows, senses = my_sense,
#                                 rhs = my_rhs, names = my_rownames)
#
#
# # 初始化模型
# my_prob = cplex.Cplex()
# # 计算
# handle = populatebyrow(my_prob)
# # 求解
# my_prob.solve()
# # 输出结果
# print(my_prob.solution.get_objective_value())
# x = my_prob.solution.get_values()
# print(x)
#########################################

import random
import pandas as pd
import docplex.mp.model as cpx

opt_model = cpx.Model(name = "MIP Model")

n = 10
m = 5
set_I = range(1, n + 1)
set_J = range(1, m + 1)
c = {(i, j): random.normalvariate(0, 1) for i in set_I for j in set_J}
a = {(i, j): random.normalvariate(0, 5) for i in set_I for j in set_J}
l = {(i, j): random.randint(0, 10) for i in set_I for j in set_J}
u = {(i, j): random.randint(10, 20) for i in set_I for j in set_J}
b = {j: random.randint(0, 30) for j in set_J}

# 定义决策变量
# if x is Continuous
x_vars = {(i, j): opt_model.continuous_var(lb = l[i, j], ub = u[i, j],
                                           name = f"x_{i}_{j}")
          for i in set_I for j in set_J}

# if x is Binary
# x_vars = {(i, j): opt_model.binary_var(name = "x_{0}_{1}".format(i, j))
#           for i in set_I for j in set_J}

# if x is Integer
# x_vars = {(i, j): opt_model.integer_var(lb = l[i, j], ub = u[i, j],
#                                         name = "x_{0}_{1}".format(i, j))
#           for i in set_I for j in set_J}

# 约束条件
# <= constraints，小于等于
constraints = {j: opt_model.add_constraint(
    ct = opt_model.sum(a[i, j] * x_vars[i, j] for i in set_I) <= b[j],
    ctname = f"constraint_{j}") for j in set_J}

# >= constraints
# constraints = {j: opt_model.add_constraint(
#     ct = opt_model.sum(a[i, j] * x_vars[i, j] for i in set_I) >= b[j],
#     ctname = "constraint_{0}".format(j))
#     for j in set_J}

# == constraints
# constraints = {j: opt_model.add_constraint(
#     ct = opt_model.sum(a[i, j] * x_vars[i, j] for i in set_I) == b[j],
#     ctname = "constraint_{0}".format(j))
#     for j in set_J}

# 目标函数
objective = opt_model.sum(x_vars[i, j] * c[i, j] for i in set_I for j in set_J)

# for maximization
opt_model.maximize(objective)

# for minimization
# opt_model.minimize(objective)

# 求解模型
# solving with local cplex
opt_model.solve()

# solving with cplex cloud
# opt_model.solve(url="your_cplex_cloud_url", key="your_api_key")

# 获得结果
opt_df = pd.DataFrame.from_dict(x_vars, orient = "index", columns = ["variable_object"])

opt_df.index = pd.MultiIndex.from_tuples(opt_df.index, names = ["column_i", "column_j"])
opt_df.reset_index(inplace = True)

# CPLEX
opt_df["solution_value"] = opt_df["variable_object"].apply(lambda item: item.solution_value)

opt_df.drop(columns = ["variable_object"], inplace = True)
opt_df.to_csv("./optimization_solution.csv")
