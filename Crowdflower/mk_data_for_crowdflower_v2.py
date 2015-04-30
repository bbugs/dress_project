
import nltk
import nltk.data
from utils_local import utils_local
import csv


import zTextProcessing as zt

from data_manager.preprocess import data_preprocessor as dp

# load excluded_sentences:
excluded_fname = 'data_manager/preprocess/excluded_phrases.pkl'
included_fname = 'data_manager/preprocess/included_phrases.pkl'

d = dp.SentenceRemover(excluded_fname, included_fname)
excluded_sentences = d.excluded_sentences

data0 = utils_local.load_data0(fname='data0.json')
#i = 239 #1224  #357

fname = 'clean_data_test.csv'
f = open(fname, 'wb')
writer = csv.writer(f)


rdir = 'http://people.cs.kuleuven.be/~susana.zoghbi/dress_imgs/'
info = ("asin", "imgid", "folder", "img_dir", "brand", "descrptive", "sentences")

# for i in info:
#     f.write(i)
#     f.write(";")
#
# f.write('\n')

writer.writerow(info)

for dress in data0['dresses']:
    #dress0 = data0['dresses'][i]

    features = dress['features']  # list of strings
    editorial = dress['editorial']  # string
    title = dress['title']  # string
    brand = dress['brand']
    asin = dress['asin']
    imgid = dress['imgid']
    folder = dress['folder']

    img_dir = rdir + folder + '/' + asin + '.jpg'

    all_text = [title] + features + [editorial]

    clean_sents = utils_local.get_sentences(all_text)
    # convert sentences to string separated by " \n"
    #str_sents = "\%".join(clean_sents).encode('utf-8')
    #str_sents = "\%".join(clean_sents)
    #print str_sents

    descriptive = " "  # this is just to leave an empty column to annotate myself the comments
    for sentence in clean_sents:
        comp_sent = d.mk_sent_comparable(sentence)
        if comp_sent in excluded_sentences:
            print "excluded", sentence.encode('utf-8')
            if sentence.isspace():
                print "just space"
        elif sentence not in excluded_sentences and not sentence.isspace():
            info = (asin, imgid, folder, img_dir, brand.encode('utf-8'), descriptive, sentence.encode('utf-8'))
            writer.writerow(info)

f.close()