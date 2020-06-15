import mlflow
import random
import sys
import time
import argparse
import pickle
import json
import os

from model_builder.model import model_builder
from dataset_builder.dataset import dataset_builder


def save_model(name, params):
    a_file = open(name, "wb")
    pickle.dump(params, a_file)
    a_file.close()


def main():
    epochs = 10
    train_loss = 10.0
    val_loss = 11.0
    best_loss = 100.0

    with open('config/dataset_config.json') as dc:
        dataset_config = json.load(dc)

    with open('config/model_config.json') as mc:
        model_config = json.load(mc)

    m = model_builder(model_config, retrain=False)
    d = dataset_builder(dataset_config)

    with mlflow.start_run():
        mlflow.log_params(dataset_config)
        mlflow.log_params(model_config)
        mlflow.log_param('epochs', epochs)
        for _ in range(epochs):
            mlflow.log_metrics(
                {'train_loss': train_loss, 'val_loss': val_loss})
            train_loss *= random.randint(5, 12)/10
            val_loss *= random.randint(5, 12)/10
            if val_loss < best_loss:
                best_loss = val_loss
                # TODO:Save model here
                save_model('DummyModel2.pkl', m.params)
        # Save artifacts
        mlflow.log_artifact('DummyModel2.pkl', 'weight')
        mlflow.log_artifacts('dataset_builder', 'code/dataset')
        mlflow.log_artifacts('model_builder', 'code/model')
        mlflow.log_artifacts('config', 'code/config')
        os.remove('DummyModel2.pkl')


if __name__ == "__main__":
    main()
