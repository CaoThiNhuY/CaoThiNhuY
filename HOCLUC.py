# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:26:01 2024

@author: nhuy
"""

print("hello world")

gpa = float(input("Nhap diem GPA :"))
if gpa < 3.5:
    print ("Hoc luc Kem")
elif 3.5 <= gpa < 5.0:
    print ("Hoc luc Yeu")
elif 5.0 <= gpa < 7.0:
    print ("Hoc luc Trung binh")
elif 7.0 <= gpa < 8.0:
    print ("Hoc luc Kha")
elif 8.0 <= gpa <9.0:
    print ("Hoc luc Gioi")
elif 9.0 <= gpa <= 10:
    print ("Hoc luc Xuat sac")
else:
    print ("khong xac dinh")
    
