import unittest
import shutil
from pathlib import Path

import pytest
from PIL import Image

from pyautest.golden_file_test import golden_file_test, _default_gold_file_test


class SimpleTestCase(unittest.TestCase):
    def tearDown(self):
        shutil.rmtree(_default_gold_file_test.file_directory)

    def test_success(self):
        def test_black():
            image = Image.new("RGB", (100, 100))
            assert golden_file_test('black', image)
        assert not (_default_gold_file_test.file_directory / 'test_black' / "black.png").exists()
        test_black()
        assert (_default_gold_file_test.file_directory / 'test_black' / "black.png").exists()
        test_black()

    def test_failed(self):
        def test_black():
            image = Image.new("RGB", (100, 100))
            assert golden_file_test('black', image)

        test_black()

        def test_black():
            image = Image.new("RGB", (100, 100), 255)
            assert golden_file_test('black', image)

        with pytest.raises(AssertionError):
            test_black()


if __name__ == '__main__':
    unittest.main()
