# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:09:17 2021

@author: yosis
"""

from dash import dcc
from dash import html, dash_table
import dash_bootstrap_components as dbc
from app import app
from datetime import datetime
import pandas as pd
import dash_leaflet as dl
from dash_extensions.javascript import Namespace
from random import random

ns_ld = Namespace("myLD", "myMarkerLD")
ns_conf_fault = Namespace("myFault", "myConf_Fault")
ns_conf_fold = Namespace("myFault", "myConf_Fold")
ns_conf_normal = Namespace("myFault", "myConf_Normal")
ns_conf_thrust = Namespace("myFault", "myConf_Thrust")
ns_inf_fault = Namespace("myFault", "myInf_Fault")
ns_inf_normal = Namespace("myFault", "myInf_Normal")
ns_inf_thrust = Namespace("myFault", "myInf_Thrust")

def get_header():
    header = html.Div([
        dbc.Row([
            dbc.Col([]),

            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.Img(
                            src = app.get_asset_url('logo.png'),
                            id='logo_header',
                            # height = '70 px',
                            # width = 'auto',
                            # style = {'margin-top' : 'auto'}
                        )], width=1
                    ),
                    dbc.Col([
                        html.P(children='SISTEM MONITORING LONGSOR',
                                style = {'textAlign' : 'left', 'color' : 'white', 'font-weight':'bold'},
                                id='judul_header'
                        )], width=11
                    )
                ])
            ], width=10),

            dbc.Col([])
            ], style={'height' : '7vh', 'align' : 'center'}),
        ], style = {'position': 'relative',
                'background-color' : 'rgb(0, 88, 156)'})

    return header

def mainpage():
    # Map Source
    attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; Esri</a>'

    # Legenda HTML
    legend = html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('normal.png'), style={'width': '23px', 'height': '23px', 'marginRight': '5px'}),
            "Sensor Normal"
        ], style={'marginBottom': '5px'}),
        html.Div([
            html.Img(src=app.get_asset_url('offline.png'), style={'width': '20px', 'height': '20px', 'marginRight': '5px'}),
            "Sensor Offline"
        ], style={'marginBottom': '5px'}),
        html.Div([
            html.Img(src=app.get_asset_url('warning.gif'), style={'width': '20px', 'height': '20px', 'marginRight': '5px'}),
            "Landslide Warning"
        ], style={'marginBottom': '5px'}),

        html.Div([
            html.Span(style={'borderTop': '2px solid red', 'display': 'inline-block', 'width': '20px', 'height': '0px', 'marginRight': '5px'}),
            "Confirmed Fault"
        ], style={'marginBottom': '5px'}),
        html.Div([
            html.Span(style={'borderTop': '2px solid blue', 'display': 'inline-block', 'width': '20px', 'height': '0px', 'marginRight': '5px'}),
            "Confirmed Fold"
        ], style={'marginBottom': '5px'}),
        html.Div([
            html.Span(style={'borderTop': '2px solid green', 'display': 'inline-block', 'width': '20px', 'height': '0px', 'marginRight': '5px'}),
            "Confirmed Normal Fault"
        ], style={'marginBottom': '5px'}),
        html.Div([
            html.Span(style={'borderTop': '2px solid yellow', 'display': 'inline-block', 'width': '20px', 'height': '0px', 'marginRight': '5px'}),
            "Confirmed Thrust Fault"
        ], style={'marginBottom': '5px'}),
        html.Div([
            html.Span(style={'borderTop': '2px dashed red', 'display': 'inline-block', 'width': '20px', 'height': '0px', 'marginRight': '5px'}),
            "Inferred Fault"
        ], style={'marginBottom': '5px'}),
        html.Div([
            html.Span(style={'borderTop': '2px dashed green', 'display': 'inline-block', 'width': '20px', 'height': '0px', 'marginRight': '5px'}),
            "Inferred Normal Fault"
        ], style={'marginBottom': '5px'}),
        html.Div([
            html.Span(style={'borderTop': '2px dashed yellow', 'display': 'inline-block', 'width': '20px', 'height': '0px', 'marginRight': '5px'}),
            "Inferred Thrust Fault"
        ])
    ], style={'background': 'rgba(255, 255, 255, 0.7)', 'padding': '10px', 'borderRadius': '5px', 'boxShadow': '2px 2px 5px rgba(0,0,0,0.2)', 'position': 'absolute', 'bottom': '25px', 'right': '10px', 'zIndex': '1000', 'fontSize': '12px'})



    page = html.Div([
        get_header(),
        dbc.Col([


            html.Div([
                dl.Map(center=[-6.779, 107.651], zoom=12, zoomControl=True, children=[
                    # Basemap
                    dl.LayersControl(
                        [dl.BaseLayer(dl.TileLayer(url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', maxZoom=20, attribution=attribution), name="OpenStreetMap", checked= "OpenStreetMap"),
                         dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', maxZoom=20, attribution=attribution), name="Esri World Topo Map", checked= "OpenStreetMap"),
                         dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', maxZoom=20, attribution=attribution), name="Esri NatGeo World Map", checked= "OpenStreetMap"),
                         dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', maxZoom=20, attribution=attribution), name="Esri World Street Map", checked= "OpenStreetMap"),
                         dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', maxZoom=20, attribution=attribution), name="Esri World Imagery", checked= "OpenStreetMap")] +

                         # Stasiun LD
                         [dl.Overlay(dl.LayerGroup(id="sensor", children=[dl.GeoJSON(url=app.get_asset_url('sensor.json?a='+str(random())), options=dict(pointToLayer=ns_ld("pointToLayer"), onEachFeature=ns_ld("bindPopup")))]), name="Sensor", checked=True),
                         dl.Overlay(dl.GeoJSON(url=app.get_asset_url('faults/confirmed_fault.geojson'), id="confirmed_fault", options=dict(style=ns_conf_fault("style"), onEachFeature=ns_conf_fault("bindPopup"))), name="Confirmed Fault", checked=True),
                         dl.Overlay(dl.GeoJSON(url=app.get_asset_url('faults/confirmed_fold.geojson'), id="confirmed_fold", options=dict(style=ns_conf_fold("style"), onEachFeature=ns_conf_fold("bindPopup"))), name="Confirmed Fold", checked=True),
                         dl.Overlay(dl.GeoJSON(url=app.get_asset_url('faults/confirmed_normal.geojson'), id="confirmed_normal", options=dict(style=ns_conf_normal("style"), onEachFeature=ns_conf_normal("bindPopup"))), name="Confirmed Normal Fault", checked=True),
                         dl.Overlay(dl.GeoJSON(url=app.get_asset_url('faults/confirmed_thrust.geojson'), id="confirmed_thrust", options=dict(style=ns_conf_thrust("style"), onEachFeature=ns_conf_thrust("bindPopup"))), name="Confirmed Thrust Fault", checked=True),
                         dl.Overlay(dl.GeoJSON(url=app.get_asset_url('faults/inferred_fault.geojson'), id="inferred_fault", options=dict(style=ns_inf_fault("style"), onEachFeature=ns_inf_fault("bindPopup"))), name="Inferred Fault", checked=True),
                         dl.Overlay(dl.GeoJSON(url=app.get_asset_url('faults/inferred_normal.geojson'), id="inferred_normal", options=dict(style=ns_inf_normal("style"), onEachFeature=ns_inf_normal("bindPopup"))), name="Inferred Normal Fault", checked=True),
                         dl.Overlay(dl.GeoJSON(url=app.get_asset_url('faults/inferred_thrust.geojson'), id="inferred_thrust", options=dict(style=ns_inf_thrust("style"), onEachFeature=ns_inf_thrust("bindPopup"))), name="Inferred Thrust Fault", checked=True),

                         dl.ScaleControl(position="bottomleft"),
                         dl.MeasureControl(position="topleft", primaryLengthUnit="kilometers", primaryAreaUnit="sqmeters", secondaryAreaUnit="hectares", activeColor="#214097", completedColor="#972158"),
                         ],
                    )], style={'width': '100vw', 'height': '93vh', 'margin': "auto", "position": "relative"}
                 ),
                 legend
            ], className = 'row sticky-top'), # External row
            ])
        ])


    return page