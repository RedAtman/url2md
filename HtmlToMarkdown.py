from html2text import HTML2Text, html2text  # pip install html2text
import os
import requests


class HtmlToMarkdown(object):
  """ Doc of HtmlToMarkdown.

  Convert HTML(url / .html) to Markdown.

  Attribute:
    source: url / .html
  """

  def __init__(self, source):
    # super(HtmlToMarkdown, self).__init__()
    self.source = source
    self.html_handle = HTML2Text()

  @property
  def source_type(self):
    return 'http' if self.source.strip()[:4] == 'http' else 'file'

  @property
  def content(self):

    if self.source_type == 'http':
      headers = {
          'Referer': 'https://www.google.com/',
          'sec-fetch-mode': 'navigate',
          'upgrade-insecure-requests': '1',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
      }
      proxies = {
          # 'https': 'socks5://user:pass@host:port',
          'http': 'socks5://127.0.0.1:1086',
          'https': 'socks5://127.0.0.1:1086',
      }

      try:
        response = requests.get(
            self.source,
            headers=headers,
            proxies=proxies,
            timeout=(3.05, 27)   # (connection, read)
        ).content.decode('utf-8')
      except Exception as e:
        print(e)
        response = ''

      return response

    return open(source, 'r', encoding='UTF-8').read()

  def markdown(self):
    """ Convert to Markdown
    return: Markdown of String.
    """
    self.html_handle.ignore_links = True
    self.html_handle.ignore_images = True
    return html2text(self.content)

  def text(self):
    """ Convert to Text
    return: Text of String.
    """
    self.html_handle.ignore_links = True
    # self.html_handle.bypass_tables = False
    return self.html_handle.handle(self.content)


source = 'https://www.baidu.com/'
source = 'https://www.google.com/'
# source = 'https://www.twitter.com/'
# source = 'https://litets.com/article/2019/4/3/103.html'
# source = './baidu.html'
# source = 'https://zh.wikipedia.org/wiki/%E9%9F%93%E5%9C%8B%E9%83%A8%E7%BD%B2%E8%96%A9%E5%BE%B7%E5%8F%8D%E5%B0%8E%E5%BD%88%E7%B3%BB%E7%B5%B1%E4%BA%8B%E4%BB%B6'
# source = 'https://www.runoob.com/html/html-tables.html'

obj = HtmlToMarkdown(source)
# print(obj.source)
# print(obj.content)
print(obj.markdown())
# print(obj.text())
# print(obj.test())
# print(obj.run())
