import json 
import pandas as pd 
from pandas.io.json import json_normalize
  
path = 'staticFiles/'

def Decode_CCSalesOptionCd(CCSalesOptionCd, DivisionCode, MarketModel):
    '''FUNCTION: decode CCSalesOptionCd code into model_identifier'''    
    fileDict = {"K": path + 'MarketModelDTK_dictionary.xlsx',
                "P": path + 'MarketModelDTP_dictionary.xlsx'}
    division = DivisionCode.upper()
    if division == "P":
        df = pd.read_excel(fileDict[division], converters={"ccm_option_cd": str, "ccm_model_cd": str, "MarketModel": str, "ops_model_cd":str}).fillna("NA")  
        if CCSalesOptionCd not in list(df["ccm_option_cd"]):
            return "006A"  
        model_identifier = list(df[df["ccm_option_cd"]==CCSalesOptionCd][df["MarketModel"]==MarketModel]["ccm_model_cd"])[0]
        model, cab_type = MarketModel, "DAY CAB" if "D" in model_identifier else "SLEEPER"

    if division == "K":
        division = "K"
        df = pd.read_excel(fileDict[division], converters={"ccm_option_cd": str, "Cab_type": str, "MarketModel": str,}).fillna("NA")    
        if CCSalesOptionCd not in list(df["ccm_option_cd"]):
            return "006A"        
        df = df[df["ccm_option_cd"]==CCSalesOptionCd][df["MarketModel"]==MarketModel]
        model_identifier = list(df["Model_identifier"])[0]
        model = list(df["Model"])[0]
        cab_type = list(df["Cab_type"])[0].upper()
        if model == "NA" or model_identifier == "NA" or cab_type =="NA":
            return "006B"
        cab_type = "DAY CAB" if "DAY" in cab_type else "SLEEPER"    
    return (model_identifier, model, cab_type)




def Decode_DealerCd_toCountry(DealerCd, DivisionCode):
    ''' FUNCTION: decode dealerCd code into country'''
    fileDict = {"K": path + 'DLR_KW.xlsx',
                "P": path + 'DLR_PB.xlsx'}
    df = pd.read_excel(fileDict[DivisionCode.upper()])
    if DealerCd not in list(df["DLR_NO"]):
        return "004"
    country = list(df[df["DLR_NO"] == DealerCd]["PL_ENTT_NAME"])[0]
    if country == "CANADA":
        return "CA"
    elif country == "UNITED STATES":
        return "US"


        
if __name__ == "__main__":
    optinocdList = ["0090076","9409001"]
    modelIdentifier = Decode_CCSalesOptionCd(CCSalesOptionCd = "9409001", DivisionCode = "P", MarketModel = "367") # should return "367-DM"
    #modelIdentifier = Decode_CCSalesOptionCd("9409001", "K") 
    print(modelIdentifier)  
