from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

def load_fits(filename):
    hdulist = fits.open(filename)
    data = hdulist[0].data
    #print(data.shape)
    #return np.unravel_index(np.argmax(data, axis=None),data.shape) #np.unravel_index converts flat index to nd index
    return data

def mean_fits(files):
    s = sum(fits.open(file)[0].data for file in files)
    return s/len(files)

def plot_img_stack(files):
    data = mean_fits(files)
    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.xlabel('x-pixels (Dec)')
    plt.ylabel('y-pixels (RA)')
    plt.colorbar()
    plt.show()

if __name__== '__main__':
    files = ["datasets/image0.fits",
    "datasets/image1.fits",
    "datasets/image2.fits",
    "datasets/image3.fits"]
    plot_img_stack(files)