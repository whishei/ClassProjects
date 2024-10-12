# Objectives

The learning objectives of this assignment are to:

1. obtain a Text Representation based on tf-idf and encode additional features 
2. create, train and run a Logistic Regression model for Text Classification

# Setup your environment and prepare data

First, carefully follow the *General Instructions for Programming Assignments*.

To install the libraries required for this assignment run:

    pip install -r requirements.txt
    
Download and prepare the **OffensEval** dataset by running:

    python prepare_data.py 

This should create the files `data/train.tsv` and `data/test.tsv`.

# Grading

The grading distribution for this assignment is listed below:
- test_create_tfidvectorizer = 16%
- test_run_vectorizer = 16%
- test_create_model = 16%
- test_run_model = 16%
- test_create_balanced_model = 16%
- test_create_column_transformer = 20%