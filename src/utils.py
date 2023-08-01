import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        # Get the directory path from the file path and create the directory if it does not exist
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in binary write mode and use dill to dump (serialize) the object into the file
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        # If any exception occurs during the process, raise a CustomException
        raise CustomException(e, sys)
