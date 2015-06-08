
import json
from utils_local import utils_local


class DataStats(object):

    def __init__(self, item_type='dresses',
                 dataset_fname='dataset/dataset.json',
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







if __name__ == '__main__':
    d = DataStats()

    print "number of dresses is: ", d.get_num_dress()
