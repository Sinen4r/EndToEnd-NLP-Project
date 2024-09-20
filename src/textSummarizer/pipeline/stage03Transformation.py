from textSummarizer.components.DataTransformation import DataTransformation
from textSummarizer.config.configuration import configurationManager3

class DataTransformationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = configurationManager3()
        data_transformation_config = config.getDataTransformationConfig()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()