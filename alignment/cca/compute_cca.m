clear all;
close all;
cd('/export/home2/NoCsBack/hci/susana/IMAGES_plus_TEXT/projects/dress_project/alignment/cca/')

i = 1:10

%% 
rpath = '../../../../DATASETS/dress_attributes/'
%% Load Train Sentences
fname = '/export/home2/NoCsBack/hci/susana/IMAGES_plus_TEXT/DATASETS/dress_attributes/txt_represention/out_title/train_val/text_features_freq_5.0_train.txt'

disp('loading train text')
Strain = load(fname);

%% Transform indices to matlab (add 1)
Strain(:,1) = Strain(:,1) + 1;
Strain(:,2) = Strain(:,2) + 1;

%% Convert to sparse matrix
Strain = spconvert(Strain);


%% Load cnn train features
disp('loading cnn')
fname = [rpath, '/cnn/cnn_dress_train.txt'];
Itrain = importdata(fname);
Itrain = Itrain';

%%
assert(size(Strain,1) == size(Itrain,1))

%% Learn Projection Matrices
disp('computing projection matrices')
[A B] = canoncorr(Strain, Itrain);

%% Save projection matrices
save('projection_txt.mat','A')
save('projection_img.mat','B')


if 0
disp(fname)

Strain = load(fname);

%% Transform indices to matlab (add 1)
Strain(:,1) = Strain(:,1) + 1;
Strain(:,2) = Strain(:,2) + 1;

%% Convert to sparse matrix
Strain = spconvert(Strain);


%% Load 

% "size of Strain"
size(Strain)

%% Set Parameters
n = 10;

%% Get train txt_features
% n x 9
txt_dim = 9;
S_train = randi(2, n, txt_dim);

%% Get train img_features
% n x 4
img_dim = 4;
I_train = rand(n, img_dim);

%% Learn Projection Matrices
[A B] = canoncorr(S_train, I_train);

%% Get test txt_features
ntest = 3;
S_test = randi(2, ntest, txt_dim);

%% GEt test img_features
I_test = rand(ntest, img_dim);


%% Project sentences
S_test_project = S_test * A;
S_train_project = S_train * A;

%% Project Images
I_test_project = I_test * B;
I_train_project = I_train * B;


%% Image to Text
%% Compute similarity between image and text
sim = I_train_project *  S_train_project';
[junk, sent_pred_ind] = max(sim,[],2);


%%
sim2 = I_test_project * S_train_project';
[junk, sent_pred_ind2] = max(sim2,[],2);

%% test only
sim3 = I_test_project * S_test_project';
[junk, sent_pred_ind3] = max(sim3,[],2);

%% Decode
sent_pred_ind

end
