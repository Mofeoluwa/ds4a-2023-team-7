#using DashBootstrapComponents
import dash_bootstrap_components as dbc
import time
from webbrowser import get
#import boto3
import json
import os
import pandas as pd


class NavBarHeader(dbc.NavbarSimple):
    def __init__(self,page_title):
        super().__init__(brand=page_title,color='#531e1e',dark=True)
        self.children=[self.build_menu()]
        self.class_name = 'navbarheader'
        self.fluid=True
    
    def build_menu(self):
        
        menu_children = [dbc.DropdownMenuItem("Home", header = True),
                                dbc.DropdownMenuItem(divider=True),dbc.DropdownMenuItem('Page 1',href='',header = True),
                                dbc.DropdownMenuItem(divider=True),dbc.DropdownMenuItem('Page 2',href='',header = True),
                                dbc.DropdownMenuItem(divider=True),dbc.DropdownMenuItem('Page 3',href='',header = True)]

        menu=dbc.DropdownMenu(
                    label='Menu',
                    children=menu_children,
                    nav=True,
                    in_navbar=True,
                    align_end=True
        )
        return menu