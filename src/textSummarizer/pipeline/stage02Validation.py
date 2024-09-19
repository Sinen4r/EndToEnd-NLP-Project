
from textSummarizer.components.DataValidation import DataValidation
from textSummarizer.config.configuration import ConfigurationManager2

class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):    
        config = ConfigurationManager2()
        data_validation_config = config.getDataValidationConfig()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()