# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:43:20 2024

@author: Student
"""

x= float(input("nhập số thuộc [-99, 99]: "))
while x<-99 or x>99:
    x= float(input("nhập lại số thuộc [-99, 99]: "))
print("Số bạn nhập đã thỏa điều kiện")