# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:58:08 2019

@author: dng5
"""

import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

def plot_closing_prices(ticker_name = 'ZUMZ',year=2005,month=6):
    api_key = "GFFgKCaH23x6cteSxCsx"
    request = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?ticker=%s&api_key=%s" %(ticker_name,api_key)
    
    data = pd.read_csv(request)
    data['date'] = pd.to_datetime(data['date'])
    #quandl.ApiConfig.api_key = "GFFgKCaH23x6cteSxCsx"
    #data = quandl.get_table('WIKI/PRICES', ticker = ticker_name,paginate=True)
    
    if data.shape[0]==0:
        html = '%s is not in the database. Please try again' %(ticker_name)
        return html
  
    else:
        
        data = data.loc[data['date'].dt.year == year]
        if data.shape[0]==0:
            html = 'The year %i is not in the database for %s. Please try again' %(year,ticker_name)
            return html
        else:
            if data.shape[0]==0:
                html = 'The month %i is not in the database for %s in %i. Please try again' %(month,ticker_name,year)
                return html
            else:
                data = data.loc[data['date'].dt.month == month]
                
                #output_file("%s_close_value_from_%i_%i.html" %(ticker_name,month,year))
                
                p = figure(title="Closing stock prices for %s" %(ticker_name), x_axis_label='date in %i' %(year),
                           y_axis_label='price',  x_axis_type="datetime",plot_width=800, plot_height=300
                           )
                p.line(data['date'].tolist(), data['close'].tolist())
                p.circle(data['date'].tolist(), data['close'].tolist(), fill_color="white", size=8)
                #show(p)
                html = file_html(p, CDN, p.title)
                return html