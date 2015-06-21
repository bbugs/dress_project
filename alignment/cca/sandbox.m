clear all;
close all;
cd('/Users/susanaparis/Documents/Belgium/IMAGES_plus_TEXT/projects/dress_project/alignment/cca/')

rpath = '../../../../DATASETS/dress_attributes/';

%% Load Train Text Features
fname = [rpath, 'txt_represention/out_title/train_val/text_features_freq_5.0_train.txt'];
disp(fname)

Strain = load(fname);

%% Transform indices to matlab (add 1)
Strain(:,1) = Strain(:,1) + 1;
Strain(:,2) = Strain(:,2) + 1;

%% Convert to sparse matrix
Strain = spconvert(Strain);


%% Load cnn train features

fname = [rpath, '/cnn/cnn_dress.txt'];
Itrain = importdata(fname);
Itrain = Itrain';

%%
assert(size(Strain,1) == size(Itrain,1))

%% Learn Projection Matrices
[A B] = canoncorr(Strain, Itrain);


%% Debug column error

Itrain_sand(Itrain_sand == 0) = rand(1);
% The problem is the Nan.
% the row 1276 corresponds to an image
% find the nans
[row, col] = find(isnan(Itrain));

%% Save projection matrices
save('projection_txt.mat','A')
save('projection_img.mat','B')

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


