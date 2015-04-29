import json
import os
import zTextProcessing as zt
import nltk
import nltk.data
import pickle

def load_data0(fname='../data0.json'):
    with open(fname, 'r') as f:
        data0 = json.load(f)

    return data0


def write_line2txt(line, file_object):
    for l in line:
        file_object.write(l, ",")
    pass

def remove_space(sentence_set):
    """(set of strings) -> set of strings
    given a set of sentences, remove spaces to compare
    """
    new_set = set()
    for s in sentence_set:
        new_set.add("".join(s.split()))
    return new_set





def get_sentences(all_text, verbose=0):
    """(list of strings) -> list of sentences (str)
    group into a list of sentences title, features and editorial
    editorial is broken into sentences.
    all_text refers to all the text in ONE dress, i.e., title, features, and editorial

    """
    # load punctuation
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    sents = []  # clean sentences
    for item in all_text:
        # print item
        # tokenize into sentences
        temp_sentences = sent_tokenizer.tokenize(item)
        for s in temp_sentences:
            #print s
            s1 = s.replace("<br />", "<br>")
            s1 = s1.replace("<br/>", "<br>")
            s1 = s1.replace("\n\n", "<br>")
            s1 = s1.replace("\n", "<br>")
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
            if not s3.isspace():
                clean_sents.append(s3)

    if verbose:
        for s in clean_sents:
            print '\n', s

    return clean_sents

if __name__ == '__main__':

    # see remove_using_keywords.py
    pass


