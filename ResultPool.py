from decimal import Decimal
from config import commisions, sites
from models.ResultModel import ResultModel
from parsers.BaseParser import BaseParser
from typing import List, Type


class ResultPool:
    parsers: List[Type[BaseParser]]
    results: List[ResultModel]

    def __init__(self,):
        self.parsers = []
        self.results = []

    def attach_parser(self, *parsers: Type[BaseParser],) -> None:
        return self.parsers.extend(list(parsers))

    def parse(self,) -> List[ResultModel]:
        self.results: List[ResultModel] = []

        for parser in self.parsers:
            instance = parser(sites.get(parser.__site__.lower(), ''))
            self.results.extend(list(instance.parse()))
        
        self._load_commision()

        return self.results
    
    def _load_commision(self,) -> None:
        for res in self.results:
            res.commission = Decimal(commisions.get(res.site_name.lower(), 0.0))
    