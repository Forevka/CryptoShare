from parsers.EmcdIo import EmcdIo
from ResultPool import ResultPool
from parsers.BtcCom import BtcComParser


if __name__ == "__main__":
    pool = ResultPool()
    pool.attach_parser(BtcComParser)
    pool.attach_parser(EmcdIo)

    for i in pool.parse():
        print(i)