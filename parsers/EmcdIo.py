from config import fake_ua
from decimal import Decimal
from models.ResultModel import ResultModel
from models.EmcdResponse import EmcdResult
from typing import Generator
from parsers.BaseParser import BaseParser
import requests
import json


class EmcdIo(BaseParser):
    __site__ = "emcd.io"

    def parse(self,) -> Generator[ResultModel, None, None]:
        resp = requests.get(self.url, headers=fake_ua,)

        j = EmcdResult.from_dict(json.loads(resp.text))
        share = float(str(j.coins.btc)) if j.coins.btc is not None else 0.0

        yield ResultModel('emcd.io', Decimal(2.5), Decimal(share))

