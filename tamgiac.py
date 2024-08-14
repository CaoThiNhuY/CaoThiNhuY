# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:00:00 2024

@author: nhuy23733881
"""
import math

a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))

if a + b > c and a + c > b and b + c > a:
    print("a, b, c là ba cạnh của một tam giác.")
    
    if a == b == c:
        print("Tam giác đều.")
    elif (math.isclose(a**2 + b**2, c**2) or
          math.isclose(a**2 + c**2, b**2) or
          math.isclose(b**2 + c**2, a**2)):
        print("Tam giác vuông.")
    elif a == b or b == c or a == c:
        print("Tam giác cân.")
    else:
        print("Tam giác thường.")
else:
    print("a, b, c không phải là ba cạnh của một tam giác.")
