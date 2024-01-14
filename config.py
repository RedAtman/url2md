import os
import sys
from typing import Type

try:
    from dotenv import load_dotenv
except ImportError:
    import subprocess
    subprocess.run(['pip', 'install', 'python-dotenv'], check=True)
    from dotenv import load_dotenv
    load_dotenv()
else:
    load_dotenv()

__all__ = [
    'CONFIG',
]


class _BaseConfig:
    # All subclasses of BaseConfig will be added to this mapping.
    mapping: dict[str, type] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.mapping[cls.__name__.lower()] = cls

    DEBUG = False
    TESTING = False
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, BASE_DIR)
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    os.makedirs(LOG_DIR, exist_ok=True)
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')


class Development(_BaseConfig):
    '''Development environment configuration'''
    DEBUG = True


class Testing(_BaseConfig):
    '''Testing environment configuration'''
    TESTING = True


class Production(_BaseConfig):
    '''Production environment configuration'''
    LOG_LEVEL = 'WARNING'


env: str = os.getenv('ENV', 'development')
CONFIG: Type[_BaseConfig] = _BaseConfig.mapping.get(env, Development)
