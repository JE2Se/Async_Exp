# -*- encoding:utf-8 -*-

#   异步并发的可能通用的脚本吧~
#   有一些漏洞可能还会有特殊的请求头，就不写了，多个逻辑而已，有需要自己添加
#   date=2019-06-14 17:23:55
__Author__ = "JE2Se"

import asyncio
import aiohttp
from fake_useragent import UserAgent
 
async def seedSMSpost(url, headers,data):
    conn = aiohttp.TCPConnector(verify_ssl = False)
    session = aiohttp.ClientSession(connector = conn) 
    response = await session.post(url, headers = headers,data = data)
    result = await response.text()
    session.close()
    return result

async def seedSMSget(url):
    conn = aiohttp.TCPConnector(verify_ssl = False)
    session = aiohttp.ClientSession(connector = conn) 
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result

async def requestpost():
    result = await seedSMSpost(url,headers,data)
    print(result)

async def requestget():
    result = await seedSMSget(url)
    print(result)

if __name__ == "__main__":
    ua = UserAgent(verify_ssl=False)
    headers = {'User-Agent':ua.random}
    caseCase = int(input("GET请求请输入「1」，POST请求请输入「2」:"))
    if caseCase == 1:
        url = str(input("请输入GET请求的链接："))
        threadCount = int(input("请输入短信发送的条数："))
        count = range(threadCount)
        tasks = [asyncio.ensure_future(requestget()) for _ in count]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
    else:
        url = str(input("请输入POST请求的链接："))
        data = str(input("请输入POST请求中的数据："))  #如修改手机号，需要再复制前修改
        threadCount = int(input("请输入发送的条数："))
        count = range(threadCount)
        tasks = [asyncio.ensure_future(requestpost()) for _ in count]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))

    