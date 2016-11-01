# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:16:38 2016

@author: os
"""

class divTable:
    
    def GetTable(self):
        content = " <div class='cell' onclick='UnitDetail(1)'> 	<table> <tr> 	<td>Jmeno:</td><td>XXXXXXX</td>	</tr><tr> <td>Třída:</td>			<td>YYYYY</td>		</tr> 	</table> </div> <div class='cell'> 	<table> <tr> 	<td>Jmeno:</td><td>XXXXXXX</td>	</tr><tr> <td>Třída:</td>			<td>YYYYY</td>		</tr> 	</table> </div>"
        return content
        
    def GetDetail(self):
        content = " <div class='detail'> Detail</div>"
        return content 