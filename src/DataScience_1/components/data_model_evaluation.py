import pandas as pd 
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np 
import joblib
from src.DataScience_1.entity.config_entity import (ModelEvaluationConfig)
from src.DataScience_1.utils.common import save_json
from pathlib import Path
from src.DataScience_1.constants import *


class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config

    def eval_metrics(self,actual,pred):
        rmse=np.sqrt(mean_squared_error(actual,pred))
        mea=mean_absolute_error(actual,pred)
        r2=r2_score(actual,pred)
        return rmse,mea,r2

    def log_into_mlflow(self):

        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)

        test_x=test_data.drop([self.config.target_column], axis=1)
        test_y=test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()) .scheme
        mlflow.set_experiment("EvaluacionElasticNet_v1")
        with mlflow.start_run():
            predict_qualities =model.predict(test_x)
            (rmse, mae, r2) = self.eval_metrics(test_y, predict_qualities)
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            if tracking_url_type_store != "file":

                mlflow.sklearn.log_model(model, name="model", registered_model_name="ElasticnetModel",input_example=test_x.iloc[:1],signature=mlflow.models.signature.infer_signature(test_x, test_y))
            else:
                mlflow.sklearn.log_model(model, name="model",input_example=test_x.iloc[:1],signature=mlflow.models.signature.infer_signature(test_x, test_y))