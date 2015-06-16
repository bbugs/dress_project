
import json
from utils_local import utils_local
import numpy as np


class DataStats(object):

    def __init__(self, item_type='dresses',
                 dataset_fname='dataset/dataset_joint_all.json',
                 img_path_root='../'):
        """
        Load data
        item_type can be dresses,
        """
        self.dataset = utils_local.load_data0(dataset_fname)
        self.item_type = item_type


    def get_num_items(self):
        # eg. dataset['dresses']
        return len(self.dataset[self.item_type])


    def get_files_split(self, split_name='train'):
        split_filepaths = []
        for item in self.dataset[self.item_type]:
            if item['split'] == split_name:
                split_filepaths.append()


class DataProvider(object):
    """

    """

    def __init__(self, dataset_fname='dataset/dataset_dress_all.json'):
        """
        """
        self.dataset = utils_local.load_data0(dataset_fname)

        return

    def get_img_paths(self, verbose=False):
        """
        """
        img_paths = []
        for item in self.dataset['items']:
            folder = item['folder']
            img_path = folder + item['img_filename']
            if verbose:
                print img_path
            img_paths.append(img_path)
        return img_paths

    def get_asins_split(self, target_split='train'):
        asins = []
        for item in self.dataset['items']:
            asin = item['asin']
            split = item['split']
            if split == target_split:
                asins.append(asin)
        return asins

    def get_ids_split(self, target_split='train'):
        ids = []
        for item in self.dataset['items']:
            imgid = item['imgid']
            split = item['split']
            if split == target_split:
                ids.append(imgid)
        return ids

    def get_asins(self):
        asins = []
        for item in self.dataset['items']:
            asin = item['asin']
            asins.append(asin)
        return asins






class CnnProvider(object):
    """

    """
    def __init__(self, dataset_fname='dataset/dataset_dress_title.json',
                 cnn_fname='../DATASETS/dress_attributes/cnn/cnn_dress_test.txt'):
        self.dataset = utils_local.load_data0(dataset_fname)
        self.cnn = np.loadtxt(cnn_fname)
        return




if __name__ == '__main__':
    # d = DataStats()
    #
    # print "number of dresses is: ", d.get_num_dress()

    root_path = '../../DATASETS/dress_attributes/data/json/'
    fname = root_path + 'dataset_berg.json'
    d = DataProvider(dataset_fname=fname)

    print len(d.dataset)

    # d.get_img_paths(verbose=True)  # use this in the command line to write to file

    pass


