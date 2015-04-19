from data_manager.preprocess import data_preprocessor as dp
from utils_local import utils_local
import random

data_fname = 'data0.json'
excluded_fname = 'data_manager/preprocess/excluded_phrases.pkl'
included_fname = 'data_manager/preprocess/included_phrases.pkl'

d = dp.SentenceRemover(excluded_fname, included_fname)

data0 = utils_local.load_data0(fname=data_fname)



dresses = data0['dresses']
#dresses = random.sample(dresses, n)

# make a list of tuples
sent_list = []
for dress in dresses:
    imgid = dress['imgid']
    adin = dress['asin']
    folder = dress['folder']
    title = dress['title']
    url = dress['url']
    brand = dress['brand']
    features = dress['features']
    editorial = dress['editorial']

    all_text = [title] + features + [editorial]

    processed_sents = utils_local.get_sentences(all_text, verbose=0)

    for sent in processed_sents:
        sent_list.append(sent)

print "sorting ..."
sent_list.sort()

#print sent_list


# number of dresses to evaluate
batch_size = 10
counter = 0




for sent in sent_list:
    #print '\n', sent
    d.get_user_input(sent, verbose=0)
    if counter % 101 == 0:
        print counter
        print "commiting"
        d.commit()
        d = dp.SentenceRemover(excluded_fname, included_fname)
    counter += 1









#
# for dress in dresses:
#     #dress0 = data0['dresses'][i]
#
#     features = dress['features']  # list of strings
#     editorial = dress['editorial']  # string
#     title = dress['title']  # string
#
#     all_text = [title] + features + [editorial]
#
#     # make a list of all sentences including title, features and editorial review
#     processed_sents = utils_local.get_sentences(all_text, verbose=0)
#
#     for sent in processed_sents:
#         #print '\n', sent
#         d.get_user_input(sent, verbose=1)
#
#     d.commit()



