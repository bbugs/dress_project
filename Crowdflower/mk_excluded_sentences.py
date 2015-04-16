"""
Print sentences to screen and press 0 to exclude the sentence or any other key to include it.

Two files are generated:
excluded_phrases.pkl
included_phrases.pkl

It builds up on these files everytime this script is run, it opens up these files and it keeps populating them.

"""

from utils_local import utils_local
import pickle
import csv
import random

excluded_fname = 'excluded_phrases.pkl'
excluded_sentences = utils_local.get_stored_sentences(excluded_fname)
excluded_sentences = utils_local.remove_space(excluded_sentences)


included_fname = 'included_phrases.pkl'
included_sentences = utils_local.get_stored_sentences(included_fname)


#i = 239 #1224  #357


data0 = utils_local.load_data0(fname='../data0.json')

n = 10  # number of dresses to evaluate

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

    # make a list of all sentences including title, features and editorial review
    processed_sents = utils_local.get_sentences(all_text, verbose=0)



    for sent in processed_sents:
        #print '\n', sent
        sent = sent.lower()




        if sent in excluded_sentences:
            print "EXCLUDED already:"
            print "sent", sent
            #raw_input("excluded. press any key to continue")
            continue

        elif sent in included_sentences:
            print "included already", sent
            #raw_input("included press any key to continue")
            continue

        print "evaluate the following sentence"
        print sent
        option = raw_input("Press 0 to exclude:\n ")


        if option == '0':
            # place it in the excluded set
            excluded_sentences.add(sent)
            print "writing to excluded file"
            #raw_input("any key to continue")


        else:
            # put it on the csv file for crowdflower
            included_sentences.add(sent)
            print "writint to INcluded file"
            # raw_input("press any key to continue")

        print "\n"

sfile = open(excluded_fname, "wb")
pickle.dump(excluded_sentences, sfile)
sfile.close()

sfile = open(included_fname, "wb")
pickle.dump(included_sentences, sfile)
sfile.close()



