import numpy as np
from statistics import mean
import time

def mean_usingnumpy(filename):
    arr = np.loadtxt(filename,delimiter=',')
    start = time.perf_counter()
    mean = np.round_(np.mean(arr),decimals=1)
    stop = time.perf_counter()
    return (mean,(stop-start))
      

def mean_usingstatsmodule(filename):
    arr = []
    for line in open(filename):
        row = []
        for col in line.strip().split(','):
            row.append(float(col))
        arr.append(row)

    arr = [item for sublist in arr for item in sublist]
    start = time.perf_counter()
    ans = round(mean(arr),1)
    stop = time.perf_counter()
    return (ans,(stop-start))

def mean_manualcomputation(filename):
    arr = []
    for line in open(filename):
        row = []
        for col in line.strip().split(','):
            row.append(float(col))
        arr.append(row)

    arr = [item for sublist in arr for item in sublist]    
    start = time.perf_counter()
    s = sum(arr)
    l = len(arr)
    ans = round(s/l,1)
    stop = time.perf_counter()
    return (ans,(stop-start))

if __name__ == '__main__':
    files = ["datasets/data.csv","datasets/data2.csv","datasets/data3.csv"]
    stats = 0
    numpy = 0
    manual = 0

    for file in files:
        (ans1,time1) = mean_usingnumpy(file)
        (ans2,time2) = mean_usingstatsmodule(file)
        (ans3,time3) = mean_manualcomputation(file)
        print(ans1,ans2,ans3)
        stats = stats+time2
        numpy = numpy+time1
        manual = manual+time3

    times = {"using mean from statistics module":stats/len(files), 
            "using numpy module":numpy/len(files),
            "manual computation":manual/len(files)}
    print("Avg time taken\n",times)