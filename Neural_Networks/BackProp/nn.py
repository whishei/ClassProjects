"""
The main code for the back propagation assignment. See README.md for details.
"""
import math
from typing import List
import scipy

import numpy as np


class SimpleNetwork:
    """A simple feedforward network where all units have sigmoid activation.
    """

    @classmethod
    def random(cls, *layer_units: int):
        """Creates a feedforward neural network with the given number of units
        for each layer.

        :param layer_units: Number of units for each layer
        :return: the neural network
        """

        def uniform(n_in, n_out):
            epsilon = math.sqrt(6) / math.sqrt(n_in + n_out)
            return np.random.uniform(-epsilon, +epsilon, size=(n_in, n_out))

        pairs = zip(layer_units, layer_units[1:])
        return cls(*[uniform(i, o) for i, o in pairs])

    def __init__(self, *layer_weights: np.ndarray):
        """Creates a neural network from a list of weight matrices.
        The weights correspond to transformations from one layer to the next, so
        the number of layers is equal to one more than the number of weight
        matrices.

        :param layer_weights: A list of weight matrices
        """
        self.layer_weights = layer_weights

    def predict(self, input_matrix: np.ndarray) -> np.ndarray:
        """Performs forward propagation over the neural network starting with
        the given input matrix.

        Each unit's output should be calculated by taking a weighted sum of its
        inputs (using the appropriate weight matrix) and passing the result of
        that sum through a logistic sigmoid activation function.

        :param input_matrix: The matrix of inputs to the network, where each
        row in the matrix represents an instance for which the neural network
        should make a prediction
        :return: A matrix of predictions, where each row is the predicted
        outputs - each in the range (0, 1) - for the corresponding row in the
        input matrix.
        """

        sigmoids = self.calculate_sigmoids(input_matrix)
        return sigmoids[len(sigmoids) - 1]

    def predict_zero_one(self, input_matrix: np.ndarray) -> np.ndarray:
        """Performs forward propagation over the neural network starting with
        the given input matrix, and converts the outputs to binary (0 or 1).

        Outputs will be converted to 0 if they are less than 0.5, and converted
        to 1 otherwise.

        :param input_matrix: The matrix of inputs to the network, where each
        row in the matrix represents an instance for which the neural network
        should make a prediction
        :return: A matrix of predictions, where each row is the predicted
        outputs - each either 0 or 1 - for the corresponding row in the input
        matrix.
        """
        almostbinary = self.predict(input_matrix)

        binary = []
        indexs = np.arange(len(almostbinary))
        for i in indexs:
            row = []
            for val in almostbinary[i]:
                if val < 0.5:
                    row.append(0)
                else:
                    row.append(1)
            binary.append(row)

        return binary

    def gradients(self,
                  input_matrix: np.ndarray,
                  output_matrix: np.ndarray) -> List[np.ndarray]:
        """Performs back-propagation to calculate the gradients for each of
        the weight matrices.

        This method first performs a pass of forward propagation through the
        network, then applies the following procedure to calculate the
        gradients. In the following description, × is matrix multiplication,
        ⊙ is element-wise product, and ⊤ is matrix transpose.

        First, calculate the error, error_L, between last layer's activations,
        h_L, and the output matrix, y:

        error_L = h_L - y

        Then, for each layer l in the network, starting with the layer before
        the output layer and working back to the first layer (the input matrix),
        calculate the gradient for the corresponding weight matrix as follows.
        First, calculate g_l as the element-wise product of the error for the
        next layer, error_{l+1}, and the sigmoid gradient of the next layer's
        weighted sum (before the activation function), a_{l+1}.

        g_l = (error_{l+1} ⊙ sigmoid'(a_{l+1}))⊤

        Then calculate the gradient matrix for layer l as the matrix
        multiplication of g_l and the layer's activations, h_l, divided by the
        number of input examples, N:

        grad_l = (g_l × h_l)⊤ / N

        Finally, calculate the error that should be backpropagated from layer l
        as the matrix multiplication of the weight matrix for layer l and g_l:

        error_l = (weights_l × g_l)⊤

        Once this procedure is complete for all layers, the grad_l matrices
        are the gradients that should be returned.

        :param input_matrix: The matrix of inputs to the network, where each
        row in the matrix represents an instance for which the neural network
        should make a prediction
        :param output_matrix: A matrix of expected outputs, where each row is
        the expected outputs - each either 0 or 1 - for the corresponding row in
        the input matrix.
        :return: two matrices of gradients, one for the input-to-hidden weights
        and one for the hidden-to-output weights
        """

        prediction = self.predict(input_matrix)
        layer_error = np.array(prediction - output_matrix)
        gradients = []
        num_input_examps = len(input_matrix)

        sigmoids = self.calculate_sigmoids(input_matrix)
        k = len(sigmoids) - 1
        while k >= 0:
            g_layers = (layer_error*(sigmoids[k]*(1-sigmoids[k])))
            if k >= 1:
                current_gradient = (np.matmul(g_layers.T,sigmoids[k-1])/num_input_examps).T
            else:
                current_gradient = (np.matmul(input_matrix.T,g_layers)/num_input_examps)
            layer_error = (np.matmul(self.layer_weights[k],g_layers.T)).T
            k = k -1
            gradients.append(current_gradient)

        gradients.reverse()
        return gradients


    def train(self,
              input_matrix: np.ndarray,
              output_matrix: np.ndarray,
              iterations: int = 10,
              learning_rate: float = 0.1) -> None:
        """Trains the neural network on an input matrix and an expected output
        matrix.

        Training should repeatedly (`iterations` times) calculate the gradients,
        and update the model by subtracting the learning rate times the
        gradients from the model weight matrices.

        :param input_matrix: The matrix of inputs to the network, where each
        row in the matrix represents an instance for which the neural network
        should make a prediction
        :param output_matrix: A matrix of expected outputs, where each row is
        the expected outputs - each either 0 or 1 - for the corresponding row in
        the input matrix.
        :param iterations: The number of gradient descent steps to take.
        :param learning_rate: The size of gradient descent steps to take, a
        number that the gradients should be multiplied by before updating the
        model weights.
        """

        for i in range(iterations):
            gradients = self.gradients(input_matrix,output_matrix)
            new_weights = []
            for idx,val in enumerate(gradients):
                new_weights.append(self.layer_weights[idx] - (learning_rate*val))
            self.layer_weights = new_weights
            i = i*1

    def calculate_sigmoids(self, input_matrix: np.ndarray) -> np.ndarray:
        """Performs forward propagation over the neural network starting with
        the given input matrix.

        Each unit's output should be calculated by taking a weighted sum of its
        inputs (using the appropriate weight matrix) and passing the result of
        that sum through a logistic sigmoid activation function.

        :param input_matrix: The matrix of inputs to the network, where each
        row in the matrix represents an instance for which the neural network
        should make a prediction
        :return: A list of matrices corresponding to the output of every sigmoid
        layer in the neural network
        """
        sigmoid_layers = []
        current_layer = input_matrix

        for val in self.layer_weights:
            current_weights = val
            hidden_matrix = np.matmul(current_layer,current_weights)
            current_layer = scipy.special.expit(hidden_matrix)
            sigmoid_layers.append(current_layer)
        return sigmoid_layers
