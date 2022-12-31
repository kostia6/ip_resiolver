import concurrent
import time
from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor

from Query import Query
from Results import Results


class MyManager:

    API_1 = ['ip-api', 'http://ip-api.com/json/<ip>']
    API_2 = ['freeipapi', 'https://freeipapi.com/api/json/<ip>']

    def __init__(self):
        self._queries = [self.API_1, self.API_2]

    def query_ip(self, ip: str):
        res = Results()
        ts = time.time()
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(Query.perform, ip, q) for q in self._queries]
            for future in concurrent.futures.as_completed(futures):
                response = future.result()
                res.add_result(*response)

        res.add_total_time(time.time()-ts)
        return {"stats": res.get_results(), "data": res.get_data()}
