from config import fake_ua
from decimal import Decimal
from models.ResultModel import ResultModel
from models.ViaBtcComResponse import ViaBtcCOMResult
from typing import Generator
from parsers.BaseParser import BaseParser
import requests
import json


class ViabtcCom(BaseParser):
    __site__ = "viabtc.com"

    def parse(self,) -> Generator[ResultModel, None, None]:
        resp = requests.get(self.url, headers=fake_ua,)

        j = ViaBtcCOMResult.from_dict(json.loads(resp.text))
        for coin in j.data:
            if (coin.coin.lower() == "btc"):
                share = float(str(coin.profit.btc)) if coin.profit.btc is not None else 0.0

                yield ResultModel('viabtc.com', Decimal(2.5), Decimal(share))

