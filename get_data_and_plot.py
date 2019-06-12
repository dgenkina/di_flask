# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:58:08 2019

@author: dng5
"""

import pandas as pd
from bokeh.plotting import figure, output_file, show


ticker_name = 'ZUMZ' #input('Ticker name: ')
year = 2005
month = 6

api_key = "GFFgKCaH23x6cteSxCsx"
request = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?ticker=%s&api_key=%s" %(ticker_name,api_key)

data = pd.read_csv(request)
data['date'] = pd.to_datetime(data['date'])
#quandl.ApiConfig.api_key = "GFFgKCaH23x6cteSxCsx"
#data = quandl.get_table('WIKI/PRICES', ticker = ticker_name,paginate=True)

if data.shape[0]==0:
    print('This ticker is not in the database. Please try again')
    raise SystemExit(0)
    
data = data.loc[data['date'].dt.year == year]
data = data.loc[data['date'].dt.month == month]

output_file("%s_close_value_from_%i_%i.html" %(ticker_name,month,year))

p = figure(title="Closing stock prices", x_axis_label='date in %i' %(year), y_axis_label='price',  x_axis_type="datetime")
p.line(data['date'].tolist(), data['close'].tolist())
p.circle(data['date'].tolist(), data['close'].tolist(), fill_color="white", size=8)
show(p)