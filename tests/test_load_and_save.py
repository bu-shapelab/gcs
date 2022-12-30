from __future__ import annotations

# import pytest

from pathlib import Path
import pandas as pd
from cls import load, save, save_mesh

FOLDER = Path(__file__).parent.resolve()


class TestLoad:
    """TODO
    """

    def test_load_single(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'shapes_single.csv').resolve()
        data = pd.read_csv(filepath_or_buffer=file, delimiter=',', header=0)
        shapes = load(file=file)
        assert len(shapes) == data.shape[0]
        for idx, shape in enumerate(shapes):
            parameters = data.iloc[idx, :].to_dict()
            assert shape.parameters == parameters

    def test_load_multi(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'shapes_multi.csv').resolve()
        data = pd.read_csv(filepath_or_buffer=file, delimiter=',', header=0)
        shapes = load(file=file)
        assert len(shapes) == data.shape[0]
        for idx, shape in enumerate(shapes):
            parameters = data.iloc[idx, :].to_dict()
            assert shape.parameters == parameters

    def test_load_none(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'shapes_none.csv').resolve()
        shapes = load(file=file)
        assert len(shapes) == 0

    def test_load_no_path(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'not_a_file.csv').resolve()
        shapes = load(file=file)
        assert len(shapes) == 0

    def test_load_invalid_parameter(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'shapes_invalid.csv').resolve()
        shapes = load(file=file)
        assert len(shapes) == 0


class TestSave:
    """TODO
    """

    def test_save_single(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'shapes_single.csv').resolve()
        shapes = load(file=file)
        file = Path(FOLDER / 'data' / 'shapes_single_save.csv').resolve()
        save(shapes=shapes, file=file)
        assert file.exists() is True
        file.unlink()

    def test_save_multi(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'shapes_multi.csv').resolve()
        shapes = load(file=file)
        file = Path(FOLDER / 'data' / 'shapes_multi_save.csv').resolve()
        save(shapes=shapes, file=file)
        assert file.exists() is True
        file.unlink()

    def test_save_none(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'shapes_none.csv').resolve()
        shapes = load(file=file)
        file = Path(FOLDER / 'data' / 'shapes_multi_save.csv').resolve()
        save(shapes=shapes, file=file)
        assert file.exists() is True
        file.unlink()

    def test_save_no_path(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'not_a_file.csv').resolve()
        shapes = load(file=file)
        file = Path(FOLDER / 'data' / 'not_a_file_save.csv').resolve()
        save(shapes=shapes, file=file)
        assert file.exists() is True
        file.unlink()

    def test_save_invalid_parameter(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'shapes_invalid.csv').resolve()
        shapes = load(file=file)
        file = Path(FOLDER / 'data' / 'shapes_invalid_save.csv').resolve()
        save(shapes=shapes, file=file)
        assert file.exists() is True
        file.unlink()

    def test_save_mesh(self):
        """TODO
        """
        file = Path(FOLDER / 'data' / 'shapes_single.csv').resolve()
        shapes = load(file=file)
        shape = shapes[0]
        file = Path(FOLDER / 'data' / 'shapes_single_mesh.stl').resolve()
        save_mesh(shape=shape, file=file)
        assert file.exists() is True
        file.unlink()
