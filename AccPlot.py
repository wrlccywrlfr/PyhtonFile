import csv
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal
from scipy.signal import find_peaks

filename = './data1/d-12.5-1A.csv'
AccX = []
GyroZ = []


def SourcePlot():#グラフの表示
    fig = plt.figure()

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    #ax3 = fig.add_subplot(2, 2, 3)
    #ax4 = fig.add_subplot(2, 2, 4)
    with open(filename) as f:
        t = []
        #y = []
        ti = []
        #gy = []
        time = []
        a = 0
        reader = csv.reader(f)
        #next(reader)
        #next(reader)

        for row in reader:
            if row[0] == "1":
                if row[1] == "ags":
                    t.append(float(row[2]))
                    AccX.append(float(row[3]))
                    GyroZ.append(float(row[8]))
                    time.append(a)
                    a = a + 1



    ax1.plot(time, AccX)
    ax2.plot(time, GyroZ)
    plt.show()



def Analysis(): #1000切ったらスタート
    n = 0
    OldAcc = 0
    OldSpeed = 0
    Olddistance = 0
    OldAngle = 0
    TimeSpan = 0.001
    Speed = 0
    Angle = 0
    Distance = 0
    num = 0
    dis = 0
    SumDistance = 0
    SumAngle = 0

    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "1":
                if row[1] == "ags":
                    AccX.append(float(row[3]))
                    GyroZ.append(float(row[8]))

    for AccValue in AccX:
        #速度計算
        Speed = ((OldAcc + AccValue) * TimeSpan) /2 
        OldAcc = AccValue

        #距離計算
        Distance = ((Speed + OldSpeed) * TimeSpan) /2 #瞬間の距離
        OldSpeed = Speed

        #角度推定
        GyroValue = GyroZ[num]
        num += 1
        #度数法をラジアンに変換
        GyroValue = math.radians(GyroValue)
        #角度計算
        Angle = ((OldAngle + GyroValue) *TimeSpan) /2
        #角度加算
        OldAngle = SumAngle
        SumAngle += Angle
        

        dis = Distance/math.cos(SumAngle)  
        SumDistance = SumDistance + dis
        #print(SumDistance)

    
    SumDistance = SumDistance
    print(SumDistance)
                    
def main():
    #SourcePlot()
    Analysis()

if __name__ == "__main__":
    main()



