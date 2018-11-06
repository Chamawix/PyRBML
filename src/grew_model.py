#TODO: Grew model id:0

import spacy

default_label_types = ["Subject-Verb-Object", "Subject-Verb", "Subject-Object"]

default_tokenizer = spacy
default_label = default_label_types[0]

class GrewModel():

    def __init__(self, **kwargs):

        self.model_path = kwargs["model_path"]
        self.model = kwargs["model"]

        self.columns_label = kwargs["columns_label"]
        


    def train(self):
        pass

    def train_default(self):
        pass

    def train_labels(self, data, labels):
        pass

    def save_model(self, path=""):
        pass

    def load_model(self, file_path=""):
        pass

    def fit(self, data):
        pass
