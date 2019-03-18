#!/bin/env python3
# -*- coding:utf-8 -*-
#------------------------------------------------------------------------------
# Author: LiuGaoyong                                                          |
# E-mail: liugaoyong_88@163.com, liugaoyong88@gmail.com                       |
# Description:                                                                 
#                            

from scipy import constants as fcp

class Phsical_Quantity(object):

    def __init__(self, number, unit):
        self.number = number
        self.unit = unit 
    
    def print(self ):
        print(self.number, self.unit)






class Energy(Phsical_Quantity):   
    def toSI(self):
        if self.unit.lower() == "ev" :
            return Energy(self.number * fcp.m_e, "J")
        if self.unit.lower() == "cal":
            return Energy(self.number * fcp.calorie, "J")
        if self.unit.lower() == "j":
            return self



b=Energy(2,"eV").toSI()
b.print()
print()


