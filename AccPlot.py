import csv
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal
from scipy.signal import find_peaks
filename_Source = './data3/d-12.5-2.csv'
filename = './data1_arrange/c-12.5-1.csv'
AccX = []
AccY = []
AccZ = []
GyroX = []
GyroY = []
GyroZ = []
with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "1":
                if row[1] == "ags":
                    AccX.append(float(row[3]))
                    AccY.append(float(row[4]))
                    AccZ.append(float(row[5]))
                    GyroX.append(float(row[6]))
                    GyroY.append(float(row[7]))
                    GyroZ.append(float(row[8]))


def SourcePlot():#データのプロット
    fig = plt.figure()

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    with open(filename_Source) as f:#生データのプロット
        time = []
        DataAX = []
        DataAY = []
        DataAZ = []
        DataGX = []
        DataGY = []
        DataGZ = []
        a = 0
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "ags":
                DataAX.append(float(row[2]))
                DataAY.append(float(row[3]))
                DataAZ.append(float(row[4]))
                DataGX.append(float(row[5]))
                DataGY.append(float(row[6]))
                DataGZ.append(float(row[7]))
                time.append(a)
                a = a + 1#(0.001秒)
    ax1.plot(time, DataAX)
    ax2.plot(time, DataGZ)
    plt.show()

def Analysis(): #距離推定の計算
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
    count = 0

    for AccValue in AccX:
        #速度計算
        AccValue = AccValue * (9.8/10000)
        Speed = ((OldAcc + AccValue) * TimeSpan) /2 
        OldAcc = AccValue #現在の加速度を保存

        #距離計算
        Distance = ((Speed + OldSpeed) * TimeSpan) /2 #瞬間の距離
        OldSpeed += Speed #現在の速度を保存(速度は加算？)

        #角度推定
        GyroValue = GyroZ[num]
        num += 1
        #度数法をラジアンに変換
        GyroValue = GyroValue * 0.01 #0.01Dps
        GyroValue = math.radians(GyroValue)#DPSだから度数法
        #角度計算
        Angle = ((OldAngle + GyroValue) *TimeSpan) /2 
        #角度加算
        OldAngle = GyroValue
        SumAngle += Angle
        

        dis = Distance/math.cos(SumAngle) #瞬間の距離
        SumDistance += dis #距離の加算

    print("推定距離")
    print(SumDistance)
    print("推定合計角度")
    print(math.degrees(SumAngle))
    #Memo
    #加速度の単位は0.1mg(1g = 9.8m/S^2)(0.1mgは1/10000)
    #10000 = 1g
    #10000 * (9.8/10000) = 9.8m/s^2
    #角速度は0.01dps(1dpsは1秒で1度)(4000は1秒で40度)

def GyroIntegral():
    GyroCheck = []
    GyroPlot = []
    AngleValue = 0
    number = 0
    OldAng = 0
    TimeSpan_2 = 0.001
    SumAngle_2 = 0
    t = 0

    for AngleValue in GyroZ:    
        #角度推定
        #度数法をラジアンに変換
        AngleValue = AngleValue * 0.01 #0.01Dps
        AngleValue = math.radians(AngleValue)#DPSだから度数法
        #角度計算
        AngleAnsor = ((OldAng + AngleValue) *TimeSpan_2) /2 
        #角度加算
        OldAng = AngleValue
        SumAngle_2 += AngleAnsor
        t += 1
        GyroPlot.append(float(SumAngle_2))

    plt.plot(t, GyroPlot)
    plt.show
    print (SumAngle_2)

def main():
    #SourcePlot()
    #Analysis()
    GyroIntegral()

if __name__ == "__main__":
    main()

    #Memo
    #縦25横18m
    #正解角度54.5494...度
    #正解距離27.90m

