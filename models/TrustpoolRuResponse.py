from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Datum:
    payment_end_time: Optional[int] = None
    payment_start_time: Optional[int] = None
    block_reward: Optional[str] = None
    block_time: Optional[int] = None
    coin: Optional[str] = None
    coin_price: Optional[str] = None
    curr_connections: Optional[int] = None
    curr_diff: Optional[str] = None
    curr_period_rest_time: Optional[int] = None
    hash_unit: Optional[str] = None
    min_payment_amount: Optional[str] = None
    mining_algorithm: Optional[str] = None
    network_hashrate: Optional[str] = None
    network_hashrate_1_days: Optional[str] = None
    network_hashrate_3_days: Optional[str] = None
    network_hashrate_7_days: Optional[str] = None
    next_period_diff: Optional[str] = None
    next_period_diff_float_rate: Optional[str] = None
    pool_hashrate: Optional[str] = None
    pre_period_diff: Optional[str] = None
    pre_period_diff_float_rate: Optional[str] = None
    pre_period_rest_time: Optional[int] = None
    pricing_currency: Optional[str] = None
    pricing_currency_symbol: Optional[str] = None
    unit_output: Optional[str] = None
    unit_output_currency: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        payment_end_time = from_union([from_none, lambda x: int(from_str(x))], obj.get("payment_end_time"))
        payment_start_time = from_union([from_none, lambda x: int(from_str(x))], obj.get("payment_start_time"))
        block_reward = from_union([from_str, from_none], obj.get("block_reward"))
        block_time = from_union([from_int, from_none], obj.get("block_time"))
        coin = from_union([from_str, from_none], obj.get("coin"))
        coin_price = from_union([from_str, from_none], obj.get("coin_price"))
        curr_connections = from_union([from_int, from_none], obj.get("curr_connections"))
        curr_diff = from_union([from_str, from_none], obj.get("curr_diff"))
        curr_period_rest_time = from_union([from_int, from_none], obj.get("curr_period_rest_time"))
        hash_unit = from_union([from_str, from_none], obj.get("hash_unit"))
        min_payment_amount = from_union([from_str, from_none], obj.get("min_payment_amount"))
        mining_algorithm = from_union([from_str, from_none], obj.get("mining_algorithm"))
        network_hashrate = from_union([from_str, from_none], obj.get("network_hashrate"))
        network_hashrate_1_days = from_union([from_str, from_none], obj.get("network_hashrate_1days"))
        network_hashrate_3_days = from_union([from_str, from_none], obj.get("network_hashrate_3days"))
        network_hashrate_7_days = from_union([from_str, from_none], obj.get("network_hashrate_7days"))
        next_period_diff = from_union([from_none, from_str], obj.get("next_period_diff"))
        next_period_diff_float_rate = from_union([from_none, from_str], obj.get("next_period_diff_float_rate"))
        pool_hashrate = from_union([from_str, from_none], obj.get("pool_hashrate"))
        pre_period_diff = from_union([from_none, from_str], obj.get("pre_period_diff"))
        pre_period_diff_float_rate = from_union([from_none, from_str], obj.get("pre_period_diff_float_rate"))
        pre_period_rest_time = from_union([from_int, from_none], obj.get("pre_period_rest_time"))
        pricing_currency = from_union([from_str, from_none], obj.get("pricing_currency"))
        pricing_currency_symbol = from_union([from_str, from_none], obj.get("pricing_currency_symbol"))
        unit_output = from_union([from_str, from_none], obj.get("unit_output"))
        unit_output_currency = from_union([from_str, from_none], obj.get("unit_output_currency"))
        return Datum(payment_end_time, payment_start_time, block_reward, block_time, coin, coin_price, curr_connections, curr_diff, curr_period_rest_time, hash_unit, min_payment_amount, mining_algorithm, network_hashrate, network_hashrate_1_days, network_hashrate_3_days, network_hashrate_7_days, next_period_diff, next_period_diff_float_rate, pool_hashrate, pre_period_diff, pre_period_diff_float_rate, pre_period_rest_time, pricing_currency, pricing_currency_symbol, unit_output, unit_output_currency)

    def to_dict(self) -> dict:
        result: dict = {}
        result["payment_end_time"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.payment_end_time)
        result["payment_start_time"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.payment_start_time)
        result["block_reward"] = from_union([from_str, from_none], self.block_reward)
        result["block_time"] = from_union([from_int, from_none], self.block_time)
        result["coin"] = from_union([from_str, from_none], self.coin)
        result["coin_price"] = from_union([from_str, from_none], self.coin_price)
        result["curr_connections"] = from_union([from_int, from_none], self.curr_connections)
        result["curr_diff"] = from_union([from_str, from_none], self.curr_diff)
        result["curr_period_rest_time"] = from_union([from_int, from_none], self.curr_period_rest_time)
        result["hash_unit"] = from_union([from_str, from_none], self.hash_unit)
        result["min_payment_amount"] = from_union([from_str, from_none], self.min_payment_amount)
        result["mining_algorithm"] = from_union([from_str, from_none], self.mining_algorithm)
        result["network_hashrate"] = from_union([from_str, from_none], self.network_hashrate)
        result["network_hashrate_1days"] = from_union([from_str, from_none], self.network_hashrate_1_days)
        result["network_hashrate_3days"] = from_union([from_str, from_none], self.network_hashrate_3_days)
        result["network_hashrate_7days"] = from_union([from_str, from_none], self.network_hashrate_7_days)
        result["next_period_diff"] = from_union([from_none, from_str], self.next_period_diff)
        result["next_period_diff_float_rate"] = from_union([from_none, from_str], self.next_period_diff_float_rate)
        result["pool_hashrate"] = from_union([from_str, from_none], self.pool_hashrate)
        result["pre_period_diff"] = from_union([from_none, from_str], self.pre_period_diff)
        result["pre_period_diff_float_rate"] = from_union([from_none, from_str], self.pre_period_diff_float_rate)
        result["pre_period_rest_time"] = from_union([from_int, from_none], self.pre_period_rest_time)
        result["pricing_currency"] = from_union([from_str, from_none], self.pricing_currency)
        result["pricing_currency_symbol"] = from_union([from_str, from_none], self.pricing_currency_symbol)
        result["unit_output"] = from_union([from_str, from_none], self.unit_output)
        result["unit_output_currency"] = from_union([from_str, from_none], self.unit_output_currency)
        return result


@dataclass
class TrustpoolRuResult:
    code: Optional[int] = None
    data: Optional[List[Datum]] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TrustpoolRuResult':
        assert isinstance(obj, dict)
        code = from_union([from_int, from_none], obj.get("code"))
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        message = from_union([from_str, from_none], obj.get("message"))
        return TrustpoolRuResult(code, data, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_int, from_none], self.code)
        result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        result["message"] = from_union([from_str, from_none], self.message)
        return result


def trustpool_ru_result_from_dict(s: Any) -> TrustpoolRuResult:
    return TrustpoolRuResult.from_dict(s)


def trustpool_ru_result_to_dict(x: TrustpoolRuResult) -> Any:
    return to_class(TrustpoolRuResult, x)
