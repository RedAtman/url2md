import json
import logging
import urllib
import urllib.error
import urllib.parse
import urllib.request
from http.client import HTTPResponse
from typing import Dict, Optional

from .response import Result

logger = logging.getLogger()


class Request:

    proxies = {
        # 'https': 'socks5://user:pass@host:port',
        # 'http': 'socks5://127.0.0.1:1086',
        # 'https': 'socks5://127.0.0.1:1086',
    }
    # Get your real headers: https://httpbin.org/get https://myhttpheader.com/
    default_headers: Dict[str, str] = {
        # 'Content-Type': 'application/json',
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        # "Host": "httpbin.org",
        # "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        # "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        # "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        # "Sec-Fetch-Site": "none",
        # "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "User-Agent": "Magic Browser",
        "Referer": "https://www.google.com/",
    }
    auth_headers = classmethod(
        property(
            lambda cls: {
                # 'Authorization': f'Bearer {cls.token}',
                # 'Cookie': 'SESSION_COOKIE_NAME_PREFIX=jms_',
            }
        )
    )
    headers = classmethod(
        property(lambda cls: dict(cls.default_headers, **cls.auth_headers))
    )

    @staticmethod
    def parse(response: HTTPResponse) -> Result:
        try:
            encoding = response.info().get("Content-Encoding")
            # logger.debug(encoding)
            if encoding == "gzip":
                import zlib

                content = zlib.decompress(response.read(), 16 + zlib.MAX_WBITS).decode(
                    "utf-8"
                )
            else:
                content = response.read()
                # content = response.read().decode('utf-8')
                # content = response.read().decode('gbk')
                # content = json.loads(response.read().decode('utf-8'))
            # logger.debug(type(content))
            # logger.debug(content)
        except Exception as err:
            logger.exception(err)
            return Result(code=response.status, msg=err)
        return Result(code=response.status, data=content)

    @classmethod
    def _request(
        cls,
        url: str,
        method: str = "GET",
        headers: Dict[str, str] = {},
        data: Optional[Dict[str, str]] = {},
    ):
        if method.upper() == "GET":
            # url = '?' + urllib.parse.urlencode({url}, data=bytes(json.dumps(data), encoding="utf-8"))
            # data = urllib.parse.urlencode(data)
            url += "?" + urllib.parse.urlencode(data)
            data = None
        elif method.upper() == "POST":
            # data = urllib.parse.urlencode(data).encode('utf-8')
            # data = json.dumps(data).encode('utf-8')
            json_str = json.dumps(data)
            data = json_str.encode("utf-8", "strict")
        else:
            raise Exception("method must be GET or POST")

        headers = headers or cls.headers
        try:
            request = urllib.request.Request(
                url,
                data=data,
                headers=headers,
                method=method,
                # origin_req_host="45.90.208.135",
            )
            response: HTTPResponse = urllib.request.urlopen(request)
        # except ConnectionRefusedError as err:
        except urllib.error.HTTPError as err:
            if err.code == 401:
                return Result(code=err.code, msg=err)
            raise err
        except urllib.error.URLError as err:
            if isinstance(err.reason, ConnectionRefusedError):
                raise Exception(f"Please check: server is running")
            return Result(code=400, msg=err)
        if response.status >= 200 and response.status < 400:
            return cls.parse(response)
        return Result(code=response.status, data=response.__dict__)

    @classmethod
    def request(
        cls,
        url: str,
        method: str = "GET",
        headers: Dict[str, str] = {},
        data: Optional[Dict[str, str]] = {},
    ) -> Result:
        return cls._request(url, method=method, headers=headers, data=data)


if __name__ == "__main__":
    url = "https://httpbin.org/get"
    url = "https://www.cnblogs.com/NanZhiHan/p/16809977.html"
    result = Request.request(url=url, method="GET", data={})
    assert result == 200
    assert result == "Success"
    logger.info(result)
    print(result.code)
