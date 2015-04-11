"""
Print sentences to screen and press 0 to exclude the sentence or any other key to include it.

Two files are generated:
excluded_phrases.csv
included_phrases.csv

It builds up on these files everytime this script is run, it opens up these files and it keeps populating them.

"""

from utils_local import utils_local
import csv
import random


excluded_fname = 'excluded_phrases.csv'
excluded_sentences = utils_local.get_stored_sentences(excluded_fname)

included_fname = 'included_phrases.csv'
included_sentences = utils_local.get_stored_sentences(included_fname)

#i = 239 #1224  #357


excluded_file = open(excluded_fname, 'a')
excluded_writer = csv.writer(excluded_file)

included_file = open(included_fname, 'a')
included_writer = csv.writer(included_file)


data0 = utils_local.load_data0(fname='../data0.json')

n = 3


dresses = data0['dresses']
dresses = random.sample(dresses, n)

for dress in dresses:
    #dress0 = data0['dresses'][i]

    features = dress['features']  # list of strings
    editorial = dress['editorial']  # string
    title = dress['title']  # string
    brand = dress['brand']
    asin = dress['asin']
    imgid = dress['imgid']
    folder = dress['folder']

    all_text = [title] + features + [editorial]

    processed_sents = utils_local.get_sentences(all_text, verbose=0)

    for sent in processed_sents:
        #print '\n', sent
        sent = sent.lower()

        if sent in excluded_sentences:
            continue

        if sent in included_sentences:
            continue

        print sent
        option = raw_input("Press 0 to exclude:\n ")


        if option == '0':
            # place it in the excluded set
            excluded_sentences.add(sent)
            info = (sent.encode('utf-8'),)
            excluded_writer.writerow(info)

        else:
            # put it on the csv file for crowdflower
            included_sentences.add(sent)
            info = (sent.encode('utf-8'),)
            included_writer.writerow(info)
        print "\n"


excluded_file.close()
included_file.close()


