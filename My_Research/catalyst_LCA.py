import brightway2 as bw
import matplotlib.pyplot as plt
import pandas as pd
import bw2analyzer as bwa
import time

start_time = time.time()
# dataframe显示所有列
pd.set_option('display.max_columns', None)
# dataframe显示所有行
pd.set_option('display.max_rows', None)

bw.projects.set_current('catalyst_LCA')
bw.bw2setup()

# 导入ecoinvent数据库
'''
fpei36 = "D:\EcoinventDatabase\ecoinvent 3.6_apos_ecoSpold02\datasets"

if 'ecoinvent_3.6_apos' in bw.databases:
    print("Database has already been imported")
else:
    ei36 = bw.SingleOutputEcospold2Importer(fpei36, 'ecoinvent_3.6_apos', use_mp = False)
    ei36.apply_strategies()
    ei36.statistics()

    ei36.write_database()
'''

# 打印已有数据库
db = bw.Database('ecoinvent_3.6_apos')
catalyst_production_db = bw.Database("Database as dict")
print(bw.databases)
print('==========')

# 写入三种催化剂的生产流程
catalyst_data = {
    ("Database as dict", "code for Ni/Al2O3 Production"): {
        'name': 'Ni/Al2O3 Production',
        'unit': 'kg',
        'location': 'CN',
        'categories': 'None',
        'exchanges': [{
            'amount': 1,
            'input': ('ecoinvent_3.6_apos', '0a3bbb13b76cb85d1b2b1bd1cbfd8055'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 270.67,
            'input': ('ecoinvent_3.6_apos', '24b9c7d5a711a78e35795158f1a4a805'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kwh'}, {
            'amount': 8,
            'input': ('ecoinvent_3.6_apos', '7feb48123f27763f71625e7cab4fec78'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 0.125,
            'input': ('ecoinvent_3.6_apos', '8ade1246d35b0c0c2585f24b5e8e5de8'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 0.54,
            'input': ('ecoinvent_3.6_apos', 'db147a694a045e4af50e2acea55087a8'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 25.21,
            'input': ('ecoinvent_3.6_apos', 'b1686c432ea1f1830253f2614dd50ee4'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 7.8585,
            'input': ('ecoinvent_3.6_apos', 'f1b03bb592e62c3516df6aeb2413f0e5'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'tkm'}, {
            'amount': -0.051,
            'input': ('ecoinvent_3.6_apos', 'aa425badc8347b06e5bf02443a8b1477'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'm3'}
        ]
    },
    ("Database as dict", "code for Ni/MCM-41 Production"): {
        'name': 'Ni/MCM-41 Production',
        'unit': 'kg',
        'location': 'CN',
        'categories': 'None',
        'exchanges': [{
            'amount': 3.645,
            'input': ('ecoinvent_3.6_apos', '6ef9fd9414bb88359d1e7df6a0fd05cd'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 87.1,
            'input': ('ecoinvent_3.6_apos', '24b9c7d5a711a78e35795158f1a4a805'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kwh'}, {
            'amount': 8,
            'input': ('ecoinvent_3.6_apos', '7feb48123f27763f71625e7cab4fec78'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 0.125,
            'input': ('ecoinvent_3.6_apos', '8ade1246d35b0c0c2585f24b5e8e5de8'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 1,
            'input': ('ecoinvent_3.6_apos', 'db147a694a045e4af50e2acea55087a8'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 4.737,
            'input': ('ecoinvent_3.6_apos', 'e0ddb80cb8547d5df5578ce923458496'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 5.2977,
            'input': ('ecoinvent_3.6_apos', 'f1b03bb592e62c3516df6aeb2413f0e5'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'tkm'}, {
            'amount': 45.9,
            'input': ('ecoinvent_3.6_apos', '62e6bec7a26c4fccec4e571512163d3e'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': -0.0535,
            'input': ('ecoinvent_3.6_apos', 'aa425badc8347b06e5bf02443a8b1477'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'm3'}
        ]
    }, ("Database as dict", "code for Ni/ABC Production"): {
        'name': 'Ni/ABC Production',
        'unit': 'kg',
        'location': 'CN',
        'categories': 'None',
        'exchanges': [{
            'amount': 42,
            'input': ('ecoinvent_3.6_apos', '24b9c7d5a711a78e35795158f1a4a805'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kwh'}, {
            'amount': 8,
            'input': ('ecoinvent_3.6_apos', '7feb48123f27763f71625e7cab4fec78'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 0.125,
            'input': ('ecoinvent_3.6_apos', '8ade1246d35b0c0c2585f24b5e8e5de8'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit=': 'kg'}, {
            'amount': 1,
            'input': ('ecoinvent_3.6_apos', 'db147a694a045e4af50e2acea55087a8'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 8,
            'input': ('ecoinvent_3.6_apos', 'b1686c432ea1f1830253f2614dd50ee4'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 3.5,
            'input': ('ecoinvent_3.6_apos', 'e0ddb80cb8547d5df5578ce923458496'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 3.9625,
            'input': ('ecoinvent_3.6_apos', 'f1b03bb592e62c3516df6aeb2413f0e5'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'tkm'}, {
            'amount': 17,
            'input': ('ecoinvent_3.6_apos', '9c3b353728fe1bb34d53d575f42e7d61'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': 2,
            'input': ('ecoinvent_3.6_apos', '6123e2d07283909e6669f164a8ba4ad5'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'kg'}, {
            'amount': -0.0245,
            'input': ('ecoinvent_3.6_apos', 'aa425badc8347b06e5bf02443a8b1477'),
            'type': 'technosphere',
            'uncertainty type': 0,
            'unit': 'm3'}
        ]}}

# 向数据库写入数据
catalyst_production_db.write(catalyst_data)

print('==========')

# 打印三种工序并写入列表
catalyst_data_list = []

Ni_Al2O3_prod = [act for act in catalyst_production_db if 'Ni/Al2O3' in act['name']][0]
print(Ni_Al2O3_prod)
catalyst_data_list.append(Ni_Al2O3_prod)

Ni_MCM_41_prod = [act for act in catalyst_production_db if 'Ni/MCM-41' in act['name']][0]
print(Ni_MCM_41_prod)
catalyst_data_list.append(Ni_MCM_41_prod)

Ni_ABC_prod = [act for act in catalyst_production_db if 'Ni/ABC' in act['name']][0]
print(Ni_ABC_prod)
catalyst_data_list.append(Ni_ABC_prod)

print('==========')

# 选择LCIA方法（mid）
recipe_mid = [m for m in bw.methods if 'ReCiPe' in m[0]
              and 'Midpoint (E)' in m[0]
              and 'w/o LT' not in m[0]
              and ' no LT' not in m[0]
              and 'V1.13' in m[0]]

# 选择LCIA方法（end）
recipe_end = [m for m in bw.methods if 'ReCiPe' in m[0]
              and 'Endpoint' in m[0]
              and '(E,A)' in m[0]
              and 'total' in m[2]
              and 'LT' not in m[2]]

# 进行计算（每种产品的所有midpoint方法计算）（使用线程池提高计算效率）（汇总）
"""results = []
for catalyst in catalyst_data_list:
    def cal(method):
        lca = bw.LCA({catalyst: 1}, method)
        lca.lci()
        lca.lcia()
        results.append((catalyst['name'], catalyst['location'], method[1], lca.score))


    method = recipe_mid

    pool = ThreadPool(8)
    pool.map(cal, method)
    pool.close()
# 将结果写入dataframe
result_df = pd.DataFrame(results, columns = ['Name', 'Location', 'Method', 'Score'])
print(result_df)
result_df.to_excel(excel_writer = "mid.xlsx", index = True, encoding = 'utf-8')"""

# 进行计算（每种产品的所有endpoint方法计算）（使用线程池提高计算效率）（汇总）
"""results = []
for catalyst in catalyst_data_list:
    def cal(method):
        lca = bw.LCA({catalyst: 1}, method)
        lca.lci()
        lca.lcia()
        results.append((catalyst['name'], catalyst['location'], method[1], lca.score))


    method = recipe_end

    pool = ThreadPool(8)
    pool.map(cal, method)
    pool.close()
# 将结果写入dataframe
result_df = pd.DataFrame(results, columns = ['Name', 'Location', 'Method', 'Score'])
print(result_df)
result_df.to_excel(excel_writer = "end.xlsx", index = True, encoding = 'utf-8')
"""

# 单独计算（mid,end）并写入单独文件
"""# Ni_Al2O3_prod计算

def cal(method):
    lca = bw.LCA({Ni_Al2O3_prod: 1}, method)
    lca.lci()
    lca.lcia()
    results.append((Ni_Al2O3_prod['name'], Ni_Al2O3_prod['location'], method[1], lca.score))


results = []
method = recipe_mid

pool = ThreadPool(8)
pool.map(cal, method)
pool.close()
# 将结果写入dataframe
result_df = pd.DataFrame(results, columns = ['Name', 'Location', 'Method', 'Score'])
print(result_df)
# 将结果输出到文件
result_df.to_csv(path_or_buf = "Ni_Al2O3_prod_mid.csv")
result_df.to_excel(excel_writer = "Ni_Al2O3_prod_mid.xlsx", encoding = 'utf-8')

results = []
method = recipe_end

pool = ThreadPool(8)
pool.map(cal, method)
pool.close()
# 将结果写入dataframe
result_df = pd.DataFrame(results, columns = ['Name', 'Location', 'Method', 'Score'])
print(result_df)
# 将结果输出到文件
result_df.to_csv(path_or_buf = "Ni_Al2O3_prod_end.csv")
result_df.to_excel(excel_writer = "Ni_Al2O3_prod_end.xlsx", encoding = 'utf-8')


# Ni_MCM_41_prod计算

def cal(method):
    lca = bw.LCA({Ni_MCM_41_prod: 1}, method)
    lca.lci()
    lca.lcia()
    results.append((Ni_MCM_41_prod['name'], Ni_MCM_41_prod['location'], method[1], lca.score))


results = []
method = recipe_mid

pool = ThreadPool(8)
pool.map(cal, method)
pool.close()
# 将结果写入dataframe
result_df = pd.DataFrame(results, columns = ['Name', 'Location', 'Method', 'Score'])
print(result_df)
# 将结果输出到文件
result_df.to_csv(path_or_buf = "Ni_MCM_41_prod_mid.csv")
result_df.to_excel(excel_writer = "Ni_MCM_41_prod_mid.xlsx", encoding = 'utf-8')

results = []
method = recipe_end

pool = ThreadPool(8)
pool.map(cal, method)
pool.close()
# 将结果写入dataframe
result_df = pd.DataFrame(results, columns = ['Name', 'Location', 'Method', 'Score'])
print(result_df)
# 将结果输出到文件
result_df.to_csv(path_or_buf = "Ni_MCM_41_prod_end.csv")
result_df.to_excel(excel_writer = "Ni_MCM_41_prod_end.xlsx", encoding = 'utf-8')


# Ni_ABC_prod计算

def cal(method):
    lca = bw.LCA({Ni_ABC_prod: 1}, method)
    lca.lci()
    lca.lcia()
    results.append((Ni_ABC_prod['name'], Ni_ABC_prod['location'], method[1], lca.score))


results = []
method = recipe_mid

pool = ThreadPool(8)
pool.map(cal, method)
pool.close()
# 将结果写入dataframe
result_df = pd.DataFrame(results, columns = ['Name', 'Location', 'Method', 'Score'])
print(result_df)
# 将结果输出到文件
result_df.to_csv(path_or_buf = "Ni_ABC_prod_mid.csv")
result_df.to_excel(excel_writer = "Ni_ABC_prod_mid.xlsx", encoding = 'utf-8')

results = []
method = recipe_end

pool = ThreadPool(8)
pool.map(cal, method)
pool.close()
# 将结果写入dataframe
result_df = pd.DataFrame(results, columns = ['Name', 'Location', 'Method', 'Score'])
print(result_df)
# 将结果输出到文件
result_df.to_csv(path_or_buf = "Ni_ABC_prod_end.csv")
result_df.to_excel(excel_writer = "Ni_ABC_prod_end.xlsx", encoding = 'utf-8')"""

# 进行计算(单个midpoint方法）
'''

for method in recipe_mid:
    results = []


    def cal(catalyst):
        lca = bw.LCA({catalyst: 1}, method)
        lca.lci()
        lca.lcia()
        results.append((method[1], catalyst['name'], lca.score))


    catalyst = catalyst_data_list

    pool = ThreadPool(8)
    pool.map(cal, catalyst)
    pool.close()
    result_df = pd.DataFrame(results, columns = ['Method', 'Name', 'Score'])
    print(result_df)
    pic = result_df.plot(kind = 'bar', color = 'k', alpha = 0.7)
    pic.set_title(f'{method[1]}')
    plt.show()
'''

# 过程间比较绘图
"""# 产品之间的单指标比较
# data1 = pd.read_excel('end.xlsx')
# data1.to_csv(path_or_buf = 'end.csv', index = None)
# data2 = pd.read_excel('mid.xlsx')
# data2.to_csv(path_or_buf = 'mid.csv', index = None)
endtotal = pd.read_csv('end.csv', index_col = ['Method', 'Name'])
print(endtotal)
midtotal = pd.read_csv('mid.csv', index_col = ['Method', 'Name'])
print(midtotal)

# end
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
# fig.subplots_adjust(wspace = 1, hspace = 1)

ax1.set_xlabel('prod')
ax1.set_ylabel('Score')
ax1data = endtotal.loc['total', ['Score']]
ax1.set_title('total', fontsize = 15)
ax1data.plot.bar(ax = ax1, color = 'k', alpha = 0.7, rot = 0, use_index = True, legend = False, fontsize = 8)

ax2.set_xlabel('prod')
ax2.set_ylabel('Score')
ax2data = endtotal.loc['human health', ['Score']]
ax2.set_title('human health', fontsize = 15)
ax2data.plot.bar(ax = ax2, color = 'r', alpha = 0.7, rot = 0, use_index = True, legend = False, fontsize = 8)

ax3.set_xlabel('prod')
ax3.set_ylabel('Score')
ax3data = endtotal.loc['resources', ['Score']]
ax3.set_title('resources', fontsize = 15)
ax3data.plot.bar(ax = ax3, color = 'b', alpha = 0.7, rot = 0, use_index = True, legend = False, fontsize = 8)

ax4.set_xlabel('prod')
ax4.set_ylabel('Score')
ax4data = endtotal.loc['ecosystem quality', ['Score']]
ax4.set_title('ecosystem quality', fontsize = 15)
ax4data.plot.bar(ax = ax4, color = 'g', alpha = 0.7, rot = 0, use_index = True, legend = False, fontsize = 8)

# mid
fig1 = plt.figure()
ax5 = fig1.add_subplot(2, 2, 1)
ax6 = fig1.add_subplot(2, 2, 2)
ax7 = fig1.add_subplot(2, 2, 3)
ax8 = fig1.add_subplot(2, 2, 4)

ax5.set_xlabel('prod')
ax5.set_ylabel('Score')
ax5data = midtotal.loc['climate change', ['Score']]
ax5.set_title('climate change', fontsize = 15)
ax5data.plot.bar(ax = ax5, color = 'k', alpha = 0.7, rot = 0, use_index = True, legend = False, fontsize = 8)

ax6.set_xlabel('prod')
ax6.set_ylabel('Score')
ax6.set_title('human toxicity', fontsize = 15)
ax6data = midtotal.loc['human toxicity', ['Score']]
ax6data.plot.bar(ax = ax6, color = 'k', alpha = 0.7, rot = 0, use_index = True, legend = False, fontsize = 8)

ax7.set_xlabel('prod')
ax7.set_ylabel('Score')
ax7.set_title('fossil depletion', fontsize = 15)
ax7data = midtotal.loc['fossil depletion', ['Score']]
ax7data.plot.bar(ax = ax7, color = 'k', alpha = 0.7, rot = 0, use_index = True, legend = False, fontsize = 8)

ax8.set_xlabel('prod')
ax8.set_ylabel('Score')
ax8.set_title('marine ecotoxicity', fontsize = 15)
ax8data = midtotal.loc['marine ecotoxicity', ['Score']]
ax8data.plot.bar(ax = ax8, color = 'k', alpha = 0.7, rot = 0, use_index = True, legend = False, fontsize = 8)

plt.show()"""

# 单LCIA方法蒙特卡洛模拟（迭代次数100）
'''
method1 = recipe_mid[0]
MyFirstMonteCarlo = bw.MonteCarloLCA({Ni_Al2O3_prod: 1}, method1)
scores = [next(MyFirstMonteCarlo) for _ in range(100)]
print(scores)
'''

# 多LCIA方法蒙特卡洛模拟
'''
def multiimpactMonteCarloLCA(function_unit, list_methods, iterations):
    MC_lca = bw.MonteCarloLCA(function_unit)
    MC_lca.lci()
    C_matrices = {}

    for method in list_methods:
        MC_lca.switch_method(method)
        C_matrices[method] = MC_lca.characterization_matrix

    results = np.empty((len(list_methods), iterations))

    for iteration in range(iterations):
        next(MC_lca)
        for method_index, method in enumerate(list_methods):
            results[method_index, iteration] = (C_matrices[method] * MC_lca.inventory).sum()
    return results


fu = {Ni_Al2O3_prod: 1}
lm = recipe_mid
iter = 100
Ni_Al2O3_prod_Monte_Results = multiimpactMonteCarloLCA(fu, lm, iter)
print(Ni_Al2O3_prod_Monte_Results)
'''

# 贡献影响分析
# method1 = recipe_mid[6]
# function_unit = {Ni_Al2O3_prod: 1}
# lca = bw.LCA(function_unit, method1)
# lca.lci()
# lca.lcia()
#
# print(lca.demand)
# print(lca.method)
# print('The {} process accounts for {:f} {}'.format(
#     list(function_unit.keys())[0]['name'],
#     lca.score,
#     bw.methods.get(method1).get('unit')
# ))
# # out：The Ni/Al2O3 Production process accounts for 26.836102 kg CO2-Eq
# print('==========')
#
# ca = bwa.ContributionAnalysis()
# print(ca.annotated_top_processes(lca, limit = 0.1, limit_type = 'percent'))
# print('==========')
# print(lca.top_activities())
# print('==========')
# print(ca.annotated_top_emissions(lca, limit = 0.1, limit_type = 'percent'))
# print('==========')
# print(lca.top_emissions())
# print('==========')
# print(ca.hinton_matrix(lca, rows = 10, cols = 10))

# def top_emissions_by_name(lca, biosphere_database = 'biosphere3'):
#     names = defaultdict(list)
#
#     for flow in bw.Database("biosphere3"):
#         if flow.key in lca.biosphere_dict:
#             names[flow['name']].append(
#                 lca.characterized_inventory[lca.biosphere_dict[flow.key], :].sum()
#             )
#
#     return sorted(
#         [(sum(scores), name) for name, scores in names.items()],
#         reverse = True
#     )
#
#
# def top_processes_by_name(lca, technosphere_database = 'ecoinvent_3.6_apos'):
#     names = defaultdict(list)
#
#     for flow in db:
#         if flow.key in lca.activity_dict:
#             names[flow['name']].append(
#                 lca.characterized_inventory[:, lca.activity_dict[flow.key]].sum()
#             )
#
#     return sorted(
#         [(sum(scores), name) for name, scores in names.items()],
#         reverse = True
#     )
#
#
# print(top_processes_by_name(lca)[:10])
# print(top_emissions_by_name(lca)[:10])
#
# print('==========')
# print(lca.score)
# l = [t[0] for t in top_processes_by_name(lca)]
# print(sum(l))
# l = [t[0] for t in top_emissions_by_name(lca)]
# print(sum(l))

'''
aluminium = [act for act in db if 'aluminium oxide production' in act['name'] and 'CN' in
             act['location']][0]
print(aluminium)
print("aluminium_key:{}".format(aluminium.key))

for key in Ni_Al2O3_prod:
    print(key, ':', Ni_Al2O3_prod[key])

print('==========')

for exc in aluminium.upstream():
    print(exc)
'''

# 三个过程的GWP MC
"""ClimateChangeMethod = recipe_mid[6]
Ni_Al2O3_MonteCarlo = bw.MonteCarloLCA({Ni_Al2O3_prod: 1}, ClimateChangeMethod)
# Ni_MCM_41_MonteCarlo = bw.MonteCarloLCA({Ni_MCM_41_prod: 1}, ClimateChangeMethod)
# Ni_ABC_MonteCarlo = bw.MonteCarloLCA({Ni_ABC_prod: 1}, ClimateChangeMethod)
score = [next(Ni_Al2O3_MonteCarlo) for _ in range(1000)]
Ni_Al2O3_MonteCarlo_score = pd.DataFrame(data = score)
Ni_Al2O3_MonteCarlo_score.to_csv(path_or_buf = 'Ni_Al2O3_MC_score_1000.csv')"""

# 绘制GWP MC箱型图
"""fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Ni/Al2O3')
ax.set_ylabel('GWP Score')
data1 = pd.read_csv('Ni_Al2O3_MC_score_1000.csv')
data = data1.iloc[:, 1]
data.plot.box(ax = ax, title = 'Ni/Al2O3 GWP MC 1000 times')
plt.show()
"""

print('==========')
print(f'time used:{time.time() - start_time}s')
