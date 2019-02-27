import inspect
from pathlib import Path
from typing import List, Any

from pyautest.adapter import basic_adapters
from pyautest.adapter import BaseAdapter


class GoldenFileTest:
    def __init__(self, file_directory: Path, adapters: List[BaseAdapter]):
        self.file_directory = file_directory
        self.adapters = adapters

    def __call__(self, name: str, obj: Any) -> bool:
        test_function_name = self._find_code_stack()
        if test_function_name is None:
            raise Exception("not found test function in call stack")

        adapter = self._find_adapter(obj)
        if adapter is None:
            raise Exception(f'not found adapter "{type(obj)}"')

        filepath = self.file_directory / test_function_name / f"{name}.{adapter.file_extension}"

        if not filepath.exists():
            filepath.parent.mkdir(parents=True, exist_ok=True)
            adapter.save(obj, filepath)
            return True
        other = adapter.load(filepath)
        return adapter.equal(obj, other)

    def _find_adapter(self, obj: Any) -> BaseAdapter:
        for adapter in self.adapters:
            if isinstance(obj, adapter.target_class):
                return adapter
        return None

    @staticmethod
    def _find_code_stack():
        framerecords = inspect.stack()

        for framerecord in framerecords:
            name = framerecord[0].f_code.co_name  # type: str
            if name.startswith("test"):
                return name
        return None


_default_gold_file_test = GoldenFileTest(Path('.') / "pyautest_assets", basic_adapters)


def golden_file_test(name: str, obj: Any) -> bool:
    return _default_gold_file_test(name, obj)
