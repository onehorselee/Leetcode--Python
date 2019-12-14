from CARS_inputs import CARS_inputs
from CARS_calculator import CARS_calculator
from cacheSFTables import cacheSFTables
from CARS_calculator_KW import CARS_calculator_KW

# The test cases are created per KW request for customer relationship size


def createTests_KW(tableDict):
    ## test1 - fixed
    CAR1 = CARS_inputs(tableDict)
    CAR1.division = "K"                    
    CAR1.CAR_num = "1475447"               
    CAR1.pricing_period = "1/1/2019"       
    CAR1.model_identifier = "T880 NS"  
    CAR1.model = "T880"
    CAR1.cab_type = "DAY CAB"    
    CAR1.list_price = 228371
    CAR1.deal_size_min = 10                 
    CAR1.customer_name = "USLBM"
    CAR1.annual_customer_vol = 30
    CAR1.conquest = "no"                  
    CAR1.chassis_type = "TRACTOR"
    CAR1.engine = "PACCAR MX-13"          
    CAR1.country = "US"
    CAR1.Stock_Bonus_Eligibility = True   
    CAR1.proposed_guideline =   36.1

    ## test 2 - fixed
    CAR2 = CARS_inputs(tableDict)
    CAR2.division = "K"                    
    CAR2.CAR_num = "1475054"               
    CAR2.pricing_period = "1/1/2019"       
    CAR2.model_identifier = "T680 SLPR"  
    CAR2.model = "T680"
    CAR2.cab_type = "SLEEPER"    
    CAR2.list_price = 229108
    CAR2.deal_size_min = 5                 
    CAR2.customer_name = "Southern Illinois Motor Xpress"
    CAR2.annual_customer_vol = 11
    CAR2.conquest = "no"                  
    CAR2.chassis_type = "TRACTOR"
    CAR2.engine = "Cummins X15"          
    CAR2.country = "US"
    CAR2.Stock_Bonus_Eligibility = True  
    CAR2.proposed_guideline = 34.78

    ## test 3 - fixed
    CAR3 = CARS_inputs(tableDict)
    CAR3.division = "K"                    
    CAR3.CAR_num = "1475187"               
    CAR3.pricing_period = "1/1/2019"       
    CAR3.model_identifier = "T880 NS"  
    CAR3.model = "T880"
    CAR3.cab_type = "Day Cab"    
    CAR3.list_price = 298262
    CAR3.deal_size_min = 4                 
    CAR3.customer_name = "C.S. McCrossan"
    CAR3.annual_customer_vol = 20
    CAR3.conquest = "no"                  
    CAR3.chassis_type = "TRACTOR"
    CAR3.engine = "PACCAR MX-11"          
    CAR3.country = "US"
    CAR3.Stock_Bonus_Eligibility = True  
    CAR3.proposed_guideline = 39.11

    ## test 4 - fixed
    CAR4 = CARS_inputs(tableDict)
    CAR4.division = "K"                    
    CAR4.CAR_num = "1475146"               
    CAR4.pricing_period = "1/1/2019"       
    CAR4.model_identifier = "W900 SLPR"  
    CAR4.model = "W900"
    CAR4.cab_type = "SLEEPER"    
    CAR4.list_price = 307673
    CAR4.deal_size_min = 1                 
    CAR4.customer_name = "EBD Enterprises Inc"
    CAR4.annual_customer_vol = 2
    CAR4.conquest = "no"                  
    CAR4.chassis_type = "TRACTOR"
    CAR4.engine = "Cummins X15"          
    CAR4.country = "CA"
    CAR4.Stock_Bonus_Eligibility = True  
    CAR4.proposed_guideline = 35.89

   
    ## test 5 - 
    CAR5 = CARS_inputs(tableDict)
    CAR5.division = "K"                    
    CAR5.CAR_num = "1474856"               
    CAR5.pricing_period = "1/1/2019"       
    CAR5.model_identifier = "W900 NS"  
    CAR5.model = "W900"
    CAR5.cab_type = "DAY CAB"    
    CAR5.list_price = 260680
    CAR5.deal_size_min = 1                 
    CAR5.customer_name = "OX BODIES INC"
    CAR5.annual_customer_vol = 219
    CAR5.conquest = "no"                  
    CAR5.chassis_type = "TRACTOR"
    CAR5.engine = "Cummins X15"          
    CAR5.country = "CA"
    CAR5.Stock_Bonus_Eligibility = True
    CAR5.proposed_guideline = 38.28


    
    ## test 6 - fixed
    CAR6 = CARS_inputs(tableDict)
    CAR6.division = "K"                    
    CAR6.CAR_num = "1473513"               
    CAR6.pricing_period = "1/1/2019"       
    CAR6.model_identifier = "T880 NS"  
    CAR6.model = "T880"
    CAR6.cab_type = "DAY CAB"    
    CAR6.list_price = 285630
    CAR6.deal_size_min = 10                 
    CAR6.customer_name = "Lane Trucking"
    CAR6.annual_customer_vol = 100
    CAR6.conquest = "no"                  
    CAR6.chassis_type = "TRACTOR"
    CAR6.engine = "CUMMINS X15"          
    CAR6.country = "US"
    CAR6.Stock_Bonus_Eligibility = True
    CAR6.proposed_guideline = 38.1


    CAR7 = CARS_inputs(tableDict)
    CAR7.division = "K"                    
    CAR7.CAR_num = "1473513"               
    CAR7.pricing_period = "1/1/2019"       
    CAR7.model_identifier = "T680 NS"  
    CAR7.model = "T680"
    CAR7.cab_type = "DAY CAB"    
    CAR7.list_price = 203790
    CAR7.deal_size_min = 2                 
    CAR7.customer_name = "Lane Trucking"
    CAR7.annual_customer_vol = 1
    CAR7.conquest = "no"                  
    CAR7.chassis_type = "TRACTOR"
    CAR7.engine = "PACCAR MX-13"          
    CAR7.country = "US"
    CAR7.Stock_Bonus_Eligibility = True
    CAR7.proposed_guideline = 35.6
  
    #return (CAR1, CAR2, CAR3, CAR4, CAR5, CAR6)
    return [CAR3]





if __name__ == "__main__":
    cache = cacheSFTables()
    tableDict = cache.getTablesFromCache()
    calculator = CARS_calculator(tableDict = tableDict)
    # test cases
    testCases = createTests_KW(tableDict)
    for test in testCases:
        calculator.CARConfig.readInputs(test)
        calculatorKW = CARS_calculator_KW()
        calculatorKW.readInputs(calculator.CARConfig)
        res = calculatorKW.cal_guideline()
        calculatorFinal = calculatorKW
        calculator.responseDict["Calculated_Dealer_Net"] = calculatorFinal.dealer_net_price
        calculator.responseDict["Requested_CAR_Guideline"] = calculatorFinal.proposed_guideline
        calculator.responseDict["Suggested_CAR_Guideline"] = calculatorFinal.final_guideline
        calculator.responseDict["Guideline_Discretion"] = calculatorFinal.guideline_disrection
        calculator.responseDict["Discretion_to_meet"] = calculatorFinal.discretion_to_meet # added
        calculator.responseDict["Price_to_increase"] = calculatorFinal.list_pricing_increase # added
        calculator.responseDict["Deal_description"] = calculator.labelDeal(calculatorFinal.guideline_disrection) # added
        calculator.responseDict["Comment_txt"] = "Guideline CAR is {:.2f}%. Requested CAR is {:.2f}%. Discretion is {:.2f}%. Price increase to hit {:.2f}% discretion is ${:.0f}. Deal Score: {}".format(calculatorFinal.final_guideline,
                                                                    calculatorFinal.proposed_guideline,
                                                                    calculatorFinal.guideline_disrection,
                                                                    calculatorFinal.discretion_to_meet,
                                                                    calculatorFinal.list_pricing_increase,
                                                                    calculator.responseDict["Deal_description"],)
        print(calculator.CARConfig.CAR_num)
        print(calculator.responseDict["Comment_txt"], "\n")