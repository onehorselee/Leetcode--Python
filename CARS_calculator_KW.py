"""
Created on Mon Aug 12 09:25:50 2019
@author: A-Qian.Li
"""
from CARS_inputs import CARS_inputs
import math
import traceback
import sys


class CARS_calculator_KW(CARS_inputs):
    def __init__(self):
        # VARS FOR INITIAL GUIDELINE BASE
        self.customer_relationship = 0    
        self.aditional_value = .0
        self.adjuster_model = .0
        self.adjuster_cab_type = .0
        self.adjuster_list_price = .0
        self.adjuster_conquest = .0
        self.adjuster_chassis_type = .0
        self.adjuster_engine = .0
        self.adjuster_identifier = .0
        self.initial_guideline_base = .0
        self.adjuster_customer_relationship_F = .0
        self.adjuster_customer_relationship_J = .0
        # VARS FOR EFFECTIVE PROGRAM PERCENT
        self.TC_indicator = "TC"              # TC, TB, Rematch
        self.twoK_listSurcharge = .0          # 2000 surcharge
        self.oneK_listSurcharge = .0          # 1000 surcharge
        self.dealer_bonus_offered = False
        self.dealer_stock_bonus_amount = .0
        self.list_min_net_price_impact = .0
        self.total_net_impact = .0
        self.DNET = .0
        self.dealer_net_price = .0
        self.guideline_net_price = .0
        self.base_CAR_net_price = .0
        self.base_program_type_selection = -0.1
        self.base_program_discount = .0        
        self.net_price_after_adjusters = .0
        self.effective_program_percent = .0
        # VARS FOR INTERMEDIARY GUIDELINE AT CUSTOMER SIZE
        self.customer_size_intercept = .0
        self.guideline_base_at_intermediary_end = .0
        self.intermediary_slope = .0
        self.original_guideline_base_at_customer_size = .0
        self.intermediary_guideline_at_customer_size = .0
        # VARS FOR CORRECTED FINAL GUIDELINE BASE
        self.final_intermediate_end_at_size = .0
        self.guideline_allowed_below_program = .0        
        self.recommendation_below_effective_program = False
        self.expected_annual_buy_blank = False 
        self.final_guideline = .0        

  
    def lookUp_adjusters(self, df_ad, df_btv):        
        try:
            # LOOK UP
            self.adjuster_model = list(df_ad[df_ad['ADJUSTER_FAMILY']== 'PRICING PERIOD'][df_ad["ADJUSTER_NAME"] == self.pricing_period][df_ad["PROGRAM_NAME"]== self.model]["ADJUSTER"])[0]
            self.adjuster_cab_type = list(df_ad[df_ad['ADJUSTER_FAMILY']== 'CAB TYPE'][df_ad["ADJUSTER_NAME"] == self.cab_type.upper()][df_ad["PROGRAM_NAME"]== self.model]["ADJUSTER"])[0]
            # LOOK UP 
            self.base_truck_price = list(df_btv[df_btv["PROGRAM"].str.contains(self.model)][df_btv["MODEL_VALUATION_DATE"].str.contains(self.pricing_period)][df_btv["CAB_TYPE"].str.contains(self.cab_type)]["TRUCK_VALUE"])[0]
            self.adjuster_list_price = list(df_ad[df_ad["ADJUSTER_NAME"]=="CONTENT"][df_ad["PROGRAM_NAME"]==self.model]["ADJUSTER"])[0]
            # CALCULATED
            self.adjuster_list_price = (self.list_price/self.base_truck_price-1)/0.1 * self.adjuster_list_price
            # LOOK UP
            self.adjuster_chassis_type = list(df_ad[df_ad['ADJUSTER_FAMILY']== 'CHASSIS TYPE'][df_ad["ADJUSTER_NAME"] == self.chassis_type.upper()][df_ad["PROGRAM_NAME"]== self.model]["ADJUSTER"])[0]
            self.adjuster_engine = list(df_ad[df_ad['ADJUSTER_FAMILY']== 'ENGINE'][df_ad["ADJUSTER_NAME"] == self.engine.upper()][df_ad["PROGRAM_NAME"]== self.model]["ADJUSTER"])[0]
            self.adjuster_identifier = list(df_ad[df_ad['ADJUSTER_FAMILY']== 'IDENTIFIER'][df_ad["ADJUSTER_NAME"] == self.model_identifier][df_ad["PROGRAM_NAME"]== self.model]["ADJUSTER"])[0]
            self.adjuster_customer_relationship_F = list(df_ad[df_ad['ADJUSTER_FAMILY']== 'SIZE'][df_ad["ADJUSTER_NAME"] == "CUSTOMER SIZE"][df_ad["PROGRAM_NAME"]== self.model]["ADJUSTER"])[0]
            # CALCULATED
            self.adjuster_customer_relationship_J = self.adjuster_customer_relationship_F * round(math.log10(max(self.deal_size_min, self.customer_relationship, 0)),9)
        except Exception as e:
            traceback.print_exc()
            return {"009": str(e)}
            

    def cal_initial_guideline_base(self):
        ### THE INITIAL/HIGHTEST DISCOUNT
        self.initial_guideline_base = .0
        self.initial_guideline_base += self.adjuster_model
        self.initial_guideline_base += self.adjuster_cab_type
        self.initial_guideline_base += self.adjuster_chassis_type
        self.initial_guideline_base += self.adjuster_engine
        self.initial_guideline_base += self.adjuster_identifier

    def cal_effective_program(self, df_scs, df_dnet):
        ### THE BASE/LOWEST DISCOUNT
        # LOOK-UP 
        filterDict = {"PRICE_PERIOD": self.pricing_period,
                      "MODEL": self.model_identifier,
                      "COUNTRY": self.country,}
        df = df_scs.copy()
        for key, value in filterDict.items():
            df = df[df[key]==value]
        # LOOK-UP
        set_a = set(list(df["CAB_TYPE"].unique()))
        set_b = set([self.cab_type])
        if len(set_a.intersection(set_b))>0:
            df = df[df["CAB_TYPE"]==self.cab_type]            
        self.TC_indicator = list(df["TC_TB_INDICATOR"])[0]
        self.dealer_bonus_offered = True if (list(df["DEALER_BONUS_INDICATOR"])[0]).upper() == "YES" else False  
        # LOOK-UP
        df_dnet = df_dnet[df_dnet["MODEL"]==self.model_identifier]
        set_c = set(list(df_dnet["CAB_TYPE"].unique()))
        if len(set_c.intersection(set_b))>0:
            df_dnet = df_dnet[df_dnet["CAB_TYPE"]==self.cab_type]
        self.DNET = self.check_NoneType(list(df_dnet["DEALER_NET"])[0])
        self.guideline_allowed_below_program = self.check_NoneType(list(df_dnet["GUIDELINE_BELOW_PROGRAM_INDICATOR"])[0])

        # CALCULATOR DEALER NET PRICE
        self.dealer_net_price = (self.list_price - self.list_discount) * self.DNET
        

        if self.TC_indicator in ["TC", "TB"]:
            # GO TO STOCK CONTROL SHEET, SEARCH FOR BASE PROGRAM DISCOUNT
            self.base_program_type_selection = list(df["PACCAR_PCT"])[0] if self.engine_brand=="PACCAR" else list(df["CUMMINS_PCT"])[0] 
            self.twoK_listSurcharge = list(df["LIST_SURCHARGE_2000"])[0]   
            self.oneK_listSurcharge = list(df["LIST_SURCHARGE_1000"])[0]
        if self.base_program_type_selection > 0:
            self.base_program_discount = self.base_program_type_selection                         
              

        if self.Stock_Bonus_Eligibility and self.dealer_bonus_offered:
            self.dealer_stock_bonus_amount = -list(df_dnet[df_dnet["MODEL"]==self.model_identifier][df_dnet["CAB_TYPE"]==self.cab_type]["DEALER_STOCK_BONUS"])[0]
        else:
            self.dealer_stock_bonus_amount = .0
         
        if self.list_price < self.twoK_listSurcharge:
            self.list_min_net_price_impact = 2000
        elif self.list_price < self.oneK_listSurcharge:
                self.list_min_net_price_impact = 1000
        else:
            self.list_min_net_price_impact = 0

        # TOTAL NET IMPACT   
        self.total_net_impact = self.list_min_net_price_impact + self.dealer_stock_bonus_amount       
        self.base_CAR_net_price = self.list_price * self.DNET * (1-self.base_program_discount * 0.01)
        self.net_price_after_adjusters = self.base_CAR_net_price + self.total_net_impact
        self.effective_program_percent = (1 - self.net_price_after_adjusters/(self.list_price * self.DNET)) * 100


    def cal_itermdediary_guideline_at_customer_size(self):
        # THE IN-BETWEEN DISCOUNT
        if self.adjuster_customer_relationship_F == .0:
            self.adjuster_customer_relationship_F = 1
        self.customer_size_intercept = 10 ** ((self.effective_program_percent - self.initial_guideline_base)/self.adjuster_customer_relationship_F)
        self.customer_size_intercept_plus_10 = self.customer_size_intercept + 10
        self.intercept_if_program_intercept_donotacross = 50
        if self.initial_guideline_base<= self.effective_program_percent:
            # D64 = D27+LOG10(D60)*F13
            self.guideline_base_at_intermediary_end = self.initial_guideline_base + round(math.log10(self.customer_size_intercept_plus_10),9)*self.adjuster_customer_relationship_F
            # (D64-D56)/(LOG10(D60)-LOG10(3))
            self.intermediary_slope = (self.guideline_base_at_intermediary_end-self.effective_program_percent)/(math.log10(self.customer_size_intercept_plus_10)-math.log10(3))
        else:
            # D27+LOG10(D62)*F13
            self.guideline_base_at_intermediary_end = self.initial_guideline_base + math.log10(self.intercept_if_program_intercept_donotacross)*self.adjuster_customer_relationship_F
            # (D64-D56)/(LOG10(D62)-LOG10(3))
            self.intermediary_slope = (self.guideline_base_at_intermediary_end-self.effective_program_percent)/(math.log10(self.intercept_if_program_intercept_donotacross)-math.log10(3))

        self.original_guideline_base_at_customer_size = self.initial_guideline_base + self.adjuster_customer_relationship_J
        # D66*(LOG10(MAX(D13,D11))-LOG10(3))+D56
        self.intermediary_guideline_at_customer_size = self.intermediary_slope*(math.log10(max(self.deal_size_min, self.customer_relationship))-math.log10(3))+self.effective_program_percent


    def cal_corrected_final_guideline_base(self):
        # BASED UPON CUSTOMER RELATIONSHIP SIZE - DECIDE WHICH DISCOUNT AMONG (INITIAL, EFFECTIVE, INTERMEDIARY) TO PICK
        # D72
        if self.initial_guideline_base <= self.effective_program_percent:
            self.final_intermediate_end_at_size = self.customer_size_intercept_plus_10
        else:
            self.final_intermediate_end_at_size = self.intercept_if_program_intercept_donotacross        

        # THREE GROUPS - BASED UPON CUSTOMER RELATIONSHIP SZIE     
        self.guideline_allowed_below_program_below3 = .0
        self.guideline_allowed_below_program_between3and50 = .0
        self.guideline_allowed_below_program_above50 = .0
        self.final_guideline_base = .0
        Max_deal_relationshipsize = max(self.deal_size_min, self.customer_relationship)
        if not ((self.initial_guideline_base > self.effective_program_percent) and (self.TC_indicator == "TB")):
            # D77
            if Max_deal_relationshipsize <=3: 
                self.guideline_allowed_below_program_below3 = self.effective_program_percent
            # F77
            if ((Max_deal_relationshipsize > 3) and (Max_deal_relationshipsize < self.final_intermediate_end_at_size)): 
                self.guideline_allowed_below_program_between3and50 = self.intermediary_guideline_at_customer_size 
            # H77
            if (Max_deal_relationshipsize > self.final_intermediate_end_at_size):                                       
                self.guideline_allowed_below_program_above50 = self.original_guideline_base_at_customer_size   
        
        # D79
        if((self.initial_guideline_base>self.effective_program_percent) and (self.TC_indicator == "TB")):
            self.final_guideline_base = self.original_guideline_base_at_customer_size

        # D81
        if self.guideline_allowed_below_program == "YES":
            self.corrected_final_guideline_base = self.original_guideline_base_at_customer_size
        else:
            self.corrected_final_guideline_base = max(self.guideline_allowed_below_program_below3, self.guideline_allowed_below_program_between3and50, self.guideline_allowed_below_program_above50, self.final_guideline_base)
        
        self.corrected_base_with_postProg_adjusters = self.corrected_final_guideline_base + self.adjuster_list_price
        self.recommendation_below_effective_program = True if self.corrected_base_with_postProg_adjusters < self.effective_program_percent else False
        if self.guideline_allowed_below_program == "YES":
            self.final_guideline = self.corrected_base_with_postProg_adjusters
        else:
            if(Max_deal_relationshipsize<=3):
                self.final_guideline = self.effective_program_percent
            else:
                if(self.recommendation_below_effective_program):
                    self.final_guideline = self.effective_program_percent
                else:
                    self.final_guideline = self.corrected_base_with_postProg_adjusters
        
        self.guideline_net_price = self.dealer_net_price * (1-self.final_guideline/100)

    def printOutSummary(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("SUMMARY REPORTS: ")
        print("           Dealer Net Price: {:.0f}".format(self.dealer_net_price))
        print("           Guideline Net Price: {:.0f}".format(self.guideline_net_price))
        print("           Initial guideline base: {:.2f}".format(self.initial_guideline_base))
        print("           Effective program percentage: {:.2f}".format(self.effective_program_percent))
        print("           Intermediary guideline at customer size: {:.2f}".format(self.intermediary_guideline_at_customer_size))
        print("           Corrected Final Guideline Base: {:.2f}".format(self.corrected_final_guideline_base))
        print("           Corrected Base with post program adjusters: {:.2f}".format(self.corrected_base_with_postProg_adjusters))
        print("           Final guideline: {:.2f}".format(self.final_guideline))
    

    def printOutAjusters(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("ADJUSTERS: ")
        print("           Customer relationship size adjuster F: {:.2f}".format(self.adjuster_customer_relationship_F))
        print("           Customer relationship size adjuster J: {:.2f}".format(self.adjuster_customer_relationship_J))
        print("           Adjuster Model: {:.2f}".format(self.adjuster_model))
        print("           Adjuster Cab type: {:.2f}".format(self.adjuster_cab_type))
        print("           Adjuster Chassis type: {:.2f}".format(self.adjuster_chassis_type))
        print("           Adjuster Engine: {:.2f}".format(self.adjuster_engine))
        print("           Adjuster Identifier: {:.2f}".format(self.adjuster_identifier))
        print("           Intial guideline base: {:.2f}".format(self.initial_guideline_base))


    def printOutIntermediary(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("INTERMEDIARY GUIDELINE RESULTS:")
        print("           Customer size intercept: {:.2f}".format(self.customer_size_intercept))
        print("           Customer size intercept plus ten: {:.2f}".format(self.customer_size_intercept_plus_10))
        print("           Intercept if program and intercept do not cross: {:.2f}".format(self.intercept_if_program_intercept_donotacross))
        print("           Guideline Base at intermediary end: {:.2f}".format(self.guideline_base_at_intermediary_end))
        print("           Intermediary slope: {:.2f}".format(self.intermediary_slope))
        print("           Original Guideline Base at customer size: {:.2f}".format(self.original_guideline_base_at_customer_size))
        print("           Intermediary guideline at customer size: {:.2f}".format(self.intermediary_guideline_at_customer_size))


    def printOutEffectiveProgram(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("EFFECTIVE PROGRAM DISCOUNT RESULTS: ")
        print("           TC or TB:{}".format(self.TC_indicator))
        print("           Base program type selection: {}".format(self.base_program_type_selection))
        print("           Base program discount: {:.2f}".format(self.base_program_discount))
        print("           2K STOCK bonus: {}".format(self.Stock_Bonus_Eligibility))
        print("           2000 List Surcharge: {:.2f}".format(self.twoK_listSurcharge))
        print("           1000 List Surcharge: {:.2f}".format(self.oneK_listSurcharge))
        print("           Dealer Bonus Offered? : {}".format(self.dealer_bonus_offered))
        print("           Dealer Stock Bonus: {:.2f}".format(self.dealer_stock_bonus_amount))
        print("           List Minimum net price impact: {}".format(self.list_min_net_price_impact))
        print("           Total Net Impact: {:.2f}".format(self.total_net_impact))
        print("           DNET(Dealer Net): {:.2f}".format(self.DNET))
        print("           Base CAR Net Price: {:.2f}".format(self.base_CAR_net_price))
        print("           Net Price After Adjusters: {:.2f}".format(self.net_price_after_adjusters))
        print("           Effective Program Percent: {:.2f}".format(self.effective_program_percent))


    def printOutCorrectedGuideline(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("CORRECTED FINAL GUIDELINE BASE: ")
        print("           Final intermediate end at size: {:.2f}".format(self.final_intermediate_end_at_size))
        print("           Guideline allowed below program? : {}".format(self.guideline_allowed_below_program))
        print("           Final Guideline Base if Model ID has TC program or a TB program above guideline intercept")
        print("           Guideline_allowed_below_program_below3: {:.2f}".format(self.guideline_allowed_below_program_below3))
        print("           Guideline_allowed_below_program_between3and50: {:.2f}".format(self.guideline_allowed_below_program_between3and50))
        print("           Guideline_allowed_below_program_above50: {:.2f}".format(self.guideline_allowed_below_program_above50))
        print("           Final Guideline Base if model ID only has TB and guideline is above: {:.2f}".format(self.final_guideline_base))
        print("           Corrected final guideline base: {:.2f}".format(self.corrected_final_guideline_base))

    def check_stock_bonus_eligibility(self, df_stock_bonus):
        # decide which quarter the pricing period is in
        # KW - pricing period format: 1/1/2019   M/D/Y
        # Q1: 1/1/ 3/31/	
        # Q2: 4/1/ - 6/30/
        # Q3: 7/1/ - 9/30/
        # Q4: 10/1/- 12/31/
        
        month = self.requested_end_date[0]  
        year = self.requested_end_date[-4:]
        if month in ["1", "2", "3"]:
            column_name = "Q1_" + year
        elif month in ["4", "5", "6"]:
            column_name = "Q2" + year
        elif month in ["7", "8", "9"]:
            column_name = "Q3" + year
        elif month in ["10", "11", "12"]:
            column_name = "Q4" + year
        
        if column_name not in list(df_stock_bonus.columns):
            return "012"
        if self.dealer_cd not in list(df_stock_bonus["DEALER_CODE"]):
            return "011"
        eligibility = list(df_stock_bonus[df_stock_bonus["DEALER_CODE"]==self.dealer_cd][column_name])[0]
        if eligibility.upper() == "YES":
            self.Stock_Bonus_Eligibility = True
        else:
            self.Stock_Bonus_Eligibility = False
        return "ok"
         
            

    def cal_guideline(self, **kwargs):    
        enginebrandDict = {"PACCAR MX-13": "PACCAR",
                            "PACCAR MX-11" : "PACCAR",
                            "PACCAR PX-9" : "Cummins",
                            "PACCAR PX-7" : "Cummins",
                            "Cummins X15" : "Cummins",
                            "Cummins ISX12" : "Cummins",
                            "Cummins ISL" : "Cummins",
                            "Cummins ISXN" : "Cummins",
                            }
        if any(i in self.engine for i in ["PX-9", "PX-7"]):
            self.engine_brand = "Cummins" 
        if "ISX12N" in self.engine:
            self.engine = "Cummins ISXN"
        if self.Stock_Bonus_Eligibility == False:
            errorCd = self.check_stock_bonus_eligibility(self.tableDict["KW_STOCK_BONUS"])
            if errorCd != "ok":
                return {errorCd: ""}
        self.lookUp_customerRelationshipSize(self.tableDict["KW_CUSTOMER_SIZE"])        
        res = self.lookUp_adjusters(self.tableDict["KW_ADJUSTER"], self.tableDict["KW_BASE_TRUCK_VALUE"])
        if type(res) in [str, dict]:
            return res
        self.cal_initial_guideline_base()
        self.cal_effective_program(self.tableDict["KW_STOCK_CONTROL"],self.tableDict["KW_DNET"])
        self.cal_itermdediary_guideline_at_customer_size()
        self.cal_corrected_final_guideline_base()
        self.cal_discretion()        
        if self.DEBUG_MODE:
            self.printOutSummary()
            self.printOutAjusters()
            self.printOutEffectiveProgram()
            self.printOutIntermediary()
            self.printOutCorrectedGuideline() 
            print("engine brand:", self.engine_brand)       
        return self.final_guideline
