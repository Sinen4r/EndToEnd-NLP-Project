from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml , create_directories

from  textSummarizer.entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig


#Data Ingestion
class ConfigurationManager:
    def __init__(self,config_filepath=ConfigFilePath,params_filepath=paramsFilePath) -> None:
        
        self.config = read_yaml(config_filepath)
        self.params= read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
    def getDataIngestionConfig(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        DataIngestion_Config=DataIngestionConfig(
            rootdir=config.root_dir,
            source_URL=config.source_URL,
            localDataFile=config.local_data_file,
            unzipDir=config.unzip_dir
        )
        return DataIngestion_Config



#Data Validation
class ConfigurationManager2:
    def __init__(self,config_filepath=ConfigFilePath,params_filepath=paramsFilePath) -> None:
        
        self.config = read_yaml(config_filepath)
        self.params= read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        
    def getDataValidationConfig(self)-> DataValidationConfig:
        config=self.config.data_validation
        create_directories([config.root_dir])
        DataValidation_Config=DataValidationConfig(
            rootDir=config.root_dir,
            StatusFile=config.STATUS_FILE,
            AllRequiredFiles=config.ALL_REQUIRED_FILES,
        )
        
        return DataValidation_Config



class configurationManager3:
    def __init__(self,config_filepath=ConfigFilePath,params_filepath=paramsFilePath):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    def getDataTransformationConfig(self)-> DataTransformationConfig:
        config= self.config.data_transformation

        create_directories([config.root_dir])
        data_transformationConfig= DataTransformationConfig(
            rootDir=config.root_dir,
            DataPath=config.data_path,
            TokonizerName=config.tokenizer_name
        )
        
        return data_transformationConfig
