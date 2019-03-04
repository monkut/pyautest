from pathlib import Path
import os

import pytest
from _pytest.main import Session

from pyautest.adapter import basic_adapters


def pytest_addoption(parser):
    group = parser.getgroup('autest', 'golden file test utility')

    group.addoption('--au-report-dir', dest="au_report_dir")
    group.addoption('--au-asset-dir', dest="au_asset_dir", default="pyautest_assets", type=Path)
    group.addoption('--au-fail-notfound-golden-file', dest="au_fail_notfound", action="store_true")


_configured_default_golden_file_test = None


def pytest_configure(config):
    from pyautest.golden_file_test import GoldenFileTest
    global _configured_default_golden_file_test
    _configured_default_golden_file_test = GoldenFileTest(config.option.au_asset_dir, basic_adapters)


def pytest_runtest_setup(item):
    t = item
    rnames = []
    while t is not None:
        if isinstance(t, Session):
            break

        rnames.append(os.path.splitext(t.name)[0])
        t = t.parent
    name = "/".join(reversed(rnames))
    global _configured_default_golden_file_test
    _configured_default_golden_file_test.set_testname(name)
