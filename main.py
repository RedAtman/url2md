from typing import Dict, Optional

import html2text

from logger import logger
from utils.request import Request
from utils.response import Result


class URLToMarkdown:
    '''Convert URL(url / .html) to Markdown.
    '''

    @staticmethod
    def source_type(url: str):
        '''Detect source type, http or local file.
        '''
        return 'http' if url.strip()[:4] == 'http' else 'file'

    @classmethod
    def content(
        cls,
        url: str,
        method: str = 'GET',
        data: Optional[Dict[str, str]] = {},
    ):
        source_type = cls.source_type(url)
        if source_type == 'http':
            return Request.request(url, method=method, data=data)
        content = open(url, 'r', encoding='UTF-8').read()
        return Result(code=200, data=content)

    @classmethod
    def markdown(cls, url: str):
        result: Result = cls.content(url)
        assert result == 'Success'
        html = result.data
        # return html2text.html2text(html)
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = True
        # text_maker.bypass_tables = False
        return text_maker.handle(html)


if __name__ == '__main__':
    url = 'https://segmentfault.com/a/1190000021854441'
    url = 'https://www.cnblogs.com/NanZhiHan/p/16809977.html'
    md = URLToMarkdown.markdown(url)
    logger.info(md)
