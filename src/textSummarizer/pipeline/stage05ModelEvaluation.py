from textSummarizer.logging import logger
from textSummarizer.config.configuration import configurationManager

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        config=configurationManager()
        ModelEvaluationConfig=config.getEvaluationConfig()
        ModelEvaluation=ModelEvaluation(ModelEvaluationConfig)
        ModelEvaluation.evaluate()
