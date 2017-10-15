import numpy as np

from backpropagation import Backpropagation


def export_nn(nn: Backpropagation, path: str):
    w = nn.W
    b = nn.b
    struct = nn.n_neurons
    np.savez(path, struct,  *w, *b)


def import_nn(path:str) -> Backpropagation:
    arrays = np.load(path)
    struct = tuple(arrays['arr_0'])
    n_layers = len(struct)

    nn = Backpropagation(struct)

    l = 0
    for key in arrays.files[1:n_layers]:
        nn.W[l] = arrays[key]
        l += 1

    l = 0
    for key in arrays.files[n_layers:]:
        nn.b[l] = arrays[key]
        l += 1

    return nn