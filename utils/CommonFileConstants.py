import os

class CommonFileConstants:
    _WORKING_DIRECTORY_PATH: str = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    BASE_PATH: str = os.path.dirname(_WORKING_DIRECTORY_PATH)
