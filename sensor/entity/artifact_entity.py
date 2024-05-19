from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:  # paths of the train and test files
    train_file_path:str 
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str
    train_file_path:str 
    test_file_path:str 
    status:bool

@dataclass
class DataTransformationArtifact:
    transform_object_path:str
    transform_train_path:str
    transform_test_path:str
    target_encoder_path:str