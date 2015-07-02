from gibbs_output import process_gibbs_output as pgibbs


# assume there is one .n and one .v file in wdir
wdir = '../../DATASETS/geert_output/POS/training_output/bilda100/text/'
gibbs_train = pgibbs.GibbsOutputTrain(wdir=wdir)
print gibbs_train

Pwz = pgibbs.mk_cond_prob(gibbs_train.vmatrix, gibbs_train.beta, gibbs_train.n_samples)
pgibbs.check_cond_prob(Pwz)


# assume there is one .theta and one .perplexity file in wdir
wdir = '../../DATASETS/geert_output/POS/inference_output/bilda100/vis_750/'
gibbs_infer = pgibbs.GibbsOutputInfer(wdir=wdir)
print gibbs_infer

Pzd = gibbs_infer.theta
pgibbs.check_cond_prob(Pzd)


# vfile_name = gibbs_train.vfile_path
# print vfile_name
#
# pgibbs.read_vfile(vfile_name)

# compute probability

# map(float, l.strip().split())