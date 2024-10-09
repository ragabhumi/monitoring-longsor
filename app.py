# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:08:31 2021

@author: yosis
"""

import dash
app = dash.Dash(__name__, suppress_callback_exceptions=True, routes_pathname_prefix='/monitoring-longsor/', requests_pathname_prefix='/monitoring-longsor/')
app.title = 'Monitoring Longsor'
server = app.server