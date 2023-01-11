from typing import List
import requests as rq
import time

def no_with_context(url:str)-> None:
    # Session Open
    session = rq.Session()
    # session get
    session.get(url=url)

def use_with_context(url:str)-> None:
    # session open
    with rq.Session() as session:
        with session.get(url=url) as response:
            if response.ok:
                return response

def fetch(url:str)-> None:
    # Get Response
    response = use_with_context(url=url)
    print(response.status_code)

def main()-> None:
    urls : str = ['https://www.naver.com','https://www.google.com']

    # Execute Fetch
    [fetch(url=url) for url in urls]
    
if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)