"""
Given a trained vocabulary, project it onto images
"""

import pickle
import numpy as np
import scipy.cluster.vq as vq
import local_descriptors.sift as sift
from visual_features.dsift.dsift_data_provider import get_dsift_paths_from_file
import json


class VocabularyProjector():
    """
    """

    def __init__(self, voc_fname, dsift_paths_fname, out_fname):

        self.voc = pickle.load(open(voc_fname, 'rb'))
        #print dir(self.voc)
        #print self.voc

        self.dsift_paths = get_dsift_paths_from_file(dsift_paths_fname)
        self.all_img_words = []
        # for p in self.dsift_paths[0:5]:
        #     print p
        # self.voc.nbr_words number of words
        self.out_fname = out_fname

        return

    def test_voc(self):
        print "vocabulary shape", self.voc.voc.shape
        # print dir(self.voc)
        pass

    def project_on_img(self, img_desc):
        # input: descriptors for one image,
        # return words
        words, distance = vq.vq(img_desc, self.voc.voc)
        return words

    def get_descriptors(self, dsift_fname):
        #print "get_descriptors", dsift_fname
        location, descriptors = sift.read_features_from_file(dsift_fname)
        # print descriptors.shape
        # print img_descriptor.shape
        return descriptors

    def project_all(self):
        # project on all images
        # create a list of lists with the words
        for dsift_fname in self.dsift_paths:
            # print "main", dsift_fname
            img_descriptors = self.get_descriptors(dsift_fname)
            # project on img (get words) and covert to list
            words = self.project_on_img(img_descriptors).tolist()
            self.all_img_words.append(words)
        assert len(self.all_img_words) == len(self.dsift_paths)


    def write_to_json(self, word_type, split):
        data = {}
        data['word_type'] = word_type
        data['words'] = self.all_img_words
        data['nwords'] = self.voc.nbr_words
        data['split'] = split
        data['ndocs'] = len(self.dsift_paths)

        with open(self.out_fname, 'wb') as f:
            json.dump(data, f, sort_keys=True)
        return

    def main(self, word_type='dsift', split='train_val'):
        self.project_all()
        self.write_to_json(word_type, split)
        return




if __name__ == '__main__':
    rpath = '../../DATASETS/dress_attributes/'

    nwords = 750
    size, steps = (90, 40)
    split = 'test'
    word_type = 'dsift'
    subsample = 2  # this subsample is for the k-means algorithm: take every other descriptor. not all
    voc_fname = rpath + 'vis_representation/dsift_words/nwords%s/ss2_paris/dress_dsift_nwords%s_size%s_steps%s_ss%s_vocab.pkl' % (nwords, nwords, size, steps, subsample)


    dsift_paths_fname = rpath + 'data/paths_dsift/paths_dress_dsift_%s_size%s_steps%s.txt' % (split, size, steps)
    #print dsift_paths_fname

    out_fname = rpath + 'vis_representation/dsift_words/nwords%s/ss2_paris/dsift_words_%s_size%s_steps%s_ss%s.json' % (nwords, split, size, steps, subsample)
    vp = VocabularyProjector(voc_fname, dsift_paths_fname, out_fname)
    vp.main(word_type, split)












