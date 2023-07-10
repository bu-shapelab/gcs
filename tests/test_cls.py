from __future__ import annotations

from pathlib import Path
from numpy.testing import assert_almost_equal
from stl import mesh
from pytest import approx
from cls import CLS, Cylinder, discretize, triangulate
from cls.verify import verify_base_perimeter, verify_radius, verify
from ._data import TEST_1_PARAMETERS, TEST_2_PARAMETERS, TEST_CYLINDER_PARAMETERS

TEST_1_SHAPE = CLS(**TEST_1_PARAMETERS)
TEST_2_SHAPE = CLS(**TEST_2_PARAMETERS)
TEST_3_SHAPE = CLS(**TEST_CYLINDER_PARAMETERS)


class TestCLS:
    """Tests for:
        - cls.py

    """

    def test_parameters(self):
        """Test ``cls.CLS.parameters`` property.

        """
        assert TEST_1_SHAPE.parameters == TEST_1_PARAMETERS
        assert TEST_2_SHAPE.parameters == TEST_2_PARAMETERS

    def test_valid_base_perimeter(self):
        """Test ``cls.CLS.valid_base_perimeter`` property.

        """
        assert TEST_1_SHAPE.valid_base_perimeter == verify_base_perimeter(shape=TEST_1_SHAPE)
        assert TEST_2_SHAPE.valid_base_perimeter == verify_base_perimeter(shape=TEST_2_SHAPE)

    def test_valid_radius(self):
        """Test ``cls.CLS.valid_radius`` property.

        """
        assert TEST_1_SHAPE.valid_radius == verify_radius(shape=TEST_1_SHAPE)
        assert TEST_2_SHAPE.valid_radius == verify_radius(shape=TEST_2_SHAPE)

    def test_valid(self):
        """Test ``cls.CLS.valid`` property.

        """
        assert TEST_1_SHAPE.valid == verify(shape=TEST_1_SHAPE)
        assert TEST_2_SHAPE.valid == verify(shape=TEST_2_SHAPE)

    def test_base_perimeter(self):
        """Test ``cls.CLS.base_perimeter`` property.

        """
        assert TEST_1_SHAPE.base_perimeter == approx(expected=137.5,
                                                     abs=0.0001)
        assert TEST_2_SHAPE.base_perimeter == approx(expected=97.52759019523566,
                                                     abs=0.0001)

    def test_top_perimeter(self):
        """Test ``cls.CLS.top_perimeter`` property.

        """
        assert TEST_1_SHAPE.top_perimeter == approx(expected=412.5,
                                                    abs=0.0001)
        assert TEST_2_SHAPE.top_perimeter == approx(expected=140.98271236306823,
                                                    abs=0.0001)

    def test_vertices(self):
        """Test ``cls.CLS.vertices`` property.

        """
        assert_almost_equal(actual=TEST_1_SHAPE.vertices,
                            desired=discretize(shape=TEST_1_SHAPE))
        assert_almost_equal(actual=TEST_2_SHAPE.vertices,
                            desired=discretize(shape=TEST_2_SHAPE))

    def test_faces(self):
        """Test ``cls.CLS.faces`` property.

        """
        assert_almost_equal(actual=TEST_1_SHAPE.faces,
                            desired=triangulate(shape=TEST_1_SHAPE))
        assert_almost_equal(actual=TEST_2_SHAPE.faces,
                            desired=triangulate(shape=TEST_2_SHAPE))

    def test_mesh(self):
        """Test ``cls.CLS.mesh`` property.

        """
        stl_file = (Path(__file__).parent / '_test1.stl').resolve()
        assert_almost_equal(actual=TEST_1_SHAPE.mesh.vectors,
                            desired=mesh.Mesh.from_file(filename=stl_file).vectors)
        stl_file = (Path(__file__).parent / '_test2.stl').resolve()
        assert_almost_equal(actual=TEST_2_SHAPE.mesh.vectors,
                            desired=mesh.Mesh.from_file(filename=stl_file).vectors)

    def test_cylinder(self):
        """Test ``cls.Cylinder``.

        """
        cylinder = Cylinder(height=TEST_CYLINDER_PARAMETERS['height'],
                            mass=TEST_CYLINDER_PARAMETERS['mass'],
                            thickness=TEST_CYLINDER_PARAMETERS['thickness'],
                            n_steps=TEST_CYLINDER_PARAMETERS['n_steps'],
                            d_theta=TEST_CYLINDER_PARAMETERS['d_theta'])
        assert TEST_3_SHAPE.parameters == cylinder.parameters
