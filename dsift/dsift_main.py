"""
images live in
/Users/susanaparis/Documents/Belgium/PARIS/Amazon/scripts/dresses/data/images
"""

import setup
from utils_local import utils_local
from pcv.local_descriptors import dsift, sift
import numpy as np
from PIL import Image
import pylab as pl
import os

#
# import sys
# sys.path.append('/Users/susanaparis/Documents/Belgium/myComputerVisionLibrary/pcv/local_descriptors/')

def compute_dsift(data_fname, img_rpath, dsift_rpath, pic_show=False):
    """
    Compute dense sift features for a all the images in the data_fname
    data_fname points to a json file where

    """
    data0 = utils_local.load_data0(fname=data_fname)

    for dress in data0['dresses']:
        folder = dress['folder']

        asin = dress['asin']
        #print asin

        src_file = img_rpath + folder + '/' + asin + '.jpg'

        dsift_folder = dsift_rpath + folder + '/'
        dsift_folder = dsift_folder.replace(" ", "")  # to avoid spaces when ./sift is called from python
        dsift_folder = dsift_folder.replace("&", "")   # to avoid the symbol & when ./sift is called from python on the terminal

        if not os.path.isdir(dsift_folder):
            os.mkdir(dsift_folder)

        dst_file = dsift_folder + asin + '.dsift'

        dsift.process_image_dsift(src_file, dst_file, size=40, steps=20, force_orientation=True)

        if pic_show:
            l, d = sift.read_features_from_file(dst_file)  # feature locations l, and descriptors d
            # l.shape  (273, 4)
            # d.shape  (273, 128)

            im = np.array(Image.open(src_file))
            sift.plot_features(im, l, True)
            pl.show()


if __name__ == '__main__':

    data_fname = 'data0.json'
    img_rpath = '/Users/susanaparis/Documents/Belgium/PARIS/Amazon/scripts/dresses/data/images/'
    dsift_rpath = '/Users/susanaparis/Documents/Belgium/PARIS/Amazon/scripts/dresses/data/dsift_images/'

    dsift_size = 40
    dsift_steps = 20

    dsift_rpath = dsift_rpath + 'size' + str(dsift_size) + '_steps' + str(dsift_steps) + '/'
    if not os.path.isdir(dsift_rpath):
        os.mkdir(dsift_rpath)

    compute_dsift(data_fname, img_rpath, dsift_rpath, pic_show=False)


    # verify the number or files in img_rpath and dsift_rpath
    folders1 = [f for f in os.listdir(img_rpath) if not f.startswith(".")]
    folders2 = [f for f in os.listdir(dsift_rpath) if not f.startswith(".")]

    for i in range(len(folders1)):
        p1 = img_rpath + folders1[i]
        p2 = dsift_rpath + folders2[i]
        v = utils_local.verify_nfiles(p1, p2)
        if not v:
            print "not equal number of files"
            print p1, p2
        assert v


