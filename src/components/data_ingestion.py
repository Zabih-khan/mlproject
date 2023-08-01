import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation

# Data class to hold configuration for data ingestion paths
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')  # Default path for train data CSV
    test_data_path: str = os.path.join('artifacts', 'test.csv')    # Default path for test data CSV
    raw_data_path: str = os.path.join('artifacts', 'data.csv')     # Default path for raw data CSV

# Data ingestion class
class Dataingestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  # Initialize the DataIngestionConfig object

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')
        try:
            df = pd.read_csv('notebook/data/stud.csv')  # Read the dataset from CSV file (fixed the file path here)
            logging.info('Read the dataset as a dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            # Create necessary directories if they don't exist for train data CSV

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            # Save the raw dataset as a CSV file

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            # Perform train-test split with 80% training and 20% testing data

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            # Save the training dataset as a CSV file

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            # Save the testing dataset as a CSV file

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,    # Return the path of the train data CSV
                self.ingestion_config.test_data_path      # Return the path of the test data CSV
            )

        except Exception as e:
            raise CustomException(e, sys)  # Raise a custom exception with the error message and system info

if __name__ == "__main__":
    obj = Dataingestion()
    
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)    








"""
The purpose of the data_ingestion.py file is to handle the data ingestion process for a machine learning or data analysis pipeline. It reads data from a CSV file, performs a train-test split, and saves the data into separate CSV files. It also includes logging and exception handling for monitoring and error reporting.
"""
