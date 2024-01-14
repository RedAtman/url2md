import unittest

from base.test import BaseTest
from logger import logger
from utils.response import Result


class ExampleTest(BaseTest):

    def test_request(self):
        '''python -m unittest tests.test_request.ExampleTest.test_request
        '''
        # url = 'https://httpbin.org/get'
        # url = 'https://www.baidu.com/'
        url = 'https://segmentfault.com/a/1190000021854441'
        url = 'https://www.runoob.com/go/go-fmt-sprintf.html'
        result: Result = self.request(
            url=url,
            method='GET',
            data={}
        )
        assert isinstance(result, Result)
        assert result.code == 200
        assert isinstance(result.__dict__, dict)
        assert isinstance(result.data, str)
        logger.json(result.__class__)
        logger.json(type(result.data))
        logger.json(result)
        # logger.json(json.loads(result.data))
        # assert False


if __name__ == '__main__':
    unittest.main(verbosity=2)
