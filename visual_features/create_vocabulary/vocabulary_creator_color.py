

"""
Here I create the vocabulary

input:  path to file that contains a list of paths for the training .dsift images or another desriptor like color_descriptor.

output:  pickle file

"""

import pickle

import sys
sys.path.append('../../../myComputerVisionLibrary')
sys.path.append('../../../myComputerVisionLibrary/pcv/')
sys.path.append('../../../myComputerVisionLibrary/pcv/vocabularies/')

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as pylab

from vocabularies.vocabulary import Vocabulary
from visual_features.color import color_data_provider as color_dp


class VocabularyCreator(object):
    """

    """

    def __init__(self, color_batch_fname, verbose=True):
        """
        input:
        dsift_all_imgs_fname: file where all dsift are saved
        """


        self.color_batch = color_dp.read_features_from_file(color_batch_fname, delimiter=',')
        if verbose:
            print "number of descriptors", self.color_batch.shape[0]

        return

    def create_vocabulary(self, nbr_words, subsample_rate=10):
        self.voc = Vocabulary('dress_visual_vocabulary_%s' % nbr_words)
        print "Training vocabulary"
        self.voc.train_batch(self.color_batch, nbr_words, subsample_rate)

    def save_vocabulary(self, fout_name):
        # saving vocabulary using pickle
        print "Saving vocabulary"
        with open(fout_name, 'wb') as f:
            pickle.dump(self.voc, f)
        print 'vocabulary is: ', self.voc.name, self.voc.nbr_words



if __name__ == '__main__':

    rpath = '../../DATASETS/dress_attributes/vis_representation/color_descriptors/'

    split = 'train_val'
    dataset_fname = '../../DATASETS/dress_attributes/data/json/dataset_dress_all_%s.json' % split
    ds = color_dp.ColorDataProvider(n_img_sample=None, verbose=False, dataset_fname=dataset_fname)


    # Full features
    color_space = 'rgb'
    color_imgs_fname = rpath + 'color_descriptors_%s.%s' % (split, color_space)

    vc = VocabularyCreator(color_imgs_fname)

    nwords = [10, 25, 50, 100]
    for n in nwords:
        vc.create_vocabulary(n, subsample_rate=1)
        fout_name = '../../DATASETS/dress_attributes/vis_representation/color_words/%s/nwords%s/dress_color_nwords%s_%s_vocab.pkl' % (color_space, n, n, color_space)
        vc.save_vocabulary(fout_name)

