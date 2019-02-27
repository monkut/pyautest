from abc import ABC, abstractmethod
from pathlib import Path
from typing import TypeVar, Union, Generic

T = TypeVar('T')
PathType = Union[Path, str]


class BaseAdapter(ABC, Generic[T]):
    @abstractmethod
    def save(self, obj: T, path: PathType):
        pass

    @abstractmethod
    def load(self, path: PathType) -> T:
        pass

    def equal(self, obj1: T, obj2: T) -> bool:
        return obj1 == obj2

    @property
    @abstractmethod
    def file_extension(self):
        pass

    @property
    @abstractmethod
    def target_class(self):
        pass

    def diff_description(self, obj1: T, obj2: T) -> str:
        return "no diff description"
