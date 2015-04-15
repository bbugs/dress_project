"""
images live in
/Users/susanaparis/Documents/Belgium/PARIS/Amazon/scripts/dresses/data/images
"""


from utils_local import utils_local
from pcv.local_descriptors import dsift, sift
import numpy as np
from PIL import Image
import pylab as pl
import os

data0 = utils_local.load_data0(fname='../data0.json')
img_rpath = '/Users/susanaparis/Documents/Belgium/PARIS/Amazon/scripts/dresses/data/images/'


for dress in data0['dresses']:
    folder = dress['folder']
    asin = dress['asin']
    #print asin

    src_file = img_rpath + folder + '/' + asin + '.jpg'

    dsift_folder = '/Users/susanaparis/Documents/Belgium/PARIS/Amazon/scripts/dresses/data/dsift_images/' + folder + '/'
    dsift_folder = dsift_folder.replace(" ", "_")  # to avoid spaces when ./sift is called from python

    if not os.path.isdir(dsift_folder):
        os.mkdir(dsift_folder)

    dst_file = dsift_folder + asin + '.dsift'

    dsift.process_image_dsift(src_file, dst_file, size=40, steps=20, force_orientation=True)

    if True:
        l, d = sift.read_features_from_file(dst_file)  # feature locations l, and descriptors d
        # l.shape  (273, 4)
        # d.shape  (273, 128)

        im = np.array(Image.open(src_file))
        sift.plot_features(im, l, True)
        pl.show()
