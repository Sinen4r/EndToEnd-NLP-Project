from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml , create_directories

from  textSummarizer.entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig


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



class ConfigurationManager4:
    def __init__(
        self,
        config_filepath = ConfigFilePath,
        params_filepath = paramsFilePath):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.evaluation_strategy,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )

        return model_trainer_config