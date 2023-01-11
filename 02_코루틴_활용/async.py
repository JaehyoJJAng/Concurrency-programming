from typing import List
import aiohttp
import time
import asyncio

def no_with_context(url:str)-> None:
    # Session Open
    session = rq.Session()
    # session get
    session.get(url=url)

async def use_with_context(url:str)-> None:
    # aiohttp로 Session Open
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            if response.ok:
                return await response.text()

# fetcher 자체를 코루틴으로 정의
async def fetcher(url:str)-> None:
    # Get Response
    response = await use_with_context(url=url)
    print(response.status_code)

async def main()-> None:
    urls : str = ['https://www.naver.com','https://www.google.com']

    # Execute Fetch
    [await fetcher(url=url) for url in urls]
    
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)