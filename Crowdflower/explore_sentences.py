
import nltk
import nltk.data
from utils_local import utils_local
import csv
import time


import zTextProcessing as zt

# load punctuation
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')



def init_dress_dict1():
    dress = {}
    fields = ['imgid', 'asin', 'folder', 'url', 'brand', 'color', 'sentences']
    for f in fields:
        if f == 'imgid':
            dress[f] = 0
        else:
            dress[f] = ''
    return dress


def get_sentences(all_text, verbose=0):
    """(list of strings) -> list of sentences (str)
    group into a list of sentences title, features and editorial
    editorial is broken into sentences.

    """
    sents = []  # clean sentences
    for item in all_text:
        # print item
        # tokenize into sentences
        temp_sentences = sent_tokenizer.tokenize(item)
        for s in temp_sentences:
            #print s
            s1 = s.replace("<br />", "<br>")
            s1 = s1.replace("<br/>", "<br>")
            if s1:
                sents.append(s1)

    clean_sents = []
    for s in sents:
        s2 = s.split("<br>")
        for ss in s2:
            #print ss
            # s3 = ss.replace("<br />", "  ")
            # s3 = ss.replace("<br/>", "  ")
            s3 = zt.strip_tags(ss)  # strip html tags
            s4 = s3.replace("\n\n", "\%")
            s4 = s4.replace("\n", "\%")
            clean_sents.append(s4)

    if verbose:
        for s in clean_sents:
            print '\n', s

    return clean_sents



data0 = utils_local.load_data0(fname='../data0.json')
#i = 239 #1224  #357

rdir = 'http://people.cs.kuleuven.be/~susana.zoghbi/dress_imgs/'


# set up the excluded set and the excluded phrases csv file
excluded_fname = 'excluded_phrases.csv'
excluded_file = open(excluded_fname, 'wb')
excluded_writer = csv.writer(excluded_file)

info = ("asin", "img_id", "brand", "folder", "sentence")
excluded_writer.writerow(info)
excluded_sentence_set = set()


# set up the crowdflower
crowd_fname = 'data_crowdflower.csv'
crowd_file = open(crowd_fname, 'wb')
crowd_writer = csv.writer(crowd_file)
info = ("asin", "imgid", "folder", "img_dir", "brand", "sentences")
crowd_writer.writerow(info)

# set up included set
included_set = set()

ecount = 0
icount = 1

for dress in data0['dresses'][0:10]:
    #dress0 = data0['dresses'][i]

    features = dress['features']  # list of strings
    editorial = dress['editorial']  # string
    title = dress['title']  # string
    brand = dress['brand']
    asin = dress['asin']
    imgid = dress['imgid']
    folder = dress['folder']

    dir = rdir + folder + '/' + asin + '.jpg'

    all_text = [title] + features + [editorial]

    processed_sents = get_sentences(all_text, verbose=0)

    for sent in processed_sents:
        print '\n', sent

        if sent in excluded_sentence_set:
            ecount += 1
            print "sentence already in excluded set", ecount
            info = (asin, imgid, brand, folder, sent)
            excluded_writer.writerow(info)
            continue

        if sent in included_set:
            icount += 1
            print "sentence already in INCLUDED set", icount
            info = (asin, imgid, folder, dir, brand, sent)
            crowd_writer.writerow(info)
            print "sentence added to crowds"
            continue

        option = raw_input("Press 0 to exclude")

        if option == '0':
            # place it in the excluded set
            excluded_sentence_set.add(sent)
            info = (asin, imgid, brand, folder, sent)
            excluded_writer.writerow(info)

        else:
            # put it on the csv file for crowdflower
            included_set.add(sent)
            info = (asin, imgid, folder, dir, brand, sent)
            crowd_writer.writerow(info)


excluded_file.close()
crowd_file.close()


