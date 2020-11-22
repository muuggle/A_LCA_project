# Parametrized model for onshore and offshore wind turbines

import brightway2 as bw
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate

plt.style.use('ggplot')

bw.projects.set_current('my_project')
bw.bw2setup()
'''
ei34 = 'C:/Users/muuuuggle/Desktop/ecoinvent 3.4_cutoff_ecoSpold02/datasets'

if 'ecoinvent3.4cutoff' in bw.databases:
    print('Database has already been imported')
else:
    eicutoff34 = bw.SingleOutputEcospold2Importer(ei34, 'ecoinvent3.4cutoff', use_mp = False)
    eicutoff34.apply_strategies()
    eicutoff34.statistics()
    eicutoff34.write_database()

eidb = bw.Database('ecoinvent3.4cutoff')

# Creation of datasets for power transformers

# creation of 500 MVA transformer dataset
if [act for act in eidb if 'Power transformer TrafoStar 500 MVA' in act['name']] == []:
    act_transfo = [act for act in eidb if act["name"] == "transformer production, high voltage use"][0]

    new_act = act_transfo.copy()
    new_act["name"] = "Power transformer TrafoStar 500 MVA"
    new_act["unit"] = "unit"
    new_act.save()

    for exc in new_act.exchanges():
        exc.delete()
    new_act.save()

    # electricity steel
    steel = \
        [act for act in eidb if "steel production, electric, low-alloyed" in act['name'] and 'PER' in act['location']][
            0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 99640, unit = "kilogram", type = 'technosphere')
    new_exc.save()
    new_act.save()

    # transformer oil
    steel = [act for act in eidb if 'market for lubricating oil' in act['name'] and 'GLO' in act['location']][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 63000, unit = 'kilogram', type = 'technosphere')
    new_exc.save()
    new_act.save()

    # copper
    steel = [act for act in eidb if act["name"] == "market for copper" and "GLO" in act["location"]][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 39960, unit = "kilogram", type = 'technosphere')
    new_exc.save()
    new_act.save()

    # insulation
    steel = [act for act in eidb if act["name"] == "market for glass wool mat" and "GLO" in act["location"]][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 6500, unit = "kilogram", type = 'technosphere')
    new_exc.save()
    new_act.save()

    # wood
    steel = [act for act in eidb if act["name"] == "planing, board, softwood, u=20%" and "CH" in act["location"]][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 15000, unit = "kilogram", type = 'technosphere')
    new_exc.save()
    new_act.save()

    # porcelain
    steel = [act for act in eidb if act["name"] == "market for ceramic tile" and "GLO" in act["location"]][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 2650, unit = "kilogram", type = 'technosphere')
    new_exc.save()
    new_act.save()

    # construction steel
    steel = [act for act in eidb if act["name"] == "market for steel, unalloyed" and "GLO" in act["location"]][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 53618, unit = "kilogram", type = 'technosphere')
    new_exc.save()
    new_act.save()

    # paint
    steel = [act for act in eidb if act["name"] == "market for electrostatic paint" and "GLO" in act["location"]][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 2200, unit = "kilogram", type = 'technosphere')
    new_exc.save()
    new_act.save()

    # electricity, medium
    steel = \
        [act for act in eidb if act["name"] == "market for electricity, medium voltage" and "SE" in act["location"]][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 750000, unit = "kilowatt hour", type = 'technosphere')
    new_exc.save()
    new_act.save()

    # heat
    steel = [act for act in eidb if act[
        "name"] == "heat, from municipal waste incineration to generic market for heat district or industrial, other than natural gas" and "SE" in
             act["location"]][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 1080000, unit = "megajoule", type = 'technosphere')
    new_exc.save()
    new_act.save()

    # output
    steel = [act for act in eidb if act["name"] == "Power transformer TrafoStar 500 MVA"][0]
    new_exc = new_act.new_exchange(input = new_act.key, amount = 1, unit = "unit", categories = "", type = 'production')
    new_exc.save()
    new_act.save()

# creation of 10 MVA transformer dataset
if [act for act in eidb if 'Power transformer TrafoStar 10 MVA' in act['name']] == []:
    act = [a for a in eidb if 'Power transformer TrafoStar 500 MVA' in a['name']][0]
    new_act = act.copy()
    new_act['name'] = 'Power transformer TrafoStar 10 MVA'
    new_act.save()

    for exc in new_act.exchanges():
        print(exc.input['name'])
        if exc.input['name'] == "steel production, electric, low-alloyed":
            exc["amount"] = 6820
            exc.save()

        if exc.input['name'] == "market for lubricating oil":
            exc["amount"] = 6780
            exc.save()

        if exc.input['name'] == "market for copper":
            exc["amount"] = 3526
            exc.save()

        if exc.input['name'] == "market for ceramic tile":
            exc["amount"] = 53
            exc.save()

        if exc.input['name'] == "market for steel, unalloyed":
            exc["amount"] = 9066
            exc.save()

        if exc.input['name'] == "market for electrostatic paint":
            exc["amount"] = 95
            exc.save()

        if exc.input['name'] == "market for electricity, medium voltage":
            exc["amount"] = 105200
            exc.save()

        if exc.input[
            'name'] == "heat, from municipal waste incineration to generic market for heat district or industrial, other than natural gas":
            exc["amount"] = 68760
            exc.save()

        if exc.input['name'] == "market for aluminium, cast alloy":
            exc["amount"] = 65
            exc.save()

        if exc.input['name'] == "market for sheet rolling, steel":
            exc.delete()
        if exc.input['name'] == "market for epoxy resin, liquid":
            exc.delete()
        if exc.input['name'] == "market for glass fibre":
            exc.delete()
        if exc.input['name'] == "market for kraft paper, bleached":
            exc.delete()
        if exc.input['name'] == "market for paper, melamine impregnated":
            exc.delete()
        if exc.input['name'] == "market for electrostatic paint":
            exc.delete()
        if exc.input['name'] == "market for glass fibre":
            exc.delete()

        if exc.input['name'] == "Power transformer TrafoStar 250 MVA":
            exc.input['name'] = "Power transformer TrafoStar 10 MVA"
            exc.input = new_act
            exc.save()

    # insulation
    steel = [act for act in eidb if "market for glass wool mat" in act["name"] and "GLO" in act["location"]][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 337, unit = "kilogram", type = 'technosphere')
    new_exc.save()
    new_act.save()

    # wood
    steel = [act for act in eidb if "planing, board, softwood, u=20%" in act["name"] and "CH" in act["location"]][0]
    new_exc = new_act.new_exchange(input = steel.key, amount = 366, unit = "kilogram", type = 'technosphere')
    new_exc.save()
    new_act.save()


# Foundation functions
def pile_weight(p, pile_height):
    # diameters,inmeters
    diameter = [5, 5.5, 5.75, 6.75, 7.75]
    # KW
    power = [3000, 3600, 4000, 8000, 10000]
    fit_diameter = np.polyfit(power, diameter, 1)
    f_fit_diameter = np.poly1d(fit_diameter)

    # diameter for given power,in m
    outer_diameter = f_fit_diameter(p)
    # Cross section area of pile
    outer_area = (np.pi / 4) * (outer_diameter ** 2)
    # Pile volume, in m3
    outer_volume = outer_area * pile_height

    inner_diameter = outer_diameter
    pile_thickness = np.interp(p, [2000, 3000, 3600, 4000, 8000, 10000], [0.07, 0.10, 0.13, 0.16, 0.19, 0.22])
    inner_diameter -= 2 * pile_thickness
    inner_area = (np.pi / 4) * (inner_diameter ** 2)
    inner_volume = inner_area * pile_height
    volume_steel = outer_volume - inner_volume
    weight_steel = 8000 * volume_steel
    return weight_steel


def transition_height():
    pile_length = [35, 55, 35, 60, 40, 65, 50, 70, 50, 80]
    transition_length = [15, 20, 15, 20, 15, 24, 20, 30, 20, 31]
    fit_transition_length = np.polyfit(pile_length, transition_length, 1)
    return np.poly1d(fit_transition_length)


fit_transition_height = transition_height()


def transition_weight():
    transition_length = [15, 20, 15, 20, 15, 24, 20, 30, 20, 31]
    transition_weight = [150, 250, 150, 250, 160, 260, 200, 370, 250, 420]
    fit_transition_weight = np.polyfit(transition_length, transition_weight, 1)
    return np.poly1d(fit_transition_weight)


fit_transition_weight = transition_weight()


def grout_volume():
    transition_length = [15, 20, 15, 20, 15, 24, 20, 30, 20, 31]
    grout = [15, 35, 15, 35, 20, 40, 25, 60, 30, 65]
    fit_grout = np.polyfit(transition_length, grout, 1)
    return np.poly1d(fit_grout)


fit_grout_volume = grout_volume()


def scour_volume():
    scour = [2200, 2200, 2600, 3100, 3600]
    turbine_power = [3000, 3600, 4000, 8000, 10000]
    fit_scour = np.polyfit(turbine_power, scour, 1)
    return np.poly1d(fit_scour)


fit_scour_volume = scour_volume()


def pile_height(P, fit_penetration_depth, sea_depth):
    return 9 + fit_penetration_depth(P) + sea_depth


def penetration_depth():
    # meters
    depth = [22.5, 22.5, 23.5, 26, 29.5]
    # kW
    P = [3000, 3600, 4000, 8000, 10000]
    fit_penetration = np.polyfit(P, depth, 1)
    f_fit_penetration = np.poly1d(fit_penetration)
    return f_fit_penetration


fit_penetration_depth = penetration_depth()


def transport_requirements(M_nacelle, M_tower, M_rotor, M_foundation, M_all, LT):
    # taken from Vestas 2012 LCA report
    # https://www.vestas.com/~/media/vestas/about/sustainability/pdfs/lca_v903mw_version_1_1.pdf
    trsp_truck_nacelle = 1025 * (M_nacelle / 1000)
    trsp_truck_rotor = 600 * (M_rotor / 1000)
    trsp_truck_tower = 1100 * (M_tower / 1000)
    trsp_ship_tower = 8050 * (M_tower / 1000)
    trsp_truck_foundation = 50 * (M_foundation / 1000)

    # transport to local waste facilities
    trsp_end_of_life = 200 * (M_all / 1000)

    # 30 turbines per plant
    trsp_maintenance_per_year = 2160 / 30 / 1000 * LT

    # 600 km by ship assumed
    trsp_ship_offshore = 600 * (M_all / 1000)
    return trsp_truck_nacelle, trsp_truck_rotor, trsp_truck_tower, trsp_ship_tower, trsp_truck_foundation, trsp_end_of_life, trsp_maintenance_per_year, trsp_ship_offshore


def grout_and_monopile_requirements(P, sea_depth):
    pile_length = pile_height(P, fit_penetration_depth, sea_depth)
    transition_lenght = fit_transition_height(pile_length)

    density = 2400  # kg/m**3
    m_grout = fit_grout_volume(transition_lenght) * density

    m_monopile = 1e3 * fit_transition_weight(transition_lenght)
    return m_grout, m_monopile


# Nexans cable at 150 kV, section, ampacity and power capacity in kW
df150 = pd.DataFrame(index = [400, 500, 630, 800, 1000, 1200, 1600, 2000])
df150['I'] = [710, 815, 925, 1045, 1160, 1335, 1425, 1560]
df150['P'] = 150 * df150['I']

# Nexans cable at 150 kV, section, ampacity and power capacity in kW
df33 = pd.DataFrame(index = [95, 120, 150, 185, 240, 300, 400, 500, 630, 800])
df33['I'] = [352, 399, 446, 502, 581, 652, 726, 811, 904, 993]
df33['P'] = 33 * df33['I']


# defines cable requirements for offshore foundations
def cable_requirements(P, park_size, dist_transfo, dist_coast, affiche = False):
    copper_density = 8960

    # Cable of 300 mm² cross section allocated according to the wind turbine power
    cross_section1 = 300 * P / df33.loc[300].P
    if affiche:
        print('cross_section1 : %s mm²' % cross_section1)
    #
    m_copper = (cross_section1 * 1e-6 * (dist_transfo * 1e3)) * copper_density
    energy_cable_laying_ship = 450 * 39 / 15 * dist_transfo  # 450 l diesel/hour for the ship that lays the cable at sea bottom
    # 39 MJ/liter, 15 km/h as speed of laying the cable

    # Cross section calculated based on the farm cumulated power,
    # and the transport capacity of the Nexans cables @ 150kV if the cumulated power of the park cannot be
    # transported @ 33kV

    # Test if the cumulated power of teh wind farm is inferior to 30 MW,
    # If so, we use 33 kV cables.

    if P * park_size <= 30e3:
        cross_section2 = np.interp(P * park_size, df33.P.values, df33.index.values)
    # Otherwise, we use 150 kV cables
    else:
        cross_section2 = np.interp(P * park_size, df150.P.values, df150.index.values)
    if affiche:
        print('cross_section2 : %s mm²' % cross_section2)

    m_copper += (cross_section2 * 1e-6 * (dist_coast * 1e3 / park_size)) * copper_density
    energy_cable_laying_ship += 450 * 39 / 15 * dist_coast / park_size  # 450 l/h de conso, 39 MJ/l, 15 km/h de vitesse d'installation

    m_cable = m_copper * 617 / 220
    return m_cable * 0.5, energy_cable_laying_ship * 0.5


# defines cable requirements for onshore foundations
def cable_requirements_Onshore(P, affiche = False):
    copper_density = 8960

    # Cable of 300 mm² cross section allocated according to the wind turbine power
    cross_section1 = 300 * P / df33.loc[300].P
    # Calculation of the cable length starting fromt eh road surface, with assumed with of 8 meters
    cable_length = np.interp(P, [0, 2000], [0, 8000]) / 8

    if affiche:
        print('cross_section1 : %s mm²' % cross_section1)
        print('cable length : %s m' % cable_length)
    #
    m_copper = (cross_section1 * 1e-6 * (cable_length)) * copper_density

    m_cable = m_copper * 617 / 220
    return m_cable * 0.5


def add_to_dict(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    else:
        dictionary[key] = dictionary[key] + value


# Activities
# to create a pickle
datasets = pd.read_excel('Wind turbines inventories.xlsx', dtype = None, decimal = ";", header = 0)
del datasets['Unnamed: 9']
print(datasets.head())

# Use of cement for foundation and reinforcing steel for foundation
datasets = datasets.replace('market for concrete, normal', 'market for concrete, sole plate and foundation')
datasets.loc[datasets[(datasets['Component'] == 'Foundation') & (datasets[
                                                                     'Market name'] == 'market for steel, low-alloyed')].index, 'Market name'] = 'market for reinforcing steel'
datasets.loc[datasets[(datasets['Component'] == 'Foundation') & (
        datasets['Market name'] == 'market for reinforcing steel')].index, 'Dataset'] = 'Reinforcing steel'

print(datasets.Dataset.unique())


def find_UUID():
    list_unique_act = datasets['Market name'].unique()
    order_preference = ["DK", "DE", "CH", "RER", "RoW", "GLO"]

    for act in list_unique_act:
        print(act)
        for pref in order_preference:
            list_act = [a for a in eidb if act in a['location']]
            if len(list_act) == 1:
                datasets.loc[:, 'UUID'][datasets.loc[:, 'Market name'] == act] = list_act[0]['code']
            if len(list_act) > 0:
                list_act = [a for a in eidb if act == a["name"] and pref in a["location"]]
                datasets.loc[:, 'UUID'][datasets.loc[:, 'Market name'] == act] = list_act[0]['code']
            else:
                list_act = [a for a in bw.Database("biosphere3") if act in a["name"]]
                if len(list_act) > 0:
                    datasets.loc[:, "UUID"][datasets.loc[:, "Market name"] == act] = list_act[0]["code"]
                    break
                else:
                    datasets.loc[:, "UUID"][datasets.loc[:, "Market name"] == act] = \
                        [a for a in bw.Database("biosphere3") if
                         'Transformation, from pasture, man made, intensive' in a["name"]][0]['code']


def get_act_country():
    list_unique_uuid = datasets.loc[:, "UUID"].unique()
    for uuid in list_unique_uuid:
        try:
            datasets.loc[:, "Location"][datasets.loc[:, "UUID"] == uuid] = bw.get_activity((eidb.name, uuid))[
                "location"]
        except:
            datasets.loc[:, "Location"][datasets.loc[:, "UUID"] == uuid] = None


datasets["UUID"] = 0
find_UUID()
datasets["Location"] = 0
get_act_country()

# We add recycling of aluminium and chromium steel
df_act = datasets
df_act2 = pd.DataFrame(index = df_act.columns)

new_act = [act for act in eidb if 'market for waste' in act['name'] and 'aluminium' in act['name']][0]
print(new_act)
df_act2[new_act['name']] = [None, 'Disposal', None, None, 'Aluminium waste', 'kg', None, eidb.name,
                            new_act['name'], new_act['code'],
                            new_act['location']]  # new_act['code'], new_act['location']

df_act = df_act.append(df_act2.T)
df_act = df_act.append(
    df_act[df_act['Dataset'] == 'Steel, inert waste'].iloc[0].replace('Steel, inert waste', 'Chromium Steel waste'))
df_act

df_act = df_act.replace('ecoinvent 3.3 cutoff', eidb.name)

# Saving data into a pickle
df_act.to_pickle('activities and uuids.pkl')

# To load the pickle
df_act = pd.read_pickle('activities and uuids.pkl')

# To create the pickle
# Loading wind turbine inventories dataframe and creating 'df_inv.pkl'
# All that has "kg" as unit
df_inv = pd.read_excel('Wind turbines inventories.xlsx')

df_inv = df_inv.replace('30kW', 30)
df_inv = df_inv.replace('150kW', 150)
df_inv = df_inv.replace('600kW', 600)
df_inv = df_inv.replace('800kW', 800)
df_inv = df_inv.replace('2000kW', 2000)

df_inv = df_inv[df_inv.Unit == 'kg']

# df_inv = df_inv.pivot_table(columns= 'Power', values= 'Quantity', index=['Phase', 'Component','Sub-component', 'Dataset'])
df_inv = df_inv.pivot_table(columns = 'Power', values = ['Quantity', 'Unit'],
                            index = ['Phase', 'Component', 'Sub-component', 'Dataset'])
df_inv = df_inv.T

# Filling nan values
df_inv = df_inv.loc['Quantity']
df_inv.loc[0] = 0
df_inv = df_inv.sort_index()
df_inv.interpolate(method = 'index', limit_direction = 'both', inplace = True)
df_inv = df_inv.drop(df_inv.index[0])

print('NaN filled')

df_inv_tot = df_inv.T.groupby(level = ['Phase', 'Component']).sum().T

for phase in set(df_inv.columns.get_level_values(0)):
    print(phase + ' is being normalised')
    for component in set(df_inv[phase].columns.get_level_values(0)):
        for sub_comp in set(df_inv[phase][component].columns.get_level_values(0)):
            for dataset in set(df_inv[phase][component][sub_comp].columns.get_level_values(0)):
                # print(phase, component, sub_comp, dataset)
                df_inv[phase][component][sub_comp][dataset] = df_inv[phase][component][sub_comp][dataset] / \
                                                              df_inv_tot[phase][component]

df_inv.to_pickle('df_inv.pkl')

# Loading wind turbine inventories dataframe and creating 'df_inv_not_kg.pkl'
# All that has not "kg" as unit
df_inv_not_kg = pd.read_excel('Wind turbines inventories.xlsx')
df_inv_not_kg = df_inv_not_kg.replace('30kW', 30)
df_inv_not_kg = df_inv_not_kg.replace('150kW', 150)
df_inv_not_kg = df_inv_not_kg.replace('600kW', 600)
df_inv_not_kg = df_inv_not_kg.replace('800kW', 800)
df_inv_not_kg = df_inv_not_kg.replace('2000kW', 2000)

df_inv_not_kg = df_inv_not_kg[df_inv_not_kg.Unit != 'kg']

df_inv_not_kg = df_inv_not_kg.pivot_table(columns = 'Power', values = ['Quantity', 'Unit'],
                                          index = ['Phase', 'Component', 'Sub-component', 'Dataset'])
df_inv_not_kg = df_inv_not_kg.T

for phase in set(df_inv_not_kg.columns.get_level_values(0)):
    for component in set(df_inv_not_kg[phase].columns.get_level_values(0)):
        df_inv_not_kg[phase][component].loc['Quantity'].plot()
        plt.title('%s,%s' % (phase, component))
        plt.ylim([0, df_inv_not_kg[phase][component].loc['Quantity'].max().max()])
        plt.xlim([0, 8000])
        # plt.show()

df_inv_not_kg['Assembly']['Tower']['Assembly']['Galvanizing [m]'] = df_inv_not_kg['Assembly']['Tower']['Assembly'][
    'Steel arc welding [m]']
df_inv_not_kg = df_inv_not_kg.loc['Quantity']

df_inv_not_kg = df_inv_not_kg.drop('Electricity [kWh]', axis = 1, level = 3)
df_inv_not_kg.to_pickle('df_inv_not_kg.pkl')

# To load the pickle

df_inv = pd.read_pickle('df_inv.pkl')
df_inv_not_kg = pd.read_pickle('df_inv_not_kg.pkl')

diesel_burned_activity = [act for act in eidb if 'market for diesel, burned in building machine' in act['name']][0]
MV_transfo = [act for act in eidb if 'Power transformer TrafoStar 10 MVA' in act['name']][0]
HV_transfo = [act for act in eidb if 'Power transformer TrafoStar 500 MVA' in act['name']][0]

assembly_activities = list(set(df_inv['Assembly'].columns.get_level_values(2)))
# Assembly activites to add
Copper_wire_drawing = [act for act in eidb if 'market for wire drawing, copper' in act['name']][0]
print(Copper_wire_drawing)
Explosive = [act for act in eidb if 'market for explosive, tovex' in act['name']][0]
print(Explosive)
Steel_sheet_rolling = [act for act in eidb if 'market for sheet rolling, steel' in act['name']][0]
print(Steel_sheet_rolling)
Aluminium_sheet_rolling = [act for act in eidb if 'market for sheet rolling, aluminium' in act['name']][0]
print(Aluminium_sheet_rolling)
Chromium_sheet_rolling = [act for act in eidb if 'market for sheet rolling, chromium steel' in act['name']][0]
print(Chromium_sheet_rolling)
Road = [act for act in eidb if 'market for road' == act['name'] and 'CH' in act['location']][0]
print(Road)
Truck_transport = [act for act in eidb if 'market for transport, freight, lorry >32 metric ton, EURO6' in act['name']][
    0]
print(Truck_transport)
Ship_transport = [act for act in eidb if 'market for transport, freight, inland waterways, barge' in act['name']][0]
print(Ship_transport)
Digger = [act for act in eidb if 'market for excavation, hydraulic digger' in act['name']][0]
print(Digger)
Cement = [act for act in eidb if 'market for cement, Portland' in act['name']][0]
print(Cement)
print('-----------------------------')

disposal_activities = list(set(df_inv['Disposal'].columns.get_level_values(2)))
disposal_activities.append('Aluminium waste')
disposal_activities.append('Chromium Steel waste')
print(disposal_activities)

# Dataset for electricity directly used and steel low-alloyed
Electricity_dataset = \
    [act for act in eidb if 'market for electricity, high voltage' in act['name'] and 'DK' in act['location']][0]
print(Electricity_dataset)
Steel_dataset = [act for act in eidb if 'market for steel, low-alloyed' == act['name']][0]
print(Steel_dataset)
print('-----------------------------')


# Scaling models used in the publication are defined below
# Scaling model: Rotor diameter (m) - Rated power (kW)

def func_rotor_power(x, a, b, c, d):
    y = a - b * np.exp(-(x - d) / c)
    return y


p_rotor_power_ON = [152.66222073, 136.56772435, 2478.03511414, 16.44042379]
p_rotor_power_OFF = [191.83651588, 147.37205671, 5101.28555377, 376.62814798]


# Scaling model: Hub height (m) - Rated power (kW)
def func_height_power(x, a, b, c):
    y = a - b * np.exp(-(x) / c)
    return y


p_height_power_ON = [116.43035193, 91.64953366, 2391.88662558]
p_height_power_OFF = [120.75491612, 82.75390577, 4177.56520433]


# Scaling model: Nacelle weight (kg) - Rated power (kW)
def func_nacelle_weight_power(x, a, b):
    y = a * x ** 2 + b * x
    return 1e3 * y


p_nacelle_weight_power_ON = [1.66691134e-06, 3.20700974e-02]
p_nacelle_weight_power_OFF = [2.15668283e-06, 3.24712680e-02]


# Scaling model: Rotor weight (kg) - Rotor diameter (m)
def func_rotor_weight_rotor_diameter(x, a, b):
    y = a * x ** 2 + b * x
    return 1e3 * y


p_rotor_weight_rotor_diameter_ON = [0.00460956, 0.11199577]
p_rotor_weight_rotor_diameter_OFF = [0.0088365, -0.16435292]


# Scaling model: Tower (kg) - D²*h (m**3)
def func_tower_weight_d2h(d, h, a, b):
    y = a * d ** 2 * h + b
    return 1e3 * y


p_tower_weight_d2h = [3.03584782e-04, 9.68652909e+00]


# Function to generate the wind turbine LCI
def create_dictionary(P, d = None, h = None, M_tower = None, M_foundation = None, M_reinfSteel_foundation = None,
                      V_conc_foundation = None, M_nacelle = None, M_power_supply = None, M_rotor = None,
                      M_electronics = None, offshore = False, park_size = 50, dist_transfo = 1, dist_coast = 5,
                      sea_depth = 5, print_details = False, lifetime = 20):
    """
    This function generates the lifecycle inventory of a wind turbine
    List of parameters : P (rated power) expressed in kW, d (rotor diameter) expressed in m, h (hub height) expressed in m,
    offshore = True/False (False by default), park_size (number of wind turbines in a park) as integer,
    dist_transfo (ditance to transformer) in meters, disct_coast (distance to coast for offshore) in meters,
    sea_depth (for offshore) in meters, print_details (to print details) as boolean and lifetime (in years) as integer.
    """
    # Setting parameters for scaling model with onshore-offshore distinctions.
    if not (offshore):
        p_rotor_power = p_rotor_power_ON
        p_height_power = p_height_power_ON
        p_nacelle_weight_power = p_nacelle_weight_power_ON
        p_rotor_weight_rotor_diameter = p_rotor_weight_rotor_diameter_ON

    if offshore:
        p_rotor_power = p_rotor_power_OFF
        p_height_power = p_height_power_OFF
        p_nacelle_weight_power = p_nacelle_weight_power_OFF
        p_rotor_weight_rotor_diameter = p_rotor_weight_rotor_diameter_OFF

    # Using scaling model for missing values
    if d == None:
        d = func_rotor_power(P, *p_rotor_power)
    if h == None:
        h = func_height_power(P, *p_height_power)
    if M_tower == None:
        M_tower = func_tower_weight_d2h(d, h, *p_tower_weight_d2h)
    if M_foundation == None:
        M_foundation = 1696e3 * h / 80 * d ** 2 / (100 ** 2)
    if M_reinfSteel_foundation == None:
        M_reinfSteel_foundation = np.interp(P, [750, 2000, 4500], [10210, 27000, 51900])
    if V_conc_foundation == None:
        V_conc_foundation = (M_foundation - M_reinfSteel_foundation) / 2200
    if M_nacelle == None:
        M_nacelle = func_nacelle_weight_power(P, *p_nacelle_weight_power)
    if M_power_supply == None:
        M_power_supply = 620
    if M_rotor == None:
        M_rotor = func_rotor_weight_rotor_diameter(d, *p_rotor_weight_rotor_diameter)
    if M_electronics == None:
        M_electronics = np.interp(P, [30, 150, 600, 800, 2000], [150, 300, 862, 1112, 3946])

    M_all = M_nacelle + M_tower + M_rotor + M_foundation + M_electronics

    # A reprendre avec tous les paramètres possibles
    if print_details:
        print('Nominal power : %s kW' % P)
        print('Rotor diameter : %s m' % d)
        print('Hub height : %s m' % h)
        print('Tower weight : %s kg' % M_tower)
        print('Foundation weight : %s kg' % M_foundation)
        print('Foundation reinforced steel: %s kg' % M_reinfSteel_foundation)
        print('Foundation concrete volume: %s m3' % V_conc_foundation)
        print('Nacelle weight: %s kg' % M_nacelle)
        print('Rotor weight: %s' % M_rotor)
        print('Electronics: %s' % M_electronics)
        print('Total weight: %s kg' % M_all)

    dict_activities = {}

    # Adding input element expressed in percentage of mass * M
    phase = 'Input'
    if print_details:
        print(phase)
    for component in set(df_inv[phase].columns.get_level_values(0)):
        if print_details:
            print('\t' + component)

        if component == 'Electronics':
            M = M_electronics

        if component == 'Foundation':
            continue

        if component == 'Nacelle':
            M = M_nacelle

        if component == 'Power supply':
            M = M_power_supply

        if component == 'Rotor':
            M = M_rotor

        if component == 'Tower':
            M = M_tower

        if print_details:
            print(M)

        for sub_comp in set(df_inv[phase][component].columns.get_level_values(0)):
            if print_details:
                print('\t \t' + sub_comp)
            for dataset in set(df_inv[phase][component][sub_comp].columns.get_level_values(0)):
                df_inv_i = df_inv[phase][component][sub_comp][dataset]
                if print_details:
                    print('\t \t \t' + dataset + '\t M = %s' % M + '\t pctg = %s' % (
                        np.interp(P, df_inv_i.index.values, df_inv_i.values)) + '\t %s' % (
                                  np.interp(P, df_inv_i.index.values, df_inv_i.values) * M))
                    print('\t \t \t' + df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0][
                        'Database name'],
                          df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0]['UUID'])
                add_to_dict(dict_activities, key = bw.get_activity((df_act[(df_act['Dataset'] == dataset) & (
                        df_act['Phase'] == phase)].iloc[0]['Database name'], df_act[
                                                                        (df_act['Dataset'] == dataset) & (
                                                                                df_act['Phase'] == phase)].iloc[0][
                                                                        'UUID'])),
                            value = np.interp(P, df_inv_i.index.values, df_inv_i.values) * M)

    # Adding onshore foundation:
    if not (offshore):
        if print_details:
            print('\t Onshore foundation')
            print('\t \t M_fond = %s' % M_foundation)
            print('\t \t concrete = %s' % V_conc_foundation + 'm3')
            print('\t \t reinforced steel = %s' % M_reinfSteel_foundation + 'kg')
        # V_conc_foundation
        add_to_dict(dict_activities, key = bw.get_activity((eidb.name, df_act[(df_act['Component'] == 'Foundation') & (
                df_act['Market name'] == 'market for concrete, sole plate and foundation')]['UUID'].iloc[0])),
                    value = V_conc_foundation)
        # M_reinfSteel_foundation
        add_to_dict(dict_activities, key = bw.get_activity((eidb.name, df_act[
            (df_act['Component'] == 'Foundation') & (df_act['Market name'] == 'market for waste reinforced concrete')][
            'UUID'].iloc[0])), value = M_reinfSteel_foundation)

    # Adding road
    if not (offshore):
        value = np.interp(P, [0, 2000], [0, 8000])
        add_to_dict(dict_activities, key = bw.get_activity((eidb.name, Road['code'])), value = value)

    # Adding land use
    if False:
        phase = 'Input'
        if print_details:
            print('Land use')
        if not (offshore):
            for dataset in df_inv_not_kg['Input']['Foundation']['Land use']:
                df_inv_not_kg_i = df_inv_not_kg['Input']['Foundation']['Land use'][dataset].dropna()
                if print_details:
                    print(
                        '\t' + dataset + '\t %s' % (np.interp(P, df_inv_not_kg_i.index.values, df_inv_not_kg_i.values)))
                    print('\t' + df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0][
                        'Database name'],
                          df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0]['UUID'])
                add_to_dict(dict_activities, key = bw.get_activity((df_act[(df_act['Dataset'] == dataset) & (
                        df_act['Phase'] == phase)].iloc[0]['Database name'], df_act[
                                                                        (df_act['Dataset'] == dataset) & (
                                                                                df_act['Phase'] == phase)].iloc[0][
                                                                        'UUID'])),
                            value = np.interp(P, df_inv_not_kg_i.index.values, df_inv_not_kg_i.values))

    # Maintenance
    if False:
        if print_details:
            print('Maintenance')
        dataset = 'Car [km]'
        df_inv_not_kg_i = df_inv_not_kg['Maintenance']['Nacelle']['Transport by car'][dataset].dropna()
        if print_details:
            print('\t' + dataset + '\t %s' % (np.interp(P, df_inv_not_kg_i.index.values, df_inv_not_kg_i.values)))
            print('\t' + df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0]['Database name'],
                  df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0]['UUID'])
        add_to_dict(dict_activities, key = bw.get_activity((df_act[(df_act['Dataset'] == dataset) & (
                df_act['Phase'] == phase)].iloc[0]['Database name'], df_act[(df_act['Dataset'] == dataset) & (
                df_act['Phase'] == phase)].iloc[0]['UUID'])),
                    value = np.interp(P, df_inv_not_kg_i.index.values, df_inv_not_kg_i.values))

    # Assembly activities not in kg
    phase = 'Assembly'
    if print_details:
        print(phase + 'not in kg')
    for component in set(df_inv_not_kg[phase].columns.get_level_values(0)):
        if print_details:
            print('\t' + component)
        for sub_comp in set(df_inv_not_kg[phase][component].columns.get_level_values(0)):
            if print_details:
                print('\t \t' + sub_comp)
            for dataset in set(df_inv_not_kg[phase][component][sub_comp].columns.get_level_values(0)):
                df_inv_not_kg_i = df_inv_not_kg[phase][component][sub_comp][dataset].dropna()
                if print_details:
                    print(dataset)
                if component == 'Foundation':
                    df_inv_not_kg_i = df_inv_not_kg[phase][component][sub_comp][dataset].dropna()
                    if print_details:
                        print('\t' + dataset + '\t %s' % (
                            np.interp(P, df_inv_not_kg_i.index.values, df_inv_not_kg_i.values)))
                        print('\t' + df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0][
                            'Database name'],
                              df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0]['UUID'])
                    add_to_dict(dict_activities, key = bw.get_activity((df_act[(df_act['Dataset'] == dataset) & (
                            df_act['Phase'] == phase)].iloc[0]['Database name'], df_act[
                                                                            (df_act['Dataset'] == dataset) & (
                                                                                    df_act['Phase'] == phase)].iloc[
                                                                            0]['UUID'])),
                                value = np.interp(P, df_inv_not_kg_i.index.values, df_inv_not_kg_i.values))

                else:
                    s = InterpolatedUnivariateSpline(df_inv_not_kg_i.index.values, df_inv_not_kg_i.values, k = 1)
                    if print_details:
                        print('\t' + dataset + '\t %s' % (s(P)))
                        print('\t' + df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0][
                            'Database name'],
                              df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0]['UUID'])
                    add_to_dict(dict_activities, key = bw.get_activity((df_act[(df_act['Dataset'] == dataset) & (
                            df_act['Phase'] == phase)].iloc[0]['Database name'], df_act[((df_act[
                                                                                              'Dataset'] == dataset) & (
                                                                                                 df_act[
                                                                                                     'Phase'] == phase)) & (
                                                                                                df_act[
                                                                                                    'Phase'] == phase)].iloc[
                                                                            0]['UUID'])), value = s(P))

    # Connexion_requirements
    if offshore:
        if print_details:
            print('Raccordement offshore')
        M, E_CLS = cable_requirements(P = P, park_size = park_size, dist_transfo = dist_transfo,
                                      dist_coast = dist_coast)

        phase = 'Input'
        component = 'Power supply'
        for sub_comp in set(df_inv[phase][component].columns.get_level_values(0)):
            if print_details:
                print('\t \t' + sub_comp)
            for dataset in set(df_inv[phase][component][sub_comp].columns.get_level_values(0)):
                df_inv_i = df_inv[phase][component][sub_comp][dataset].dropna()
                if print_details:
                    print('\t \t \t' + dataset + '\t %s' % (np.interp(P, df_inv_i.index.values, df_inv_i.values) * M))
                    print('\t \t \t' + df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0][
                        'Database name'],
                          df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0]['UUID'])
                add_to_dict(dict_activities, key = bw.get_activity((df_act[(df_act['Dataset'] == dataset) & (
                        df_act['Phase'] == phase)].iloc[0]['Database name'], df_act[((df_act[
                                                                                          'Dataset'] == dataset) & (
                                                                                             df_act[
                                                                                                 'Phase'] == phase)) & (
                                                                                            df_act[
                                                                                                'Phase'] == phase)].iloc[
                                                                        0]['UUID'])),
                            value = np.interp(P, df_inv_i.index.values, df_inv_i.values) * M)

        # Energy for cable laying ship
        add_to_dict(dict_activities, key = diesel_burned_activity, value = E_CLS)

        # Transfo
        add_to_dict(dict_activities, key = MV_transfo,
                    value = P / 10e3 / 0.85 * lifetime / 35)  # calcul au proratat de la puissance, facteur 0.85 en puissance active et apparente et durée de vie
        add_to_dict(dict_activities, key = HV_transfo, value = P / 500e3 / 0.85 * lifetime / 35)

    # Pour les onshore, Transfo moyenne tension au proratat de la puissance, et cable section et longueur suivant la puissance
    if not (offshore):
        add_to_dict(dict_activities, key = MV_transfo, value = P / 10e3 / 0.85 * 19 / 35)

        M = cable_requirements_Onshore(P)
        phase = 'Input'
        component = 'Power supply'

        for sub_comp in set(df_inv[phase][component].columns.get_level_values(0)):
            if print_details:
                print('\t \t' + sub_comp)
            for dataset in set(df_inv[phase][component][sub_comp].columns.get_level_values(0)):
                df_inv_i = df_inv[phase][component][sub_comp][dataset].dropna()
                if print_details:
                    print('\t \t \t' + dataset + '\t %s' % (np.interp(P, df_inv_i.index.values, df_inv_i.values) * M))
                    print('\t \t \t' + df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0][
                        'Database name'],
                          df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0]['UUID'])
                add_to_dict(dict_activities, key = bw.get_activity((df_act[(df_act['Dataset'] == dataset) & (
                        df_act['Phase'] == phase)].iloc[0]['Database name'], df_act[((df_act[
                                                                                          'Dataset'] == dataset) & (
                                                                                             df_act[
                                                                                                 'Phase'] == phase)) & (
                                                                                            df_act[
                                                                                                'Phase'] == phase)].iloc[
                                                                        0]['UUID'])),
                            value = np.interp(P, df_inv_i.index.values, df_inv_i.values) * M)

    # Transport activities
    trsp_truck_nacelle, trsp_truck_rotor, trsp_truck_tower, trsp_ship_tower, trsp_truck_foundation, trsp_end_of_life, trsp_maintenance_per_year, trsp_ship_offshore = transport_requirements(
        M_nacelle, M_tower, M_rotor, M_foundation, M_all, lifetime)

    # Truck transportation
    trsp_truck = trsp_truck_nacelle + trsp_truck_rotor + trsp_truck_tower + trsp_truck_foundation + trsp_end_of_life + trsp_maintenance_per_year
    add_to_dict(dict_activities, key = bw.get_activity((eidb.name, Truck_transport['code'])), value = trsp_truck)

    # Ship transportation
    if offshore:
        trsp_ship = trsp_ship_tower + trsp_ship_offshore
    else:
        trsp_ship = trsp_ship_tower

    add_to_dict(dict_activities, key = bw.get_activity((eidb.name, Ship_transport['code'])), value = trsp_ship)

    # Scour stuff
    if offshore:
        scour_volume = fit_scour_volume(P)
        add_to_dict(dict_activities, key = bw.get_activity((eidb.name, Digger['code'])), value = scour_volume)

    # Grout stuff and monopile
    if offshore:
        m_grout, m_monopile = grout_and_monopile_requirements(P, sea_depth)
        add_to_dict(dict_activities, key = bw.get_activity((eidb.name, Cement['code'])), value = m_grout)

        phase = 'Input'
        component = 'Tower'
        sub_comp = 'Material'
        M = m_monopile
        for dataset in set(df_inv[phase][component][sub_comp].columns.get_level_values(0)):
            df_inv_i = df_inv[phase][component][sub_comp][dataset].dropna()
            if print_details:
                print('\t \t \t' + dataset + '\t %s' % (np.interp(P, df_inv_i.index.values, df_inv_i.values) * M))
                print('\t \t \t' + df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0][
                    'Database name'],
                      df_act[(df_act['Dataset'] == dataset) & (df_act['Phase'] == phase)].iloc[0]['UUID'])
            add_to_dict(dict_activities, key = bw.get_activity((df_act[(df_act['Dataset'] == dataset) & (
                    df_act['Phase'] == phase)].iloc[0]['Database name'], df_act[((df_act['Dataset'] == dataset) & (
                    df_act['Phase'] == phase)) & (df_act['Phase'] == 'Input')].iloc[0]['UUID'])),
                        value = np.interp(P, df_inv_i.index.values, df_inv_i.values) * M)

    # Assembly depending on kg
    for AA in assembly_activities:
        if print_details:
            print(AA)
        if AA == 'Explosives':
            value = 10
            add_to_dict(dict_activities, key = Explosive, value = value)
        if AA == 'Copper wire drawing':
            value = dict_activities[bw.get_activity((eidb.name, df_act[df_act['Dataset'] == 'Copper']['UUID'].iloc[0]))]
            add_to_dict(dict_activities, key = Copper_wire_drawing, value = value)
        if AA == 'Steel sheet rolling':
            value = dict_activities[
                        bw.get_activity((eidb.name, df_act[df_act['Dataset'] == 'Low-alloy steel']['UUID'].iloc[0]))] + \
                    dict_activities[
                        bw.get_activity((eidb.name, df_act[df_act['Dataset'] == 'Cast iron']['UUID'].iloc[0]))]
            add_to_dict(dict_activities, key = Steel_sheet_rolling, value = value)
        if AA == 'Aluminium sheet rolling':
            value = dict_activities[
                bw.get_activity((eidb.name, df_act[df_act['Dataset'] == 'Aluminium 0% recycled']['UUID'].iloc[0]))]
            add_to_dict(dict_activities, key = Aluminium_sheet_rolling, value = value)
        if AA == 'Chromium sheet rolling':
            value = dict_activities[
                bw.get_activity((eidb.name, df_act[df_act['Dataset'] == 'Chromium steel']['UUID'].iloc[0]))]
            add_to_dict(dict_activities, key = Chromium_sheet_rolling, value = value)

    # Disposal activities
    for DA in disposal_activities:
        if print_details:
            print(DA)
        ei_key_disposal = df_act[(df_act['Dataset'] == DA) & (df_act['Phase'] == 'Disposal')]['UUID'].iloc[0]
        DA = DA.replace(' -waste', '').replace('Steel, inert waste', 'Low-alloy steel').replace('Concrete, inert waste',
                                                                                                'Concrete [m3]').replace(
            'Aluminium waste', 'Aluminium 0% recycled').replace('Chromium Steel waste', 'Chromium steel')
        ei_key_input = df_act[(df_act['Dataset'] == DA) & (df_act['Phase'] == 'Input')]['UUID'].iloc[0]
        try:
            value = - dict_activities[bw.get_activity((eidb.name, ei_key_input))]
            add_to_dict(dict_activities, key = bw.get_activity((eidb.name, ei_key_disposal)), value = value)
        except:
            pass

    # Electicity dataset
    value = 0.5 * (M_nacelle + M_rotor + M_tower)
    add_to_dict(dict_activities, key = bw.get_activity((eidb.name, Electricity_dataset['code'])), value = value)

    # Steel dataset
    value = dict_activities[bw.get_activity((eidb.name, Steel_dataset['code']))]
    del dict_activities[bw.get_activity((eidb.name, Steel_dataset['code']))]
    add_to_dict(dict_activities, key = bw.get_activity((eidb.name, Steel_dataset['code'])), value = value)

    return dict_activities


dict_activities = create_dictionary(P = 2000, print_details = True)

# Calculation with Brightway2
# Huge set of methods

# Acidification
Acid_method = [m for m in bw.methods if 'acidification' in str(m) and 'ILCD' in str(m) and not 'no LT' in str(m)][0]
# Climate change
CC_method = [m for m in bw.methods if
             'IPCC 2013' in str(m) and 'climate change' in str(m) and 'GWP 100a' in str(m) and not 'no LT' in str(m)][0]
# Eutrophication
Eutro_method = \
    [m for m in bw.methods if 'freshwater eutrophication' in str(m) and 'ILCD' in str(m) and not 'no LT' in str(m)][0]
# Ecotoxicity
Ecotox_method = \
    [m for m in bw.methods if 'freshwater ecotoxicity' in str(m) and 'ILCD' in str(m) and not 'no LT' in str(m)][0]
# CED
# non renewable
CEDfossil_method = \
    [m for m in bw.methods if
     'cumulative energy demand' in str(m) and 'non-renewable energy resources, fossil' in str(m)][
        0]
CEDnuclear_method = [m for m in bw.methods if 'cumulative energy demand' in str(m) and 'nuclear' in str(m)][0]
CEDbioNR_method = [m for m in bw.methods if
                   'cumulative energy demand' in str(m) and 'non-renewable energy resources, primary forest' in str(m)][
    0]
# renewable
CEDbiomR_method = \
    [m for m in bw.methods if 'cumulative energy demand' in str(m) and 'renewable energy resources, biomass' in str(m)][
        0]
CEDgeoth_method = \
    [m for m in bw.methods if 'renewable energy resources, geothermal, converted' in str(m) and '' in str(m)][0]
CEDsolar_method = [m for m in bw.methods if 'renewable energy resources, solar, converted' in str(m) and '' in str(m)][
    0]
CEDwater_method = [m for m in bw.methods if
                   'renewable energy resources, potential (in barrage water), converted' in str(m) and '' in str(m)][0]
CEDwind_method = \
    [m for m in bw.methods if 'renewable energy resources, kinetic (in wind), converted' in str(m) and '' in str(m)][0]
# Land use
Land_method = [m for m in bw.methods if 'land' in str(m) and 'ILCD' in str(m) and not 'no LT' in str(m)][0]
# Depletion
Fossildeplet_method = [m for m in bw.methods if
                       'fossil depletion' in str(m) and 'resource' in str(m) and 'H' in str(m) and not 'w/o LT' in str(
                           m)][0]
Metaldeplet_method = [m for m in bw.methods if
                      'metal depletion' in str(m) and 'resource' in str(m) and 'H' in str(m) and not 'w/o LT' in str(
                          m)][0]
Deplet_method = [m for m in bw.methods if
                 'ILCD' in str(m) and 'resource' in str(m) and 'mineral, fossils and renewables' in str(
                     m) and not 'no LT' in str(m)][0]
# Ozone
Ozone_method = \
    [m for m in bw.methods if 'ozone layer depletion' in str(m) and 'ILCD' in str(m) and not 'no LT' in str(m)][0]
# Human health
HH_carcinogenic_method = [m for m in bw.methods if
                          'carcinogenic effects' in str(m) and '' in str(m) and 'ILCD' in str(m) and not 'LT' in str(
                              m) and not '-' in str(m)][0]
HH_noncarcinogenic_method = [m for m in bw.methods if
                             '-carcinogenic effects' in str(m) and '' in str(m) and 'ILCD' in str(
                                 m) and not 'LT' in str(m)][0]
# PM emissions : ILCD
PM_method = [m for m in bw.methods if
             'ILCD' in str(m) and 'human health' in str(m) and 'respiratory effects, inorganics' in str(m)][0]
# Water
Water_method = [m for m in bw.methods if
                'water' in str(m) and 'scarcity' in str(m) and 'water resources' in str(m) and not 'no LT' in str(m)][0]

list_methods = [Acid_method, CC_method, Eutro_method, Ecotox_method, Land_method, Fossildeplet_method,
                Metaldeplet_method, Deplet_method, Ozone_method, HH_carcinogenic_method, HH_noncarcinogenic_method,
                Water_method, PM_method, CEDfossil_method, CEDnuclear_method, CEDbioNR_method, CEDbiomR_method,
                CEDgeoth_method, CEDsolar_method, CEDwater_method, CEDwind_method]
print('set_of_methods: \n %s \n' % list_methods)


def calculate_impact(dict_activities = None, P = None, lifetime = 20, load_factor = 0.3, list_methods = list_methods):
    bw.calculation_setups['multiLCA'] = {'inv': [dict_activities], 'ia': list_methods}
    bw.calculation_setups['multiLCA']
    myMultiLCA = bw.MultiLCA('multiLCA')
    myMultiLCA.results
    df_impact = pd.DataFrame(columns = list_methods, data = myMultiLCA.results)

    df_impact_kWh = df_impact / (P * lifetime * 8760 * load_factor)
    return df_impact, df_impact_kWh
'''

# Visualization
df_all = pd.read_csv('Complete_dataframe.csv')
df_all['Carbon footprint per kWh'] = df_all["('IPCC 2013', 'climate change', 'GWP 100a')"] / df_all.loc[:,
                                                                                             '1977':'2050'].sum(
    axis = 1) * 1000
print(df_all["Carbon footprint per kWh"].head())

from mpl_toolkits.basemap import Basemap
from matplotlib import cm

plt.rcParams.update({'font.size': 16})
import matplotlib.colors as mcolors

cdict = {'red': ((0.0, 0.0, 0.0),
                 (0.5, 0.0, 0.0),
                 (1.0, 1.0, 1.0)),
         'blue': ((0.0, 0.0, 0.0),
                  (1.0, 0.0, 0.0)),
         'green': ((0.0, 0.0, 1.0),
                   (0.5, 0.0, 0.0),
                   (1.0, 0.0, 0.0))}

color_map = mcolors.LinearSegmentedColormap('my_colormap', cdict, 100)

plt.figure(figsize = (14, 16))
my_map = Basemap(projection = 'merc', lat_0 = 56, lon_0 = 11,
                 resolution = 'h', area_thresh = 0.1,
                 llcrnrlon = 7, llcrnrlat = 54,
                 urcrnrlon = 13, urcrnrlat = 58)

my_map.drawcoastlines()
my_map.drawcountries(color = "grey", zorder = 1)
my_map.fillcontinents(color = 'grey', zorder = 1, alpha = .1)
my_map.drawmapboundary(fill_color = "white")

df_data = df_all[(df_all["Estimated load factor"] > 0.1)]
data = np.array(df_data['Carbon footprint per kWh'])
p_max = max(data)

x,y=my_map(df_data['lon'].tolist(),df_data['lat'].tolist())
my_map.scatter(x, y, marker='o', edgecolor=None, zorder=1, cmap=color_map, c=color_map(df_data['Carbon footprint per kWh']/1000))

l1 = plt.scatter([],[], s=100,  edgecolor='black', linewidth='0.1', color=color_map(5), cmap=color_map)
l2 = plt.scatter([],[], s=100, edgecolor='black', linewidth='0.1', color=color_map(10), cmap=color_map)
l3 = plt.scatter([],[], s=100,  edgecolor='black', linewidth='0.1', color=color_map(20), cmap=color_map)
l4 = plt.scatter([],[], s=100,  edgecolor='black', linewidth='0.1', color=color_map(30), cmap=color_map)
l5 = plt.scatter([],[], s=100, edgecolor='black', linewidth='0.1', color=color_map(40), cmap=color_map)
l6 = plt.scatter([],[], s=100,  edgecolor='black', linewidth='0.1', color=color_map(50), cmap=color_map)
l7 = plt.scatter([],[], s=100,  edgecolor='black', linewidth='0.1', color=color_map(100), cmap=color_map)

labels = ["5 g", "10 g", "20 g", "30 g", "40 g", "50 g", "100 g"]

leg = plt.legend([l1, l2, l3, l4, l5, l6, l7], labels, ncol=7, frameon=True, fontsize=16,
handlelength=2, loc = 8, borderpad = 1, handletextpad=.2, title='$CO_2$ [g] per kWh produced', scatterpoints = 1)
plt.title('Carbon footprint per kWh', fontsize = 40)

plt.show()