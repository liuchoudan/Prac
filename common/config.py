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

from django.conf import settings

parser = configparser.ConfigParser()
parser.read(os.path.join(settings.BASE_DIR, 'settings.py'))


class BaseSettings:

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
        for attr, _type in cls.__annotations__:


if __name__ == '__main__':
    print(settings.DEBUG)

