
from textSummarizer.components.ModelTrainer import ModelTrainer
from textSummarizer.config.configuration import ConfigurationManager4

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):    
        config = ConfigurationManager4()
        ModerlTrainConfig = config.get_model_trainer_config()
        ModelTrain = ModelTrainer(config=ModerlTrainConfig)
        ModelTrain.train()