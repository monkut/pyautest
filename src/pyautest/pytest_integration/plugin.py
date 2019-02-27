import pytest


def pytest_addoption(parser):
    group = parser.getgroup('autest', 'golden file test utility')

    group.addoption('--au-report-dir', dest="report_dir")
    group.addoption('--au-asset-dir', dest="asset_dir")
    group.addoption('--au-fail-notfound-golden-file', dest="fail_notfound", action="store_true")


@pytest.fixture
def hello(request):
    report_dir = request.config.getoption("report_dir")
    print(report_dir)
