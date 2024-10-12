import os
import pandas as pd
import zipfile
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def process_data():
    train = pd.read_csv("OLIDv1.0/olid-training-v1.0.tsv", sep="\t")
    train["subtask_a"] = train["subtask_a"] == "OFF"
    train["subtask_b"] = train["subtask_b"].fillna("NOT")
    test = pd.read_csv("OLIDv1.0/testset-levela.tsv", sep="\t")

    labels_levela = pd.read_csv("OLIDv1.0/labels-levela.csv", header=None).rename(columns={0: "id", 1: "subtask_a"})
    test = pd.merge(test, labels_levela, how="left", on="id")
    test["subtask_a"] = test["subtask_a"] == "OFF"
    labels_levelb = pd.read_csv("OLIDv1.0/labels-levelb.csv", header=None).rename(columns={0: "id", 1: "subtask_b"})
    test = pd.merge(test, labels_levelb, how="left", on="id").fillna("NOT")

    train_sentiment = pd.read_csv("data/olid-training-v1.0-sentiment.tsv", sep="\t")
    train = pd.merge(train, train_sentiment, on="id")
    test_sentiment = pd.read_csv("data/testset-sentiment.tsv", sep="\t")
    test = pd.merge(test, test_sentiment, on="id")

    train.to_csv("data/train.tsv", index=False, sep="\t")
    test.to_csv("data/test.tsv", index=False, sep="\t")
    return train, test


def prepare_data():
    if not os.path.exists("OLIDv1.0.zip"):
        #  wget https://sites.google.com/site/offensevalsharedtask/olid/OLIDv1.0.zip
        print("Downloading OLIDv1.0.zip...", end=" ", flush=True)
        urlretrieve("https://sites.google.com/site/offensevalsharedtask/olid/OLIDv1.0.zip", "OLIDv1.0.zip")
        print("Done.")
    if not os.path.exists("OLIDv1.0/olid-training-v1.0.tsv"):
        #  unzip -d OLIDv1.0 OLIDv1.0.zip
        print("Unzipping...", end=" ", flush=True)
        with zipfile.ZipFile('OLIDv1.0.zip', 'r') as zip_ref:
            zip_ref.extractall("OLIDv1.0")
        print("Done.")
    print("Processing...", end=" ", flush=True)
    process_data()
    print("Done.")


if __name__ == "__main__":
    prepare_data()
