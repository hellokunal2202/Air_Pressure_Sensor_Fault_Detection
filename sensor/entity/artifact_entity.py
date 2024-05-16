from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:  # paths of the train and test files
    train_file_path:str 
    test_file_path:str