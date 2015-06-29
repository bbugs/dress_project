"""
dsift features have already been computed with dsift_main.py

This is a small script to generate the paths to the dsift files

Here we generate the paths of the training set

fout_name = 'paths_dress_dsift_train_val.txt
fout_name = 'paths_dress_dsift_test.txt



"""

# import os
# print os.getcwd()



from data_manager.data_provider import DataProvider
import random
import numpy as np
from local_descriptors import sift

class dSiftDataProvider(object):
    """

    """

    def __init__(self, n_img_sample=None, verbose=False,
                 dataset_fname='../../DATASETS/dress_attributes/data/json/dataset_dress_all_train_val.json'):

        """
        n_img_sample:  number of random images to use.  If none, use all images

        """


        d = DataProvider(dataset_fname=dataset_fname)
        self.img_paths = d.get_img_paths()
        self.dsift_paths = []  # initialize dsift paths

        if n_img_sample:
            self.img_paths = random.sample(self.img_paths, n_img_sample)

        if verbose:
            print self.img_paths[0:20]

        return

    def generate_dsfit_paths(self, prefix='../../DATASETS/', size=90, steps=40, verbose=False):
        for path in self.img_paths:
            dsift_path = path.replace('data/images',
                                      '/vis_representation/dsift_images/size%s_steps%s' % (size, steps))
            dsift_path = dsift_path.replace('.jpg', '.dsift')
            dsift_path = prefix + dsift_path
            self.dsift_paths.append(dsift_path)
            if verbose:
                print dsift_path


    def write_dsift_to_file(self, out_fname=''):
        """
        Write ALL dsfit descriptors to one single file
        """

        f = open(out_fname, 'w')
        for path in self.dsift_paths:
            print path
            locations, descriptors = sift.read_features_from_file(path, desc_dim=132)

            # check that it's safe to cast ot uint16
            check = descriptors[descriptors > 2 ** 16]
            if check != 0:
                print path
                print descriptors
                print descriptors[descriptors > 2 ** 16]
                raw_input("uint16 is not enough")
            descriptors = descriptors.astype(np.uint16)

            savetxt_compact(f, descriptors) # pass file handle to function
            # print descriptors.shape
            # print type(descriptors)

        f.close()

    def get_dsift_batch_imgs(self, fname):
        # read all dsfit descriptors from a single file
        print "loading dsift descriptors"
        return np.loadtxt(fname, delimiter=',', dtype=np.uint16)



def savetxt_compact(fh, x, fmt="%.6g", delimiter=','):
    """
    method may be used to save a numpy array compactly.
    I used for saving the cnn matrices
    http://stackoverflow.com/questions/24691755/how-to-format-in-numpy-savetxt-such-that-zeros-are-saved-only-as-0
    """

    for row in x:
        line = delimiter.join("0" if value == 0 else fmt % value for value in row)
        fh.write(line + '\n')


def get_dsift_paths_from_file(fname='../../DATASETS/dress_attributes/data/paths_dsift/paths_dress_dsift_train_val_size90_steps40.txt',
                              prefix='../../DATASETS/'):
    # just retrieve the paths from a previously computed file
    with open(fname, 'r') as f:
        paths = [prefix + l.replace("\n", '') for l in f.readlines()]
    return paths




if __name__ == '__main__':

    split = 'train_val'
    dataset_fname = '../../DATASETS/dress_attributes/data/json/dataset_dress_all_%s.json' % split
    ds = dSiftDataProvider(n_img_sample=None, dataset_fname=dataset_fname)
    size, steps = (90, 40)
    ds.generate_dsfit_paths(size=size, steps=steps)
    dsift_all_fname = '../../DATASETS/dress_attributes/dsift_images/dsift_dress_%s_size%s_steps%s.txt' % (split, size, steps)
    ds.write_dsift_to_file(out_fname=dsift_all_fname)

    #dsift_all = ds.get_dsift_batch_imgs(fname='test_dsift_all.txt')

    print "here"








#print len(dsift_paths)








