import unittest

from base.test import BaseTest
from logger import logger
from utils.response import Result


class ExampleTest(BaseTest):

    def test_request(self):
        # python apps/manage.py test apps.common.basetest.ExampleTest.test_health
        url = 'https://segmentfault.com/a/1190000021854441'
        # url = 'https://www.baidu.com/'
        # url = 'https://httpbin.org/get'
        # url = 'https://www.runoob.com/go/go-fmt-sprintf.html'
        result: Result = self.request(
            url=url,
            method='GET',
            data={}
        )
        assert result.code == 200
        logger.json(result.data)
        assert isinstance(result.__dict__, dict)
        assert isinstance(result.data, str)
        logger.json(type(result.data))
        # logger.json(json.loads(result.data))
        assert isinstance(result, Result)
        logger.json(result.__class__)
        # assert False
        # return response


if __name__ == '__main__':
    # example = ExampleTest()
    # example.test_request()
    unittest.main(verbosity=2)
