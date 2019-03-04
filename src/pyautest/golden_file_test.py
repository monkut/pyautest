import inspect
from pathlib import Path
from typing import List, Any

from pyautest.adapter import basic_adapters
from pyautest.adapter import BaseAdapter


class GoldenFileTest:
    def __init__(self, file_directory: Path, adapters: List[BaseAdapter], is_notfound_goldenfile_fail: bool = False):
        self.file_directory = file_directory
        self.adapters = adapters
        self.is_notfound_goldnenfile_fail = is_notfound_goldenfile_fail
        self.testname = None

    def __call__(self, name: str, obj: Any) -> bool:
        if self.testname is None:
            test_function_name = self._find_code_stack()
            if test_function_name is None:
                raise Exception("not found test function in call stack")
        else:
            test_function_name = self.testname

        adapter = self._find_adapter(obj)
        if adapter is None:
            raise Exception(f'not found adapter "{type(obj)}"')

        filepath = self.file_directory / test_function_name / f"{name}.{adapter.file_extension}"

        if not filepath.exists():
            if self.is_notfound_goldnenfile_fail:
                raise Exception(
                    f"golden file(\"{filepath}\") is not found,"
                    " if you want to create file than please set is_notfound_goldenfile_fail = False")
            filepath.parent.mkdir(parents=True, exist_ok=True)
            adapter.save(obj, filepath)
            return True
        other = adapter.load(filepath)
        return adapter.equal(obj, other)

    def set_testname(self, testname):
        self.testname = testname

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

import pyautest.pytest_integration.plugin as plugin


def golden_file_test(name: str, obj: Any):
    if plugin._configured_default_golden_file_test is None:
        _golden_file_test = _default_gold_file_test
    else:
        _golden_file_test = plugin._configured_default_golden_file_test
    return _golden_file_test(name, obj)
