#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:19:28 2022

@author: ndoumbe
"""

def f(i,j):
    n=j-i+1
    s1=n*(j+i)/2
    s2=0
    for x in range(i,j+1):
        s2=s2+x
    y=i
    s3=0
    while(y<j+1):
        s3=s3+y
        y=y+1
    return s1,s2,s3
v=f(2,4) 
print(v)   
    