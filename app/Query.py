import threading
import time
import requests
from typing import List


class Query:

    cache = {}
    lock = threading.Lock()
    TTL = 60

    @staticmethod
    def perform(ip: str, api: List[str]):
        ts = time.time()
        with Query.lock:
            name = api[0]
            if name in Query.cache:
                if Query.cache[name]['time'] + Query.TTL >= time.time():
                    return Query.cache[name]['res'], name, time.time() - ts
                else:
                    del Query.cache[name]

            url = api[1].replace('<ip>', ip)
            r = requests.get(url)
            Query.cache[name] = {'res': r, 'time': time.time()}

            return r, name, time.time() - ts


