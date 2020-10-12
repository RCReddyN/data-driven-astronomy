from astropy.io import fits
import matplotlib.pyplot as plt

hdulist = fits.open("datasets/image0.fits")
hdulist.info()
data = hdulist[0].data

print(data.shape)

plt.imshow(data,cmap=plt.cm.viridis)
plt.xlabel('x-pixels (RA)')
plt.ylabel('y-pixels (Dec)')
plt.colorbar()
plt.show()