import numpy as np
import matplotlib.pyplot as plt
import imageio
from sklearn.cluster import KMeans
from sklearn.utils import shuffle


# define a function to quantize the image
def quantize(imgName, k):
	# load the image
	img = imageio.imread(imgName)
	# convert to floats
	img = np.array(img, dtype=np.float64) / 255

	width, height, depth = img.shape
	# transform to a 2D numpy array
	imgArray = np.reshape(img, (width * height, depth))

	# use Kmeans
	model = KMeans(n_clusters=k, random_state=0)
	# fit model on a sample of the data
	imgSample = shuffle(imgArray, random_state=0)[:1000]
	kmeans = model.fit(imgSample)

	# get labels for all points
	labels = kmeans.predict(imgArray)
	palette = kmeans.cluster_centers_
	# recreate the image from the labels
	quantizeImage = np.reshape(palette[labels], (width, height, palette.shape[1]))

	return quantizeImage


if __name__ == '__main__':
	# display the quantized images
	quantizeImage1 = quantize("image1.jpg", 5)
	plt.figure(1)
	plt.axis('off')
	plt.imshow(quantizeImage1)
	plt.show()

	quantizeImage2 = quantize("image3.jpg", 10)
	plt.figure(2)
	plt.axis('off')
	plt.imshow(quantizeImage2)
	plt.show()

	quantizeImage3 = quantize("image5.jpg", 11)
	plt.figure(3)
	plt.axis('off')
	plt.imshow(quantizeImage3)
	plt.show()