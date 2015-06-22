"""
Process previously computed cnn
"""

from data_manager.data_provider import DataProvider as DP

import numpy as np
from utils_local import utils_local

class CnnProvider(object):
    """

    """
    def __init__(self, cnn_feat_fname, dataset_fname, target_layer='fc7'):
        """
        Get cnn features
        """
        self.cnn = np.loadtxt(cnn_feat_fname, delimiter=',')
        print type(self.cnn)

        self.dp = DP(dataset_fname=dataset_fname)
        self.dataset = self.dp.dataset['items']

        self.m = self.cnn.shape[0]  # 4096
        self.n = self.cnn.shape[1]


        # print "number items dataset", len(self.dataset)
        assert self.n == len(self.dataset)
        if target_layer == 'fc7':
            assert self.cnn.shape[0] == 4096  # num dimensions from cnn 7th layer

        if target_layer == 'conv5':
            assert self.cnn.shape[0] == 256 * 13 * 13  # num dimensions from conv5 layer

        return


    def get_features_split(self, fout_name, target_split='train',
                           include_val=False, verbose=False,
                           transpose=True, save=False):

        ids_split = self.dp.get_ids_split(target_split=target_split)

        if include_val:
            ids_val = self.dp.get_ids_split(target_split='val')
            ids_split.extend(ids_val)
            # print ids_split
            # print len(ids_split)

        cnn_split = np.zeros((self.m, len(ids_split)))
        col = 0
        for id in ids_split:
            if verbose:
                print target_split, id
            img_cnn = self.cnn[:, id]
            # substitue NaNs with zeros
            where_are_NaNs = np.isnan(img_cnn)
            img_cnn[where_are_NaNs] = 0

            cnn_split[:, col] = img_cnn


            col += 1

        if transpose:
            cnn_split = np.transpose(cnn_split)

        if save:
            print "saving array"
            utils_local.savetxt_compact(fout_name, cnn_split)
            #np.savetxt(open(fout_name, 'w'), cnn_split, delimiter=',')
            print "done saving array"




if __name__ == '__main__':
    rpath = '../../DATASETS/dress_attributes/'
    target_layer = 'conv5'
    cnn_feat_fname = rpath + 'cnn/cnn_dress_' + target_layer + '.txt'

    dataset_fname = rpath + 'data/json/dataset_dress_title.json'
    c = CnnProvider(cnn_feat_fname, dataset_fname, target_layer=target_layer)

    # save test features
    fout_name = rpath + 'cnn/cnn_dress_' + target_layer + '_test.txt'
    print "getting test features"
    c.get_features_split(fout_name, target_split='test', verbose=True, save=True)

    # save train features
    fout_name = rpath + 'cnn/cnn_dress_' + target_layer + '_train.txt'
    print "getting train features"
    c.get_features_split(fout_name, target_split='train', include_val=True, verbose=True, save=True)


    #
    # # save train features
    # fout_name = rpath + 'txt_represention/out_title/train_val/text_features_freq_5.0_train.txt'
    # t.get_features_split(fout_name, target_split='train', include_val=True, verbose=True, save=False)



    print "done"
