import numpy
import pytest

from pyautest import golden_file_test
from pyautest.golden_file_test import _default_gold_file_test


def test_basic_adapter_success():
    def test_zeros():
        a = [0, 0, 0]
        assert golden_file_test('zeros', a)
    assert not (_default_gold_file_test.file_directory / 'test_zeros' / "zeros.pkl").exists()
    test_zeros()
    assert (_default_gold_file_test.file_directory / 'test_zeros' / "zeros.pkl").exists()


def test_basic_adapter_failed():
    def test_zeros():
        a = [0, 0, 0]
        assert golden_file_test('zeros', a)

    test_zeros()

    def test_zeros():
        a = [1, 1, 1]
        assert golden_file_test('zeros', a)

    with pytest.raises(AssertionError):
        test_zeros()


def test_basic_adapter_uneven_list():
    def test_zeros():
        a = [0, 0, 0]
        assert golden_file_test('zeros', a)

    test_zeros()

    def test_zeros():
        a = [0, 0, 0, 1]
        return golden_file_test('zeros', a)

    expected = False
    actual = test_zeros()
    assert actual == expected


def test_basic_allownance_error_success():
    def test_zeros():
        a = 0.0
        assert golden_file_test('zeros', a)
    assert not (_default_gold_file_test.file_directory / 'test_zeros' / "zeros.pkl").exists()
    test_zeros()
    assert (_default_gold_file_test.file_directory / 'test_zeros' / "zeros.pkl").exists()

    def test_zeros():
        a = 0.0000001
        assert golden_file_test('zeros', a)
    test_zeros()


def test_basic_allownance_error_success_dict():
    def test_zeros():
        a = {"a": 0.0, "b": 6}
        assert golden_file_test('zeros', a)
    assert not (_default_gold_file_test.file_directory / 'test_zeros' / "zeros.pkl").exists()
    test_zeros()
    assert (_default_gold_file_test.file_directory / 'test_zeros' / "zeros.pkl").exists()

    def test_zeros():
        a = {"b": 6, "a": 0.0000001}
        assert golden_file_test('zeros', a)
    test_zeros()


def test_basic_allownance_error_success_list():
    def test_zeros():
        a = [0.0]
        assert golden_file_test('zeros', a)
    assert not (_default_gold_file_test.file_directory / 'test_zeros' / "zeros.pkl").exists()
    test_zeros()
    assert (_default_gold_file_test.file_directory / 'test_zeros' / "zeros.pkl").exists()

    def test_zeros():
        a = [0.0000001]
        assert golden_file_test('zeros', a)
    test_zeros()

