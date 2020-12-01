""" 
@author:lx 
@file: config.py 
@time: 2020/12/01

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""
import os
import configparser

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'settings.ini'))
print()


class BaseSettings(object):
    section = None

    def __getattr__(self, item):
        """
        通过注解类型获取配置的值
        :param item:
        :return:
        """
        if item not in self.__annotations__:
            raise AttributeError(f'No such option defined in section [{self.section}].')
        return self.__annotations__[item](parser.get(self.section, item))

    def __new__(cls, *args, **kwargs):
        """
        检查不支持的注解类型
        :param args:
        :param kwargs:
        :return:
        """
        if cls.section is None:
            raise AttributeError("Attribute 'section' requires a string value.")
        for attr, _type in cls.__annotations__.items():
            if _type not in [str, int, bool, float]:
                raise AttributeError(f'Type {_type} of attribute {attr} is not supported by settings.')
        return super().__new__(cls)


class Default(BaseSettings):
    section = 'Default'
    debug: bool


class MySQL(BaseSettings):
    section = 'MySQL'
    name: str
    host: str
    port: str
    user: str
    password: str


class Settings:
    default = Default()
    mysql = MySQL()


settings = Settings()

if __name__ == '__main__':
    print(settings.DEBUG)
