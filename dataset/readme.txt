data0.json was created with xml2json0.py

mk_dataset.py created:
dataset_dress_all.json
dataset_dress_title.json
Some cleaning took place, i.e., some sentences were manually removed as non-descriptive


mk_dataset_berg.py created
dataset_berg.json

mk_joint_dataset.py created
dataset_joint_all.json (combines dress_all and berg)



####################
####  Dataset  ####
####################
dataset_dress_*.json contains:
53,689 dresses

Train set:
48,689 dresses
Test set:
1,000 dresses
Val set:
4,000 dresses
####################

paths_berg.txt, paths_dress.txt, paths_joint.txt were created from the command line. For example, like so:

python data_manager/data_provider.py > dataset/paths_joint.txt

