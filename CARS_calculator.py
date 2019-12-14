"""
Created on Mon Aug 12 09:25:50 2019
@author: A-Qian.Li
"""
from CARS_inputs import CARS_inputs
from CARS_calculator_KW import CARS_calculator_KW
from CARS_calculator_PB import CARS_calculator_PB
from errorDict import errorDict
import traceback
import time
import sys, os
import logging

class CARS_calculator:
    def __init__(self, tableDict):
        self.responseDict = {"hasError": False,
                             "hasAlert": False, 
                             "errorCode": "000",
                             "alertCode": "000",
                             "errorMsg":"Everything is fine.",  
                             "alertMsg": "Everything is fine.",                          
                             "Calculated_Dealer_Net": .0, 
                             "Requested_CAR_Guideline": .0,
                             "Suggested_CAR_Guideline": .0,
                             "Guideline_Discretion": .0,
                             "Discretion_to_meet": .0,
                             "Price_to_increase": .0,
                             "Deal_description": " ",
                             "Comment_txt": " ",
                            }
        self.CAR_guideline = float()
        self.CARConfig = CARS_inputs(tableDict)

    def updateError(self, errorCode):
        self.responseDict["hasError"] = True if errorCode not in ["000", "003", "005"] else False        
        self.responseDict["errorCode"] = errorCode
        self.responseDict["errorMsg"] = errorDict[errorCode]
    
    def updateAlert(self, alertCode):
        self.responseDict["hasAlert"] = True if alertCode in ["003", "005"] else False
        self.responseDict["alertCode"] = alertCode
        self.responseDict["alertMsg"] = errorDict[alertCode]

    def labelDeal(self, discretion):
        '''
        Discretion ranking for Peterbilt should be:
         <=1% - good, 
         <=2% - ok, 
         <=3% - watch out,
         <=4% - bad, 
         >4% - very bad 
        '''
        if self.CARConfig.division == "P": 
            if discretion <= 1.00:
                return "Good"
            elif discretion <= 2.00 and discretion > 1.00: 
                return "Ok"
            elif discretion <= 3.00 and discretion > 2.00: 
                return "Watch Out"
            elif discretion <= 4.00 and discretion > 3.00: 
                return "Bad"
            elif discretion > 4.00:
                return "Very Bad"

        if self.CARConfig.division == "K": 
            if discretion < 0.75:
                return "Very Good"
            elif discretion < 1.50 and discretion >= 0.75:
                return "Good"
            elif discretion < 2.25 and discretion >= 1.50: 
                return "Ok"
            elif discretion < 3.00 and discretion >= 2.25: 
                return "Watch Out"
            elif discretion < 3.75 and discretion >= 3.00: 
                return "Bad"
            elif discretion >= 3.75:
                return "Very Bad"

    def CARS_calculator(self, inputDict):     
        errorCode = self.CARConfig.readInputsDict(inputDict)   
        if errorCode not in ["000", "003", "005"]: 
            self.updateError(errorCode)
            return self.responseDict        
        if self.CARConfig.division == "K":
            calculatorKW = CARS_calculator_KW()
            calculatorKW.readInputs(self.CARConfig)
            res = calculatorKW.cal_guideline()
            if type(res) == dict:
                errorCd = list(res.keys())[0]
                self.updateError(errorCd)
                self.responseDict["errorMsg"] += res[errorCd]
                return self.responseDict
            else:
                self.CAR_guideline = res
            calculatorFinal = calculatorKW
        if self.CARConfig.division == "P":
            calculatorPB = CARS_calculator_PB()
            calculatorPB.readInputs(self.CARConfig)
            res = calculatorPB.cal_guideline()
            if type(res) == str:
                self.updateError(res)
                return self.responseDict
            else:
                self.CAR_guideline = res
            calculatorFinal = calculatorPB
        # UPDATE RESPONSE DICTIONARY            
        self.responseDict["Calculated_Dealer_Net"] = calculatorFinal.dealer_net_price
        self.responseDict["Requested_CAR_Guideline"] = calculatorFinal.proposed_guideline
        self.responseDict["Suggested_CAR_Guideline"] = calculatorFinal.final_guideline
        self.responseDict["Guideline_Discretion"] = calculatorFinal.guideline_disrection
        self.responseDict["Discretion_to_meet"] = calculatorFinal.discretion_to_meet # added
        self.responseDict["Price_to_increase"] = calculatorFinal.list_pricing_increase # added
        self.responseDict["Deal_description"] = self.labelDeal(calculatorFinal.guideline_disrection) # added
        self.responseDict["Comment_txt"] = "GUIDELINE {:.2f}%. DISCRETION {:.2f}%. PRICE INCREASE {:.2f}% DISCRETION ${:.0f}. DEAL:{}".format(
                                                                    calculatorFinal.final_guideline,
                                                                    #calculatorFinal.proposed_guideline,
                                                                    calculatorFinal.guideline_disrection,
                                                                    calculatorFinal.discretion_to_meet,
                                                                    calculatorFinal.list_pricing_increase,
                                                                    self.responseDict["Deal_description"],)
    
        if True : # debug 
            self.responseDict["model"] = calculatorFinal.model
            self.responseDict["model_identifier"] = calculatorFinal.model_identifier
            self.responseDict["cab_type"] = calculatorFinal.cab_type
            self.responseDict["chassis_type"] = calculatorFinal.chassis_type
            self.responseDict["pricing_period"] = calculatorFinal.pricing_period
            self.responseDict["division"] = calculatorFinal.division
            self.responseDict["country"] = calculatorFinal.country
            self.responseDict["region"] = calculatorFinal.region
            self.responseDict["engine"] = calculatorFinal.engine
            self.responseDict["stock_bonus_eligibility"] = calculatorFinal.Stock_Bonus_Eligibility

        if abs(calculatorFinal.ReceivedDealerNet - calculatorFinal.dealer_net_price) > 5.0:
            self.updateAlert("005") 
        if calculatorFinal.customer_alert:
            self.updateAlert("003")
        return self.responseDict


if __name__ == "__main__":
    start = time.time()
    #CARS_calculator()
    end = time.time()
    print("TOTAL RUNNING TIME(s): {:.2f}".format(end-start))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  