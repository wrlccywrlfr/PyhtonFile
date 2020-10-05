import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import find_peaks

filename = 'd-12.5-1.csv'

def plot():
    fig = plt.figure()

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    #ax3 = fig.add_subplot(2, 2, 3)
    #ax4 = fig.add_subplot(2, 2, 4)
    with open('./data1/'+ filename) as f:
        t = []
        y = []
        ti = []
        gy = []

        reader = csv.reader(f)
        #next(reader)
        #next(reader)

        for row in reader:
            if row[0] == "ags":
                t.append(float(row[1]))
                ti.append(float(row[1]))
                y.append(float(row[2]))
                gy.append(float(row[7]))



    ax1.plot(t, y)
    ax2.plot(ti, gy)
    plt.show()



# def analysis():
#     AccX = []
#     with open('./deta1/'+filename) as f:
#         readline = csv.reader(f)
#         for row in readline:
#             if row [0] == "ags":
#                 AccX.append = (float(row[1]))
        

                    
def main():
    plot()


if __name__ == "__main__":
    main()



