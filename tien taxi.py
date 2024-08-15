# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:15:59 2024

@author: nhuy23733881
"""
print ("Tinh tien taxi")
a=float(input("So km di duoc la"))
if a==1:
    print("Tien taxi la 20k")
if a==2 or a==3:
    b=a*13
    print ("Tien taxi la ",b,"k")
if a>=4 and a<=8:
    b=a*12
    print("Tien taxi la",b,"k")
if a>8 and a<=100:
    b=a*10
    print("Tien taxi la",b,"k")
if a>100:
    b=(a*10)-(a*10*8/100)
    print ("Tien taxi la",b,"k")