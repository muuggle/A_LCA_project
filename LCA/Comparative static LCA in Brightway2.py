import brightway2 as bw
import pandas as pd

bw.projects.set_current('Comparative static LCA')
bw.bw2setup()

# Importing the LCI database
fpei36 = 'C:/Users/muuuuggle/Desktop/ecoinvent 3.6_apos_ecoSpold02/datasets'

if 'ecoinvent3.6apos' in bw.databases:
    print('Database has already been imported')
else:
    eiapos36 = bw.SingleOutputEcospold2Importer(fpei36, 'ecoinvent3.6apos', use_mp = False)
    eiapos36.apply_strategies()
    eiapos36.statistics()
    eiapos36.write_database()

bioDB = bw.Database('biosphere3')
ecoinDB = bw.Database('ecoinvent3.6apos')
print('The ecoinvnet DB type is', type(ecoinDB),
      'The biosphere DB type is ', type(bioDB),
      'just you know')

# Finding my two products
ecoinDB.make_searchable()
dairy = ecoinDB.search('dairy')
print(dairy)

Milk1 = dairy[1]
Milk2 = dairy[5]
print(' I will compare \n{} and \n{}'.format(Milk1, Milk2))
myMilk = [Milk1, Milk2]

# select LCIA methods
print(len(bw.methods))
mymethod = [method for method in bw.methods
            if 'ReCiPe' in method[0]
            and 'H,A' in method[0]
            and 'w/o' not in method[0]
            and 'total' in method[2]
            and 'total' not in method[1]
            ]
print(mymethod)

# Calculating results and storing them in a table (actually, a Pandas dataframe
result = []
for milk in myMilk:
    lca = bw.LCA({milk: 1})
    lca.lci()
    for method in mymethod:
        lca.switch_method(method)
        lca.lcia()
        result.append((milk['name'].replace('_20', '').strip(), method[1].title(), lca.score))
print(result)

result_df = pd.DataFrame(result, columns = ['name', 'method', 'score'])
result_df = pd.pivot_table(result_df, index = 'name', columns = 'method', values = 'score')
print(result_df)

normal_result_df=result_df/result_df.max()
print(normal_result_df)