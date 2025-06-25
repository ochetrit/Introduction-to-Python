import math
from typing import Any

def NULL_not_found(obj: Any) -> int:
    checks = [
        ("Nothing", lambda x: x is None, type(None)),
        ("Garlic", lambda x: isinstance(x, float) and math.isnan(x), float),
        ("Zero",   lambda x: isinstance(x, int) and x == 0, int),
        ("Empty",  lambda x: isinstance(x, str) and x == '', str),
        ("Fake",   lambda x: isinstance(x, bool) and x is False, bool),
    ]

    for label, condition, obj_type in checks:
        if condition(obj):
            print(f"{label}: {obj_type}")
            return 0

    print("Type not found")
    return 1