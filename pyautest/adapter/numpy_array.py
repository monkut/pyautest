import numpy

from PIL import Image

from pyautest.adapter.base_adapter import BaseAdapter, T, PathType


class NumpyArrayAdapter(BaseAdapter[numpy.ndarray]):
    @property
    def target_class(self):
        return numpy.ndarray

    def save(self, obj: numpy.ndarray, path: PathType):
        return numpy.savez(path)

    def load(self, path: PathType) -> Image.Image:
        return numpy.load(path)

    @property
    def file_extension(self):
        return 'npz'

    def equal(self, obj1: T, obj2: T) -> bool:
        return numpy.array_equal(obj1, obj2)

    def diff_description(self, obj1: T, obj2: T) -> str:
        return super().diff_description(obj1, obj2)
