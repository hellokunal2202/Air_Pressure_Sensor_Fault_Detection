from datetime import datetime
import os,sys
from sensor.exception import SensorException
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

#creating artifact directory
class TrainingPipelineConfig:
    def __init__(self):
        timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        self.artifact_dir = os.path.join("artifact",timestamp)

#creating each component output directory
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion") 
            self.dataset_dir = os.path.join(data_ingestion_dir,"dataset")
            self.train_file_path = os.path.join(self.dataset_dir ,TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.dataset_dir,TEST_FILE_NAME)
            self.database_name="air_pressure_system"
            self.collection_name="air_pressure_system"
            self.test_size = 0.2
        except Exception as e:
                    raise SensorException(e, sys)
        

#for data validation component        
class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            data_validation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_validation")
            self.valid_dir = os.path.join(data_validation_dir,"valid")
            self.invalid_dir = os.path.join(data_validation_dir,"invalid")
            self.valid_train_file_path = os.path.join(self.valid_dir,TRAIN_FILE_NAME)
            self.invalid_train_file_path= os.path.join(self.invalid_dir,TRAIN_FILE_NAME)
            self.valid_test_file_path = os.path.join(self.valid_dir,TEST_FILE_NAME)
            self.invalid_test_file_path= os.path.join(self.invalid_dir,TEST_FILE_NAME)
            self.report_file_name = os.path.join(data_validation_dir,"report","report.yaml")
            self.schema_file_path=os.path.join("schema.yaml")
            self.missing_thresold = 70
        except Exception as e:
                raise SensorException(e, sys)