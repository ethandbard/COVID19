import pandas as pd
import itertools
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import warnings
from datetime import datetime
plt.style.use('fivethirtyeight')

data = pd.read_csv("Sales.csv")

datesHolder = data["Date"]
sales = []
dates = []
for item in datesHolder:
    dates.append(item)

#convert sales from string to int
for item in data["Sales"]:
    number = item.replace(",","")
    sales.append(int(float(number)))

# #Data Preprocessing
# #Create modified dataframe
df = pd.DataFrame(sales, index = dates)

# print(df.head())

# df.plot(figsize=(15,6))
# plt.title("Store 3052")
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.show()

#ARIMA Time Series Model
# #Define p, d, and q to be between 0 and 2
# p = d = q = range(0,2)

# #Generate all different combinations of p,  d, and q triplets
# pdq = list(itertools.product(p, d, q))

# # #generate all different combinations of seasonal p, d, and q triplets
# seasonal_pdq = [(x[0], x[1], x[2], 52) for x in list(itertools.product(p, d, q))]

# warnings.filterwarnings("ignore") # specify to ignore warning messages
# for param in pdq:
#     for param_seasonal in seasonal_pdq:
#         try:
#             mod = sm.tsa.statespace.SARIMAX(df,
#                                             order=param,
#                                             seasonal_order=param_seasonal,
#                                             enforce_stationarity=False,
#                                             enforce_invertibility=False)

#             results = mod.fit()

#             with open('3052.txt', 'a') as the_file:
#                 the_file.write(('ARIMA{}x{} - AIC:{}\n'.format(param, param_seasonal, results.aic)))
#         except:
#             continue

# Note model structure with lowest AIC below:
############################################################
# ARIMA(0, 1, 1)x(1, 0, 1, 52) - AIC:437.9370101216383   ##
############################################################

#Comment lines 46 - 61 before running code again

#Fit model below: 
# mod = sm.tsa.statespace.SARIMAX(df,
#                                 order = (1,1,1),
#                                 seasonal_order = (0,0,0,52),
#                                 enforce_stationarity=False,
#                                 enforce_invertibility=False)

# results = mod.fit()

# results.plot_diagnostics(figsize=(15,12))
# plt.show()

# pred = results.get_prediction(start=pd.to_datetime('2019-5-26'), dynamic=False)
# pred_ci = pred.conf_int()

# #Display predictions and confidence interval
# print(pred.predicted_mean)
# print(pred_ci)

# #Plot predictions
# pred.predicted_mean.plot(label = 'Forecast', figsize=(15,6))
# plt.title("Store 3052 Forecast")
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()

# #Plot Observed values in same range for comparison
# observed = df["2019-05-26":]
# observed.plot(label = 'Observed', figsize = (15,6))
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()

#TODO: Write sales forecast + confidence interval together in text file
#TODO: Plot observed values and predicted values on same graph. I couldn't get it to work correctly.
#TODO: Algorithm that considers forecast/last years sales, and reports how much extra sales need to be made to meet desired increase

