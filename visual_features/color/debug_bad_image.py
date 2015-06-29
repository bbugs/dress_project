from PIL import Image
import numpy as np
import pylab as pl

# img_path = '../../DATASETS/dress_attributes/data/images/BridesmaidDresses2/B00UYRHAPM.jpg'
img_path = '../../DATASETS/dress_attributes/data/images/Dresses2/B00PW0C7YA.jpg'

img = np.array(Image.open(img_path))

print img
print type(img)
print "shape ", img.shape
print img.dtype

pl.figure()
pl.imshow(img)
pl.show()

print "I'm here"
