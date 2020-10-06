import numpy as np #included in anaconda
import matplotlib.pyplot as plt #included in anaconda
from astropy.io import fits #install from pip
from matplotlib.colors import LogNorm   

# refer to FITS file contents part from https://github.com/RCReddyN/radio-data-analysis

def openandload(filename):  #returns "header data unit" object
    hdu_list = fits.open(filename)
    return hdu_list

def main():
    imagelocation = "./images/nebulae/dss.2.33.22+61.26.36.fits" #download fits file for respective coordinates
    image = openandload(imagelocation) #assigns hdu_list object

    #image.info() #displays information contained in the .fits file
    image_data = image[0].data #image information is located in primary block

    print(type(image_data)) #2D array containing the information of the image
    print(image_data.shape) #dimensions of the image

    image.close()   

    plt.imshow(image_data)
    plt.imsave('heart.png', image_data)

if __name__ == "__main__":
    main()    