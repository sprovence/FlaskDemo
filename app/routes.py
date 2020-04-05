from flask import Flask, render_template, request, redirect, url_for
from bokeh.embed import components
#from bokeh.plotting import figure
from app.models import Ticker, add_to_db
from app.app_utils import plot_data
from app import app

app.vars={}

@app.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == "POST":
        app.vars['ticker'] = request.form['ticker']
        ticker = app.vars['ticker']
        plots = request.form.getlist('plots')
        close = 'close' in plots
        adj_close = 'adj_close' in plots
        opn = 'open' in plots
        adj_opn = 'adj_open' in plots
        #db_addition = Ticker(symbol=ticker, closing_price=True, 
        #                     adj_closing_price=True, opening_price=True, 
        #                     adj_opening_price=True)
        #add_to_db(db_addition)
        p = plot_data(ticker=ticker, close=close, adj_close=adj_close, 
                      opn=opn, adj_open=adj_opn)
        script, div = components(p)
        return render_template('test.html', title='Bokeh Plot', script=script, 
                               div=div)
    else:
        return render_template('test.html', title='Home')
  
@app.route('/plot', methods=['GET','POST'])
def plot():
    ticker = app.vars['ticker']
    p = plot_data(ticker=ticker, close=True, adj_close=True, 
                         opn=True, adj_open=True)
    script, div = components(p)
    return render_template('plot.html', title='Bokeh Plot', script=script, 
                           div=div)

