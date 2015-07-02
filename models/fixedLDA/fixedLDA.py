"""


"""

import numpy as np
from gibbs_output import process_gibbs_output as gibbs_output

class FixedLDA(object):
    """

    """

    def __init__(self, train_wdir, infer_wdir):
        self.phi = np.array([])
        self.theta = np.array([])
        self.K = 0
        self.D = 0
        self.V = 0
        self.Pwd = np.array([])  # V x D
        self.train_wdir = train_wdir
        self.infer_wdir = infer_wdir

        return

    def fit(self):
        # load vmatrix (this is the *_text.v matrix)

        gibbs_train = gibbs_output.GibbsOutputTrain(self.train_wdir)
        vmatrix = gibbs_train.vmatrix


        # make phi
        self.phi = gibbs_output.mk_cond_prob(vmatrix, gibbs_train.beta, gibbs_train.n_samples)
        self.K, self.V = self.phi.shape

        # self.K = 3
        # self.V = 3
        # self.phi = np.random.randint(0, 4, (self.K, self.V))

        return

    def predict(self):
        # load theta (this is the *vis750.theta)
        gibbs_infer = gibbs_output.GibbsOutputInfer(self.infer_wdir)
        self.theta = gibbs_infer.theta
        self.D = gibbs_infer.D
        assert self.K == self.theta.shape[1]
        assert self.theta.shape == (self.D, self.K)

        # self.theta = np.random.randint(0, 4, (self.D, self.K))

        # compute P(w|d) = Sum P(w|z) * P (z|d)  (sum over topics)
        self.Pwd = np.dot(self.theta, self.phi)  # D x V

        predicted_wordids = np.argsort(-self.Pwd, axis=1)   # D x V

        return predicted_wordids

    def write_pred_to_file(self, fname=''):
        # create a file like the .docs, but call it .pred_wordid and .pred_word

        pass

if __name__ == '__main__':


    nominal_alpha = 0.11
    n_vis_words = 750
    # '{0}, {1}, {2}'.format('a', 'b', 'c')

    rpath = '../../DATASETS/geert_output/zappos-preprocessing/flda/textvis{}/'.format(n_vis_words)
    train_wdir = rpath + '/ptm_training_output/alpha_{0}/text/'.format(nominal_alpha, n_vis_words)

    infer_wdir = rpath + '/ptm_inference_output/zappos-preprocessing{1}/alpha_{0}/vis{1}/'.format(nominal_alpha, n_vis_words)

    flda = FixedLDA(train_wdir, infer_wdir)
    flda.fit()
    predicted_wordids = flda.predict()

    print predicted_wordids

    # b = BiLDA()
    #
    # b.fit()
    # b.predict()
    #
    # print b.Pwd  #
    # print np.argsort(-b.Pwd, axis=1)
    # print np.argsort(b.Pwd, axis=0)
