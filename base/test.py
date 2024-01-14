import functools
import sys
import unittest
from typing import Callable, Dict, Optional, TypeVar

from logger import logger
from utils.request import Request

T = TypeVar('T')


class _AssertWrapMeta(type):
    def __new__(cls, name, bases, attr__map: Dict[str, Callable]):
        for key, attr in attr__map.items():
            if hasattr(attr, '__call__') and key.startswith('test_'):
                attr = cls.wrap(attr)
        return type.__new__(cls, name, bases, attr__map)

    # @staticmethod
    # def assert_response(response):
    #     assert response.status >= 200 and response.status < 300, \
    #         f'{response.status}, {response.data}'
    #     assert getattr(response, 'data', None) is not None, 'response.data is None'
    #     assert isinstance(response.data, (dict, list)), 'response.data is not dict or list'

    @classmethod
    def wrap(cls, f: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(f)
        def func(self, *args, **kwargs):
            try:
                response = f(self, *args, **kwargs)
                # logger.info(schema)
                # cls.assert_response(response)
                return response
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


class BaseTest(
    unittest.TestCase,
    # metaclass=_AssertWrapMeta,
):

    def request(self,
        url: str,
        method: str = 'GET',
        headers: Dict[str, str] = {},
        data: Optional[Dict[str, str]] = {}):
        return Request.request(url, method=method, headers=headers, data=data)
