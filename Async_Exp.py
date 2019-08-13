# -*- encoding: utf-8 -*-
'''
@File : Async_Exp.py
@Time : 2019/08/13 14:16:33
@Author : JE2Se 
@Version : 2.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''




#   异步并发的可能通用的脚本吧~
#   有一些漏洞可能还会有特殊的请求头，就不写了，多个逻辑而已，有需要自己添加


import asyncio
import aiohttp
 
async def seedSMSpost(url,data):
    conn = aiohttp.TCPConnector(ssl = False)
    session = aiohttp.ClientSession(connector = conn) 
    response = await session.post(url,headers = header,data = data)
    result = await response.text()
    print(result)
    await session.close()

async def seedSMSget(url):
    conn = aiohttp.TCPConnector(ssl = False)
    session = aiohttp.ClientSession(connector = conn) 
    response = await session.get(url,headers = header)
    result = await response.text()
    print(result)
    await session.close()


async def requestpost():
    await seedSMSpost(url,data)

async def requestget():
    await seedSMSget(url)

if __name__ == "__main__":
    try:
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
            "Accept": "application/json, text/plain, */*",
            "Connection": "close"
            } 
        caseCase = int(input("GET请求请输入「1」，POST请求请输入「2」:"))
        if caseCase == 1:
            url = str(input("请输入GET请求的链接："))
            if 'http' not in url:
                print("请在请求前添加http(s)://") 
                url = str(input("请输入GET请求的链接："))   
                threadCount = int(input("请输入发送的条数："))
                count = range(threadCount)
                tasks = [asyncio.ensure_future(requestget()) for _ in count]
                loop = asyncio.get_event_loop()
                loop.run_until_complete(asyncio.wait(tasks))
                print("%d条信息已发送成功~"% threadCount)
            else:
                threadCount = int(input("请输入发送的条数："))
                count = range(threadCount)
                tasks = [asyncio.ensure_future(requestget()) for _ in count]
                loop = asyncio.get_event_loop()
                loop.run_until_complete(asyncio.wait(tasks))
                print("%d条信息已发送成功~"% threadCount)
        else:
            url = str(input("请输入POST请求的链接："))
            if 'http' not in url:
                print("请在请求前添加http(s)://")
                url = str(input("请输入POST请求的链接："))
                data = str(input("请输入POST请求中的数据：")) #如修改手机号，需要再复制前修改
                threadCount = int(input("请输入发送的条数："))
                count = range(threadCount)
                tasks = [asyncio.ensure_future(requestpost()) for _ in count]
                loop = asyncio.get_event_loop()
                loop.run_until_complete(asyncio.wait(tasks))
                print("%d条信息已发送成功~"% threadCount)
            else:
                data = str(input("请输入POST请求中的数据："))  #如修改手机号，需要再复制前修改
                threadCount = int(input("请输入发送的条数："))
                count = range(threadCount)
                tasks = [asyncio.ensure_future(requestpost()) for _ in count]
                loop = asyncio.get_event_loop()
                loop.run_until_complete(asyncio.wait(tasks))
                print("%d条信息已发送成功~"% threadCount)
    except:
        print("请检查输入的有效性")