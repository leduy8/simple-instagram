import os

from dotenv import load_dotenv

load_dotenv()


def get_env():
    env = BaseConfig.ENVIRONMENT

    if env in ["dev", "develop", "development"]:
        return DevelopmentConfig
    elif env in ["production", "prod", "staging", "stag"]:
        return ProductionConfig
    elif env in ["testing", "test"]:
        return TestingConfig


class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "abcdefg132456"
    ENVIRONMENT = os.environ.get("ENVIRONMENT")
    DATABASE_URL = os.environ.get("DATABASE_URL_DEV")


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    DATABASE_URL = os.environ.get("DATABASE_URL_TEST")


config = get_env()
