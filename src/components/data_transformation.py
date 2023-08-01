# Import necessary libraries and modules
import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Import custom exception and utility functions from project-specific modules
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

# Data class for configuration settings related to data transformation
@dataclass
class DataTransformationConfig:
    # Define the file path to save the preprocessor object
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

# Class for data transformation operations
class DataTransformation:
    def __init__(self):
        # Initialize the configuration object
        self.data_transformation_config = DataTransformationConfig()

    # Method to obtain the data transformation object (preprocessor)
    def get_data_transform_object(self):
        try:
            # Define numerical and categorical columns
            numerical_columns = ['writing_score', 'reading_score']
            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]

            # Define the pipelines for numerical and categorical columns
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),  # Fill missing values with the median
                    ('scaler', StandardScaler())  # Standardize numerical features
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),  # Fill missing values with the most frequent category
                    ('one_hot_encoder', OneHotEncoder()),  # One-hot encode categorical features
                ]
            )

            # Log the completion of preprocessing steps
            logging.info("Numerical columns standard scaling is completed")
            logging.info('Categorical columns One hot encoding is completed')

            # Create a ColumnTransformer to apply the pipelines to specific columns
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat_pipeline', cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            # Raise a custom exception if any error occurs during data transformation
            raise CustomException(sys, e)

    # Method to perform data transformation on input dataframes
    def initiate_data_transformation(self, train_path, test_path):
        try:
            # Read train and test data from CSV files
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            # Log the completion of data reading
            logging.info('Read train and test data is completed')

            # Obtain the data transformation object (preprocessor)
            logging.info("Obtaining Preprocessing Object")
            preprocessing_obj = self.get_data_transform_object()

            # Define the target column and numerical columns
            target_column_name = ['math_score']
            numerical_columns = ['writing_score', 'reading_score']

            # Separate input features and target features for both train and test data
            input_feature_train_df = train_df.drop(columns=target_column_name, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=target_column_name, axis=1)
            target_feature_test_df = test_df[target_column_name]

            # Log the application of preprocessing object on train and test dataframes
            logging.info(f'Applying preprocessing object on train and test dataframe')

            # Apply the preprocessor to transform input features into arrays
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.fit_transform(input_feature_test_df)

            # Combine transformed input features with target features
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            # Log the completion of data transformation
            logging.info('Saved preprocessing object')

            # Save the preprocessor object to a file
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            # Return the transformed data arrays and the file path of the saved preprocessor object
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            # Raise a custom exception if any error occurs during data transformation
            raise CustomException(e, sys)
