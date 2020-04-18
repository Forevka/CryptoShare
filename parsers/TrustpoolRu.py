from config import fake_ua
from decimal import Decimal
from models.ResultModel import ResultModel
from models.TrustpoolRuResponse import TrustpoolRuResult
from typing import Generator
from parsers.BaseParser import BaseParser
import requests
import json


class TrustpoolRu(BaseParser):
    __site__ = "trustpool.ru"

    def parse(self,) -> Generator[ResultModel, None, None]:
        resp = requests.get(self.url, headers=fake_ua,)

        j = TrustpoolRuResult.from_dict(json.loads(resp.text))
        for coin in j.data:
            if (coin.coin.lower() == "btc"):
                share = float(str(coin.unit_output)) if coin.unit_output is not None else 0.0

                yield ResultModel('trustpool.ru', Decimal(2.5), Decimal(share))

