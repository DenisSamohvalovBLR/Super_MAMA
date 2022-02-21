import datetime
from dataclasses import dataclass

from errors import BrokenTimerError


@dataclass
class Timer:
    start: datetime
    stop: datetime = None


@dataclass
class LeftTimer(Timer):
    side: str = "left"


@dataclass
class RightTimer(Timer):
    side: str = "right"


@dataclass
class SleepTimer(Timer):
    sleep: str = "sleep"


def create_timer(side: str = None, sleep: bool = False):
    start = datetime.datetime.now()
    if sleep:
        return SleepTimer(start=start)

    if side and side == "left":
        return LeftTimer(start=start)
    elif side and side == "right":
        return RightTimer(start=start)

    raise BrokenTimerError


def stop_timer(side: str = None, sleep: bool = False):
    stop = datetime.datetime.now()
    if sleep:
        return SleepTimer(start=stop)

    if side and side == "left":
        return LeftTimer(start=stop)
    elif side and side == "right":
        return RightTimer(start=stop)

    raise BrokenTimerError


if __name__ == '__main__':
    a = create_timer(sleep=True)
    print(a)
    b = stop_timer(side="right")
    print(b)
