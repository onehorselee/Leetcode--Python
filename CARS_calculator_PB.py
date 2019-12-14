"""
Created on Mon Aug 12 09:25:50 2019
@author: A-Qian.Li
"""
from CARS_inputs import CARS_inputs
import math

class CARS_calculator_PB(CARS_inputs):
    def __init__(self):
        # ADJUSTERS
        self.adjuster_identifier= .0          #G7
        self.adjuster_engine = .0
        self.adjuster_annualVol = .0
        self.adjuster_region = .0
        self.adjuster_chassis_type = .0
        self.adjuster_conquest = .0
        # GUIDELINE OUTPUTS
        self.adjusted_list_price = .0
        self.DNET_no_list_promo = .0
        self.guideline_CAR = .0
        self.guideline_NSP = .0
        self.dealer_net_price = .0
        self.dealer_discount = .0
        # PROGRAM
        self.sales_allowance = .0
        self.program_discount_amount = .0      #C36
        self.program_discount_percent = .0     #C37
        self.effective_base_program_discount = .0
        self.net_sale_at_base_program = .0
        self.final_guideline = .0        
        # DATES MATCHES COLUMNS NANES IN GUIDELINE_LOOKUP TABLE
        
        
    def lookUp_adjusters(self, df_gdlp):
        df_gdlp = df_gdlp[df_gdlp["CC_MODEL"].str.contains(self.model_identifier)]
        #G7
        if self.pricing_period not in self.PB_pricing_dates: 
            raise Exception ("Pricing Period should be in {}".format(self.PB_pricing_dates))
        self.adjuster_identifier = self.check_NoneType(list(df_gdlp[self.pricing_period+"_GUIDELINE_BASE"])[0])   
        #G9
        if self.engine == "NATURAL GAS" or "GAS" in self.engine:
            self.adjuster_engine = self.check_NoneType(list(df_gdlp["NAT_GAS"])[0]) 
        #G10 function: 
                        #G10==MAX(VAR1, VAR2)
                        # VAR1 = LOG10(3)*VLOOKUP($C$8,GuidelinesLookup!$F$2:$W$97,7,FALSE),
                        # IF(C10=0,
                        #   VAR2 = LOG10(C11)*VLOOKUP($C$8,GuidelinesLookup!$F$2:$W$97,7,FALSE),
                        # else: 
                        #   VAR2 = MAX(LOG10(C10),LOG10(C11))*VLOOKUP($C$8,GuidelinesLookup!$F$2:$W$97,7,FALSE)
                        #   ))
        self.customer_slope = self.check_NoneType(list(df_gdlp["CUSTOMER_SLOPE"])[0])
        var1 = math.log10(3) * self.customer_slope
        if self.annual_customer_vol == 0:
            var2 = math.log10(self.deal_size_min) * self.customer_slope
        else:
            var2 = max(math.log10(self.annual_customer_vol), math.log10(self.deal_size_min)) * self.customer_slope        
        self.adjuster_annualVol = max(var1, var2)
        ##
        #G12
        if self.region in ["CANADA", "CA"] :
            self.adjuster_region = self.check_NoneType(list(df_gdlp["CANADA"])[0])
        #G13
        if self.chassis_type == "TRUCK":
            self.adjuster_chassis_type = self.check_NoneType(list(df_gdlp["TRUCK"])[0])
        #G14
        if self.conquest == "REGION":
            self.adjuster_conquest = self.check_NoneType(list(df_gdlp["REGION_CONQUEST"])[0] )
        elif self.conquest == "FLEET":
            self.adjuster_conquest = self.check_NoneType(list(df_gdlp["FLEET_CONQUEST"])[0])
        #G19 
        self.dealer_discount = self.check_NoneType(list(df_gdlp["DEALER_DISCOUNT"])[0])
        #C34
        self.sales_allowance = self.check_NoneType(list(df_gdlp["SALES_ALLOWANCE"])[0])
        #C36
        if self.engine_brand == "PACCAR":
            self.program_discount_amount = self.check_NoneType(list(df_gdlp["MX_LIST_DISCOUNT"])[0])
        else:
            self.program_discount_amount = self.check_NoneType(list(df_gdlp["CUMMINS_LIST_DISCOUNT"])[0])
            
        if self.program_discount_amount == None:
            self.program_discount_amount = .0


    def cal_CARguideline_addsup(self):
        self.adjusted_list_price = self.list_price - self.list_discount
        self.DNET_no_list_promo = self.list_price * self.dealer_discount/100
        self.guideline_CAR += self.adjuster_identifier
        self.guideline_CAR += self.adjuster_engine
        self.guideline_CAR += self.adjuster_annualVol
        self.guideline_CAR += self.adjuster_region
        self.guideline_CAR += self.adjuster_chassis_type
        self.guideline_CAR += self.adjuster_conquest
        self.guideline_NSP = self.DNET_no_list_promo * (1-self.guideline_CAR/100)
        self.dealer_net_price = self.adjusted_list_price * self.dealer_discount/100
        #C25
        self.final_guideline = (self.dealer_net_price - self.guideline_NSP) * 100 / self.dealer_net_price


    def cal_programDiscount(self):
        #C37
        self.program_discount_percent = 100 * (self.program_discount_amount * (self.dealer_discount/100) * (1-(self.sales_allowance/100)) )/self.DNET_no_list_promo
        #C39
        self.effective_base_program_discount = self.program_discount_percent + self.sales_allowance
        #C40
        self.net_sale_at_base_program = self.DNET_no_list_promo * (1- (self.effective_base_program_discount/100))


    def printOutSummary(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("SUMMARY REPORT: ")
        print("           Adjusted List: {:.2f}".format(self.adjusted_list_price))
        print("           DNet_No List Promo: {:.2f}".format(self.DNET_no_list_promo))
        print("           Guideline CAR: {:.2f}".format(self.guideline_CAR))
        print("           Guideline NSP: {:.2f}".format(self.guideline_NSP))
        print("           Dealer Net: {:.2f}".format(self.dealer_net_price))
        print("           Final guideline:  {:.2f}".format(self.final_guideline)) 
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    def printOutAjusters(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("ADJUSTERS: ")
        print("           Adjuster of identifier(CCMODEL, G7):  {:.2f}".format(self.adjuster_identifier)) 
        print("           Adjuster of engine (G9): {:.2f}".format(self.adjuster_engine))
        print("           Adjuster of customer_slope: {:.2f}".format(self.customer_slope))
        print("           Adjuster of annual volume(G10): {:.2f}".format(self.adjuster_annualVol))
        print("           Adjuster of region (G12): {:.2f}".format(self.adjuster_region))
        print("           Adjuster of chassis type (G13): {:.2f}".format(self.adjuster_chassis_type))
        print("           Adjuster of conquest (G14): {:.2f}".format(self.adjuster_conquest))        
        print("           Adjuster of dealer discount(G19): {:.2f}".format(self.dealer_discount))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    def printOutGuidelinesSec(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("GUIDELINES: ")
        print("           Adusted list price:  {:.2f}".format(self.adjusted_list_price)) 
        print("           DNet_No List promo: {}".format(self.DNET_no_list_promo))
        print("           Guideline CAR(cell C21): {:.2f}".format(self.guideline_CAR))
        print("           Guideline NSP: {:.2f}".format(self.guideline_NSP))
        print("           Dealer Net: {:.2f}".format(self.dealer_net_price))
        print("           Final Guideline CAR(cell C25): {:.2f}".format(self.final_guideline))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")       


    def printOutProgramDiscount(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("PROGRAM: ")
        print("           Sales Allowance: {:.2f}".format(self.sales_allowance))
        print("           Engine Brand: {}".format(self.engine_brand))
        print("           Program List Discount: {:.2f}".format(self.program_discount_amount))
        print("           Program List Discount (%): {:.2f}".format(self.program_discount_percent))
        print("           Effective Base Program Discount: {:.2f}".format(self.effective_base_program_discount))
        print("           Net Sale at Base Program: {:.2f}".format(self.net_sale_at_base_program))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    def cal_guideline(self, **kwargs):
        self.lookUp_customerRelationshipSize(self.tableDict["PB_CUSTOMER_SIZE"])
        self.lookUp_adjusters(self.tableDict["PB_GUIDELINE_LOOKUP"])
        self.cal_CARguideline_addsup()
        self.cal_programDiscount()
        self.guideline_disrection = self.proposed_guideline - self.final_guideline
        self.cal_discretion()
        self.printOutSummary()
        if self.DEBUG_MODE:
            self.printOutAjusters()
            self.printOutProgramDiscount()
        return self.final_guideline

    
    
    
