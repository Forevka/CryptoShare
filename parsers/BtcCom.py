from config import fake_ua
from decimal import Decimal
from models.ResultModel import ResultModel
from models.BtcComResponse import BtcComResult
from typing import Generator
from parsers.BaseParser import BaseParser
import requests
import json


class BtcComParser(BaseParser):
    __site__ = "BTC.com"

    def parse(self,) -> Generator[ResultModel, None, None]:
        resp = requests.get(self.url, headers=fake_ua,)

        for i in BtcComResult.from_dict(json.loads(resp.text,)).data.pools_hashrate:
            share = i.pool_share if i.pool_share is not None else 0.0
            name = i.relayed_by if i.relayed_by is not None else 'Cant Recognize Name'
            yield ResultModel(name, Decimal(2.5), Decimal(share))

