from __future__ import annotations

from pathlib import Path
from cls import CLS
from cls.io import load, save, save_mesh
from ._data import TEST_PARAMETERS


class TestIO:
    """Tests for:
        - utils/save.py
        - utils/load.py

    """

    def test_save_and_load(self):
        """Test ``cls.save`` and ``cls.load`` functions.
        - Single CLS

        """
        shape = CLS(**TEST_PARAMETERS)
        file = Path(Path(__file__).parent / 'test.csv').resolve()

        save(shapes=[shape, shape], file=file)

        assert file.exists() is True

        shapes = load(file=file)

        assert len(shapes) == 2
        assert shape.parameters == shapes[0].parameters
        assert shape.parameters == shapes[1].parameters

        file.unlink()

    def test_save_mesh(self):
        """Test ``cls.save_mesh`` function.

        """
        shape = CLS(**TEST_PARAMETERS)
        file = Path(Path(__file__).parent / 'test.csv').resolve()
        save_mesh(shape=shape, file=file)
        assert file.exists() is True
        file.unlink()
