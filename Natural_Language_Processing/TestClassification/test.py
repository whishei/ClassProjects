import pytest
import nbimporter
import numpy as np
import pickle as pkl
import pandas as pd
from numpy.testing import assert_array_equal, assert_allclose
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.dummy import DummyClassifier
from pandas import DataFrame
from dataclasses import dataclass

from textclassification import (create_tfidvectorizer, run_vectorizer,
                                create_model, run_model,
                                create_balanced_model,
                                create_column_transformer)


@dataclass
class Shared:
    train: DataFrame
    test: DataFrame
    target_vectorizer: TfidfVectorizer
    target_train_x: np.array
    target_test_x: np.array
    target_model: LogisticRegression
    target_prediction: np.array
    target_balanced_model: LogisticRegression

   
@pytest.fixture(scope="session")
def shared():
    train = pd.read_csv("test_utils/train.tsv", sep="\t")
    test = pd.read_csv("test_utils/test.tsv", sep="\t")
    with open("test_utils/vectorizer.pkl", "rb") as pklfile:
        target_vectorizer = pkl.load(pklfile)
    with open("test_utils/train_x_vectorized.pkl", "rb") as pklfile:
        target_train_x = pkl.load(pklfile)
    with open("test_utils/test_x_vectorized.pkl", "rb") as pklfile:
        target_test_x = pkl.load(pklfile)
    with open("test_utils/model.pkl", "rb") as pklfile:
        target_model = pkl.load(pklfile)
    with open("test_utils/prediction.pkl", "rb") as pklfile:
        target_prediction = pkl.load(pklfile)
    with open("test_utils/balanced_model.pkl", "rb") as pklfile:
        target_balanced_model = pkl.load(pklfile)
    return Shared(train, test, target_vectorizer,
                  target_train_x, target_test_x,
                  target_model, target_prediction,
                  target_balanced_model)


def test_create_tfidvectorizer(shared):
    test_vectorizer = create_tfidvectorizer()
    assert isinstance(test_vectorizer, type(shared.target_vectorizer))
   
   
def test_run_vectorizer(shared):
    test_train_x, test_test_x = run_vectorizer(shared.target_vectorizer,
                                               shared.train["tweet"],
                                               shared.test["tweet"])
    assert_allclose(test_train_x.toarray(), shared.target_train_x.toarray())
    assert_allclose(test_test_x.toarray(), shared.target_test_x.toarray())


def test_create_model(shared):
    test_model = create_model()
    assert isinstance(test_model, type(shared.target_model))


def test_run_model(shared):
    test_prediction = run_model(shared.target_model, shared.target_train_x,
                                shared.train["subtask_a"], shared.target_test_x)
    assert_array_equal(test_prediction, shared.target_prediction)


def test_create_balanced_model(shared):
    test_balanced_model = create_balanced_model()
    assert test_balanced_model.get_params()["class_weight"] == "balanced"


def test_create_column_transformer(shared):
    test_column_transformer = create_column_transformer()
    test_transformers = test_column_transformer.get_params()['transformers']
    assert any([type(transformer[1]) == TfidfVectorizer and transformer[2] == "tweet"
                for transformer in test_transformers])
    assert any([type(transformer[1]) == OneHotEncoder and transformer[2] == ["sentiment"]
                for transformer in test_transformers])
