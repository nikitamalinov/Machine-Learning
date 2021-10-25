Performed data cleaning through Python Pandas using the Quandl API to get 
relevant features to implement in our neural network to predict the price of Bitcoin.

The main.py function of this program requests data from the Quandl API and creates
a CSV file to store them in after changing the columns names for organization purposes.
The data_collection.py source then gets the 5 day rolling average for our data and
creates our random, traind and test data to use for our matlab linear regression
model.
