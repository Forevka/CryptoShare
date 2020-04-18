from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class CoinPrice:
    cny: Optional[str] = None
    usd: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CoinPrice':
        assert isinstance(obj, dict)
        cny = from_union([from_str, from_none], obj.get("CNY"))
        usd = from_union([from_str, from_none], obj.get("USD"))
        return CoinPrice(cny, usd)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CNY"] = from_union([from_str, from_none], self.cny)
        result["USD"] = from_union([from_str, from_none], self.usd)
        return result


@dataclass
class Profit:
    btc: Optional[str] = None
    cny: Optional[str] = None
    usd: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Profit':
        assert isinstance(obj, dict)
        btc = from_union([from_str, from_none], obj.get("BTC"))
        cny = from_union([from_str, from_none], obj.get("CNY"))
        usd = from_union([from_str, from_none], obj.get("USD"))
        return Profit(btc, cny, usd)

    def to_dict(self) -> dict:
        result: dict = {}
        result["BTC"] = from_union([from_str, from_none], self.btc)
        result["CNY"] = from_union([from_str, from_none], self.cny)
        result["USD"] = from_union([from_str, from_none], self.usd)
        return result


@dataclass
class Datum:
    hashrate: Optional[int] = None
    coin: Optional[str] = None
    coin_price: Optional[CoinPrice] = None
    diff: Optional[str] = None
    hash_unit: Optional[List[str]] = None
    pps_fee_rate: Optional[str] = None
    profit: Optional[Profit] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        hashrate = from_union([from_none, lambda x: int(from_str(x))], obj.get("hashrate"))
        coin = from_union([from_str, from_none], obj.get("coin"))
        coin_price = from_union([CoinPrice.from_dict, from_none], obj.get("coin_price"))
        diff = from_union([from_str, from_none], obj.get("diff"))
        hash_unit = from_union([lambda x: from_list(from_str, x), from_none], obj.get("hash_unit"))
        pps_fee_rate = from_union([from_str, from_none], obj.get("pps_fee_rate"))
        profit = from_union([Profit.from_dict, from_none], obj.get("profit"))
        return Datum(hashrate, coin, coin_price, diff, hash_unit, pps_fee_rate, profit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hashrate"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.hashrate)
        result["coin"] = from_union([from_str, from_none], self.coin)
        result["coin_price"] = from_union([lambda x: to_class(CoinPrice, x), from_none], self.coin_price)
        result["diff"] = from_union([from_str, from_none], self.diff)
        result["hash_unit"] = from_union([lambda x: from_list(from_str, x), from_none], self.hash_unit)
        result["pps_fee_rate"] = from_union([from_str, from_none], self.pps_fee_rate)
        result["profit"] = from_union([lambda x: to_class(Profit, x), from_none], self.profit)
        return result


@dataclass
class ViaBtcCOMResult:
    code: Optional[int] = None
    data: Optional[List[Datum]] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ViaBtcCOMResult':
        assert isinstance(obj, dict)
        code = from_union([from_int, from_none], obj.get("code"))
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        message = from_union([from_str, from_none], obj.get("message"))
        return ViaBtcCOMResult(code, data, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_int, from_none], self.code)
        result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        result["message"] = from_union([from_str, from_none], self.message)
        return result


def via_btc_com_result_from_dict(s: Any) -> ViaBtcCOMResult:
    return ViaBtcCOMResult.from_dict(s)


def via_btc_com_result_to_dict(x: ViaBtcCOMResult) -> Any:
    return to_class(ViaBtcCOMResult, x)
