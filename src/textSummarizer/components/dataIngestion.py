import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
import os
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config: DataIngestionConfig) :
        self.config = config
    def download_file(self):
        if not os.path.exists(self.config.localDataFile):
            filename,headers=request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.localDataFile
            )
            logger.info(f"{filename} download! with following info : \n{headers}")
        else:
            logger.info(f"File already exists of size : {get_size(Path(self.config.localDataFile))}")
    def extractZpFile(self):
        unzipPath=self.config.unzipDir
        os.makedirs(unzipPath,exist_ok=True)
        with zipfile.ZipFile(self.config.localDataFile,'r') as zip_ref:
            zip_ref.extractall(unzipPath)
        