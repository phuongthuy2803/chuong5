# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:29:53 2024

@author: Student
"""

n= int(input("Nhập số cần tính giai thừa:"))
gth=1
for i in range(1, n+1):
   gth*=i
print("Kết quả phép tính giai thừa bằng", gth)