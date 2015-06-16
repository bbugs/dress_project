"""
Process previously computed cnn
"""

from data_manager.data_provider import DataProvider as DP

import numpy as np

class CnnProvider(object):
    """

    """
    def __init__(self, cnn_feat_fname, dataset_fname):
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
        assert self.cnn.shape[0] == 4096  # num dimensions from cnn 7th layer


        return


    def get_features_split(self, fout_name, target_split='train',
                           include_val=False, verbose=False, save=False):

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
            cnn_split[:, col] = self.cnn[:, id]
            col += 1

        if save:
            np.savetxt(open(fout_name, 'w'), cnn_split, delimiter=',')





if __name__ == '__main__':
    rpath = '../../DATASETS/dress_attributes/'
    cnn_feat_fname = rpath + 'cnn/cnn_dress.txt'

    dataset_fname = rpath + 'data/json/dataset_dress_title.json'
    c = CnnProvider(cnn_feat_fname, dataset_fname)

    # save test features
    fout_name = rpath + 'cnn/cnn_dress_test.txt'
    print "getting test features"
    c.get_features_split(fout_name, target_split='test', verbose=True, save=True)

    # save train features
    fout_name = rpath + 'cnn/cnn_dress_train.txt'
    print "getting train features"
    c.get_features_split(fout_name, target_split='train', include_val=True, verbose=True, save=True)


    #
    # # save train features
    # fout_name = rpath + 'txt_represention/out_title/train_val/text_features_freq_5.0_train.txt'
    # t.get_features_split(fout_name, target_split='train', include_val=True, verbose=True, save=False)



    print "done"