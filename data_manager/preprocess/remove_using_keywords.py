"""

Read the data00.json which contains

"""


to_exclude = ['size', 'chart', 'deliver', 'days', 'cm', 'inch', 'inthepicture', 'please', 'plz', 'measurement', 'ship', 'expedite', 'dimension', 'help', 'email', 'call', 'contact', 'question', 'quality', 'problem', 'madein', 'sizing', 'send', 'buyer', 'dryclean', 'weight', 'wash', 'check', 'pls', 'price', 'refer', 'policy', 'return', 'refund', 'onsale', 'question', 'machine', 'visit', 'waisttoknee', '"', 'trademark']

#to_exclude = ['custom', 'buyer', 'Wecreatescomfortable']




from data_manager.preprocess import data_preprocessor as dp
from utils_local import utils_local
import random

data_fname = 'data00.json'
excluded_fname = 'data_manager/preprocess/excluded_phrases.pkl'
included_fname = 'data_manager/preprocess/included_phrases.pkl'

d = dp.SentenceRemover(excluded_fname, included_fname)

data0 = utils_local.load_data0(fname=data_fname)



dresses = data0['dresses']
print "number of dresses ", len(dresses)
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


# only get input from sentences that contain words in to_exclude

for sent in sent_list:
    comp_sent = d.mk_sent_comparable(sent)
    if dp.is_in_set(comp_sent, to_exclude):
        d.get_user_input(sent, verbose=0)
        if counter % 101 == 0:
            print counter
            print "commiting"
            d.commit()
            # reload
            d = dp.SentenceRemover(excluded_fname, included_fname)
    counter += 1



# examples of excluded sentences:

#     if you need it within 2 weeks, please contact our customer service via amazon before placing the order
# in order for your return or exchange to be accepted, we advise you to follow these steps:
# 6.
#  custom-made notes
# please kindly refer to our size chart images.do not refer other size chart!
# please refer to the pacificplex junior formal size chart for this item
# find your hip bones and measure there.
# )
# expected ship date:we will cost about 6-15 days to make for different dresses, if have any problems, please email us.
# buyers must select their size from the size chart.
# each customized item is unique.






