import os
import sys
from typing import Any
from src.mlproject import exception
from src.mlproject.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
sys.path.insert(0, '..//components')

from src.mlproject.components.data_transformation import DataTransformation, DataTransformationConfig

@dataclass
class DataIngestionConfig():
    train_data_path: str=os.path.join('artifacts', 'train.csv')
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('read the dataset as dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
        
            df.to_csv(self.ingestion_config.raw_data_path,index=False, header=True)
            
            logging.info("train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            train_set.to_csv(self.ingestion_config.test_data_path,index=False, header=True)
            
            logging.info("Ingestion of data completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,  
            )
        except Exception as e:
            raise exception.CustomException(e, sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
        