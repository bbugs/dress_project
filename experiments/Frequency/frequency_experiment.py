
from models.frequency import frequency_vote
from gibbs_input import process_gibbs_input as gibbs_input
from evaluation import metrics


rpath2 = '../../DATASETS/dress_attributes/txt_represention/out_all/zappos/'
dot_docs_fname = rpath2 + 'text_features_test_zappos_0.0.docs'
dot_docs = gibbs_input.DotDocs(dot_docs_fname)
dot_names_fname = rpath2 + 'file_names_test_zappos_0.0.names'
# dot_names = gibbs_input.DotNames(dot_names_fname)
dot_words_fname = rpath2 + 'filtered_vocabulary_zappos_0.0.words'
# dot_words = gibbs_input.DotWordsFile(dot_words_fname)
dot_wc_fname = rpath2 + 'vocabulary_counts_test_zappos_0.0.wc'
# dot_wc = gibbs_input.DotWCFile(dot_wc_fname)


freq_vote = frequency_vote.FrequecyVote(dot_docs_fname,
                                        dot_names_fname,
                                        dot_words_fname,
                                        dot_wc_fname)

freq_vote.fit()
predicted_list = freq_vote.predict(n=None)

true_list = dot_docs.wordid_list_all_docs


print predicted_list

assert len(true_list) == len(predicted_list)

k = 10
avg_prec = metrics.avg_metric_at_k(metrics.precision_at_k, true_list, predicted_list, k)
avg_recall = metrics.avg_metric_at_k(metrics.recall_at_k, true_list, predicted_list, k)
avg_f1 = metrics.avg_metric_at_k(metrics.f1_score, true_list, predicted_list, k)

print "avg_prec", avg_prec
print "avg_recall", avg_recall
print "avg_f1", avg_f1

