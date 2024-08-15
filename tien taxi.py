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
    b= 3*13+ (a-3)*12
    print("Tien taxi la",b,"k")
if a>8:
    b=3*13+ 5*12+ (a-8)*10
    print("Tien taxi la",b,"k")
if b>100:
    b=b*92/100
    print ("Tien taxi la",b,"k")