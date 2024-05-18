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