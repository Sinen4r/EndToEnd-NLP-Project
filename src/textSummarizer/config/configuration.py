from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml , create_directories

from  textSummarizer.entity import DataIngestionConfig


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

         