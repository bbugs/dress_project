"""


"""

import numpy as np
from gibbs_input import process_gibbs_input as gibbs_input

class FrequecyVote(object):
    """
    Frequency Vote predicts the most common words from the
    training set for every single test image
    """

    def __init__(self, dot_docs_fname, dot_names_fname,
                 dot_words_fname, dot_wc_fname):

        self.dot_docs = gibbs_input.DotDocs(dot_docs_fname)
        self.dot_names = gibbs_input.DotNames(dot_names_fname)
        self.dot_words = gibbs_input.DotWordsFile(dot_words_fname)
        self.dot_wc = gibbs_input.DotWCFile(dot_wc_fname)
        self.ordered_word_counts = []


        return

    def fit(self):
        # load word counts using the class DotWCFile
        self.ordered_word_counts = self.dot_wc.ordered_word_counts
        pass

    def predict(self, n=20):
        """
        n can be an integer or None
        Return a D x V matrix that contains the word ids of predicted words
        """

        if n:
            self.ordered_word_counts = self.ordered_word_counts[0:n]

        # words_file.word2id
        top_word_ids = []
        for count, word in self.ordered_word_counts:
            wordid = self.dot_words.word2id[word]
            top_word_ids.append(wordid)

        # Generate a matrix D x V
        predicted_wordids_slice = np.asarray(top_word_ids)


        self.dot_names.D = 1000  # TODO remove this after JC fixes .names files
        predicted_wordids = np.tile(predicted_wordids_slice, (self.dot_names.D, 1))  # repeat D times

        return predicted_wordids

    def write_pred_to_file(self, fname=''):
        # create a file like the .docs, but call it .pred_wordid and .pred_word

        pass

if __name__ == '__main__':

    pass
    # b = FrequecyVote()
    #
    # b.fit()
    # b.predict()
    #
    # print b.Pwd  #
    # print np.argsort(-b.Pwd, axis=1)
    # # print np.argsort(b.Pwd, axis=0)
