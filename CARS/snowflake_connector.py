#!/usr/bin/env python
import snowflake.connector
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
import pandas as pd
import time

def snowflake_connector(tableLists):
    url = URL(
            account = 'PACCAR',
            user = 'n-ITD_03968_PRICING_TEST_SVC',
            password = 'TEST@PACCARme1VYGVmrN',
            database = 'ITD_TEXT_TEST_RAW_DB',
            schema = 'BCG',
            warehouse = 'ITD_REN_03_968_XSMALL_WH',
            role='ITD_03968_PRICING_TEST_RW'
        )
    engine = create_engine(url)
    connection = engine.connect()
    tableDict = {}
    for tablename in tableLists:
        query = ''' select * from {};'''.format(tablename)
        df = pd.read_sql(query, connection)
        df.columns = map(str.upper, df.columns)
        tableDict[tablename] = df
    connection.close()
    engine.dispose()
    return tableDict


if __name__ == "__main__":
    start = time.time()
    tableDict = snowflake_connector(["KW_STOCK_BONUS"])
    for tablename in tableDict:
        print("{} : , row : {}， col: {}".format(tablename, tableDict[tablename].shape[0], tableDict[tablename].shape[1]))
        print(tableDict[tablename].head(5))
        print(list(tableDict[tablename].columns))
    end = time.time()
    print("SNOWFALKE CONNECTION TIME(s): {:.2f}".format(end-start))
