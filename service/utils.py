from typing import List, Dict
import toolz as t

@t.curry
def has_all_keys(keys: List[str], d: Dict[str, str]) -> bool:
    return all(k in d for k in keys)