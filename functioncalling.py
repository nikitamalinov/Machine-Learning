import pandas as pd


dates = pd.read_csv("C:\\Users\\nikit\\PycharmProjects\\MFC Summer Crypto\TimeSheet.csv")
dates.rename(columns())
dates = dates['matching_date']
print(dates)


data_collection = data_collection.drop(data_collection.index[0:1145])

data_collection = data_collection.drop(columns="wallet_transaction_volume")

varlist = ['Volume', 'wallet_num_transaction']
for var in varlist:
    data_collection['1_for_log_' + str(var)] = data_collection[str(var)].shift(1)
    data_collection['1_back_log_', + str(var)] = data_collection[str(var)].shift(-1)
    data_collection.loc[data_collection[str(var)] ==0, str(var)] = (data_collection['1_for_log_' + str(var)] + data_collection['1_back_log_' + str(var)])/2
    data_collection = data_collection.drop(['1_back_log_' + str(var), '1_for_log_' + str(var)], axis=1)


