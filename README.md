copyheaders
===========

方便的从浏览器复制headers

本项目是从https://github.com/scrapy/w3lib 修改过来的

为什么要修改请看https://github.com/scrapy/w3lib/issues/90


Sample Code
-----------

```python
from copyheaders import headers_raw_to_dict
import requests

headers_raw = b"""Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
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
z = requests.get('https://httpbin.org/',headers=headers)
```
Installation
------------
* `pip install copyheaders`


