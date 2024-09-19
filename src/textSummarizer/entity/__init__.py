from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    rootdir: Path
    source_URL: str
    localDataFile: Path
    unzipDir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    rootDir: Path
    StatusFile:str
    AllRequiredFiles:list