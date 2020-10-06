import numpy as np

def ra2deg(h,m,s):
    return 15*(h+m/60+s/3600)

def dec2deg(deg,amin,asec):
    sign = 1
    if deg < 0:
        deg = deg*-1
        sign = -1
    return sign*(deg+amin/60+asec/3600)

def main():
    a = np.array([ra2deg(5,34,32.16), dec2deg(22,1,6.63)])
    print(a)
if __name__ == "__main__":
    main()