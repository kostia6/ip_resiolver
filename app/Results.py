from requests import Response


class Results:

    def __init__(self):
        self._results = {}
        self._data = {}
        self._total_time = 0
        self._status = True

    def reset(self):
        self._results.clear()
        self._data.clear()

    def add_result(self, r: Response, name: str, t: float):
        success = True if r.status_code == 200 else False
        self._results[name] = {'time': f'{t:.3f}', 'status': success}
        self._total_time += t
        self._status = self._status and success
        self._data[name] = r.json()

    def get_results(self):
        total_stats = {'total': {'time': f'{self._total_time:.3f}', 'status': self._status}}
        return {'stats': total_stats | self._results}

    def get_data(self):
        return self._data
