from pyautest.adapter.base_adapter import BaseAdapter
from pyautest.adapter.numpy_array import NumpyArrayAdapter
from pyautest.adapter.pil_image import PILImageAdapter

basic_adapters = [
    PILImageAdapter(),
    NumpyArrayAdapter(),
]

__all__ = (
    basic_adapters,
    BaseAdapter,
)
