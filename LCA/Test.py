from lci_to_bw2 import *
from brightway2 import *
import time
import matplotlib
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bw2data.parameters import ActivityParameter, DatabaseParameter, ProjectParameter, Group

when = time.strftime("%Y%m%d")

projects.set_current('Test')

bw2setup()

fpei36 = 'C:/Users/muuuuggle/Desktop/ecoinvent 3.6_apos_ecoSpold02/datasets'

if 'ecoinvent 3.6 apos' in databases:
    print('Database has already been imported')
else:
    ei36 = SingleOutputEcospold2Importer(fpei36, 'ecoinvent 3.6 apos', use_mp = False)
    ei36.apply_strategies()
    ei36.statistics()
    ei36.write_database()
print('--------------------'
      '--------------------')

eidb = Database('ecoinvent 3.6 apos')

'''
eidb.search('electricity,low voltage')
process = [act for act in eidb if 'electricity' in act['name'] and 'mix' in act['name'] and 'CN-ZJ' in act['location']][0]
print(process)
print('--------------------'
      '--------------------')

waste_handling = eidb.new_activity(code = 'test1', name = "Waste handling", unit = "unit")

project_data = [{
    'name': 'M',
    'amount': 0.06,
}, {
    'name': 'D',
    'amount': 200
}]
parameters.new_project_parameters(project_data)
for param in ProjectParameter.select():
    print(param,param.amount)
print('--------------------'
      '--------------------')

aluminium=[act for act in eidb if 'treatment of aluminium scrap, post-consumer, prepared for recycling, at refiner' in act['name'] and 'RER' in act['location']][0]
waste_handling.new_exchange(input=aluminium.key,amount=0,unit="kilogram",type='technosphere', formula='M').save()

transport=[act for act in eidb if act['name']=='market for transport, freight, lorry 3.5-7.5 metric ton, EURO5' and 'RoW' in act['location']][0]
waste_handling.new_exchange(input=transport.key,amount=0,unit="ton kilometer",type='technosphere', formula='D*M/1000').save()


air=[act for act in eidb if act['name']=='market for air input/output unit, heat and power co-generation unit, 160kW electrical' and 'GLO' in act['location']][0]
waste_handling.new_exchange(input=air.key,amount=0,unit="cubic meter",type='technosphere', formula='D*M/1000').save()


parameters.add_exchanges_to_group('again another group', waste_handling)
ActivityParameter.recalculate_exchanges('again another group')


# Have a look at all exchanges of the selected activity
for exc in waste_handling.exchanges():
    print(exc)
print('--------------------'
      '--------------------')

for act in waste_handling.technosphere():
    print(act.input)
print('--------------------'
      '--------------------')

# get general information on the new activity
act = eidb.get('test1')
print(act)
'''

'''

# Delete parameters and activities

name=['M']
for name in ProjectParameter.select():
    name.delete()
    
parameters.remove_exchanges_from_group('again another group', waste_handling)

ProjectParameter.drop_table(safe=True,drop_sequences=True)
ProjectParameter.create_table()
for name in ProjectParameter.select():
    print(name)

for activity in [act for act in eidb if act['name']=='Waste handling' and 'GLO' in act['location']]:
    activity.delete()

eidb.search('waste handling')'''

'''
#   The following for-loop is only to guarantee that we can create a new bottle production process
for activity in [act for act in eidb if 'Bottle production' in act['name'] and 'GLO' in act['location']]:
    activity.delete()

# activities and exchanges for simple bottle production model
bottle_production = eidb.new_activity(code = 'test2', name = 'Bottle production', unit = 'unit')

project_data = [{
    'name': 'M',
    'amount': 0.06,
}, {
    'name': 'D',
    'amount': 200
}]

parameters.new_project_parameters(project_data)

for param in ProjectParameter.select():
    print(param, param.amount)

electricity = \
    [act for act in eidb if 'electricity' in act['name'] and 'mix' in act['name'] and 'CN-ZJ' in act['location']][0]
bottle_production.new_exchange(input = electricity.key, amount = 0, unit = 'kilowatt hour', type = 'technosphere',
                               formula = '20*M/3.6').save()

polyethylene = \
    [act for act in eidb if 'market for polyethylene, high density' in act['name'] and 'GLO' in act['location']][0]
pe = bottle_production.new_exchange(input = polyethylene.key, amount = 0, unit = 'kilogram', type = 'technosphere',
                                    formula = 'M')
pe.save()

transport = [act for act in eidb if
             act['name'] == 'market for transport, freight, lorry 3.5-7.5 metric ton, EURO5' and 'RoW' in act[
                 'location']][0]
bottle_production.new_exchange(input = transport.key, amount = 0, unit = "ton kilometer", type = 'technosphere',
                               formula = 'D*M/1000').save()

parameters.add_exchanges_to_group('group bottle', bottle_production)
ActivityParameter.recalculate_exchanges('group bottle')

for exc in bottle_production.exchanges():
    print(exc)
bottle_production.as_dict()

for key in bottle_production():
    print((key,':',bottle_production[key]))

for exc in polyethylene.exchanges():
    print(exc)

for exc in polyethylene.upstream():
    print(exc)
'''
'''
#delete the table of existing project parameters, i.e. actually deletes the project parameters
ProjectParameter.drop_table(safe=True,drop_sequences = True)
#create a new empty table of project parameters
ProjectParameter.create_table()
#create a new empty table of project parameters
for name in ProjectParameter.select():
    print(name)
#Delete the list of project data (or any other dictionary); does not affect the parametrised exchanges until they get recalculated
project_data.clear() #.remove would only clear the content but leave empty instances
#quick check to see that it got deleted
for data in project_data:
    print(data)
#delete the table of existing project parameters, i.e. actually deletes the project parameters
ProjectParameter.drop_table(safe=True, drop_sequences=True)
#create a new empty table of project parameters
ProjectParameter.create_table()

for name in ProjectParameter.select():
    name.print()
#delete all bottle production activities that were accidentally created
for activity in [act for act in eidb if act['name']=='Bottle production' and 'GLO' in act['location']]:
    activity.delete()
#delete individual bottle production activity
#waste_handling.delete
'''





