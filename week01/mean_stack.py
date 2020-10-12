import numpy as np
def mean(files):
    s = sum(np.loadtxt(file,delimiter=',') for file in files)
    return np.round_(s/len(files),1)

if __name__ == "__main__":
    print(mean(["datasets/data.csv","datasets/data2.csv","datasets/data3.csv"]))
    print()
    print(mean(["datasets/data4.csv","datasets/data5.csv"]))