"""
The main code for the feedforward networks assignment.
See README.md for details.
"""
from typing import Tuple, Dict

import tensorflow


def create_auto_mpg_deep_and_wide_networks(
        n_inputs: int, n_outputs: int) -> Tuple[tensorflow.keras.models.Model,
                                                tensorflow.keras.models.Model]:
    """Creates one deep neural network and one wide neural network.
    The networks should have the same (or very close to the same) number of
    parameters and the same activation functions.

    The neural networks will be asked to predict the number of miles per gallon
    that different cars get. They will be trained and tested on the Auto MPG
    dataset from:
    https://archive.ics.uci.edu/ml/datasets/auto+mpg

    :param n_inputs: The number of inputs to the models.
    :param n_outputs: The number of outputs from the models.
    :return: A tuple of (deep neural network, wide neural network)
    """
    print (n_inputs)
    deep_network = tensorflow.keras.Sequential(
        [
            tensorflow.keras.layers.Dense(units = 64,input_shape =(n_inputs,)\
            ,activation="relu", name="layer1"),
            tensorflow.keras.layers.Dense(units = 16, activation="relu", \
            name="layer2"),
            tensorflow.keras.layers.Dense(units = 8, activation="relu", \
            name="layer3"),
            tensorflow.keras.layers.Dense(units = 6, activation="relu", \
            name="layer4"),
            tensorflow.keras.layers.Dense(units = 4, activation="relu", \
            name="layer5"),
            tensorflow.keras.layers.Dense(units = n_outputs, activation="linear",\
            name="layer6"),
        ]
    )
    wide_network = tensorflow.keras.Sequential(
        [
            tensorflow.keras.layers.Dense(units = 197, input_shape = \
            (n_inputs,), activation="relu", name="layer1"),
            tensorflow.keras.layers.Dense(units = n_outputs, activation="linear", \
            name="layer2"),
        ]
    )
    deep_network.compile(loss = 'mean_squared_error',optimizer='adam',\
    metrics=['accuracy'])
    wide_network.compile(loss = 'mean_squared_error',optimizer='adam',\
    metrics=['accuracy'])
    return[deep_network,wide_network]


def create_delicious_relu_vs_tanh_networks(
        n_inputs: int, n_outputs: int) -> Tuple[tensorflow.keras.models.Model,
                                                tensorflow.keras.models.Model]:
    """Creates one neural network where all hidden layers have ReLU activations,
    and one where all hidden layers have tanh activations. The networks should
    be identical other than the difference in activation functions.

    The neural networks will be asked to predict the 0 or more tags associated
    with a del.icio.us bookmark. They will be trained and tested on the
    del.icio.us dataset from:
    https://github.com/dhruvramani/Multilabel-Classification-Datasets
    which is a slightly simplified version of:
    https://archive.ics.uci.edu/ml/datasets/DeliciousMIL%3A+A+Data+Set+for+Multi-Label+Multi-Instance+Learning+with+Instance+Labels

    :param n_inputs: The number of inputs to the models.
    :param n_outputs: The number of outputs from the models.
    :return: A tuple of (ReLU neural network, tanh neural network)
    """
    relu_network = tensorflow.keras.Sequential(
        [
            tensorflow.keras.layers.Dense(units = 256,input_shape =(n_inputs,)\
            , activation="relu", name="layer1"),
            tensorflow.keras.layers.Dense(units = 128, activation="relu", \
            name="layer2"),
            tensorflow.keras.layers.Dense(units = 64, activation="relu", \
            name="layer3"),
            tensorflow.keras.layers.Dense(units = 32, activation="relu", \
            name="layer4"),
            tensorflow.keras.layers.Dense(units = 8, activation="relu", \
            name="layer5"),
            tensorflow.keras.layers.Dense(units = 6, activation="relu", \
            name="layer6"),
            tensorflow.keras.layers.Dense(units = n_outputs, activation="sigmoid", \
            name="layer7"),
        ]
    )
    tanh_network = tensorflow.keras.Sequential(
        [
            tensorflow.keras.layers.Dense(units = 256,input_shape =(n_inputs,)\
            , activation="tanh", name="layer1"),
            tensorflow.keras.layers.Dense(units = 128, activation="tanh", \
            name="layer2"),
            tensorflow.keras.layers.Dense(units = 64, activation="tanh", \
            name="layer3"),
            tensorflow.keras.layers.Dense(units = 32, activation="tanh", \
            name="layer4"),
            tensorflow.keras.layers.Dense(units = 8, activation="tanh", \
            name="layer5"),
            tensorflow.keras.layers.Dense(units = 6, activation="tanh",\
            name="layer6"),
            tensorflow.keras.layers.Dense(units = n_outputs, activation="sigmoid", \
            name="layer7"),
        ]
    )
    relu_network.compile(loss = 'binary_crossentropy',optimizer='adam',\
    metrics=['accuracy'])
    tanh_network.compile(loss = 'binary_crossentropy',optimizer='adam',\
    metrics=['accuracy'])
    return[relu_network,tanh_network]

def create_activity_dropout_and_nodropout_networks(
        n_inputs: int, n_outputs: int) -> Tuple[tensorflow.keras.models.Model,
                                                tensorflow.keras.models.Model]:
    """Creates one neural network with dropout applied after each layer, and
    one neural network without dropout. The networks should be identical other
    than the presence or absence of dropout.

    The neural networks will be asked to predict which one of six activity types
    a smartphone user was performing. They will be trained and tested on the
    UCI-HAR dataset from:
    https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones

    :param n_inputs: The number of inputs to the models.
    :param n_outputs: The number of outputs from the models.
    :return: A tuple of (dropout neural network, no-dropout neural network)
    """

    dropout_network = tensorflow.keras.Sequential()
    dropout_network.add(tensorflow.keras.layers.Dense(units = 256,\
    input_shape =(n_inputs,), activation="relu", name="layer1"))
    dropout_network.add(tensorflow.keras.layers.Dense(units = 128, \
    activation="relu", name="layer2"))
    dropout_network.add(tensorflow.keras.layers.Dense(units = 64, \
    activation="relu", name="layer3"))
    dropout_network.add(tensorflow.keras.layers.Dense(units = 32, \
    activation="relu", name="layer4"))
    dropout_network.add(tensorflow.keras.layers.Dropout(0.2))
    dropout_network.add(tensorflow.keras.layers.Dense(units = 8, \
    activation="relu", name="layer5"))
    dropout_network.add(tensorflow.keras.layers.Dense(units = n_outputs, \
    activation="softmax", name="layer6"))

    nodropout_network = tensorflow.keras.Sequential(
        [
            tensorflow.keras.layers.Dense(units = 256,input_shape = \
            (n_inputs,), activation="relu", name="layer1"),
            tensorflow.keras.layers.Dense(units = 128, activation="relu",\
            name="layer2"),
            tensorflow.keras.layers.Dense(units = 64, activation="relu", \
            name="layer3"),
            tensorflow.keras.layers.Dense(units = 32, activation="relu", \
            name="layer4"),
            tensorflow.keras.layers.Dense(units = 8, activation="relu", \
            name="layer5"),
            tensorflow.keras.layers.Dense(units = n_outputs, activation="softmax", \
            name="layer6")
        ]
    )
    dropout_network.compile(loss = 'categorical_crossentropy',\
    optimizer='adam',metrics=['accuracy'])
    nodropout_network.compile(loss = 'categorical_crossentropy',\
    optimizer='adam',metrics=['accuracy'])
    return[dropout_network,nodropout_network]

def create_income_earlystopping_and_noearlystopping_networks(
        n_inputs: int, n_outputs: int) -> Tuple[tensorflow.keras.models.Model,
                                                Dict,
                                                tensorflow.keras.models.Model,
                                                Dict]:
    """Creates one neural network that uses early stopping during training, and
    one that does not. The networks should be identical other than the presence
    or absence of early stopping.

    The neural networks will be asked to predict whether a person makes more
    than $50K per year. They will be trained and tested on the "adult" dataset
    from:
    https://archive.ics.uci.edu/ml/datasets/adult

    :param n_inputs: The number of inputs to the models.
    :param n_outputs: The number of outputs from the models.
    :return: A tuple of (
        early-stopping neural network,
        early-stopping parameters that should be passed to Model.fit,
        no-early-stopping neural network,
        no-early-stopping parameters that should be passed to Model.fit
    )
    """

    early_stopping_network = tensorflow.keras.Sequential(
        [
            tensorflow.keras.layers.Dense(units = 256,input_shape =\
            (n_inputs,), activation="relu", name="layer1"),
            tensorflow.keras.layers.Dense(units = 8, activation="relu", \
            name="layer2"),
            tensorflow.keras.layers.Dense(units = 6, activation="relu", \
            name="layer3"),
            tensorflow.keras.layers.Dense(units = n_outputs, activation="sigmoid",\
            name="layer4"),
        ]
    )
    epoch_number = tensorflow.keras.callbacks.EarlyStopping(monitor='val_loss', \
    mode='min', verbose=1)
    no_early_stopping_network = tensorflow.keras.Sequential(
        [
            tensorflow.keras.layers.Dense(units = 256,input_shape =\
            (n_inputs,), activation="relu", name="layer1"),
            tensorflow.keras.layers.Dense(units = 8, activation="relu", \
            name="layer2"),
            tensorflow.keras.layers.Dense(units = 6, activation="relu", \
            name="layer3"),
            tensorflow.keras.layers.Dense(units = n_outputs, activation="sigmoid",\
            name="layer4"),
        ]
    )

    early_stopping_network.compile(loss = 'binary_crossentropy',\
    optimizer='adam',metrics=['accuracy'])
    no_early_stopping_network.compile(loss = 'binary_crossentropy',\
    optimizer='adam',metrics=['accuracy'])
    return[early_stopping_network,{'callbacks':[epoch_number]},no_early_stopping_network,{}]
