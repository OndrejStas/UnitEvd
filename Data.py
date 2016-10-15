# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:10:07 2016

@author: os
"""

from  sqlalchemy import *
metadata = MetaData('sqlite:///tutorial.sqlite')
from datetime import datetime

#user_table = Table('tf_user', metadata,Column('id', Integer, primary_key=True),Column('user_name', Unicode(16),unique=True, nullable=False),Column('password', Unicode(40), nullable=False),Column('display_name', Unicode(255), default=''),Column('created', DateTime, default=datetime.now))

class DataStructure:
    """Create empty Db IF NOT Exists"""
    def CreateDB(self):
        metadata = MetaData('sqlite:///unitevd.sqlite')
        unit_table=Table('unit', metadata, Column('id', Integer, primary_key=True),Column('nazev', Unicode(20),unique=True, nullable=False),Column('cislo', Unicode(20),unique=True, nullable=False),Column('typ', Unicode(20),unique=True, nullable=true),Column('kod', Unicode(20),unique=True, nullable=true),Column('image1',BLOB, nullable=true),Column('image2',BLOB, nullable=true))
        job_table = Table('job', metadata, Column('id', Integer, primary_key=True),   Column('unit_id', Integer, nullable=False),Column('predmet_id', Integer, nullable=False) ,Column('pocet_predmetu', Integer, nullable=true), Column('aktula_pocet', Integer, nullable=true))        
        predmet_table = Table('predmet', metadata, Column('id', Integer, primary_key=True), Column('oznaceni', Unicode(20),unique=True, nullable=False), Column('popis', Unicode(200), nullable=true),Column('kod', Unicode(20), nullable=true),Column('image1',BLOB, nullable=true),Column('image2',BLOB, nullable=true))
        metadata.create_all()

x=DataStructure()
x.CreateDB()