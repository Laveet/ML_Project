from src.exception import CustomException
import os
import sys
from src.loger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.transformation import DataTransformation
from src.components.transformation import TransformationConfig



@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingest_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data ingestion is started")
        try:
            df=pd.read_csv(r"C:\Users\lavee\Desktop\ML_Project\Notebook\data\stud.csv")
            logging.info("Read the dataset as DF")
            os.makedirs(os.path.dirname(self.ingest_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingest_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            df.to_csv(self.ingest_config.train_data_path,index=False,header=True)
            df.to_csv(self.ingest_config.test_data_path,index=False,header=True)
            logging.info("Ingestion is completed")
            return(
            self.ingest_config.train_data_path,
            self.ingest_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
    

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transform=DataTransformation()
    data_transform.initiate_data_transformation(train_data,test_data)
    print("code is successfull run")
    # print(train_data,test_data)

    
            

