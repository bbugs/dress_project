

"""
Here I create the vocabulary

input:  path to file that contains a list of paths for the training .dsift images or another desriptor like color.

output:  pickle file

"""

import pickle


from vocabularies.vocabulary import Vocabulary
from visual_features.dsift.dsift_data_provider import dSiftDataProvider as dsp

import sys
sys.path.append('../../../myComputerVisionLibrary')
sys.path.append('../../../myComputerVisionLibrary/pcv/')
sys.path.append('../../../myComputerVisionLibrary/pcv/vocabularies/')

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as pylab

class VocabularyCreator(object):
    """

    """

    def __init__(self, dsift_batch_fname, verbose=True):
        """
        input:
        dsift_all_imgs_fname: file where all dsift are saved
        """


        self.dsift_batch = ds.get_dsift_batch_imgs(dsift_batch_fname)
        if verbose:
            print "number of descriptors", self.dsift_batch.shape[0]

        return

    def create_vocabulary(self, nbr_words, subsample_rate=10):
        self.voc = Vocabulary('dress_visual_vocabulary_%s' % nbr_words)
        print "Training vocabulary"
        self.voc.train_batch(self.dsift_batch, nbr_words, subsample_rate)

    def save_vocabulary(self, fout_name):
        # saving vocabulary using pickle
        print "Saving vocabulary"
        with open(fout_name, 'wb') as f:
            pickle.dump(self.voc, f)
        print 'vocabulary is: ', self.voc.name, self.voc.nbr_words



if __name__ == '__main__':

    rpath = '../../DATASETS/dress_attributes/dsift_images/'

    split = 'train_val'
    dataset_fname = '../../DATASETS/dress_attributes/data/json/dataset_dress_all_%s.json' % split
    ds = dsp(dataset_fname=dataset_fname)


    size, steps = (90, 40)
    dsift_batch_imgs_fname = rpath + 'dsift_dress_%s_size%s_steps%s.txt' % (split, size, steps)

    # sift_paths_fname = rpath + 'path_error.txt'
    vc = VocabularyCreator(dsift_batch_imgs_fname)

    nwords = [20, 50, 100, 200, 500, 750, 1000]
    for n in nwords:
        vc.create_vocabulary(n, subsample_rate=500)
        fout_name = '../../DATASETS/dress_attributes/dsift_images/dress_dsift_nwords%s_size%s_steps%s_vocab.pkl' % (n, size, steps)
        vc.save_vocabulary(fout_name)

