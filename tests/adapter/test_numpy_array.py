import numpy
import pytest

from pyautest import golden_file_test
from pyautest.golden_file_test import _default_gold_file_test


def teardown_method(self, method):
    print('method{}:'.format(method.__name__))


def test_numpy_adapter_success():
    def test_zeros():
        a = numpy.zeros((100, 100))
        assert golden_file_test('zeros', a)
    assert not (_default_gold_file_test.file_directory / 'test_zeros' / "zeros.npz").exists()
    test_zeros()
    assert (_default_gold_file_test.file_directory / 'test_zeros' / "zeros.npz").exists()


def test_numpy_adapter_failed():
    def test_zeros():
        a = numpy.zeros((100, 100))
        assert golden_file_test('zeros', a)

    test_zeros()

    def test_zeros():
        a = numpy.ones((100, 100))
        assert golden_file_test('zeros', a)

    with pytest.raises(AssertionError):
        test_zeros()
