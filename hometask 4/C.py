import signal
import functools
from time import sleep


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def timeout(seconds=0.5):
    def decorator(func):
        if not seconds or seconds <= 0.: # если таймаута нет/он неположительный
            return func

        def handler(signum, frame):
            raise TimeoutException("Timed out")

        @functools.wraps(func)
        def new_func(*args, **kwargs):
            old = signal.signal(signal.SIGALRM, handler)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0) # если функция выполняется дольше таймаута, то выводить Timed out
                signal.signal(signal.SIGALRM, old)
        return new_func
    return decorator
