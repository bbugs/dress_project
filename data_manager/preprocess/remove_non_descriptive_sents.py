from data_manager.preprocess import data_preprocessor as dp
from utils_local import utils_local
import random

data_fname = 'data0.json'
excluded_fname = 'data_manager/preprocess/excluded_phrases.pkl'
included_fname = 'data_manager/preprocess/included_phrases.pkl'

d = dp.SentenceRemover(excluded_fname, included_fname)

data0 = utils_local.load_data0(fname=data_fname)

n = 1  # number of dresses to evaluate

dresses = data0['dresses'][0:n]
#dresses = random.sample(dresses, n)


for dress in dresses:
    #dress0 = data0['dresses'][i]

    features = dress['features']  # list of strings
    editorial = dress['editorial']  # string
    title = dress['title']  # string

    all_text = [title] + features + [editorial]

    # make a list of all sentences including title, features and editorial review
    processed_sents = utils_local.get_sentences(all_text, verbose=0)

    for sent in processed_sents:
        #print '\n', sent
        d.get_user_input(sent, verbose=1)

    d.commit()



