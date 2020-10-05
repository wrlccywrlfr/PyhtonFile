import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import find_peaks

t = []
y = []
with open('./data1/d-12.5-1.csv') as f:

    reader = csv.reader(f)
    #next(reader)
    #next(reader)

    for row in reader:
        if row[0] == "ags":
            t.append(float(row[1]))
            y.append(float(row[2]))

plt.plot(t, y)
plt.show()

