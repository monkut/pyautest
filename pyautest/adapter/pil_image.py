from PIL import Image

from pyautest.adapter.base_adapter import BaseAdapter, T, PathType


class PILImageAdapter(BaseAdapter[Image.Image]):
    @property
    def target_class(self):
        return Image.Image

    def save(self, obj: Image.Image, path: PathType):
        return obj.save(path)

    def load(self, path: PathType) -> Image.Image:
        return Image.open(path)

    @property
    def file_extension(self):
        return 'png'

    def diff_description(self, obj1: T, obj2: T) -> str:
        return super().diff_description(obj1, obj2)
