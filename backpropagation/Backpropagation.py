import numpy as np


class Backpropagation:
    def __init__(self, structure: tuple):
        self.alpha = 0.4
        self.lmda = 0.1

        self.n_neurons = structure
        self.n_layers = len(structure)
        self.a_stored = None
        self.W = []
        self.b = []

        for l in range(1, self.n_layers):
            shape_w = (self.n_neurons[l], self.n_neurons[l - 1])
            shape_b = (self.n_neurons[l], 1)

            #rands = np.random.normal(0, 0.01 ** 2, shape_w[0] * shape_w[1])
            #w_l = rands.reshape(shape_w)
            w_l = np.random.random(shape_w)
            self.W.append(np.asmatrix(w_l))

            #rands = np.random.normal(0, 0.01 ** 2, shape_b[0] * shape_b[1])
            #b_l = rands.reshape(shape_b)
            b_l = np.random.random(shape_b)
            self.b.append(np.asmatrix(b_l))

    def learn(self, x: list, y: list):
        if len(x) != len(y):
            raise ValueError("x and y must have the same length!")

        m = len(x)
        dW = [np.zeros((self.n_neurons[l], self.n_neurons[l-1])) for l in range(1, self.n_layers)]
        db = [np.zeros((self.n_neurons[l], 1)) for l in range(1, self.n_layers)]
        for i in range(m):
            self.a_stored = [x[i]]
            for l in range(self.n_layers-1):
                grad_b_x_i = self.delta(l+1, y[i])
                grad_w_x_i = grad_b_x_i * self.a(l).transpose()
                dW[l] = dW[l] + grad_w_x_i
                db[l] = db[l] + grad_b_x_i

        for l in range(self.n_layers-1):
            self.W[l] = self.W[l] - self.alpha * dW[l]
            self.b[l] = self.b[l] - self.lmda * db[l]
        #    self.W[l] = self.W[l] - self.alpha * ((1/m) * dW[l] + self.lmda * self.W[l])
        #    self.b[l] = self.b[l] - self.alpha * ((1/m) * db[l])

    def classify(self, x):
        self.a_stored = [x]
        result = self.a(self.n_layers-1)
        return result

    def calculate_error(self, data):
        total_error = 0
        for i in range(len(data)):
            q, t = data[i]
            self.a_stored = [q]
            y = self.a(self.n_layers - 1)
            total_error += np.multiply(0.5, np.power((t - y), 2)).sum()

        return total_error

    def delta(self, l, y):
        if l == self.n_layers - 1:
            return np.multiply(-(y - self.a(l)), self.f_(l))
        else:
            return np.multiply(self.W[l].transpose() * self.delta(l + 1, y), self.f_(l))

    def a(self, l):
        try:
            return self.a_stored[l]
        except IndexError:
            a_l = f(self.z(l))
            self.a_stored.append(a_l)
            return self.a_stored[l]

    def f_(self, l):
        return np.multiply(self.a(l), (1 - self.a(l)))

    def z(self, l):
        return self.W[l - 1] * self.a(l - 1) + self.b[l - 1]


def f(z):
    return 1/(1 + np.exp(-z))
