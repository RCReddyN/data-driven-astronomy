<h1>Radio Data Analysis</h1>
<h2>Introduction</h2>

<p>The scientific capabilites of the Arecibo and Green Bank instruments must be accessible to all astronomers without requiring detailed knowledge of the electronics, software, and observing techniques.</p> 

<p>So, observatories supply standard setups and data reduction software and procedures for some of the most commonly used modes. However, there are many cases where observers must or  prefer their own data analysis software.</p>

<p>Astronomers can choose from specific packages (CLASS, AIPS, AIPS++, IRAF, etc.), scripting languages (Python, glish, Perl, Tcl, Java, etc.)  and major toolkits (PGPLOT, Tk, cfitsio, scientific libraries, etc.) without much concern about reinventing wheels in the process of creating your own data analysis environment.</p>

<p>The science and the observing techniques an astronomer does should not be confined by these packages. Observational Astronomy depends on innovation and improvements to existing techniques. If one chooses to assemble his/her own data analysis environment from a range of high and low level pieces, they should keep in mind that they are not trying to rewrite a complete analysis package. </p>

<p>Writing software routines for specific scientific objectives is mush more limited objective. If any of the inventions are of use to others, they can be cleaned up, documented, and published on the web.</p>

<h2>Data paths from the Telescope</h2>

<p>Source: Green Bank Telescope</p>
<p>Keep in mind that raw data is available without great effort.</p>

<img src="./images/gbt_if_dfa.png">

<p>Data formats written by the signal processing back-ends depend on how widely accessible the data are intended to be. It is generally easier and sometimes significantly faster to write data in binary format close to the native format produced by the electronics. However, these data require detailed external documentation and specialized software routines to read them.</p>

<p>If the data are used by only one or two groups, a binary format is usually simple and efficient.</p> 

<p>Data that are intended to be read by more than one or two programmers are generally written in standard, self documenting format. In the astronomical world, this is Flexible Image Transport System (FITS) or more specifically, FITS Binary Table Format.</p>

<p>The original FITS was pure text data so you could read the whole file with a text reader or any program that reads ASCII text. Large data sets require too much storage space or processing power to convert from ASCII to native binary format. So, a hybrid ASCII/binary format was developed. ASCII headers contain self documentation. The data arrays are recorded as binary integers or floating point numbers. This is the most common FITS format we see at most observatories.</p> 

<p>All information from the observations like antenna position, bandwidth settings, cal state, etc is stored with signal processor output so that all the information required to interpret data is available without a manual log.</p> 

<p>In an automated telescope system, there are too many parameters to keep track of manually.</p>

<p>At GBT, every subsystem writes its own FITS file for every observing scan. These are stored in GBT data directory under the project ID.</p>

<p>The project AGBT02A_069 is for a public domain survey.</p>

<p>Collation of the information from all the GBT subsystems is one of the functions of the "Filler" in Figure 1.</p> 

<h2>FITS File Contents</h2>

<p>There are a number of FITS file readers, both stand-alone and as functions in different programming languages.</p> 

<p>Here's <a href ="https://www.cv.nrao.edu/~rfisher/DIYanalysis/Ccode/list_fits.c">an example C program</a> to print ASCII header lines while skipping the binary tables:</p>

<h3>FITS rules for writing the above program:</h3>
<ol>
<li>All header lines are eighty characters long.</li>
<li>Headers and Binary Table Lengths are integer multiples of 2880 bytes, which are padded at the ends with blank <li>lines to make up the length.</li>
<li>The last blank ASCII header line contains only the END keyword.</li>
<li>The dimensions of the useful binary table is specified by the values of the keywords NAXIS, and NAXISn.</li>
<li>FITS binary tables are organized in Header Data Units (HDUs) with an ASCII header and a binary tablle in each HDU.</li>
<li>The binary table may be ommited in an HDU, as is always the case in the first HDU.</li></ol>

<p>Try "fv" utility for looking at FITS files. Type fv at the UNIX prompt followed by the path name of your FITS file. By comparing the header keywords with the table organization in 'fv' you can get a pretty good idea how the table format is specified by the TTYPEn, TFORMn, and TUNITn keywords.</p>

<h4>For gory details on FITS Format:</h4>
<ul><li><a href= "https://heasarc.gsfc.nasa.gov/docs/heasarc/fits.html"> FITS Data Format</a></li>
<li><a href= "https://fits.gsfc.nasa.gov/fits_home.html">The Fits Support Office</a></li></ul></p>

<h2>Back-End and Telescope Data Notes</h2>
<p>The basic data from a radio telescope is simply signal intensity as a function of time, frequency, antenna position, and possibly one or more hardware states, such as the position of a beam switch</p>

<p>The method for synchronizing the intensity variables vary from one telescope to the other. On the GBT the antenna position, local oscillator frequency, and signal intensities are sampled asynchronously with time tags so an averaging or interpolation operation is required to determine the antenna position and observing frequency at the mean time of each intensity sample.</p>

<p>Hardware states are much more directly synchronized with intensity accumulation in real time with common switching signals that send all data from a given combination of switch states to the same accumulator and data from different combinations to different accumulators. For example, if a spectrometer setup is to frequency switch at a two-second period and turn the calibration signal on and off at a synchronous one-second period, you will get four spectra from each IF channel corresponding to the state combinations (cal~off, frequency~1), (cal~on, frequency~1), (cal~off, frequency~2), and (cal~on, frequency~2). The state combinations are found in the STATE variables of the STATE header data unit of the back-end and LO FITS files. These correspond to the phase or state index in the DATA arrays.</p>

<p>The intensity measurements can be simple total power integrations from the full IF passband from the digital continuum receiver (DCR), accumulated spectra from the spectral processor, accumulated autocorrelation functions (ACF) from the spectrometer, or a high-speed stream of IF signal voltage samples from a VLBI, pulsar, or other direct-sampling device. The DCR and spectral processor outputs may be used more or less without further processing to derive system temperatures from the cal-on/cal-off measurements and spectral line or continuum intensities from on-source/off-source values.</p>

<p>The output of the autocorrelation spectrometer requires three signal processing operations to turn the recorded ACF's into spectra: quantization corrections (often called van Vleck corrections), linearization, and Fourier Transform. At Arecibo these three operations are performed in real time so that the autocorrelation spectrometer output is corrected spectra that you can use directly. The GBT design choice was to record the raw autocorrelation data to retain maximum flexibility.</p>

<p>At first glance the quantization and linearization corrections appear to be shrouded in the esotericism of integrals of complicated error functions, but the basic ideas are pretty simple. To save on hardware cost and maximize signal processing speed an autocorrelator generally samples the IF voltage with only 2, 3, or 9 levels of quantization. Most of the spectral and intensity information of noise-dominated signals is retained, but distortions are introduced that must be corrected to recover the true autocorrelation and spectrum values.</p>

<p>These corrections are derived by starting with the assumption that the sampler input voltage has a normal probability distribution of amplitudes. From this we can compute the response of a given sampler to a range of known signal autocorrelation values over a range of sampler input levels. We can then fit an analytic function to a chosen accuracy to this two-dimensional array of true-to-measured correlation value ratios as a function of sampler input level and measured correlation values. This function is then the quantization correction function. The same is done to get the ratio of true sampler input power to measured output power as a function of measured output power to get the linearization function. These computations are straightforward but a bit tedious to program so the coefficients can be computed once and packaged as a module to be accessed by a higher level data analysis language, as has been done for the GBT spectrometer. One point to make here is that the quantization and linearization corrections are not necessarily a compute-and-forget black box. The assumptions of normal voltage distribution and symmetric, evenly spaced sampler levels are different from reality at some level. This might be an area for further improvement by someone working closely with the data.</p>

<p>Transforming the ACF to a power spectrum is pretty straightforward with any of a number of FFT tools. The main trick is to create a real, symmetric data array of twice the length of the measured ACF by reflecting the ACF around its zero-delay data value.</p>

<h2>Binary Data Formats</h2>
<p>If you are reading FITS data files, you don't have to worry much about the details of how the binary data is stored on disk. This is generally taken care of by the FITS reader code. However, if your data is a stream of IF voltage samples or in a format defined by a low-level language data structure, the details are important.</p>

<p>Binary data comes in three flavors: character, integer, and floating point. A character is always 8 bits (1 byte) long, where the translation from numeric value to alphabetic letter is standardized in the ASCII code table.</p>

<p>Integers can be 8, 16, 32, and sometimes 64 bits long (1, 2, 4, or 8 bytes), and they can be signed or unsigned. The distinction between signed and unsigned determines the interpreted data range. A 16-bit, unsigned integer can store values from 0 to 65535 while a signed, 16-bit number runs from -32768 to +32767. The binary bits in the unsigned value of 65535 are the same as in the signed value of -1.</p>

<p>Floating point binary numbers are almost always 32 bits (single precision) or 64 bits (double precision) long (4 or 8 bytes). Very very rarely you may see 16- or 128-bit floating point numbers, but these are not generally supported by most computing languages. The allocation of bits between exponent and mantissa in the data word is specified by the IEEE Standard 754.</p>

<p>To add variety to life, there is no standard on the order in which computers store the bytes of a multi-byte integer or floating point number on disk. Intel processors store the least significant byte first (called "little endian"), and Sun computers and the Motorola processor store the most significant byte first ("big endian"). (See Gulliver's Travels by Jonathan Swift.) If you read data written by a Sun computer with an Intel machine or vice versa, you will see data garbage unless your reading program is aware of the problem. You can reverse the byte swap by treating all bytes as characters and swapping the order in each 2-, 4-, or 8-byte word.</p>

<h2>Processing Direct IF Voltage Samples</h2>
<p>The most basic form of data collection is to directly sample band-limited IF output voltages with an analog to digital (A/D) converter. If the data sampling rate is twice the IF bandwidth, all information is retained. You are then free to process and reprocess your data any way you like on a general-purpose computer - Fourier transform spectroscopy, autocorrelation functions, pulse period and dispersion searches, interference excision, etc. Since there is no data rate reduction in this type of data collection it uses a prodigious amount of disk space and requires considerable post-processing resources, but the rapid growth of processing power and disk sizes has moved this option into astronomically interesting bandwidths and integration times. Some pulsar searches and planetary radar are now done this way. One terabyte of disk space, costing about $5000, can store about 14 hours of directly-sampled data from a 10 MHz bandwidth using 8-bit samples.</p>

<p><b>The content is mostly reproduced from <a href = "https://www.cv.nrao.edu/~rfisher/DIYanalysis/diy_analysis.html"> Do-It-Yourself Data Analysis <b></a></p>

