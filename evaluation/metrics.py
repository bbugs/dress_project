

def precision_at_k(ytrue, ypred, k):
    """(lst, lst, int) -> float

    """

    if len(ytrue) == 0:
        return None

    ypred = set(ypred[0:k])
    ytrue = set(ytrue)

    print "ypred", ypred
    print "ytrue", ytrue
    print "\n"

    return float(len(set.intersection(ypred, ytrue))) / k


def recall_at_k(ytrue, ypred, k):
    """(lst, lst, int) -> float

    """
    if len(ytrue) == 0:
        return None

    ypred = set(ypred[0:k])
    ytrue = set(ytrue)
    return float(len(set.intersection(ypred, ytrue))) / len(ytrue)


def f1_score(ytrue, ypred, k):
    """(lst, lst, int) -> float

    """
    if len(ytrue) == 0:
        return None
    P = precision_at_k(ytrue, ypred, k)
    R = recall_at_k(ytrue, ypred, k)

    if P == 0 or R == 0:
        return 0.0

    if (P + R) == 0:
        return None

    return float(2 * (P * R) / (P + R))


def avg_metric_at_k(metric, ytrue_list, ypred_list, k):
    """ (list of lists, list of lists) -> float

    """
    assert len(ytrue_list) == len(ypred_list)
    idx = 0
    counter = 0
    avg_metric = 0.
    for ytrue in ytrue_list:
        ypred = ypred_list[idx]

        metric_at_k = metric(ytrue, ypred, k)
        idx += 1
        # check that prec_at_k is not None
        if metric_at_k is None:
            continue
        counter += 1
        avg_metric += metric_at_k

    if counter == 0:
        return None

    print "idx, counter, metric:", idx, counter, metric.__name__

    return avg_metric / counter



if __name__ == '__main__':
    true = [4, 9, 10, 13, 14, 24, 37, 39, 76, 90]
    predicted1 = [4, 10, 13, 37, 100, 198, 200]

    k = 5
    p = precision_at_k(true, predicted1, k)
    r = recall_at_k(true, predicted1, k)
    f1 = f1_score(true, predicted1, k)
    print "precision", p
    print "recall", r
    print "f1", f1


    true_list = [[2, 3], [], [], []]
    predicted1_list = [[4, 5], [], [], []]

    avg_prec = avg_metric_at_k(precision_at_k, true_list, predicted1_list, k)
    avg_recall = avg_metric_at_k(recall_at_k, true_list, predicted1_list, k)
    avg_f1 = avg_metric_at_k(f1_score, true_list, predicted1_list, k)

    print "avg_prec", avg_prec
    print "avg_recall", avg_recall
    print "avg_f1", avg_f1


