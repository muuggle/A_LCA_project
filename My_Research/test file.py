import brightway2 as bw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bw2analyzer as bwa

bw.projects.set_current('catalyst_LCA')
bw.bw2setup()
db = bw.Database('ecoinvent_3.6_apos')
catalyst_production_db = bw.Database("Database as dict")
biodb = bw.Database('biosphere3')
print(bw.databases)
print('==========')
'''
CTAB_Production = {("Database as dict", "code for CTAB Production"): {
    'name': 'CTAB Production',
    'unit': 'kg',
    'location': 'CN',
    'categories': 'None',
    'exchanges': [{
        'amount': 3,
        'input': ('ecoinvent_3.6_apos', '6ef9fd9414bb88359d1e7df6a0fd05cd'),
        'type': 'production',
        'uncertainty type': 0,
        'unit=': 'kg'}]
}}
catalyst_production_db.write(CTAB_Production)

CTAB = [act for act in catalyst_production_db if 'CTAB' in act['name']][0]
print(CTAB)

for exc in CTAB.exchanges():
    print(exc)

Ni_MCM_41_production = {
    ("Database as dict", "code for Ni/MCM-41 Production"): {
        'name': 'Ni/MCM-41 Production',
        'unit': 'kg',
        'location': 'CN',
        'categories': 'None',
        'exchanges': [{
            'amount': 1.215,
            'input': ('Database as dict', 'code for CTAB Production'),
            'type': 'technosphere',
            'uncertainty type': 5,
            'loc': 0.005,
            'minimum': 0.0005,
            'maximum': 0.05,
            'unit=': 'kg',
        }]}}

catalyst_production_db.write(Ni_MCM_41_production)
Ni_MCM_41_production = [act for act in catalyst_production_db if 'Ni/MCM-41' in act['name']][0]
print(Ni_MCM_41_production)
for exc in Ni_MCM_41_production.exchanges():
    print(exc)
'''

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

recipe_mid = [m for m in bw.methods if 'ReCiPe' in m[0]
              and 'Midpoint (E)' in m[0]
              and 'w/o LT' not in m[0]
              and ' no LT' not in m[0]
              and 'V1.13' in m[0]]

catalyst_production_db.write(catalyst_data)

print('==========')

Ni_Al2O3_prod = [act for act in catalyst_production_db if 'Ni/Al2O3' in act['name']][0]
Ni_Al2O3_prod_exc_list = [exc for exc in Ni_Al2O3_prod.exchanges()]

method1 = recipe_mid[6]
function_unit = {Ni_Al2O3_prod: 1}
lca = bw.LCA(function_unit, method1)
lca.lci()
lca.lcia()

print(lca.demand)
print(lca.method)
print('The {} process accounts for {:f} {}'.format(
    list(function_unit.keys())[0]['name'],
    lca.score,
    bw.methods.get(method1).get('unit')
))
# out：The Ni/Al2O3 Production process accounts for 26.836102 kg CO2-Eq
print('==========')

ca = bwa.ContributionAnalysis()
# print(ca.annotated_top_processes(lca, limit = 0.1, limit_type = 'percent'))
# print('==========')
print(lca.top_activities())
print('==========')
# print(ca.annotated_top_emissions(lca, limit = 0.1, limit_type = 'percent'))
# print('==========')
# print(lca.top_emissions())
# print('==========')
# print(ca.hinton_matrix(lca, rows = 10, cols = 10))
