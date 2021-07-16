import quandl
import pandas as pd


quandl.ApiConfig.api_key = 'xjSsWdgge_f_GeHy-BV_'

Bitcoin_my_wallet_num_users = quandl.get("BCHAIN/MWNUS")
Bitcoin_my_wallet_num_users = Bitcoin_my_wallet_num_users.fillna(method = 'ffill')
Bitcoin_my_wallet_num_users.isnull().sum()
Bitcoin_my_wallet_num_users['Date'] = Bitcoin_my_wallet_num_users.index
Bitcoin_my_wallet_num_users['MA_5'] = Bitcoin_my_wallet_num_users['Value'].rolling(5).mean()
Bitcoin_my_wallet_num_users = Bitcoin_my_wallet_num_users.dropna()


exchange_vol = quandl.get("BCHAIN/TRVOU")
exchange_vol =exchange_vol.fillna(method = 'ffill')
exchange_vol.isnull().sum()
exchange_vol['Date'] = exchange_vol.index
exchange_vol['MA_5'] = exchange_vol['Value'].rolling(5).mean()
exchange_vol = exchange_vol.dropna()


bchain_diff = quandl.get("BCHAIN/DIFF")
bchain_diff = bchain_diff.fillna(method = 'ffill')
bchain_diff.isnull().sum()
bchain_diff['Date'] = bchain_diff.index
bchain_diff['MA_5'] = bchain_diff['Value'].rolling(5).mean()
bchain_diff = bchain_diff.dropna()


txn_vol_per_day = quandl.get("BCHAIN/MWNTD")
txn_vol_per_day = txn_vol_per_day.fillna(method = 'ffill')
txn_vol_per_day.isnull().sum()
txn_vol_per_day['Date'] = txn_vol_per_day.index
txn_vol_per_day['MA_5'] = txn_vol_per_day['Value'].rolling(5).mean()
txn_vol_per_day = txn_vol_per_day.dropna()

my_wallet_txn_vol = quandl.get("BCHAIN/MWTRV")
my_wallet_txn_vol = my_wallet_txn_vol.fillna(method = 'ffill')
my_wallet_txn_vol.isnull().sum()
my_wallet_txn_vol['Date'] = my_wallet_txn_vol.index
my_wallet_txn_vol['MA_5'] = my_wallet_txn_vol['Value'].rolling(5).mean()
my_wallet_txn_vol = my_wallet_txn_vol.dropna()

avg_block_size = quandl.get("BCHAIN/MWTRV")
avg_block_size = avg_block_size.fillna(method = 'ffill')
avg_block_size.isnull().sum()
avg_block_size['Date'] = avg_block_size.index
avg_block_size['MA_5'] = avg_block_size['Value'].rolling(5).mean()
avg_block_size = avg_block_size.dropna()

miners_rev = quandl.get("BCHAIN/MIREV")
miners_rev = miners_rev.fillna(method = 'ffill')
miners_rev.isnull().sum()
miners_rev['Date'] = miners_rev.index
miners_rev['MA_5'] = miners_rev['Value'].rolling(5).mean()
miners_rev = miners_rev.dropna()

hash_rate = quandl.get("BCHAIN/HRATE")
hash_rate = hash_rate.fillna(method = 'ffill')
hash_rate.isnull().sum()
hash_rate['Date'] = hash_rate.index
hash_rate['MA_5'] = hash_rate['Value'].rolling(5).mean()
hash_rate = hash_rate.dropna()

cost_per_txn = quandl.get("BCHAIN/CPTRA")
cost_per_txn = cost_per_txn.fillna(method = 'ffill')
cost_per_txn.isnull().sum()
cost_per_txn['Date'] = cost_per_txn.index
cost_per_txn['MA_5'] = cost_per_txn['Value'].rolling(5).mean()
cost_per_txn = cost_per_txn.dropna()

cost_perc_of_txn_flow = quandl.get("BCHAIN/CPTRV")
cost_perc_of_txn_flow = cost_perc_of_txn_flow.fillna(method = 'ffill')
cost_perc_of_txn_flow.isnull().sum()
cost_perc_of_txn_flow['Date'] = cost_perc_of_txn_flow.index
cost_perc_of_txn_flow['MA_5'] = cost_perc_of_txn_flow['Value'].rolling(5).mean()
cost_perc_of_txn_flow = cost_perc_of_txn_flow.dropna()

est_txn_vol = quandl.get("BCHAIN/ETRAV")
est_txn_vol = est_txn_vol.fillna(method = 'ffill')
est_txn_vol.isnull().sum()
est_txn_vol['Date'] = est_txn_vol.index
est_txn_vol['MA_5'] = est_txn_vol['Value'].rolling(5).mean()
est_txn_vol = est_txn_vol.dropna()

tov = quandl.get("BCHAIN/TOUTV")
tov = tov.fillna(method = 'ffill')
tov.isnull().sum()
tov['Date'] = tov.index
tov['MA_5'] = tov['Value'].rolling(5).mean()
tov = tov.dropna()


txn_per_block = quandl.get("BCHAIN/NTRBL")
txn_per_block = txn_per_block.fillna(method = 'ffill')
txn_per_block.isnull().sum()
txn_per_block['Date'] = txn_per_block.index
txn_per_block['MA_5'] = txn_per_block['Value'].rolling(5).mean()
txn_per_block = txn_per_block.dropna()

unique_addresses = quandl.get("BCHAIN/NADDU")
unique_addresses = unique_addresses.fillna(method = 'ffill')
unique_addresses.isnull().sum()
unique_addresses['Date'] = unique_addresses.index
unique_addresses['MA_5'] = unique_addresses['Value'].rolling(5).mean()
unique_addresses = unique_addresses.dropna()


num_txn = quandl.get("BCHAIN/NTRAN")
num_txn = num_txn.fillna(method = 'ffill')
num_txn.isnull().sum()
num_txn['Date'] = num_txn.index
num_txn['MA_5'] = num_txn['Value'].rolling(5).mean()
num_txn = num_txn.dropna()

tot_txn_fees = quandl.get("BCHAIN/TRFEE")
tot_txn_fees = tot_txn_fees.fillna(method = 'ffill')
tot_txn_fees.isnull().sum()
tot_txn_fees['Date'] = tot_txn_fees.index
tot_txn_fees['MA_5'] = tot_txn_fees['Value'].rolling(5).mean()
tot_txn_fees = tot_txn_fees.dropna()

tot_btc = quandl.get("BCHAIN/TOTBC")
tot_btc = tot_btc.fillna(method = 'ffill')
tot_btc.isnull().sum()
tot_btc['Date'] = tot_btc.index
tot_btc['MA_5'] = tot_btc['Value'].rolling(5).mean()
tot_btc = tot_btc.dropna()

txn_confirm_time = quandl.get("BCHAIN/ATRCT")
txn_confirm_time = txn_confirm_time.fillna(method = 'ffill')
txn_confirm_time.isnull().sum()
txn_confirm_time['Date'] = txn_confirm_time.index
txn_confirm_time['MA_5'] = txn_confirm_time['Value'].rolling(5).mean()
txn_confirm_time = txn_confirm_time.dropna()



dates = pd.read_csv("C:\\Users\\nikit\\PycharmProjects\\MFC Summer Crypto\\TimeSheet.csv")
dates = dates['matching_date']

Data_Collection = pd.DataFrame()
Data_Collection['Bitcoin_my_wallet_num_users'] = Bitcoin_my_wallet_num_users.loc[dates, 'MA_5']
Data_Collection['exchange_vol'] = exchange_vol.loc[dates, 'MA_5']
Data_Collection['bchain_diff'] = bchain_diff.loc[dates, 'MA_5']
Data_Collection['txn_vol_per_day'] = txn_vol_per_day.loc[dates, 'MA_5']
Data_Collection['my_wallet_txn_vol'] = my_wallet_txn_vol.loc[dates, 'MA_5']
Data_Collection['avg_block_size'] = avg_block_size.loc[dates, 'MA_5']
Data_Collection['miners_rev'] = miners_rev.loc[dates, 'MA_5']
Data_Collection['hash_rate'] = hash_rate.loc[dates, 'MA_5']
Data_Collection['cost_per_txn'] = cost_per_txn.loc[dates, 'MA_5']
Data_Collection['cost_perc_of_txn_flow'] = cost_perc_of_txn_flow.loc[dates, 'MA_5']
Data_Collection['est_txn_vol'] = est_txn_vol.loc[dates, 'MA_5']
Data_Collection['tov'] = tov.loc[dates, 'MA_5']
Data_Collection['txn_per_block'] = txn_per_block.loc[dates, 'MA_5']
Data_Collection['unique_addresses'] = unique_addresses.loc[dates, 'MA_5']
Data_Collection['num_txn'] = num_txn.loc[dates, 'MA_5']
Data_Collection['tot_txn_fees'] = tot_txn_fees.loc[dates, 'MA_5']
Data_Collection['tot_btc'] = tot_btc.loc[dates, 'MA_5']
Data_Collection['txn_confirm_time'] = txn_confirm_time.loc[dates, 'MA_5']

Data_collection.to_csv(["C:\\Users\\nikit\\Downloads"])

