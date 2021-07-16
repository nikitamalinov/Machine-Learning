import quandl
import pandas as pd
import random


data_collection = pd.read_csv("C:\\Users\\nikit\\PycharmProjects\\MFC Summer Crypto\\DataCollection.csv")

data_collection['MA5_Bitcoin_my_wallet_num_users'] = data_collection['Bitcoin_my_wallet_num_users'].rolling(5).mean()
data_collection['MA5_Volume'] = data_collection['Volume'].rolling(5).mean()
data_collection['MA5_Difficulty'] = data_collection['Difficulty'].rolling(5).mean()
data_collection['MA5_wallet_num_transaction'] = data_collection['wallet_num_transaction'].rolling(5).mean()
data_collection['MA5_wallet_transaction_volume'] = data_collection['wallet_transaction_volume'].rolling(5).mean()
data_collection['MA5_Bitcoin_Avg_Block_Size'] = data_collection['Bitcoin_Avg_Block_Size'].rolling(5).mean()
data_collection['MA5_Miners_Revenue'] = data_collection['Miners_Revenue'].rolling(5).mean()
data_collection['MA5_Hash_Rate'] = data_collection['Hash_Rate'].rolling(5).mean()
data_collection['MA5_Bitcoin_Cost_Transaction'] = data_collection['Bitcoin_Cost_Transaction'].rolling(5).mean()
data_collection['MA5_Bitcoin_Cost_percentage_of_Transaction_Volume'] = data_collection['Bitcoin_Cost_percentage_of_Transaction_Volume'].rolling(5).mean()
data_collection['MA5_Estimated_Transaction_Volume'] = data_collection['Estimated_Transaction_Volume'].rolling(5).mean()
data_collection['MA5_Total_Output_Volume'] = data_collection['Total_Output_Volume'].rolling(5).mean()
data_collection['MA5_num_transaction_per_Block'] = data_collection['num_transaction_per_Block'].rolling(5).mean()
data_collection['MA5_num_of_unique_addresses'] = data_collection['num_of_unique_addresses'].rolling(5).mean()
data_collection['MA5_num_of_transaction'] = data_collection['num_of_transaction'].rolling(5).mean()
data_collection['MA5_Total_transaction_fees'] = data_collection['Total_transaction_fees'].rolling(5).mean()
data_collection['MA5_Total_Bitcoins'] = data_collection['Total_Bitcoins'].rolling(5).mean()
data_collection['MA5_Median_transaction_confirmation_time'] = data_collection['Median_transaction_confirmation_time'].rolling(5).mean()

data_collection = data_collection.drop(data_collection.index[0:1145])

data_collection = data_collection.drop(columns="wallet_transaction_volume")

varlist = ['Volume', 'wallet_num_transaction']
for var in varlist:
    data_collection['1_for_log_' + str(var)] = data_collection[str(var)].shift(1)
    data_collection['1_back_log_' + str(var)] = data_collection[str(var)].shift(-1)
    data_collection.loc[data_collection[str(var)] ==0, str(var)] = (data_collection['1_for_log_' + str(var)] + data_collection['1_back_log_' + str(var)])/2
    data_collection = data_collection.drop(['1_back_log_' + str(var), '1_for_log_' + str(var)], axis=1)


btc_price = quandl.get('BCHAIN/MKPRU')
btc_price['Date'] = btc_price.index
#btc_price.index.names = ['Index']
btc_price['Date'] = pd.to_datetime(btc_price["Date"]).dt.strftime('%Y-%m-%d')


date_vec8 = []
for i in data_collection['Date']:
    for j in btc_price['Date']:
        if i == j:
            date_vec8.append(i)

price_table = pd.DataFrame()
price_table['Bitcoin_Price'] = btc_price.loc[date_vec8, 'Value']


price_table['Growth'] = (price_table['Bitcoin_Price'].shift(-1) - price_table['Bitcoin_Price'])/price_table['Bitcoin_Price']

class_vec = []


for i in price_table['Growth']:
    if i >= 0.1:
        class_vec.append(1)
    elif i <= 0:
        class_vec.append(3)
    else:
        class_vec.append(2)

data_collection['Class'] = class_vec

data_collection = data_collection.iloc[:, 18:]
data_collection.to_csv(r'C:\Users\nikit\Downloads\data\DataCollection.csv')

random_index = random.sample(range(0, len(price_table)), len(price_table))
random_data = pd.DataFrame()
random_data = data_collection.iloc[random_index, :]
random_data.to_csv(r'C:\Users\nikit\Downloads\data\random_data.csv')

train_data = pd.DataFrame()
train_data = random_data.iloc[0:2088, :]
train_data.to_csv(r'C:\Users\nikit\Downloads\data\train_data.csv')

test_data = pd.DataFrame()
test_data = random_data.iloc[2088:2535, :]
test_data.to_csv(r'C:\Users\nikit\Downloads\data\test_data.csv')

cv_data = pd.DataFrame()
cv_data = random_data.iloc[2535:, :]
cv_data.to_csv(r'C:\Users\nikit\Downloads\data\cv_data.csv')
