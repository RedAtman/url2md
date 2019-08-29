# HtmlToMarkdown
- Converting HTML(url / .html) to Markdown or Plain Text.
- 转换HTML（支持url或本地html文件）为Markdown格式 或 Text纯文本。

table2md.py（已废弃）手动实现table转Markdown。

## Environment
    python 3.6.0

## Usage

1. 安装依赖

    pip install -r requirements.txt

2. 实例化并获取Markdown or Text

    source = 'https://www.baidu.com/'
    obj = HtmlToMarkdown(source)

    print(obj.markdown())
    print(obj.text())