"""
Given a trained vocabulary, project it onto images
"""

import pickle
import numpy as np
import scipy.cluster.vq as vq
import local_descriptors.sift as sift
from visual_features.color import color_data_provider
import json


class VocabularyProjector():
    """
    """

    def __init__(self, voc_fname, color_paths, out_fname):

        self.voc = pickle.load(open(voc_fname, 'rb'))
        #print dir(self.voc)
        #print self.voc

        self.color_paths = color_paths
        self.all_img_words = []
        # for p in self.dsift_paths[0:5]:
        #     print p
        # self.voc.nbr_words number of words
        self.out_fname = out_fname

        return

    def test_voc(self):
        print "vocabulary shape", self.voc.voc.shape
        print dir(self.voc)
        pass

    def project_on_img(self, img_desc):
        # input: descriptors for one image,
        # return words
        words, distance = vq.vq(img_desc, self.voc.voc)
        return words

    def get_descriptors(self, dsift_fname):
        #print "get_descriptors", dsift_fname
        descriptors = color_data_provider.read_features_from_file(dsift_fname, delimiter=' ')
        # print descriptors.shape
        # print img_descriptor.shape
        return descriptors

    def project_all(self):
        # project on all images
        # create a list of lists with the words
        for dsift_fname in self.color_paths:
            # print "main", dsift_fname
            img_descriptors = self.get_descriptors(dsift_fname)
            # project on img (get words) and covert to list
            words = self.project_on_img(img_descriptors).tolist()
            self.all_img_words.append(words)
        assert len(self.all_img_words) == len(self.color_paths)


    def write_to_json(self, word_type, split):
        data = {}
        data['word_type'] = word_type
        data['words'] = self.all_img_words
        data['nwords'] = self.voc.nbr_words
        data['split'] = split
        data['ndocs'] = len(self.color_paths)

        with open(self.out_fname, 'wb') as f:
            json.dump(data, f, sort_keys=True)
        return

    def main(self, word_type='dsift', split='train_val'):
        self.project_all()
        self.write_to_json(word_type, split)
        return




if __name__ == '__main__':

    split = 'train_val'
    nwords = 100
    color_space = 'hsv'
    word_type = color_space

    rpath = '../../DATASETS/dress_attributes/'
    dataset_fname = '../../DATASETS/dress_attributes/data/json/dataset_dress_all_%s.json' % split
    color_dp = color_data_provider.ColorDataProvider(n_img_sample=None, dataset_fname=dataset_fname)
    color_paths = color_dp.generate_color_paths(color_space=color_space)



    voc_fname = rpath + 'vis_representation/color_words/%s/nwords%s/dress_color_nwords%s_%s_vocab.pkl' % (color_space, nwords, nwords, color_space)


    out_fname = rpath + 'vis_representation/color_words/%s/nwords%s/color_words_%s_%s_%s.json' % (color_space, nwords, split, nwords, color_space)
    vp = VocabularyProjector(voc_fname, color_paths, out_fname)

    vp.test_voc()


    vp.main(word_type, split)












