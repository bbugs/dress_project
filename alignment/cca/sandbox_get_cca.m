%% Example of cca, cananonical correlaltion analysis

% % Load sample data
% load carbig;
% X = [Displacement Horsepower Weight Acceleration MPG];
% nans = sum(isnan(X),2) > 0;
% 
% %% Compute the sample canonical correlation.
% [A B r U V] = canoncorr(X(~nans,1:3),X(~nans,4:5));
% 
% %% Plot the canonical variables scores.
% plot(U(:,1),V(:,1),'.')
% xlabel('0.0025*Disp+0.020*HP-0.000025*Wgt')
% ylabel('-0.17*Accel-0.092*MPG')


%% Load Text Features
fname = '../../../../DATASETS/dress_attributes/txt_represention/out_title/train_val/text_features_freq_5.0_test.txt';
S = load(fname);

%% Transform indices to matlab (add 1)
S(:,1) = S(:,1) + 1;
S(:,2) = S(:,2) + 1;


%% Convert to sparse matrix
Ss = spconvert(S);
% cnn = cnn';

%%
% Load cnn features

fname = '../../../../DATASETS/dress_attributes/cnn/cnn_dress_test.txt';
cnn_test = importdata(fname);
cnn_test = cnn_test';

%% Load text features
Vsize = 1000;
n = 10;
term_freq = rand(n, Vsize);

%% Compute cca

[A B r U V] = canoncorr(cnn, term_freq);


%%
n = 10
% Load cnn features

fname = '../../../../DATASETS/dress_attributes/cnn/cnn_dress_test.txt'
cnn = importdata(fname);
cnn = cnn';
cnn = rand(n, 4096) + 5;


%% Load text features
Vsize = 1000;
n = 10;
term_freq = rand(n, Vsize) + 4

%% Compute cca
[A B r U V] = canoncorr(cnn, term_freq);

size(U)
size(V)

%% Test sparse matrix
load test_sparse_matrix.txt
%%
H = spconvert(test_sparse_matrix)

%%
J = H + 2
%%

[A B r U V] = canoncorr(H, J);





