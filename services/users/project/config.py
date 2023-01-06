# services/users/project/config.py

import os  # new


class BaseConfig:
    """Base configuration"""
    DEBUG = False  # new
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'  # new
    DEBUG_TB_ENABLED = False              # new
    DEBUG_TB_INTERCEPT_REDIRECTS = False  # new
    BCRYPT_LOG_ROUNDS = 13  # new


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # new
    DEBUG_TB_ENABLED = True  # new
    BCRYPT_LOG_ROUNDS = 4  # new


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")  # new
    BCRYPT_LOG_ROUNDS = 4  # new


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False  # new
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # new
