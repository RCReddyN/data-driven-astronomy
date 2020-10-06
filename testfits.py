import numpy as np #included in anaconda
import matplotlib.pyplot as plt #included in anaconda
from astropy.io import fits #install from pip
from matplotlib.colors import LogNorm

# refer to FITS file contents part from https://github.com/RCReddyN/radio-data-analysis

def retrievedata(filename):  #returns "header data unit" object
    hdu_list = fits.open(filename)
    image_data = hdu_list[0].data #image information is contained in primaryHDU
    hdu_list.close()
    return image_data

def plot(img):
    plt.imshow(img, cmap='gray')
    plt.colorbar()
    plt.savefig('orion.png')

def disp_stats(img):
    stats = np.array([np.min(img), np.max(img), np.mean(img), np.median(img), np.std(img)])
    print("statistics:", stats)

def plot_hist(img):
    histogram = plt.hist(img.flatten(), bins = 'auto')
    plt.savefig('orionhist.png')

def plot_logcolors(img):
    plt.imshow(img, cmap='gray', norm=LogNorm())
    cbar = plt.colorbar(ticks=[5.e3,1.e4,2.e4])
    cbar.ax.set_yticklabels(['5,000','10,000','19,000']) #set labels by looking at the histogram 
    plt.savefig('orion_logcolors.png')

def main():
    fitspath = "./images/nebulae/dss.5.35.17-5.23.28.fits" #download fits file for respective coordinates
    image = retrievedata(fitspath) #assigns hdu_list object
    print("dimensions:", image.shape)
    #plot(image)
    disp_stats(image)
    #plot_hist(image)
    plot_logcolors(image)
     
if __name__ == "__main__":
    main()    