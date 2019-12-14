"""
Created on Mon Aug 12 09:23:46 2019
@author: A-Qian.Li
"""
from Decode_STCodes import Decode_DealerCd_toCountry
from Decode_STCodes import Decode_CCSalesOptionCd
from snowflake_connector import snowflake_connector


class CARS_inputs:
    def __init__(self, tableDict):
        self.DEBUG_MODE = False
        # ATTRIBUTES FOR BOTH KW & PB
        self.division = " "                     # "P"
        self.CAR_num = "0000000"               # 7 digits string
        self.CCSalesOptionCd = "0000000"       # 7 digits
        self.pricing_period = " "               # M/D/YYYY
        self.requested_end_date = " "
        self.model_identifier = " "             # CC model (description?ID?)in Sales Tool 
        self.model = " "
        self.cab_type = " "                     # DAY CAB  
        self.list_price = 300000
        self.deal_size_min = .0                # sales tool does not have it
        self.customer_name = " "
        self.annual_customer_vol = 1
        self.customer_alert = False
        self.conquest = "no"                   # fleet/region/no, not included in CARS calculation
        self.chassis_type = " "
        self.engine = " "                       # manufacture/model/horse power
        self.engine_brand = " "
        self.country = " "
        self.Stock_Bonus_Eligibility = False   # this should be added as input value    
        self.list_discount = .0  
        self.dealer_cd = " "
        # ATTRIBUTES ONLY FOR PB
        self.CCModel = " "
        self.region = " "                       # West, Great Lakes, Midwest, Northeast,Southeast,Canada   
        self.proposed_guideline = 0.00         # default
        self.guideline_disrection = .0            
        self.setUpperCase()
        # OTHER GLOBAL ATTRIBUTES
        self.PBTablesNames = ["PB_CUSTOMER_SIZE", "PB_GUIDELINE_LOOKUP"]
        self.KWTablesNames = ["KW_CUSTOMER_SIZE", "KW_ADJUSTER", "KW_BASE_TRUCK_VALUE", "KW_STOCK_CONTROL","KW_DNET", "KW_STOCK_BONUS"]
        self.tableDict = tableDict
        self.KW_models = list(tableDict["KW_ADJUSTER"]["PROGRAM_NAME"].unique())
        self.PB_model_identifiers = list(tableDict["PB_GUIDELINE_LOOKUP"]["CC_MODEL"].unique())        
        self.PB_dates_cols = [col for col in list(tableDict["PB_GUIDELINE_LOOKUP"].columns) if "_GUIDELINE_BASE" in col]
        self.PB_pricing_dates = [x.replace("_GUIDELINE_BASE", "") for x in self.PB_dates_cols]
        dftp = tableDict["KW_ADJUSTER"]
        self.KW_pricing_dates = list(dftp[dftp["ADJUSTER_FAMILY"]=="PRICING PERIOD"]["ADJUSTER_NAME"])
        self.KW_dearlerList = list(tableDict["KW_STOCK_BONUS"]["DEALER_CODE"])
        del dftp
        # Other 
        self.guideline_disrection = .0 
        self.proposed_guideline = .0 
        self.final_guideline = .0 
        self.discretion_to_meet = .0
        self.list_pricing_increase = .0

    def setUpperCase(self):
        for attr, value in self.__dict__.items():
            if type(value) == str: 
                setattr(self, attr, value.upper())

    def reformatPricingPeriod(self, pricing_period):
        # input format: 01/01/2019
        # output format: 1/1/2019
        # only for KW

        replaceDict = { "01": "1",
                        "02": "2", 
                        "03": "3", 
                        "04": "4", 
                        "05": "5",
                        "06": "6", 
                        "07": "7", 
                        "08": "8", 
                        "09": "9", 
                        "10": "10"}

        firstPart = pricing_period[:5]
        secondPart = pricing_period[5:]

        for old in replaceDict.keys():
            firstPart = firstPart.replace(old, replaceDict[old])
        return firstPart + secondPart

    def readInputsDict(self, elementDict):
        self.division = elementDict["DivisionCode"].upper()
        if self.division not in ["K", "P"]:
            return "001"
        self.pricing_period = elementDict["PriceProtectionDt"]
        self.requested_end_date = elementDict["RequestedEndDate"]
        if (self.division == "P") and (self.pricing_period not in self.PB_pricing_dates):
            return "010"
        if self.division == "K":
            self.pricing_period = self.reformatPricingPeriod(self.pricing_period)
            self.requested_end_date = self.reformatPricingPeriod(self.requested_end_date)
            if (self.pricing_period not in self.KW_pricing_dates):
                return "010"     
        self.model = elementDict["MarketModel"]
        self.list_price = float(elementDict["DealerList"])
        self.ReceivedDealerNet = float(elementDict["DealerNet"])
        self.deal_size_min = float(elementDict["MinQuantity"])      
        self.engine =  elementDict["Engine"]            
        self.engine_brand = elementDict["EngineBrand"]
        self.proposed_guideline = float(elementDict["RequestedCARPercent"])               
        self.customer_name = elementDict["CustomerName"]
        #  DECODE UNIT TYPE CODE INTO CHASSIS TYPE: 1-tractor, 2-truck, 3-glider
        UnitTypeCd = int(elementDict["UnitTypeCd"])
        if UnitTypeCd == 1:
            self.chassis_type = "TRACTOR"
        elif UnitTypeCd == 2: 
            self.chassis_type = "TRUCK"
        else: 
            return "002"        
        # DECODE DEALER CODE INTO COUNTRY 
        self.dealer_cd = elementDict["DealerCd"]
        if self.division =="K" and self.dealer_cd not in self.KW_dearlerList:
            return "011"
        self.country = Decode_DealerCd_toCountry(elementDict["DealerCd"], elementDict["DivisionCode"])
        if self.country not in ["CA", "US"]:
            return self.country
        else:
            self.region = self.country 
        
        # DECODE CC OPPTION CODE INTO MODEL IDENTIFIER AND CAB_TYPE
        decodedRes = Decode_CCSalesOptionCd(CCSalesOptionCd = elementDict["CCSalesOptionCd"], 
                                            DivisionCode = elementDict["DivisionCode"],
                                            MarketModel = elementDict["MarketModel"])
        if type(decodedRes) == str:
            return decodedRes
        (self.model_identifier, self.model, self.cab_type) = decodedRes
        if (self.division == "K") and (self.model not in self.KW_models):
            return "007"
        if (self.division == "P") and (self.model_identifier not in self.PB_model_identifiers):
            return "008"  
        self.setUpperCase()
        return  "000"


    def readInputs(self, UserInputs):  
        for attr, value in UserInputs.__dict__.items():
            setattr(self, attr, value)
        self.setUpperCase()    
        self.engine_brand = "PACCAR" if "PACCAR" in self.engine else "CUMMINS"
        if False:    # THIS PART WILL BE ONLY RUN WHEN TESTING          
            if self.division == "P" and self.CCModel != " " and "-" in self.CCModel:    
                self.model_identifier = "{}{}".format(self.model, self.CCModel)
            elif self.division == "P" and self.CCModel != " " and "-" not in self.CCModel:
                self.model_identifier = "{}-{}".format(self.model, self.CCModel)
            elif self.division == "P" and self.CCModel == " "  and self.model != " ":
                self.model_identifier = self.model
            

    def printOutAttrs(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("INPUT ATTRIBUTES:")
        for attr, value in self.__dict__.items():
            if self.division == "K" and attr in ["CCModel", "trim", "region", "list discount"]:
                continue
            print("           {}: {}".format(attr.replace("_", " ").upper(), value))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        

    def getTables(self, tablelists):  
        '''INPUT: A LIST OF TABLE NAMES,
           OUTPUTS: A DICTIONARY OF DATAFRAMES,
           OBJECT: CONNECT TO SNOWFALKE AND RETRIEVE TABLES'''   
        tableDicts = snowflake_connector(tablelists)
        return tableDicts

    def lookUp_customerRelationshipSize(self, df_cus):
        '''LOOK FOR THE AVERAGE PURCHASE VOLUME OF A CUSTOMER'''        
        df_cus["CUSTOMER_NAME"] = df_cus["CUSTOMER_NAME"].map(lambda x: x.upper())
        customerList = df_cus["CUSTOMER_NAME"].tolist()
        self.customer_name = self.customer_name.upper()
        if(self.customer_name == "OTHER/NEW") or (self.customer_name not in customerList):
            # EXPECTED ANNUAL PURCHASE VOLUME -- DEALER SHOULD MANNUALLY INPUT THIS VALUE
            self.customer_relationship = 1 
            self.customer_alert = True            
        else:
            self.customer_relationship = list(df_cus[df_cus["CUSTOMER_NAME"]==self.customer_name]["CUSTOMER_SIZE"])[0]   
    
    def cal_discretion(self):
        self.guideline_disrection = self.proposed_guideline - self.final_guideline
        if self.guideline_disrection <= 0:
            return
        if self.division=="K":
            if (self.guideline_disrection > 0) and (self.guideline_disrection < 0.75):
                self.discretion_to_meet = .0
            elif (self.guideline_disrection >= .75) and (self.guideline_disrection < 1.5):
                self.discretion_to_meet = .75
            elif (self.guideline_disrection >= 1.5) and (self.guideline_disrection < 2.25):
                self.discretion_to_meet = 1.5
            elif (self.guideline_disrection >= 2.25) and (self.guideline_disrection < 3): 
                self.discretion_to_meet = 2.25
            elif (self.guideline_disrection >= 3) and (self.guideline_disrection < 3.75): 
                self.discretion_to_meet = 3
            elif self.guideline_disrection >= 3.75:
                self.discretion_to_meet = 3.75
        if self.division=="P":
            if (self.guideline_disrection > 0) and (self.guideline_disrection <=1.00):
                self.discretion_to_meet = .0
            elif (self.guideline_disrection >1.00) and (self.guideline_disrection <=2.00):
                self.discretion_to_meet = 1.00
            elif (self.guideline_disrection >2.00) and (self.guideline_disrection <=3.00):
                self.discretion_to_meet = 2.00
            elif (self.guideline_disrection >3.00) and (self.guideline_disrection <=4.00): 
                self.discretion_to_meet = 3.00
            elif (self.guideline_disrection > 4): 
                self.discretion_to_meet = 4.00


        self.list_pricing_increase = (self.guideline_disrection - self.discretion_to_meet) * self.dealer_net_price * 0.01
        return 

        
    def check_NoneType(self, num):    	
        #CHECK IF num IS NoneType
        if num == num:
            return num
        return .0 