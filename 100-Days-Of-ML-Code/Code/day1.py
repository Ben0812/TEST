# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:54:25 2018

@author: liuwei
"""

a = '100'
b = '110010'

if len(a) > len(b):
    c = a
    a = b
    b = c
out = ''
flag = 0
        
for i in range(1, len(a)+1):
    if int(a[-i]) + int(b[-i]) + flag == 0:
        out = '0' + out
        flag = 0
        
    elif int(a[-i]) + int(b[-i]) + flag == 1:
        out = '1' + out
        flag = 0
       
    elif int(a[-i]) + int(b[-i]) + flag == 2:
        out = '0' + out
        flag = 1
        
    elif int(a[-i]) + int(b[-i]) + flag == 3:
        out = '1' + out
        flag = 1
        
                
for j in range(len(a)+1, len(b)+1):
    if int(b[-j]) + flag == 0:
        out = '0' + out

    elif int(b[-j]) + flag == 1:
        out = '1' + out
        flag = 0
    elif int(b[-j]) + flag == 2:
        out = '0' + out
        flag = 1
if flag == 1:
    out = '1' + out
