from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class HashrateUnit(Enum):
    P = "P"


@dataclass
class PoolsHashrate:
    count: Optional[int] = None
    pool_id: Optional[int] = None
    relayed_by: Optional[str] = None
    pool_share: Optional[float] = None
    hash_share: Optional[float] = None
    link: Optional[str] = None
    real_hashrate: Optional[str] = None
    diff_24_h: Optional[float] = None
    pool_name: Optional[str] = None
    pool_icon_class: Optional[str] = None
    icon_link: Optional[str] = None
    hashrate: Optional[float] = None
    hashrate_unit: Optional[HashrateUnit] = None
    lucky: Optional[float] = None
    cur2_max_percent: Optional[float] = None
    index: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PoolsHashrate':
        assert isinstance(obj, dict)
        count = from_union([from_none, lambda x: int(from_str(x))], obj.get("count"))
        pool_id = from_union([from_none, lambda x: int(from_str(x))], obj.get("pool_id"))
        relayed_by = from_union([from_str, from_none], obj.get("relayed_by"))
        pool_share = from_union([from_float, from_none], obj.get("pool_share"))
        hash_share = from_union([from_float, from_none], obj.get("hash_share"))
        link = from_union([from_str, from_none], obj.get("link"))
        real_hashrate = from_union([from_none, from_str], obj.get("real_hashrate"))
        diff_24_h = from_union([from_float, from_none], obj.get("diff_24h"))
        pool_name = from_union([from_str, from_none], obj.get("pool_name"))
        pool_icon_class = from_union([from_str, from_none], obj.get("pool_icon_class"))
        icon_link = from_union([from_str, from_none], obj.get("icon_link"))
        hashrate = from_union([from_float, from_none], obj.get("hashrate"))
        hashrate_unit = from_union([HashrateUnit, from_none], obj.get("hashrate_unit"))
        lucky = from_union([from_float, from_none], obj.get("lucky"))
        cur2_max_percent = from_union([from_float, from_none], obj.get("cur2max_percent"))
        index = from_union([from_int, from_none], obj.get("index"))
        return PoolsHashrate(count, pool_id, relayed_by, pool_share, hash_share, link, real_hashrate, diff_24_h, pool_name, pool_icon_class, icon_link, hashrate, hashrate_unit, lucky, cur2_max_percent, index)

    def to_dict(self) -> dict:
        result: dict = {}
        result["count"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.count)
        result["pool_id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.pool_id)
        result["relayed_by"] = from_union([from_str, from_none], self.relayed_by)
        result["pool_share"] = from_union([to_float, from_none], self.pool_share)
        result["hash_share"] = from_union([to_float, from_none], self.hash_share)
        result["link"] = from_union([from_str, from_none], self.link)
        result["real_hashrate"] = from_union([from_none, from_str], self.real_hashrate)
        result["diff_24h"] = from_union([to_float, from_none], self.diff_24_h)
        result["pool_name"] = from_union([from_str, from_none], self.pool_name)
        result["pool_icon_class"] = from_union([from_str, from_none], self.pool_icon_class)
        result["icon_link"] = from_union([from_str, from_none], self.icon_link)
        result["hashrate"] = from_union([to_float, from_none], self.hashrate)
        result["hashrate_unit"] = from_union([lambda x: to_enum(HashrateUnit, x), from_none], self.hashrate_unit)
        result["lucky"] = from_union([to_float, from_none], self.lucky)
        result["cur2max_percent"] = from_union([to_float, from_none], self.cur2_max_percent)
        result["index"] = from_union([from_int, from_none], self.index)
        return result


@dataclass
class Data:
    pools_hashrate: Optional[List[PoolsHashrate]] = None
    pools_compute_hashrate: Optional[List[PoolsHashrate]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        pools_hashrate = from_union([lambda x: from_list(PoolsHashrate.from_dict, x), from_none], obj.get("pools_hashrate"))
        pools_compute_hashrate = from_union([lambda x: from_list(PoolsHashrate.from_dict, x), from_none], obj.get("pools_compute_hashrate"))
        return Data(pools_hashrate, pools_compute_hashrate)

    def to_dict(self) -> dict:
        result: dict = {}
        result["pools_hashrate"] = from_union([lambda x: from_list(lambda x: to_class(PoolsHashrate, x), x), from_none], self.pools_hashrate)
        result["pools_compute_hashrate"] = from_union([lambda x: from_list(lambda x: to_class(PoolsHashrate, x), x), from_none], self.pools_compute_hashrate)
        return result


@dataclass
class BtcComResult:
    err_no: Optional[int] = None
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BtcComResult':
        assert isinstance(obj, dict)
        err_no = from_union([from_int, from_none], obj.get("err_no"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return BtcComResult(err_no, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["err_no"] = from_union([from_int, from_none], self.err_no)
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def BtcComResult_from_dict(s: Any) -> BtcComResult:
    return BtcComResult.from_dict(s)


def BtcComResult_to_dict(x: BtcComResult) -> Any:
    return to_class(BtcComResult, x)
