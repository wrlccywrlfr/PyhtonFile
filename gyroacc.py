# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 08:54:37 2020

@author: daisu
"""


import sympy as sym
import csv
import pandas as pd
import numpy as np
import math 
from sympy.plotting import plot
from sympy import sin, cos, tan, log, exp
sym.init_printing(use_unicode=True)
#% matplotlib inline
a, b, c, x, y = sym.symbols("a b c x y")
gyro_data_x=[]
gyro_data_y=[]
gyro_data_z = []
Acc_data_x = []
Acc_data_y = []
Acc_data_z = []
data_z_1 = []
data = []

df = pd.read_csv('filename')

#gyroセンサの値を格納
with open("filename") as f:#ラジアンで格納されている(rad/s)
    for row in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        gyro_data_x.append(row[0])#x座標
        gyro_data_y.append(row[1])#y座標
        gyro_data_z.append(row[2])#z座標

#Accセンサの値を格納
with open("filename") as f:
    for Arow in csv.reader(f, quoting = csv.QUOTE_NONNUMERIC):
        Acc_data_x.append(Arow[0])#x座標(スマホの横向き)
        Acc_data_y.append(Arow[1])#y座標(進行方向)
        Acc_data_z.append(Arow[2])#z座標(重力方面)
        
      
long_value = 25/(len(df)+1)
print("1データ当たりの距離:",long_value)
print(len(Acc_data_x))
 
#filterCoefficient = 0.9
#lowpassValue = 0
oldangle = 0
oldSpeed = 0
oldAcc = 0
timeSpan = 18/len(df)
Speed = 0
difference = 0
angle = 0 #角度
long = 0 #区間の実際の距離
long_sum = 0#距離の合計
i = 0


for AccValue in Acc_data_y:
    #速度計算
    Speed = ((oldSpeed + AccValue)*timeSpan) / 2 + Speed
    oldAcc = AccValue
    #変位計算
    difference = ((oldSpeed + Speed)*timeSpan) / 2 
    oldSpeed = Speed   
    if(i<len(df)):
        gyrovalue = gyro_data_z[i]
        #角度計算
        angle = (gyrovalue + oldangle)
        #距離の計算
        long = difference/math.cos(angle * timeSpan /2) 
        #距離加算
        long_sum += long
        #現在の値を保存
        oldangle = angle 
        i = i + 1
    
    
    



for value in gyro_data_z:
    #print(value)    
    #value = np.abs(value)
    #ローパスフィルタ
    #lowpassValue = lowpassValue * filterCoefficient + value * (1 - filterCoefficient)
    #ハイパスフィルタ
    #highpassValue = value - lowpassValue
    
    #角度計算
    angle = (value + oldangle)
    #距離の計算
    long = long_value/math.cos(angle * timeSpan /2) 
    #距離加算
    long_sum += long
    #現在の値を保存
    oldangle = angle 
    

print("結果:",long_sum)

