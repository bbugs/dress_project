

"""
Here I create the vocabulary

input:  path to file that contains a list of paths for the training .dsift images or another desriptor like color.

output:  pickle file

"""

import pickle

from vocabularies.vocabulary import Vocabulary
from setup import *

class VocabularyCreator(object):
    """

    """

    def __init__(self, sift_paths_fname,
                 sample=False, img_sample=100,
                 prefix='../../DATASETS/'):
        """
        input:
        sift_paths_fname: file with paths to sift or dsfit features
        sample indicates whether you want to consider only a sample of the data
        img_sample indicates the number of images that you want to consider
        """

        f = open(sift_paths_fname, 'r')
        self.sift_paths = [prefix + p.replace("\n", "") for p in f.readlines()]
        f.close()

        if sample:
            self.sift_paths = self.sift_paths[0:img_sample]

        return

    def create_vocabulary(self, nbr_words, subsample_rate=10):
        self.voc = Vocabulary('dress_visual_vocabulary_%s' % nbr_words)
        print "Training vocabulary"
        self.voc.train(self.sift_paths, nbr_words, subsample_rate)  # featlist contains the path to the .sift files.

    def save_vocabulary(self, fout_name):
        # saving vocabulary using pickle
        print "Saving vocabulary"
        with open(fout_name, 'wb') as f:
            pickle.dump(self.voc, f)
        print 'vocabulary is: ', self.voc.name, self.voc.nbr_words



if __name__ == '__main__':

    rpath = '../../DATASETS/dress_attributes/data/paths/'
    sift_paths_fname = rpath + 'paths_dress_dsift_train_val.txt'
    # sift_paths_fname = rpath + 'path_error.txt'
    vc = VocabularyCreator(sift_paths_fname, sample=False, img_sample=100)
    n_words = 5
    vc.create_vocabulary(n_words, subsample_rate=10)
    fout_name = '../../DATASETS/dress_attributes/dsift_images/dress_dsift_nwords_' + str(n_words) + '_vocab.pkl'
    vc.save_vocabulary(fout_name)

