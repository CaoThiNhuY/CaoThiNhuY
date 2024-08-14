# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:56:16 2024

@author: nhuy23733881
"""
a = float (input("Nhap gia tri a: "))
b= float (input("Nhap gia tri b: "))
if a == 0:
    if b== 0:
        print ("Phuong trinh co vo so nghiem.")
    else: 
        print ("Phuong trinh vo nghiem.")
else: 
    x = -b/a
    print (f"Nghiem cua phuong trinh la: x = {x}")
    
