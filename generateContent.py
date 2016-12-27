# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:16:38 2016

@author: os
"""
import Data

class divTable:
    
    def GetTable(self):
        x=Data.DataStructure()
        rs=x.GetAllUnits()
        content=''
        for row in rs:
            content += " <div class='cell' onclick='UnitDetail(1)' style='float: left;display: inline;'> 	<table> <tr> 	<td>Jmeno:</td><td>{}</td>	</tr><tr> <td>Třída:</td>			<td>{}</td>		</tr> 	</table> </div>".format(row.nazev,row.cislo)
        return content
        
    def GetDetail(self):
        content = " <div class='detail'> Detail</div>"
        return content 