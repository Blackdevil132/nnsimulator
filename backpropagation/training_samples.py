import numpy as np

tr_sets_id_3 = [
    [np.matrix("0; 0; 0"), np.matrix("1; 1; 1")],
    [np.matrix("0; 0; 1"), np.matrix("1; 1; 0")],
    [np.matrix("0; 1; 0"), np.matrix("1; 0; 1")],
    [np.matrix("0; 1; 1"), np.matrix("1; 0; 0")],
    [np.matrix("1; 0; 0"), np.matrix("0; 1; 1")],
    [np.matrix("1; 0; 1"), np.matrix("0; 1; 0")],
    [np.matrix("1; 1; 0"), np.matrix("0; 0; 1")],
    [np.matrix("1; 1; 1"), np.matrix("0; 0; 0")]]

tr_sets_id_8 = [
    [np.matrix("1; 0; 0; 0; 0; 0; 0; 0"), np.matrix("1; 0; 0; 0; 0; 0; 0; 0")],
    [np.matrix("0; 1; 0; 0; 0; 0; 0; 0"), np.matrix("0; 1; 0; 0; 0; 0; 0; 0")],
    [np.matrix("0; 0; 1; 0; 0; 0; 0; 0"), np.matrix("0; 0; 1; 0; 0; 0; 0; 0")],
    [np.matrix("0; 0; 0; 1; 0; 0; 0; 0"), np.matrix("0; 0; 0; 1; 0; 0; 0; 0")],
    [np.matrix("0; 0; 0; 0; 1; 0; 0; 0"), np.matrix("0; 0; 0; 0; 1; 0; 0; 0")],
    [np.matrix("0; 0; 0; 0; 0; 1; 0; 0"), np.matrix("0; 0; 0; 0; 0; 1; 0; 0")],
    [np.matrix("0; 0; 0; 0; 0; 0; 1; 0"), np.matrix("0; 0; 0; 0; 0; 0; 1; 0")],
    [np.matrix("0; 0; 0; 0; 0; 0; 0; 1"), np.matrix("0; 0; 0; 0; 0; 0; 0; 1")]]

tr_sets_xor = [
    [np.matrix("0; 0"), 0],
    [np.matrix("0; 1"), 1],
    [np.matrix("1; 0"), 1],
    [np.matrix("1; 1"), 0]]