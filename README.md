# CS6375ML-Color-Quantization
Unsupervised learning to reduce the number of color points in an image

The package used and installation instructions
==============================================
We use some image processing and machine learning libraries to implement color quantization by using k-means algorithm.

Their names and installation instructions are as follows:
1. numpy
	
	Open the terminal and input: pip3 install numpy
2. matplotlib
	
	Open the terminal and input: pip3 install matplotlib
3. imageio
	
	Open the terminal and input: pip3 install imageio
4. sklearn
	
	Open the terminal and input: pip3 install sklearn

Development environment
=======================
Python 3.7.2

Algorithm and compile
=====================
We use k-means algorithm to quantize the images. Firstly using numpy to convert the original image to 2D array and using sklearn to fit k-means model on a small sub-sample of data. Then predict all points to get labels to recreate the image form them. Finally, using matplotlib to display the quantized images with different values of k.
