import pickle
from itertools import zip_longest
from typing import Union, List

from pyautest.adapter.base_adapter import BaseAdapter, T, PathType

ObjectType = Union[int, float, str, list, dict, set]

# TODO(higumachan): 今はpickleでdumpしてるが、jsonにできるものはjsonにして見て確認しやすくしたい。


class BasicPyobjectsAdapter(BaseAdapter[ObjectType]):
    @property
    def target_classes(self) -> List[type]:
        return [int, float, str, list, dict, set, tuple]

    def save(self, obj: ObjectType, path: PathType):
        return pickle.dump(obj, path.open("wb"))

    def load(self, path: PathType) -> ObjectType:
        return pickle.load(path.open("rb"))

    @property
    def file_extension(self):
        return 'pkl'

    def equal(self, obj1: ObjectType, obj2: ObjectType) -> bool:
        iteratives = (list, set, tuple)
        if isinstance(obj1, iteratives) and isinstance(obj2, iteratives):
            return all(self.equal(o1, o2) for o1, o2 in zip_longest(obj1, obj2))
        if isinstance(obj1, dict) and isinstance(obj2, dict):
            obj1_keys = set(obj1.keys())
            obj2_keys = set(obj2.keys())
            added_keys = obj1_keys - obj2_keys
            removed_keys = obj2_keys - obj1_keys
            if added_keys or removed_keys:
                return False
            # keys are the same
            return all(self.equal(obj1[k], obj2[k]) for k in obj1_keys)

        if isinstance(obj1, float) and isinstance(obj2, float):
            return abs(obj1 - obj2) < self.allowable_error
        return obj1 == obj2

    def diff_description(self, obj1: T, obj2: T) -> str:
        return super().diff_description(obj1, obj2)
