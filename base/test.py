import functools
import sys
import unittest
from typing import Callable

from logger import logger
from utils.request import Request


class AssertWrap(type):
    def __new__(cls, name, bases, attr__map):
        for attr in attr__map:
            if hasattr(attr__map[attr], '__call__') and attr.startswith('test_'):
                attr__map[attr] = cls.wrap(attr__map[attr])
        return type.__new__(cls, name, bases, attr__map)

    # @staticmethod
    # def assert_response(schemer, response):
    #     assert response.status >= 200 and response.status < 300, \
    #         f'{response.status}, {response.data}'
    #     schemer.validate(response.data)
    #     try:
    #         schemer.validate(response.data)
    #     except SchemaError as err:
    #         raise err
    #         # raise ApiInputException(101, f'输入数据不合法: msg: {err}')

    @staticmethod
    def assert_response(response):
        assert response.status >= 200 and response.status < 300, \
            f'{response.status}, {response.data}'
        assert getattr(response, 'data', None) is not None, 'response.data is None'
        assert isinstance(response.data, (dict, list)), 'response.data is not dict or list'

    @classmethod
    def wrap(cls, f: Callable):
        @functools.wraps(f)
        def func(self, *args, **kwargs):
            try:
                response = f(self, *args, **kwargs)
                # logger.info(schema)
                # cls.assert_response(response)
                # return response
            except Exception as err:
                f_back = sys._getframe().f_back
                logger.json({
                    '__qualname__': f.__qualname__,
                    'args': args,
                    'kwargs': kwargs,
                    'caller': '%s:%s:%s' % (f_back.f_code.co_filename, f_back.f_lineno, f_back.f_code.co_name),
                    'err': err,
                    # 'traceback': traceback.format_exc(),
                })
                raise err
        return func


class BaseTest(unittest.TestCase, metaclass=AssertWrap):

    def request(self, *args, **kwargs):
        return Request.request(*args, **kwargs)
