<h1> Introdution</h1>
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

<h1>The mean, the median and the mode</h1>
<p>Mean, median and mode are numbers that represent a whole set of data or information. Mean, median and mode are together called the measures of central tendency.<p>
<h3>Mean:</h3>
<p>The mean is often called the average. To find the mean you take a set of data and calculate the sum of the data, after that you divide the sum by the number of pieces in the set.</p>
<h3>Median:</h3>
<p>The median is the number in an ordered set of data that is in the middle.</p>

<ol><li>If we have a set of data with an odd number of data points then the median is the data point in the middle.</li>
<li>If we have a set of data with an even number of data points, then the median is the mean of the two data points in the middle.</li></ol>

<h3>Mode:</h3>
<p>The mode is the most common number in the set of data.</p>

<h1>Calculating the mean stack of a set of FITS images</h1>
<p>Python lists are very flexible, but they are slow for big calculations.</p>

<p>NumPy arrays can store purely numerical data in much less space, and are much simpler and faster for calculations.</p>
<p><a href="mean.py">This code</a> compares performance of calculating mean using Numpy, Statistics modules to manual computation.</p> 
<footer> The above content is reproduced from:
<ol><li><a href="https://www.coursera.org/learn/data-driven-astronomy">Data-driven Astronomy</a></li>
<li><a href="https://www.mathplanet.com/education/pre-algebra/probability-and-statistic/the-mean-the-median-and-the-mode">Math Planet</a></li>

</ol>