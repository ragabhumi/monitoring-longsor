# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:08:50 2021

@author: yosis
"""

from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import dash_leaflet as dl
from dash_extensions.javascript import Namespace
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import dash
from dash import dash_table
from datetime import datetime as dt
from app import app
from random import random
import subprocess
import os
import fnmatch

####################################################################################################
# 000 - FORMATTING INFO
####################################################################################################

####################### Corporate css formatting
corporate_colors = {
    'dark-blue-grey' : 'rgb(62, 64, 76)',
    'medium-blue-grey' : 'rgb(77, 79, 91)',
    'superdark-green' : 'rgb(255, 255, 255)',
    'dark-green' : 'rgb(0, 100, 0)',
    'medium-green' : 'rgb(93, 113, 120)',
    'light-green' : 'rgb(170, 211, 223)',
    'pink-red' : 'rgb(255, 101, 131)',
    'dark-pink-red' : 'rgb(247, 80, 99)',
    'white' : 'rgb(251, 251, 252)',
    'light-grey' : 'rgb(236, 236, 236)',
    'darkest-grey' : 'rgb(7, 9, 17)',
    'dark-grey' : 'rgb(57, 65, 77)',
    'red' : 'rgb(255, 0, 0)',
    'green' : 'rgb(0, 255, 0)',
    'blue' : 'rgb(0, 0, 255)',
    'yellow' : 'rgb(255, 255, 0)',
    'cyan' : 'rgb(0, 255, 255)',
    'magenta' : 'rgb(255, 0, 255)',
    'black' : 'rgb(0, 0, 0)',
    'orange' : 'rgb(255, 128, 0)',
    'purple' : 'rgb(127, 0, 255)'
}

externalgraph_rowstyling = {
    'margin-left' : '15px',
    'margin-right' : '15px'
}

externalgraph_colstyling = {
    'border-radius' : '10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['superdark-green'],
    'background-color' : corporate_colors['superdark-green'],
    'box-shadow' : '0px 0px 17px 0px rgba(186, 218, 212, .5)',
    'padding-top' : '7px'
}

filterdiv_borderstyling = {
    'border-radius' : '0px 0px 10px 10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['light-green'],
    'background-color' : corporate_colors['light-green'],
    'box-shadow' : '2px 5px 5px 1px rgba(255, 101, 131, .5)'
    }

navbarcurrentpage = {
    'text-decoration' : 'underline',
    'text-decoration-color' : corporate_colors['pink-red'],
    'text-shadow': '0px 0px 1px rgb(251, 251, 252)'
    }

recapdiv = {
    'border-radius' : '10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : 'rgb(251, 251, 252, 0.1)',
    'margin-left' : '15px',
    'margin-right' : '15px',
    'margin-top' : '15px',
    'margin-bottom' : '15px',
    'padding-top' : '5px',
    'padding-bottom' : '5px',
    'background-color' : 'rgb(251, 251, 252, 0.1)'
    }

recapdiv_text = {
    'text-align' : 'left',
    'font-weight' : '350',
    'color' : corporate_colors['white'],
    'font-size' : '1.5rem',
    'letter-spacing' : '0.04em'
    }

####################### Corporate chart formatting

corporate_title = {
    'font' : {
        'size' : 16,
        'color' : corporate_colors['white']}
}

corporate_xaxis = {
    'showgrid' : False,
    'ticks' : 'outside',
    'linecolor' : corporate_colors['black'],
    'color' : corporate_colors['black'],
    'tickangle' : 0,
    'titlefont' : {
        'size' : 12,
        'color' : corporate_colors['black']},
    'tickfont' : {
        'size' : 11,
        'color' : corporate_colors['black']},
    'zeroline': False
}

corporate_yaxis = {
    'showgrid' : True,
    'color' : corporate_colors['black'],
    'gridwidth' : 0.5,
    'gridcolor' : corporate_colors['light-grey'],
    'linecolor' : corporate_colors['black'],
    'titlefont' : {
        'size' : 12,
        'color' : corporate_colors['black']},
    'tickfont' : {
        'size' : 11,
        'color' : corporate_colors['black']},
    'zeroline': False
}

corporate_font_family = 'Dosis'

corporate_legend = {
    'orientation' : 'h',
    'yanchor' : 'bottom',
    'y' : 1.01,
    'xanchor' : 'right',
    'x' : 1.05,
	'font' : {'size' : 9, 'color' : corporate_colors['light-grey']}
} # Legend will be on the top right, above the graph, horizontally

corporate_margins = {'l' : 5, 'r' : 5, 't' : 45, 'b' : 15}  # Set top margin to in case there is a legend

corporate_layout = go.Layout(
    font = {'family' : corporate_font_family},
    title = corporate_title,
    title_x = 0.5, # Align chart title to center
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
    xaxis = corporate_xaxis,
    yaxis = corporate_yaxis,
    height = 270,
    legend = corporate_legend,
    margin = corporate_margins
    )
