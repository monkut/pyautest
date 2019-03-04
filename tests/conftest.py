import shutil
from pyautest.golden_file_test import _default_gold_file_test

import pytest


@pytest.fixture(scope='function', autouse=True)
def remove_pyautest_assets():
    yield

    shutil.rmtree(_default_gold_file_test.file_directory, ignore_errors=True)
