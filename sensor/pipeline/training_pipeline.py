from sensor.entity.config_entity import (DataIngestionConfig, TrainingPipelineConfig,DataValidationConfig)
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
import os,sys 

class TrainingPipeline:
        
        def __init__(self,training_pipleine_config:TrainingPipelineConfig):
            try:
                self.training_pipleine_config=training_pipleine_config
            except Exception as e:
                raise SensorException(e, sys)
            

        def start_data_ingestion(self)->DataIngestionArtifact:
            try:
                data_ingestion_config =DataIngestionConfig(
                    training_pipeline_config=self.training_pipleine_config)

                data_ingestion = DataIngestion(data_ingestion_config)
                data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
                return data_ingestion_artifact
            except Exception as e:
                raise SensorException(e, sys)

        

        def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
            try:
                data_validation_config = DataValidationConfig(
                    training_pipeline_config=self.training_pipleine_config)
                data_validation = DataValidation(data_validation_config=data_validation_config,
                data_ingestion_artifact=data_ingestion_artifact)
                
                return data_validation.initiate_data_validation()
            except Exception as e:
                raise SensorException(e, sys)

        def start(self):
            try:
               
               data_ingestion_artifact = self.start_data_ingestion()
               data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
                
            except Exception as e:
                print(e)
                raise SensorException(e, sys)