from __future__ import annotations

from pathlib import Path
from numpy.testing import assert_almost_equal
from stl import mesh
from pytest import approx
from gcs import GCS, Cylinder, discretize, triangulate
from gcs.verify import verify_base_perimeter, verify_radius, verify
from ._data import TEST_1_PARAMETERS, TEST_2_PARAMETERS, TEST_CYLINDER_PARAMETERS

TEST_1_SHAPE = GCS(**TEST_1_PARAMETERS)
TEST_2_SHAPE = GCS(**TEST_2_PARAMETERS)
TEST_3_SHAPE = GCS(**TEST_CYLINDER_PARAMETERS)


class TestGCS:
    """Tests for:
        - gcs.py

    """

    def test_parameters(self):
        """Test ``gcs.GCS.parameters`` property.

        """
        assert TEST_1_SHAPE.parameters == TEST_1_PARAMETERS
        assert TEST_2_SHAPE.parameters == TEST_2_PARAMETERS

    def test_valid_base_perimeter(self):
        """Test ``gcs.GCS.valid_base_perimeter`` property.

        """
        assert TEST_1_SHAPE.valid_base_perimeter == verify_base_perimeter(shape=TEST_1_SHAPE)
        assert TEST_2_SHAPE.valid_base_perimeter == verify_base_perimeter(shape=TEST_2_SHAPE)

    def test_valid_radius(self):
        """Test ``gcs.GCS.valid_radius`` property.

        """
        assert TEST_1_SHAPE.valid_radius == verify_radius(shape=TEST_1_SHAPE)
        assert TEST_2_SHAPE.valid_radius == verify_radius(shape=TEST_2_SHAPE)

    def test_valid(self):
        """Test ``gcs.GCS.valid`` property.

        """
        assert TEST_1_SHAPE.valid == verify(shape=TEST_1_SHAPE)
        assert TEST_2_SHAPE.valid == verify(shape=TEST_2_SHAPE)

    def test_base_perimeter(self):
        """Test ``gcs.GCS.base_perimeter`` property.

        """
        assert TEST_1_SHAPE.base_perimeter == approx(expected=137.5,
                                                     abs=0.0001)
        assert TEST_2_SHAPE.base_perimeter == approx(expected=97.52759019523566,
                                                     abs=0.0001)

    def test_top_perimeter(self):
        """Test ``gcs.GCS.top_perimeter`` property.

        """
        assert TEST_1_SHAPE.top_perimeter == approx(expected=412.5,
                                                    abs=0.0001)
        assert TEST_2_SHAPE.top_perimeter == approx(expected=140.98271236306823,
                                                    abs=0.0001)

    def test_vertices(self):
        """Test ``gcs.GCS.vertices`` property.

        """
        assert_almost_equal(actual=TEST_1_SHAPE.vertices,
                            desired=discretize(shape=TEST_1_SHAPE))
        assert_almost_equal(actual=discretize(shape=TEST_2_SHAPE),
                            desired=TEST_2_SHAPE.vertices)

    def test_faces(self):
        """Test ``gcs.GCS.faces`` property.

        """
        assert_almost_equal(actual=TEST_1_SHAPE.faces,
                            desired=triangulate(shape=TEST_1_SHAPE))
        assert_almost_equal(actual=triangulate(shape=TEST_2_SHAPE),
                            desired=TEST_2_SHAPE.faces)
        # Need this to pass coverage of GCS.faces...
        assert_almost_equal(actual=TEST_1_SHAPE.faces,
                            desired=TEST_1_SHAPE.faces)

    def test_mesh(self):
        """Test ``gcs.GCS.mesh`` property.

        """
        stl_file = (Path(__file__).parent / '_test3.stl').resolve()
        assert_almost_equal(actual=TEST_3_SHAPE.mesh.vectors,
                            desired=mesh.Mesh.from_file(filename=stl_file).vectors)

    def test_cylinder(self):
        """Test ``gcs.Cylinder``.

        """
        cylinder = Cylinder(height=TEST_CYLINDER_PARAMETERS['height'],
                            mass=TEST_CYLINDER_PARAMETERS['mass'],
                            thickness=TEST_CYLINDER_PARAMETERS['thickness'],
                            n_steps=TEST_CYLINDER_PARAMETERS['n_steps'],
                            d_theta=TEST_CYLINDER_PARAMETERS['d_theta'],
                            triangulate_faces=TEST_CYLINDER_PARAMETERS['triangulate_faces'])
        assert TEST_3_SHAPE.parameters == cylinder.parameters
