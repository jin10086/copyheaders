import requests
import re


def headers_raw_to_dict(headers_raw):
    r"""
    Convert raw headers (single multi-line bytestring)
    to a dictionary.

    For example:

    >>> from copyheaders import headers_raw_to_dict
    >>> headers_raw_to_dict(b"Content-type: text/html\n\rAccept: gzip\n\n")   # doctest: +SKIP
    {'Content-type': ['text/html'], 'Accept': ['gzip']}

    Incorrect input:

    >>> headers_raw_to_dict(b"Content-typt gzip\n\n")
    {}
    >>>

    Argument is ``None`` (return ``None``):

    >>> headers_raw_to_dict(None)
    >>>

    """

    if headers_raw:
        headers_raw = re.sub(r'$', '\n$', headers_raw)
        result_dict = dict(re.findall(r'(.*?):(.*?)\n', headers_raw))
    else:
        result_dict = None    

    return result_dict


def main():
    headers_raw = """Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate, br
Accept-Language:zh-CN,zh;q=0.8,zh-TW;q=0.6
Cache-Control:max-age=0
Connection:keep-alive
Cookie:_gauges_unique_year=1; _gauges_unique=1; _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1
Host:httpbin.org
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"""

    headers = headers_raw_to_dict(headers_raw)
    # 然后就可以在requests中直接用了
    z = requests.get('https://httpbin.org/', headers=headers)


if __name__ == '__main__':
    main()

