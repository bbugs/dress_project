"""
Process txt out put from Juan Carlos

Functionality:
INPUT:
root_path = '/DATASETS/dress_attributes/txt_represention/out_title/train_val'


OUTPUT:


"""

from data_manager.data_provider import DataProvider as DP


class TxtProcess(object):
    """

    """

    def __init__(self, txt_feat_fname, dataset_fname):
        """
        fname: juan carlos output file

        """
        f = open(txt_feat_fname)
        self.txt = f.readlines()
        f.close()

        self.n = len(self.txt)  # number of items
        # print "numer items in list from jc", self.n

        self.dp = DP(dataset_fname=dataset_fname)
        self.dataset = self.dp.dataset['items']

        # print "number items dataset", len(self.dataset)
        assert self.n == len(self.dataset)
        assert self.verify_order()

        return

    def verify_order(self):
        """
        Verify that the order between txt_features and dataset is exactly the same
        """
        # asins as ordered in the json dataset
        original_asins = self.dp.get_asins()
        # asins as ordered in the txt_features file (juan carlos)
        txt_asins = self.get_all_asins()
        return original_asins == txt_asins



    def get_all_asins(self):
        """
        Get asins from the txt feature file
        """
        all_asins = []
        for line in self.txt:
            s = line.find(" ")
            asin = line[0:s]
            all_asins.append(asin)
        return all_asins



    def get_asin(self, line):
        s = line.find(' ')  # end of the asin and start of the first feature id
        asin = line[0:s]
        print asin
        # replace ending by space
        line = line.replace('\r\n', ' ')
        # advance line
        advance_line = line[s + 1:]
        return asin, advance_line

    def _get_next_word_id_and_freq(self, line):
        """(str) -> str, str, str
        input, line format: word_id:word_freq, for example:
        0:2 1:1 5:1 17:1 ... '
        output: '0', '2', '1:1 5:1 17:1 ...''
        """
        word_id = None
        word_freq = None
        advanced_line = None
        e = line.find(":")
        if e == -1:
            return word_id, word_freq, advanced_line
        word_id = line[0:e]
        s = line.find(" ", e)
        word_freq = line[e + 1:s]
        advanced_line = line[s + 1:]
        #print advanced_line
        # return word_id, freq, and advanced_line
        return word_id, word_freq, advanced_line

    # def get_all_txt_features(self, verbose=0, save=1):
    #     # word_id, word_freq
    #     for i in range(0, self.n):
    #         line = self.txt[i]
    #         asin, one_line = self.get_asin(line)
    #         print asin
    #         while one_line:
    #             word_id, word_freq, one_line = self._get_next_word_id_and_freq(one_line)
    #             if verbose:
    #                 print word_id, word_freq
    #             # print word_id, word_freq
    #             # txt_vec[i, int(word_id)] = int(word_freq)
    #             if save:
    #                 # f_out.write("%s\t%s\t%s\n" % (i, word_id, word_freq))
    #                 pass
    #     return


    def get_features_split(self, fout_name, target_split='train',
                           include_val=False, verbose=False, save=False):
        if save:
            f = open(fout_name, 'w')
        ids_split = self.dp.get_ids_split(target_split=target_split)

        if include_val:
            ids_val = self.dp.get_ids_split(target_split='val')
            ids_split.extend(ids_val)
            # print ids_split
            # print len(ids_split)

        row = 0
        for id in ids_split:
            line = self.txt[id]
            asin, one_line = self.get_asin(line)
            # print asin
            while one_line:
                word_id, word_freq, one_line = self._get_next_word_id_and_freq(one_line)
                if verbose:
                    print word_id, word_freq
                    if word_freq == '0':
                        print "this asin has empty text", asin, row
                        raw_input()
                if save:
                    f.write("%s\t%s\t%s\n" % (row, word_id, word_freq))
            row += 1
        if save:
            f.close()







if __name__ == '__main__':
    rpath = '../../DATASETS/dress_attributes/'
    txt_feat_fname = rpath + 'txt_represention/out_title/train_val/text_features_freq_5.0.txt'

    dataset_fname = rpath + 'data/json/dataset_dress_title.json'
    t = TxtProcess(txt_feat_fname, dataset_fname)

    # save test features
    fout_name = rpath + 'txt_represention/out_title/train_val/text_features_freq_5.0_test.txt'
    t.get_features_split(fout_name, target_split='test', verbose=True, save=False)

    # save train features
    fout_name = rpath + 'txt_represention/out_title/train_val/text_features_freq_5.0_train.txt'
    t.get_features_split(fout_name, target_split='train', include_val=True, verbose=True, save=False)



    print "done"

