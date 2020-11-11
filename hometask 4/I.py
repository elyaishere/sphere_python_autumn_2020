from copy import deepcopy


class FragileDict:
    def __init__(self, d=dict()):
        self._data = deepcopy(d)
        self._lock = True

    def __getitem__(self, key):
        return deepcopy(self._data[key]) if self._lock else self._data[key]

    def __enter__(self):
        self._lock = False
        self.tmp = deepcopy(self._data)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._lock = True
        if exc_type is not None:
            self._data = self.tmp
            print("Exception has been suppressed.")
        if self._data == self.tmp:
            self._data = self.tmp
        else:
            self._data = deepcopy(self._data)
        delattr(self, 'tmp')
        return True

    def __setitem__(self, key, value):
        if self._lock:
            raise RuntimeError("Protected state")
        self._data[key] = value

    def __contains__(self, key):
        return key in self._data
