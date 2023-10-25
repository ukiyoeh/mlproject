from src.mlproject.logger import logging
import sys
from src.mlproject.exception import CustomException


if __name__ == "__main__":
    logging.info("execution has started")
    
    try:
        a = 1/1
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)
    