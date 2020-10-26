import csv
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal
from scipy.signal import find_peaks
filename_Source = './data2/b-12.5-1.csv'
filename = './data4_arrange/a-12.5-2.csv'
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

def Plot():
    plt.plot(GyroZ)
    plt.show()


def Analysis(): #距離推定の計算
    SpeedSum = []
    AngleSum = []
    SpeedSum_1 = []
    SpeedFront = []
    DistanceFront = []
    SumDistance = 0
    Ansor = []
    Ansor_Dis = 0
    n = 0
    OldAcc = 0
    OldSpeed = 0
    OldAngle = 0
    OldDistance = 0
    distance = 0
    TimeSpan = 0.001
    Sp = 0
    Gy = 0
    Speed = 0
    SpeedValue = 0
    S = 0
    SumSpeed = 0
    SumSp = 0
    Angle = 0
    num = 0
    SumAngle = 0
    count = 0
    Front = 0
    X = 0
    Y = 0
    dis = 0

    for AccValue in AccX:
        #速度計算
        AccValue = AccValue * (9.8/10000)
        Speed = ((OldAcc + AccValue) * TimeSpan) /2 
        OldAcc = AccValue
        SumSpeed += Speed 
        SpeedSum.append(SumSpeed)#速度変化を保存

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
        AngleSum.append(SumAngle)

    for SpeedValue in SpeedSum:#直線の距離にして保存
        Gy = AngleSum[n]
        Sp = math.cos(Gy) * SpeedValue
        dis = ((Sp + OldSpeed)*TimeSpan)/2 #距離計算
        OldSpeed = Sp
        SumDistance += dis#ノイズありの直線の距離
        DistanceFront.append(dis)
        n += 1
  
    for Front in DistanceFront:
        X = 25*(Front/SumDistance)
        distance = X / math.cos(AngleSum[count])
        Ansor_Dis += distance 
        count += 1
        Y += X

    #print(Y)

    
    print("推定距離")
    print(Ansor_Dis)

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
    t = []
    count = 0
    #fig = plt.figure()

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
        count = count + 1
        t.append(count)
        GyroPlot.append(SumAngle_2)

    plt.plot(t, GyroPlot)
    plt.show()
    print(math.degrees(SumAngle_2))

def main():
    #SourcePlot()
    Analysis()
    #GyroIntegral()
    #Plot()

if __name__ == "__main__":
    main()

    #Memo
    #縦25横18m
    #正解角度54.5494...度
    #正解距離27.90m

