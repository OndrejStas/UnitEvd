# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:14:59 2016

@author: os
"""

from bottle import route, run, template,static_file, response 
from generateContent import divTable


@route('/scripts/<filename>')
def server_static(filename,method='GET'):
    print filename
    return static_file(filename, root='C:\Users\os\Documents\SpyderWS\UnitEvd\scripts')

@route('/styles/<filename>')
def server_styles(filename,method='GET'):
    print filename
    return static_file(filename, root='C:\Users\os\Documents\SpyderWS\UnitEvd\styles')

@route('/prg') 
def prg():
    filename = 'index.html'
#    return static_file(filename,  root='C:\Users\os\Documents\SpyderWS\UnitEvd' )  
    return static_file(filename,  root='' ) 


@route ('/gettable/<inputt>')
def getTable(inputt, method='GET'):
    x= divTable()
    return x.GetTable()
    return inputt

run(host='localhost', port=8080)