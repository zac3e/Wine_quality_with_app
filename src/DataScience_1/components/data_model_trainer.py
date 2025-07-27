import pandas as pd
import os
from src.DataScience_1 import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.DataScience_1.entity.config_entity import (ModeltrainerConfig)

class ModelTrainer:
    def __init__(self,config:ModeltrainerConfig):
        self.config=config
    def train(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]] 

        model=ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
        model.fit(train_x, train_y)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))

        