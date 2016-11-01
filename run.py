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
    return static_file(filename, root='scripts')

@route('/styles/<filename>')
def server_styles(filename,method='GET'):
    print filename
    return static_file(filename, root='styles')

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
    
@route ('/detailunit/<inputt>')
def detailUnit(inputt, method='GET'):
    x= divTable()
    return x.GetDetail()

@route('/hello')
@route('/hello/<name>')
def hello(name='World'):
    return template('hello_template', name=name)
 
@route ('/detail/<inputt>')
def detail(inputt, method='GET'):
    filename = 'detail.html'
    return static_file(filename,  root='' ) 

run(host='localhost', port=8080)