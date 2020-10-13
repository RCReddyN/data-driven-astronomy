<h1> Stats, FITS Files and Stacking</h1>
<p>Python's standard library includes modules for solving a wide range of data processing tasks.</p>
<p>However, for scientific computing and data analysis, the Python developer community has created packages that simplify numerical computing and optimise performance on large data sets.</p>

<p>In the astronomy community, the most common modules include:
<ul><li><a href="http://www.numpy.org/">NumPy</a> – support for numerical computing and matrices;</li>
<li><a href="http://www.scipy.org/">SciPy</a> – fundamental libraries for scientific computing;</li>
<li><a href="http://www.matplotlib.org/">Matplotlib</a> – powerful plotting and data visualisation;</li>
<li><a href="http://www.astropy.org/">Astropy</a> – community library for astronomy.</li></ul>

<p>Packages like NumPy and Astropy are not included in the standard Python installation. You need to install these packages separately.</p>

<p>Packages usually have installation instructions on their website.</p>

<p>Two common approaches are using:</p>

<ol><li>A binary installer (you must use the right version for your Python version, operating system and CPU);
Python's pip installation tool.</li>
<li>Alternatively, you can use custom Python installations such as Enthought Canopy, Anaconda Python or Python(x, y) that include a large number of scientific and engineering packages. Anaconda and Python(x,y) are completely free, and Canopy is free for students.</li></ol>

<p>One further note is that almost all astronomy software is designed to run on Linux / MacOSX. If you use Windows on your home machine you might want to install a virtual machine if you plan to work in this area in the future.</p>

<h1>Measures of Central Tendencies:</h1>
<p>A measure of central tendency is a summary statistic that represents the center point or typical value of a dataset. These measures indicate where most values in a distribution fall and are also referred to as the central location of a distribution. You can think of it as the tendency of data to cluster around a middle value. In statistics, the three most common measures of central tendency are the mean, median, and mode. Each of these measures calculates the location of the central point using a different method.<p>
<h3>Mean:</h3>
<p>The mean is often called the average. To find the mean you take a set of data and calculate the sum of the data, after that you divide the sum by the number of pieces in the set.</p>
<h3>Median:</h3>
<p>The median is the number in an ordered set of data that is in the middle.</p>

<ol><li>If we have a set of data with an odd number of data points then the median is the data point in the middle.</li>
<li>If we have a set of data with an even number of data points, then the median is the mean of the two data points in the middle.</li></ol>

<h3>Mode:</h3>
<p>The mode is the most common number in the set of data.</p>

<h1>Calculating the mean stack of a set of FITS images</h1>
<h3>Stacking Images:</h3>
<p>Python lists are very flexible, but they are slow for big calculations.</p>

<p>NumPy arrays can store purely numerical data in much less space, and are much simpler and faster for calculations. Unlike Python lists, NumPy arrays support numerical operations on entire arrays, either as element-wise or matrix operations.</p>
<p><a href="mean.py">This code</a> compares performance of calculating mean using Numpy, Statistics modules to that which is calculated manually.</p> 
<h3>FITS Files:</h3>
<ul><li>One of the most widely used formats for astronomical images is the Flexible Image Transport System. In a FITS file, the image is stored in a numerical array, which we can load into a NumPy array.</li>
<li>FITS files also have headers which store metadata about the image.</li>
<li>FITS files are a standard format and astronomers have developed many libraries (in many programming languages) that can read and write FITS files.</li>
<li>Opening a FITS file in Astropy returns a HDU (Header/Data Unit) list. Each HDU stores headers and (optionally) image data.</li>
<li>The header contains metadata about the HDU object, e.g. its dimensions and data type. Every HDU can contain image data. The first HDU is called the primary HDU.</li>
<li>If we want to access individual HDUs, we can index the HDU list object returned by fits.open. The image data can be accessed using the data attribute.</li>
<li>The image data is conveniently stored in a NumPy array, so we can operate on it directly.</li>
<li>You often want to visualise the image data stored in FITS files. We can do this using the plotting library matplotlib.
<div style="text-align: center">
<img src="../images/figure1.png" hieght=500 width=500>
<p>The above is a mean stack image of a <a href="https://www.youtube.com/watch?v=-335gUOvdhA">pulsar</a> represented by the brightest pixel which is at the center of the plot.</p>
</div> 
</ul>
<h1>Which is Best—the Mean, Median, or Mode?</h1>
<p>When you have a symmetrical distribution for continuous data, the mean, median, and mode are equal. In this case, analysts tend to use the mean because it includes all of the data in the calculations. However, if you have a skewed distribution, the median is often the best measure of central tendency.</p>

<p>When you have ordinal data, the median or mode is usually the best choice. For categorical data, you have to use the mode.</p>

<footer> The above content is reproduced from:
<ul><li><a href="https://www.coursera.org/learn/data-driven-astronomy">Data-driven Astronomy</a></li>
<li><a href="https://www.mathplanet.com/education/pre-algebra/probability-and-statistic/the-mean-the-median-and-the-mode">Math Planet</a></li>
<li><a href="https://statisticsbyjim.com/basics/measures-central-tendency-mean-median-mode/">Statistics by Jim</a></li>

</ul>