
# Import packages
import quandl
import pandas as pd
from bokeh.plotting import figure

def plot_data(ticker='GOOG', close=True, adj_close=True, opn=True, 
              adj_open=True):
    # Configure the API key
    api_token = '3TDpKqPv5_vv_iHQydy4'
    quandl.ApiConfig.api_key = api_token

    # Use the input data to query Quandl
    data = quandl.get_table('WIKI/PRICES', ticker=ticker, paginate=True)
    data['date'] = pd.to_datetime(data['date'])
    
    # Set up the plot figure
    p = figure(x_axis_type='datetime', title="Stock Plot", plot_width=1000, 
               plot_height=400)
    
    # Plot the specified data:
    if close:
        p.line(x=data['date'], y=data['close'], line_color='red', 
               legend_label='Close')
    if adj_close:
        p.line(x=data['date'], y=data['adj_close'], line_color='orange', 
               legend_label='Adjusted Close')
    if opn:
        p.line(x=data['date'], y=data['open'], line_color='blue', 
               legend_label='Open')
    if adj_open:
        p.line(x=data['date'], y=data['adj_open'], line_color='green', 
               legend_label='Adjusted Open')

    # Label axes
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Volume'
    
    # Adjust legend
    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    
    return p
