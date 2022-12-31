import time

from Query import Query
from Results import Results


class MyManager:

    API_1 = ['ip-api', 'http://ip-api.com/json/<ip>']
    API_2 = ['freeipapi', 'https://freeipapi.com/api/json/<ip>']

    def __init__(self):
        self._queries = [self.API_1, self.API_2]

    def query_ip(self, ip: str):
        res = Results()
        for q in self._queries:
            ts = time.time()
            res.add_result(Query.perform(ip, q), name=q[0], t=time.time() - ts)

        return {"stats": res.get_results(), "data": res.get_data()}
