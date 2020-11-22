from brightway2 import *
from bw2analyzer.matrix_grapher import SparseMatrixGrapher
from bw2analyzer import ContributionAnalysis
from bw2data.utils import uncertainify
from stats_arrays import NormalUncertainty

print(projects.current)
print(projects.dir)
projects.set_current('BW2 introduction')
print(projects)
print('----------------------------')

# getting basic data
bw2setup()

# a biosphere dataset
db = Database('biosphere3')
print('Number of flows in `biosphere3`:', len(db))
random_flow = db.random()
print(random_flow)

print(random_flow['name'])
print(random_flow['unit'])
print(random_flow['categories'])

print(random_flow.key)
print('----------------------------')

# an lcia method dataset
print(len(methods))

method_key = methods.random()
print(method_key)

method_data = Method(method_key).load()
print('Number of CFS:', len(method_data))
print(method_data[:20])
print('----------------------------')

# Importing the LCI database
fpei36 = 'C:/Users/muuuuggle/Desktop/ecoinvent 3.6_apos_ecoSpold02/datasets'

if 'ecoinvent3.6apos' in databases:
    print('Database has already been imported')
else:
    eiapos36 = SingleOutputEcospold2Importer(fpei36, 'ecoinvent3.6apos', use_mp = False)
    eiapos36.apply_strategies()
    eiapos36.statistics()
    eiapos36.write_database()

# Searching datasets
print(Database('ecoinvent3.6apos').search('carb*', limit = 10))
print(Database('ecoinvent3.6apos').search('carbon', filter = {'categories': 'forestry'}))
print(Database('ecoinvent3.6spos').search('carbon', limit = 10, mask = {'categories': 'forestry'}))
sr = Database('ecoinvent3.6apos').search('carbon', facet = 'categories')
for key, value in sr.items():
    print('Facet term:', key, '\n\t', value[:3], '\n')
print('----------------------------')

# Changing iteration order
db = Database('ecoinvent3.6apos')


def print_10(db):
    for i, x in enumerate(db):
        if i < 10:
            print(x)
        else:
            break


print_10(db)

db.order_by = 'name'
print_10(db)

db.order_by = None

my_activities = [x for x in db if 'Electr' in x['name']]
print(my_activities)
print('----------------------------')

# basic calculation
process = Database('ecoinvent3.6apos').random()
print(process)

function_unit = {process: 1}

lca = LCA(function_unit, method_key)
lca.lci()
lca.lcia()
print(lca.score)

new_process = Database('ecoinvent3.6apos').random()
print(new_process)
lca.redo_lcia({new_process: 1})
print(lca.score)
print('----------------------------')
'''
# looking into the LCA object
print(lca.technosphere_matrix)
print(lca.biosphere_matrix)
print(lca.characterization_matrix)

# Graphing matrices
print(SparseMatrixGrapher(lca.technosphere_matrix).ordered_graph())


# Contribution analysis
print(ContributionAnalysis.annotated_top_processes(lca))
print(ContributionAnalysis.annotated_top_emissions(lca))
'''

# Monte carlo LCA
uncertain_db = Database('ecoinvent3.6apos')
uncertain_db.write

mc = MonteCarloLCA(demand = {db.random(): 1}, method = method_key)
mc.load_data()
for x in range(10):
    print(next(mc))