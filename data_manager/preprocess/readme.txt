
## populate_excluded_phrases_user_input.py uses data_preprocessor.py

- Read the data00.json which contains a list of dictionary of dresses

- Get all the sentences from data00.json and sort them in sent_list

- Iterate over sent_list and ask the user for input if the sentence contains any word f
from the to_exclude list

to_correct.py contains a list of sentences that were misclassified by accident during the manual user input. Run to_correct.py to place these sentences in the correct set: excluded_phrases.pkl or included_phrases.pkl.
to_correct.txt is just the raw version when I was copying and pasting sentences.


