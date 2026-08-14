from typing import TypeIs


def isNull[T](var: T | None) -> TypeIs[None]:
    if isinstance(var, list):
        return bool(not var or len(var) <= 0)
    else:
        return var is None
