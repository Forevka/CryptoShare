import abc
from models.ResultModel import ResultModel
import typing

class IParser(abc.ABC):
    @abc.abstractmethod
    def parse(self,) -> typing.Generator[ResultModel, None, None]:
        pass


class BaseParser(IParser):
    __site__: str

    url: str

    def __init__(self, url: str):
        self.url = url