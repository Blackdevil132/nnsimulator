import random

import numpy as np

from backpropagation import Backpropagation

"""training_sets = [[np.matrix("1 0 0 0 0 0 0 0").transpose(), np.matrix("1 0 0 0 0 0 0 0").transpose()],
     [np.matrix("0 1 0 0 0 0 0 0").transpose(), np.matrix("0 1 0 0 0 0 0 0").transpose()],
     [np.matrix("0 0 1 0 0 0 0 0").transpose(), np.matrix("0 0 1 0 0 0 0 0").transpose()],
     [np.matrix("0 0 0 1 0 0 0 0").transpose(), np.matrix("0 0 0 1 0 0 0 0").transpose()],
     [np.matrix("0 0 0 0 1 0 0 0").transpose(), np.matrix("0 0 0 0 1 0 0 0").transpose()],
     [np.matrix("0 0 0 0 0 1 0 0").transpose(), np.matrix("0 0 0 0 0 1 0 0").transpose()],
     [np.matrix("0 0 0 0 0 0 1 0").transpose(), np.matrix("0 0 0 0 0 0 1 0").transpose()],
     [np.matrix("0 0 0 0 0 0 0 1").transpose(), np.matrix("0 0 0 0 0 0 0 1").transpose()]]


training_sets = [
    [np.matrix("0; 0"), 0],
    [np.matrix("0; 1"), 1],
    [np.matrix("1; 0"), 1],
    [np.matrix("1; 1"), 0]]"""

training_sets = [
    [np.matrix("0"), np.matrix("1")],
    [np.matrix("1"), np.matrix("0")]
]

n_n = (1, 2, 1)
nn = Backpropagation(n_n)

#for i in range(len(nn.W)):
#    print("W[%i] := \n" %(i+1), nn.W[i], "\n")

for i in range(1000000):
    x, y = random.choice(training_sets)
    nn.learn([x], [y])

#for i in range(len(nn.W)):
#    print("W[%i] := \n" %(i+1), nn.W[i], "\n")

print("Classify: ", nn.classify(np.matrix("0")))
print("Classify: ", nn.classify(np.matrix("1")))
#print("Classify: ", nn.classify(np.matrix("1; 0")))
#print("Classify: ", nn.classify(np.matrix("1; 1")))
