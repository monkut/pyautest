from pyautest.adapter.base_adapter import BaseAdapter
from pyautest.adapter.pil_image import PILImageAdapter

basic_adapters = [
    PILImageAdapter()
]

__all__ = (
    basic_adapters,
    BaseAdapter,
)
