import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import find_peaks

filename = './data1/d-12.5-1A.csv'

def SourcePlot():#グラフの表示
    fig = plt.figure()

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    #ax3 = fig.add_subplot(2, 2, 3)
    #ax4 = fig.add_subplot(2, 2, 4)
    with open(filename) as f:
        t = []
        y = []
        ti = []
        gy = []
        time = []
        a = 0
        reader = csv.reader(f)
        #next(reader)
        #next(reader)

        for row in reader:
            if row[0] == "1":
                if row[1] == "ags":
                    t.append(float(row[2]))
                    y.append(float(row[3]))
                    gy.append(float(row[8]))
                    time.append(a)
                    a = a + 1



    ax1.plot(time, y)
    ax2.plot(time, gy)
    plt.show()



# def analysis(): #1000切ったらスタート
#     AccX = []
#     AccY = []
#     AccZ = []
#     GyroX = []
#     GyroY = []
#     GyroZ = []
#     n = 0

#     with open('./deta1/'+ filename) as f:
#         readline = csv.reader(f)
#         for row in readline:
#             if row [0] == "ags":
#                 AccX.append = row
            
#             print(AccX)
#                 # AccX.append = (float(row[2]))
#                 # AccY.append = (float(row[3]))
#                 # AccY.append = (float(row[4]))
#                 # GyroX.append = (float(row[5]))
#                 # GyroY.append = (float(row[6]))
#                 # GyroZ.append = (float(row[7]))

#         # for lenge in AccX:
#         #     if lenge > 1000:
#         #         AccX = AccX[1:]
#         #     if lenge <=1000:
#         #         break

#         # for lengs in AccX:
#         #     if lengs < 6000:

#         #     if lengs >= 6000:
#         #         break 
        


                    
def main():
    SourcePlot()
    #analysis()

if __name__ == "__main__":
    main()



