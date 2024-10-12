"""
The main code for the recurrent and convolutional networks assignment.
See README.md for details.
"""
from typing import Tuple, List, Dict

import tensorflow


def create_toy_rnn(input_shape: tuple, n_outputs: int) \
        -> Tuple[tensorflow.keras.models.Model, Dict]:
    """Creates a recurrent neural network for a toy problem.

    The network will take as input a sequence of number pairs, (x_{t}, y_{t}),
    where t is the time step. It must learn to produce x_{t-3} - y{t} as the
    output of time step t.

    This method does not call Model.fit, but the dictionary it returns alongside
    the model will be passed as extra arguments whenever Model.fit is called.
    This can be used to, for example, set the batch size or use early stopping.

    :param input_shape: The shape of the inputs to the model.
    :param n_outputs: The number of outputs from the model.
    :return: A tuple of (neural network, Model.fit keyword arguments)
    """

    rnn_model = tensorflow.keras.models.Sequential()
    rnn_model.add(tensorflow.keras.layers.Bidirectional(\
        tensorflow.keras.layers.SimpleRNN(30, activation='relu',\
        return_sequences = True),input_shape=input_shape))
    rnn_model.add(tensorflow.keras.layers.Dense(units=n_outputs, \
        activation='linear'))
    optimize = tensorflow.keras.optimizers.Adam(learning_rate = 0.01)
    rnn_model.compile(loss='mean_squared_error', optimizer=optimize)

    return (rnn_model,{})


def create_mnist_cnn(input_shape: tuple, n_outputs: int) \
        -> Tuple[tensorflow.keras.models.Model, Dict]:
    """Creates a convolutional neural network for digit classification.

    The network will take as input a 28x28 grayscale image, and produce as
    output one of the digits 0 through 9. The network will be trained and tested
    on a fraction of the MNIST data: http://yann.lecun.com/exdb/mnist/

    This method does not call Model.fit, but the dictionary it returns alongside
    the model will be passed as extra arguments whenever Model.fit is called.
    This can be used to, for example, set the batch size or use early stopping.

    :param input_shape: The shape of the inputs to the model.
    :param n_outputs: The number of outputs from the model.
    :return: A tuple of (neural network, Model.fit keyword arguments)
    """
    print (input_shape)
    convolution_model = tensorflow.keras.models.Sequential()
    convolution_model.add(tensorflow.keras.layers.Conv2D(28,kernel_size = 3,\
        input_shape=input_shape, activation='relu'))
    convolution_model.add(tensorflow.keras.layers.Conv2D(14,kernel_size = 3,\
        input_shape=input_shape, activation='relu'))
    convolution_model.add(tensorflow.keras.layers.Flatten())
    convolution_model.add(tensorflow.keras.layers.Dense(units=n_outputs, \
        activation='softmax'))
    optimize = tensorflow.keras.optimizers.Adam(learning_rate = 0.001)
    convolution_model.compile(loss='categorical_crossentropy', optimizer=optimize)

    return (convolution_model,{'batch_size':8})


def create_youtube_comment_rnn(vocabulary: List[str], n_outputs: int) \
        -> Tuple[tensorflow.keras.models.Model, Dict]:
    """Creates a recurrent neural network for spam classification.

    This network will take as input a YouTube comment, and produce as output
    either 1, for spam, or 0, for ham (non-spam). The network will be trained
    and tested on data from:
    https://archive.ics.uci.edu/ml/datasets/YouTube+Spam+Collection

    Each comment is represented as a series of tokens, with each token
    represented by a number, which is its index in the vocabulary. Note that
    comments may be of variable length, so in the input matrix, comments with
    fewer tokens than the matrix width will be right-padded with zeros.

    This method does not call Model.fit, but the dictionary it returns alongside
    the model will be passed as extra arguments whenever Model.fit is called.
    This can be used to, for example, set the batch size or use early stopping.

    :param vocabulary: The vocabulary defining token indexes.
    :param n_outputs: The number of outputs from the model.
    :return: A tuple of (neural network, Model.fit keyword arguments)
    """
    rnn = tensorflow.keras.models.Sequential()
    rnn.add(tensorflow.keras.layers.Embedding(len(vocabulary)+1,100,\
        input_length = 200))
    rnn.add(tensorflow.keras.layers.Bidirectional(\
        tensorflow.keras.layers.LSTM(100)))
    rnn.add(tensorflow.keras.layers.Dense(units=n_outputs, \
        activation='sigmoid'))
    optimize = tensorflow.keras.optimizers.RMSprop()
    rnn.compile(loss='binary_crossentropy', optimizer=optimize)

    return (rnn,{})


def create_youtube_comment_cnn(vocabulary: List[str], n_outputs: int) \
        -> Tuple[tensorflow.keras.models.Model, Dict]:
    """Creates a convolutional neural network for spam classification.

    This network will take as input a YouTube comment, and produce as output
    either 1, for spam, or 0, for ham (non-spam). The network will be trained
    and tested on data from:
    https://archive.ics.uci.edu/ml/datasets/YouTube+Spam+Collection

    Each comment is represented as a series of tokens, with each token
    represented by a number, which is its index in the vocabulary. Note that
    comments may be of variable length, so in the input matrix, comments with
    fewer tokens than the matrix width will be right-padded with zeros.

    This method does not call Model.fit, but the dictionary it returns alongside
    the model will be passed as extra arguments whenever Model.fit is called.
    This can be used to, for example, set the batch size or use early stopping.

    :param vocabulary: The vocabulary defining token indexes.
    :param n_outputs: The number of outputs from the model.
    :return: A tuple of (neural network, Model.fit keyword arguments)
    """

    convolution = tensorflow.keras.models.Sequential()
    convolution.add(tensorflow.keras.layers.Embedding(len(vocabulary)+ 1,100,\
        input_length = 200))
    convolution.add(tensorflow.keras.layers.Conv1D(200,kernel_size = 20,\
        activation='relu'))
    convolution.add(tensorflow.keras.layers.Flatten())
    convolution.add(tensorflow.keras.layers.Dense(units=n_outputs, \
        activation='sigmoid'))
    optimize = tensorflow.keras.optimizers.RMSprop()
    convolution.compile(loss='binary_crossentropy', optimizer=optimize)

    return (convolution,{'batch_size':8})
