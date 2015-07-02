
# check with Geert:
# Correct files, and correct order for test images
# check that JC .names correspond to the order of the test set

from models.fixedLDA import fixedLDA
from evaluation import metrics
from gibbs_input import process_gibbs_input as gibbs_input


nominal_alpha = 0.35
n_vis_words = 750
# '{0}, {1}, {2}'.format('a', 'b', 'c')

rpath = '../../DATASETS/geert_output/zappos-preprocessing/flda/textvis{}/'.format(n_vis_words)
train_wdir = rpath + '/ptm_training_output/alpha_{0}/text/'.format(nominal_alpha, n_vis_words)

infer_wdir = rpath + '/ptm_inference_output/zappos-preprocessing{1}/alpha_{0}/vis{1}/'.format(nominal_alpha, n_vis_words)

flda = fixedLDA.FixedLDA(train_wdir, infer_wdir)
flda.fit()
predicted_wordids = flda.predict()

# print predicted_wordids
# [[196  11 106 ..., 166  71 177]
# [80 191  95..., 71 166 177]
# [4  51 180..., 150 145  71]
# ...,
# [185  74 184..., 71 166 177]
# [9  57 180..., 150 166 177]
# [175 192  74..., 150 166 177]]



# Compute Precision, Recall and F1

# Load true list
rpath2 = '../../DATASETS/dress_attributes/txt_represention/out_all/zappos/'
dot_docs_fname = rpath2 + 'text_features_test_zappos_0.0.docs'
dot_docs = gibbs_input.DotDocs(dot_docs_fname)
dot_names_fname = rpath2 + 'file_names_test_zappos_0.0.names'
dot_names = gibbs_input.DotNames(dot_names_fname)
dot_words_fname = rpath2 + 'filtered_vocabulary_zappos_0.0.words'
dot_words = gibbs_input.DotWordsFile(dot_words_fname)
dot_wc_fname = rpath2 + 'vocabulary_counts_test_zappos_0.0.wc'
dot_wc = gibbs_input.DotWCFile(dot_wc_fname)


true_list = dot_docs.wordid_list_all_docs
predicted_list = predicted_wordids

assert len(true_list) == len(predicted_list)

k = 5
avg_prec = metrics.avg_metric_at_k(metrics.precision_at_k, true_list, predicted_list, k)
avg_recall = metrics.avg_metric_at_k(metrics.recall_at_k, true_list, predicted_list, k)
avg_f1 = metrics.avg_metric_at_k(metrics.f1_score, true_list, predicted_list, k)

print "avg_prec", avg_prec
print "avg_recall", avg_recall
print "avg_f1", avg_f1


# visualize predictions

