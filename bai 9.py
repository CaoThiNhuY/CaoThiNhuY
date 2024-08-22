# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:44:11 2024

@author: nhuy23733881
"""
print("((a**2 - b**2) / (a**4 - b**4)) - ((a**2 + (a*b)**4) / (a**4 + b**4))")
a=(float(input("Nhap gia tri a=")))
b=(float(input("Nhap gia tri b=")))
bt=(((a**(1/2) - b**(1/2)) / (a**(1/4) - b**(1/4)))) - ((a**(1/2) + (a*b)**(1/4))) /(a**(1/4) + b**(1/4))
print ("ket qua la:", bt)