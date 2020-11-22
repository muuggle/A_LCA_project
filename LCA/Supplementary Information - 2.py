from brightway2 import *
import os
import numpy as np
import scipy as sp
import pandas as pd
import pickle
import copy
import matplotlib.pyplot as plt
import seaborn as sns
import sys

from bw2data.utils import uncertainify
from stats_arrays import NormalUncertainty

projects.set_current("SI2")
bw2setup()

if 'ecoinvent3.6' in databases:
    print('database exists')
else:
    ei36 = SingleOutputEcospold2Importer(
        "C:/Users/fx50/Desktop/ei3.6apos/datasets",
        "ecoinvent3.6",
        use_mp=False
    )
    ei36.apply_strategies()
    ei36.statistics()
    ei36.write_database()

ITERATIONS=10000
ecoinvent=Database("ecoinvent3.6")
recipe = [method for method in methods
             if "ReCiPe Midpoint (H) V1.13" in method[0]
                and "w/o" not in method[0]
                and 'no LT' not in method[0]
          ]

ecoinvent.make_searchable()
al=ecoinvent.search("aluminium alloy production")
aluminium=al[2]
ex=ecoinvent.search('impact extrusion of aluminium, 1 stroke')
extrusion=ex[1]

bottle_example_db = Database('bottle example database')
bottle_example_db.write(
    {('bottle example database','aluminium bottle production'):
         {'name':'aluminium bottle',
          'unit':'amount',
            'exchanges':
          [
              {'input':aluminium.key,
               'amount':0.150,
               'type':'technosphere'},
              {'input':extrusion.key,
               'amount':0.150,
               'type':'technosphere'},
              {'input':('bottle example database','aluminium bottle production'),
               'amount':1,
               'type':'production'}
          ]},
     })

bottle_production=get_activity(('bottle example database','aluminium bottle production'))
print(bottle_production)

det_results = pd.DataFrame()

bottle_LCA = LCA({bottle_production:1})
bottle_LCA.lci()
for method in recipe:
    bottle_LCA.switch_method(method)
    bottle_LCA.lcia()
    det_results.loc[method[1], 'Bottle score'] = bottle_LCA.score
    det_results.loc[method[1], 'Unit'] = Method(method).metadata['unit']
print(det_results.sort_index())

for exc in bottle_production.technosphere():
    input_lca=LCA({exc['input']:exc['amount']})
    input_lca.lci()
    for method in recipe:
        input_lca.switch_method(method)
        input_lca.lcia()
        det_results.loc[method[1],'Contribution(%):{}'.format(exc.input['name'])]=100\
        *input_lca.score/det_results.loc[method[1],'Bottle score']

print(det_results.sort_index)


#Preliminary calculations: score of electricity per kWh
elect = [exc.input for exc in aluminium.technosphere() if 'electricity' in exc.input['name']][0]

electricity_unit_impacts={}
elect_LCA=LCA({elect:1})
elect_LCA.lci()
for method in recipe:
    elect_LCA.switch_method(method)
    elect_LCA.lcia()
    electricity_unit_impacts[method[1]]=elect_LCA.score

#score of bottle attributable to electricity
for method in recipe:
    det_results.loc[method[1],'share impact of bottle due to electricity(%)']=\
    100*bottle_LCA.supply_array[bottle_LCA.activity_dict[elect.key]]\
    *electricity_unit_impacts[method[1]]\
    /det_results.loc[method[1],'Bottle score']

# Aluminium score
al_LCA=LCA({aluminium:1})
al_LCA.lci()

for method in recipe:
    al_LCA.switch_method(method)
    al_LCA.lcia()
    elect_LCA.switch_method(method)
    elect_LCA.lcia()
    elect_score_in_al=al_LCA.supply_array[al_LCA.activity_dict[elect.key]]*elect_LCA.score
    print('Share of aluminium {} score attribution to electricity:{:.1%}'.format(method[1],elect_score_in_al/al_LCA.score))

#score of extrusion attribution to electricity
extrusion_LCA=LCA({extrusion:1})
extrusion_LCA.lci()

for method in recipe:
    extrusion_LCA.switch_method(method)
    extrusion_LCA.lcia()
    elect_LCA.switch_method(method)
    elect_LCA.lcia()
    elect_score_in_al=extrusion_LCA.supply_array[extrusion_LCA.activity_dict[elect.key]]*elect_LCA.score
    print('share of extrusion {} score attributable to electricity to electricity:{:.1%}'.format(method[1],elect_score_in_al/extrusion_LCA.score))

det_results.sort_index()

#generating the samples
mu=pd.MultiIndex.from_product([['Dependent','Independent','Fitted','Presampled'],
                                ['Bottle'],
                                [method[1] for method in recipe]],
                               names=['Sampling','Product','Method'])
df_samples=pd.DataFrame(index=range(ITERATIONS),columns=mu)

 #Monte Carlo using disaggregated datasets
bottle_MC_disagg=MonteCarloLCA({bottle_production:1})
CF_matrices={}
next(bottle_MC_disagg)

for method in recipe:
    bottle_MC_disagg.switch_method(method)
    CF_matrices[method]=bottle_MC_disagg.characterization_matrix

    for iteration in range(ITERATIONS):
        sys.stdout.write("\rIteration {}/{}".format(iteration+1, ITERATIONS))
        sys.stdout.flush()
        next(bottle_MC_disagg)
        for method in recipe:
            bottle_MC_disagg.switch_method(method)
            df_samples.loc[iteration,('Dependent','Bottle',method[1])]=(CF_matrices[method]*bottle_MC_disagg.inventory).sum()

#Monte Carlo with independently sampled values for the different inputs
#Aluminium
aluminium_MC_disagg=MonteCarloLCA({aluminium:1})
CF_matrices={}
next(aluminium_MC_disagg)

for method in recipe:
    aluminium_MC_disagg.switch_method(method)
    CF_matrices[method]=aluminium_MC_disagg.characterization_matrix

# Actual Monte Carlo:
for iteration in range(ITERATIONS):
    sys.stdout.write('\rIteration{}/{}'.format(iteration+1,ITERATIONS))
    sys.stdout.flush()
    next(aluminium_MC_disagg)
    for method in recipe:
        aluminium_MC_disagg.switch_method(method)
        df_samples.loc[iteration,('Independent','aluminium',method[1])]=(CF_matrices[method]*aluminium_MC_disagg.inventory).sum()

#Extrusion
extrusion_MC_disagg=MonteCarloLCA({extrusion:1})
CF_matrices={}
next(extrusion_MC_disagg)

for method in recipe:
    extrusion_MC_disagg.switch_method(method)
    CF_matrices[method]=extrusion_MC_disagg.characterization_matrix

#Actual Monte Carlo
for iteration in range(ITERATIONS):
    sys.stdout.write("\rIteration {}/{}".format(iteration + 1, ITERATIONS))
    sys.stdout.flush()
    next(extrusion_MC_disagg)
    for method in recipe:
        extrusion_MC_disagg.switch_method(method)
        df_samples.loc[iteration, ('Independent', 'extrusion', method[1])] = (
                    CF_matrices[method] * extrusion_MC_disagg.inventory).sum()

for method in recipe:
    df_samples[('Independent','Bottle',method[1])]=0.15*df_samples[('Independent','aluminium',method[1])]\
    +0.15*df_samples[('Independent','Extrusion',method[1])]

mi_fitted=pd.MultiIndex.from_product([['aluminium','extrusion'],['shape','loc','scale']],
                                     names=['inputs','shape_params'])
df_fitted_shape_parameters=pd.DataFrame(index=[Method[1]
                            for method in recipe],colums=mi_fitted)

#generate samples for inputs(al,ex)
for product in ['aluminium','extrusion']:
    for method in recipe:
        shape,loc,scale=sp.stats.lognorm.fit(df_samples['Independent',product,method[1]].astype('float64'))
        df_fitted_shape_parameters.loc[method[1], (product, 'shape')] = shape
        df_fitted_shape_parameters.loc[method[1], (product, 'loc')] = loc
        df_fitted_shape_parameters.loc[method[1], (product, 'scale')] = scale

print(df_fitted_shape_parameters)








