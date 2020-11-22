# 直接成本
class DirectCosts:
    def __init__(self, equipment_cost):
        self.equipment_cost = equipment_cost

    def TDC_Totaldirectcosts(self):
        total_direct_cost = self.Delivery() + self.Servicefacilities() + self.Buildingsconstruction() + \
                            self.Equipmentinstallation() + self.Piping() + self.Instrumentationandcontrol() + \
                            self.Sitedevelopment() + self.Electricalsysteminstallation() + self.equipment_cost
        return total_direct_cost

    def Delivery(self):
        delivery = 0.1 * self.equipment_cost
        return delivery

    def Equipmentinstallation(self):
        equipment_installation = 0.47 * self.equipment_cost
        return equipment_installation

    def Instrumentationandcontrol(self):
        instrumentation_and_control = 0.36 * self.equipment_cost
        return instrumentation_and_control

    def Piping(self):
        piping = 0.68 * self.equipment_cost
        return piping

    def Electricalsysteminstallation(self):
        electrical_system_installation = 0.11 * self.equipment_cost
        return electrical_system_installation

    def Buildingsconstruction(self):
        buildings_construction = 0.18 * self.equipment_cost
        return buildings_construction

    def Sitedevelopment(self):
        site_development = 0.1 * self.equipment_cost
        return site_development

    def Servicefacilities(self):
        service_facilities = 0.7 * self.equipment_cost
        return service_facilities


# 间接成本
class IndirectCosts:
    def __init__(self, equipment_cost):
        self.equipment_cost = equipment_cost

    def Engineeringandsupervision(self):
        engineering_and_supervision = 0.33 * self.equipment_cost
        return engineering_and_supervision

    def Construction_fee(self):
        construction_fee = 0.41 * self.equipment_cost
        return construction_fee

    def Legalexpenses(self):
        legal_expenses = 0.04 * self.equipment_cost
        return legal_expenses

    def Contractorslabour(self):
        contractors_labour = 0.22 * self.equipment_cost
        return contractors_labour

    def Contingency(self):
        contingency = 0.44 * self.equipment_cost
        return contingency

    def TIC_Totalindirectcosts(self):
        total_indirect_costs = self.Engineeringandsupervision() + self.Construction_fee() + self.Legalexpenses()
        +self.Contractorslabour() + self.Contingency()
        return total_indirect_costs


# 资本投资
class CapitalInvestment(IndirectCosts, DirectCosts):
    def __init__(self, equipment_cost):
        super(CapitalInvestment, self).__init__(equipment_cost)

    def TCI_Totalcapitalinvestment(self):
        total_capital_investment = self.FCI_Fixedcapitalinvestment() + self.Landpurchase() + self.Startupcost() + \
                                   self.Workingcapital()
        return total_capital_investment

    def FCI_Fixedcapitalinvestment(self):
        fixed_capital_investment = self.TIC_Totalindirectcosts() + self.TDC_Totaldirectcosts()
        return fixed_capital_investment

    def Landpurchase(self):
        land_purchase = 0.09 * self.FCI_Fixedcapitalinvestment()

        return land_purchase

    def Startupcost(self):
        start_up_cost = 0.1 * self.TDC_Totaldirectcosts()
        return start_up_cost

    def Workingcapital(self):
        working_capital = 0.89 * self.Delivery()
        return working_capital


# 工厂生产成本
class ProductionCostofPlant(CapitalInvestment):
    def __init__(self, equipment_cost, number_of_operators = None, product_sale_cost = None, plant_overheads = None,
                 utilities = None, rent = None, depreciation = None, labour = None, supervision = None,
                 maintenance = None):
        super(ProductionCostofPlant, self).__init__(equipment_cost)
        self.number_of_operators = number_of_operators
        self.product_sale_cost = product_sale_cost
        self.plant_overheads = plant_overheads
        self.utilities = utilities
        self.rent = rent
        self.depreciation = depreciation
        self.labour = labour
        self.supervision = supervision
        self.maintenance = maintenance

    def TPC_Totalproductioncosts(self):
        tpc_total_production_costs = self.VOC_Variableoperatingcosts() + self.Fixedoperatingcosts() + \
                                     self.plant_overheads + self.Generalexpenses()
        return tpc_total_production_costs

    def VOC_Variableoperatingcosts(self):
        voc_variable_operating_costs = self.Operatinglabour() + self.Operatingsupervision() + self.Maintenanceandrepair() + \
                                       self.Operatingsupplies() + self.Laboratorycharges() + \
                                       self.Royalties() + self.utilities
        return voc_variable_operating_costs

    def Operatinglabour(self):
        operating_labour = self.number_of_operators
        return operating_labour

    def Operatingsupervision(self):
        operating_supervision = 0.15 * self.Operatinglabour()
        return operating_supervision

    def Maintenanceandrepair(self):
        maintenance_and_repair = 0.06 * self.FCI_Fixedcapitalinvestment()
        return maintenance_and_repair

    def Operatingsupplies(self):
        operating_supplies = 0.15 * self.Maintenanceandrepair()
        return operating_supplies

    def Laboratorycharges(self):
        laboratory_charges = 0.15 * self.Operatinglabour()
        return laboratory_charges

    def Royalties(self):
        royalties = 0.03 * self.product_sale_cost
        return royalties

    def Fixedoperatingcosts(self):
        fixed_operating_costs = self.Propertytax() + self.Insurance() + self.rent + self.depreciation
        return fixed_operating_costs

    def Propertytax(self):
        property_tax = 0.02 * self.FCI_Fixedcapitalinvestment()
        return property_tax

    def Insurance(self):
        insurance = 0.01 * self.FCI_Fixedcapitalinvestment()
        return insurance

    def Generalexpenses(self):
        general_expenses = self.Administration() + self.Distributionandselling() + self.Researchanddevelopment()
        return general_expenses

    def Administration(self):
        administration = 0.20 * self.labour + self.supervision + self.maintenance
        return administration

    def Distributionandselling(self):
        distribution_and_selling = 0.05 * self.TPC_Totalproductioncosts()
        return distribution_and_selling

    def Researchanddevelopment(self):
        research_and_development = 0.04 * self.TPC_Totalproductioncosts()
        return research_and_development

# eq = 100000
# DC = DirectCosts(eq)
# IDC = IndirectCosts(eq)
# CI = CapitalInvestment(eq)
# print(DC.TDC_Totaldirectcosts())
# print(IDC.TIC_Totalindirectcosts())
# print(CI.TCI_Totalcapitalinvestment())
