# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:09:01 2021

@author: yosis
"""

from dash import dcc
from dash import html
import dash
from app import app
from app import server
from layouts import mainpage
# import callbacks
from flask_caching import Cache


cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache',
    'CACHE_THRESHOLD': 1000
})
app.config.suppress_callback_exceptions = True

timeout = 20


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
@cache.memoize(timeout=timeout)
def display_page(pathname):
    if pathname == '/apps/mainpage':
         return mainpage()
    # elif pathname == '/apps/plot_data':
    #      return plot_data
    # elif pathname == '/apps/about':
    #      return about
    else:
        return mainpage() # This is the "home page"

if __name__ == '__main__':
    app.run_server(debug=False, host = '127.0.0.1')
