import brightway2 as bw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bw.projects.set_current('Biofuel')
bw.bw2setup()

# # 导入ecoinvent37数据库
# fpei37 = "D:\EcoinventDatabase\ecoinvent 3.7_apos_ecoSpold02\datasets"
#
# if 'ecoinvent_3.7_apos' in bw.databases:
#     print("Database has already been imported")
# else:
#     ei37 = bw.SingleOutputEcospold2Importer(fpei37, 'ecoinvent_3.7_apos', use_mp = False)
#     ei37.apply_strategies()
#     ei37.statistics()
#     ei37.write_database()

# # 导入ecoinvent数据库
# fpei36 = "D:\EcoinventDatabase\ecoinvent 3.6_apos_ecoSpold02\datasets"
#
# if 'ecoinvent_3.6_apos' in bw.databases:
#     print("Database has already been imported")
# else:
#     ei36 = bw.SingleOutputEcospold2Importer(fpei36, 'ecoinvent_3.6_apos', use_mp = False)
#     ei36.apply_strategies()
#     ei36.statistics()
#     ei36.write_database()

db = bw.Database('ecoinvent_3.7_apos')

print(bw.databases)
print('==========')

# 在数据库中提取bioethanol的流程
# electricity = [act for act in db if 'electricity production, wind, 1-3MW turbine, onshore' in act['name']
#                and 'CN-ZJ' in act['location']][0]
# print(electricity)
# print('electricity_key:{}'.format(electricity.key))
#
# ethanol = \
#     [act for act in db if 'market for ethanol, without water, in 99.7% solution state, from fermentation' in act['name']
#      and 'GLO' in act['location']][0]
# print(ethanol)
# print('ethanol_key:{}'.format(ethanol.key))
#
# nickel = [act for act in db if act['name'] == 'market for nickel, 99.5%'
#           and 'GLO' in act['location']][0]
# print(nickel)
# print('nickel_key:{}'.format(nickel.key))
#
# nitric_acid = [act for act in db if act['name'] == 'market for nitric acid, without water, in 50% solution state'
#                and 'RoW' in act['location']][0]
# print(nitric_acid)
# print('nitric_acid_key:{}'.format(nitric_acid.key))
#
# nitrogen = [act for act in db if act['name'] == 'market for nitrogen, liquid'
#             and 'RoW' in act['location']][0]
# print(nitrogen)
# print('nitrogen_key:{}'.format(nitrogen.key))
#
# sodium_silicate = [act for act in db if 'market for sodium silicate, solid' in act['name']
#                    and 'RoW' in act['location']][0]
# print(sodium_silicate)
# print('sodium_silicate_key:{}'.format(sodium_silicate.key))
#
# transport = [act for act in db if act['name'] == 'market for transport, freight train'
#              and 'CN' in act['location']][0]
# print(transport)
# print('transport_key:{}'.format(transport.key))
#
# water = [act for act in db if 'water' in act['name'] and 'deionised' in act['name']][0]
# print(water)
# print('water_key:{}'.format(water.key))
#
# wood_chip =[act for act in db if  act['name']=='market for wood chips, dry, measured as dry mass' and 'RoW' in act['location']][0]
# print(wood_chip)
# print('wood_chip:{}'.format(wood_chip.key))

enzyme = [act for act in db if 'enzymes production' in act['name'] and 'RoW' in act['location']][0]
print(enzyme)
print(f'enzyme_key:{enzyme.key}')
print('==========')

sulfuric_acid = [act for act in db if 'sulfuric acid production' in act["name"] and 'RoW' in act['location']][0]
print(sulfuric_acid)
print(f'sulfuric_acid_key:{sulfuric_acid.key}')
print('==========')

lime = [act for act in db if 'lime production, milled, packed' in act['name']and 'RoW' in act['location']][0]
print(lime)
print(f'lime:{lime.key}')

print('==========')

diammonium_phosphate = \
    [act for act in db if 'diammonium phosphate production' in act['name'] and 'CN' in act['location']][0]
print(diammonium_phosphate)
print(f'diammonium_phosphate_key:{diammonium_phosphate.key}')

print('==========')

electricity = [act for act in db if 'electricity production, wind, 1-3MW turbine, onshore' in act['name']
               and 'CN-ZJ' in act['location']][0]
print(electricity)
print('electricity_key:{}'.format(electricity.key))

print('==========')

steam = [act for act in db if 'steam production' in act['name'] and 'RoW' in act['location']][0]
print(steam)
print('steam:{}'.format(steam.key))
