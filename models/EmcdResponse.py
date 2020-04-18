# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = result_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Coins:
    btc: Optional[str] = None
    ltc: Optional[str] = None
    bsv: Optional[str] = None
    bch: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Coins':
        assert isinstance(obj, dict)
        btc = from_union([from_str, from_none], obj.get("btc"))
        ltc = from_union([from_str, from_none], obj.get("ltc"))
        bsv = from_union([from_str, from_none], obj.get("bsv"))
        bch = from_union([from_str, from_none], obj.get("bch"))
        return Coins(btc, ltc, bsv, bch)

    def to_dict(self) -> dict:
        result: dict = {}
        result["btc"] = from_union([from_str, from_none], self.btc)
        result["ltc"] = from_union([from_str, from_none], self.ltc)
        result["bsv"] = from_union([from_str, from_none], self.bsv)
        result["bch"] = from_union([from_str, from_none], self.bch)
        return result


@dataclass
class EmcdResult:
    coins: Optional[Coins] = None
    code: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EmcdResult':
        assert isinstance(obj, dict)
        coins = from_union([Coins.from_dict, from_none], obj.get("coins"))
        code = from_union([from_int, from_none], obj.get("code"))
        return EmcdResult(coins, code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["coins"] = from_union([lambda x: to_class(Coins, x), from_none], self.coins)
        result["code"] = from_union([from_int, from_none], self.code)
        return result


def result_from_dict(s: Any) -> EmcdResult:
    return EmcdResult.from_dict(s)


def result_to_dict(x: EmcdResult) -> Any:
    return to_class(EmcdResult, x)
