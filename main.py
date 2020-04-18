from parsers.TrustpoolRu import TrustpoolRu
from parsers.ViabtcCom import ViabtcCom
from parsers.EmcdIo import EmcdIo
from ResultPool import ResultPool
from parsers.BtcCom import BtcComParser

if __name__ == "__main__":
    pool = ResultPool()
    
    pool.attach_parser(
        BtcComParser, TrustpoolRu,
        EmcdIo, ViabtcCom,
    )

    for i in pool.parse():
        print(i)