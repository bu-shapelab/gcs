from __future__ import annotations

from .shape import GCS


class Cylinder(GCS):
    """GCS Cylinder.

    """

    def __init__(self,
                 height: float,
                 mass: float,
                 thickness: float,
                 n_height_steps: int = 100,
                 theta_step: float = 0.01,
                 density: float = 0.0012,
                 triangulate_caps: bool = True) -> None:
        """Initialize ``Cylinder``.

        Parameters
        ----------
        height : float
            The height (mm).
        mass : float
            The mass (g).
        thickness : float
            The wall thickness (mm).
        n_height_steps : int (default=`100`)
            Number of sampled cross-sections along the height.
        theta_step : float (default=`0.01`)
            Angular step size used to sample each cross-section in radians.
        density : float (default=`0.0012`)
            Material density (g/mm^3).
        triangulate_caps : bool (default=`True`)
            Set to `True` to triangulate the top and bottom faces.

        Examples
        --------
        >>> shape = gcs.Cylinder(height=25, mass=2, thickness=0.5)

        """
        super().__init__(c4_base=0,
                         c8_base=0,
                         c4_top=0,
                         c8_top=0,
                         twist_linear=0,
                         twist_amplitude=0,
                         twist_cycles=0,
                         perimeter_ratio=1,
                         height=height,
                         mass=mass,
                         thickness=thickness,
                         n_height_steps=n_height_steps,
                         theta_step=theta_step,
                         density=density,
                         triangulate_caps=triangulate_caps)


class Iroko(GCS):
    """Iroko CGS design from Snapp et al. (2024) [1].

    [1]: https://doi.org/10.1038/s41467-024-48534-4

    """

    def __init__(self,
                 n_height_steps: int = 100,
                 theta_step: float = 0.01,
                 density: float = 0.0012,
                 triangulate_caps: bool = True) -> None:
        """Initialize ``Iroko``.

        Parameters
        ----------
        n_height_steps : int (default=`100`)
            Number of sampled cross-sections along the height.
        theta_step : float (default=`0.01`)
            Angular step size used to sample each cross-section in radians.
        density : float (default=`0.0012`)
            Material density (g/mm^3).
        triangulate_caps : bool (default=`True`)
            Set to `True` to triangulate the top and bottom faces.

        Examples
        --------
        >>> shape = gcs.Iroko()

        """
        super().__init__(c4_base=0.730333927354502,
                         c8_base=-0.0821084429646878,
                         c4_top=0.455688084446719,
                         c8_top=-0.200458707161255,
                         twist_linear=0.11822302314236,
                         twist_amplitude=0.262031108639582,
                         twist_cycles=0.591614200392281,
                         perimeter_ratio=1.17143242893827,
                         height=20.7821180708855,
                         mass=2.15501149030671,
                         thickness=0.578365564080763,
                         n_height_steps=n_height_steps,
                         theta_step=theta_step,
                         density=density,
                         triangulate_caps=triangulate_caps)


class Willow(GCS):
    """Willow CGS design from Snapp et al. (2024) [1].

    [1]: https://doi.org/10.1038/s41467-024-48534-4

    """

    def __init__(self,
                 n_height_steps: int = 100,
                 theta_step: float = 0.01,
                 density: float = 0.0012,
                 triangulate_caps: bool = True) -> None:
        """Initialize ``Willow``.

        Parameters
        ----------
        n_height_steps : int (default=`100`)
            Number of sampled cross-sections along the height.
        theta_step : float (default=`0.01`)
            Angular step size used to sample each cross-section in radians.
        density : float (default=`0.0012`)
            Material density (g/mm^3).
        triangulate_caps : bool (default=`True`)
            Set to `True` to triangulate the top and bottom faces.

        Examples
        --------
        >>> shape = gcs.Willow()

        """
        super().__init__(c4_base=0.137494858826025,
                         c8_base=-0.223924307740836,
                         c4_top=0.990048662372857,
                         c8_top=0.281006846858847,
                         twist_linear=1.65277226755515,
                         twist_amplitude=0.136307527192256,
                         twist_cycles=0.892285681537298,
                         perimeter_ratio=1.53516566101125,
                         height=26.2960096899026,
                         mass=2.27727026727678,
                         thickness=0.771900777794452,
                         n_height_steps=n_height_steps,
                         theta_step=theta_step,
                         density=density,
                         triangulate_caps=triangulate_caps)
