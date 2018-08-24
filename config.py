# -*- coding:utf8 -*-

import sys
import os

# 得到本工程的文件位置, 绝对地址
root_dir = os.path.abspath(os.path.dirname(__file__))

# 设置默认编码是utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask

# 核心设置，包括加密密钥和设置sqlalchemy自动提交
class Config:
    # 散列值和安全令牌密钥设置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string!!!'

    # sqlalchemy的自动提交设置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 常用常量
    POSTS_PER_PAGE = 30
    USERS_PER_PAGE = 30
    COMMENTS_PER_PAGE = 30
    TAGS_HOT_NUM = 10
    POSTS_ABSTRACT_NUM = 500
    COMMENT_MAX_LEN = 1000

    # init_app 可以在创建flask应用时，获取到一些app上下文，同时自定义设置参数，一般就是更新app.config吧
    @staticmethod
    def init_app(app):
        pass


# 默认开发配置
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(root_dir, 'data-dev.sqlite')


# 默认测试配置
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(root_dir, 'data-test.sqlite')


# 默认生产配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(root_dir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}