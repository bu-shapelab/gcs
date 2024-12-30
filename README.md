<h1 align="center">
  <img src="https://github.com/bu-shapelab/gcs/blob/main/misc/images/logo.jpeg" width="400">
</h1>

[![Explore the Docs](https://img.shields.io/static/v1.svg?label=📚&message=Explore%20the%20Docs&color=green)](https://gcs-shape.readthedocs.io/)
[![Report a Bug](https://img.shields.io/static/v1.svg?label=🐛&message=Report%20a%20Bug&color=green)](https://github.com/bu-shapelab/gcs/issues)
[![Request a Feature](https://img.shields.io/static/v1.svg?label=💻&message=Request%20a%20Feature&color=green)](https://github.com/bu-shapelab/gcs/issues)
[![Read the Paper](https://img.shields.io/static/v1.svg?label=DOI&message=10.1038/s41467-024-48534-4&color=blue)](https://doi.org/10.1038/s41467-024-48534-4)

`gcs` is a Python library for creating generalized cylindrical shells (GCS).

![GCS examples](https://github.com/bu-shapelab/gcs/blob/main/misc/images/examples.jpeg)

GCS are parameterized by 11 values:

| Syntax | Description |
| - | - |
| `c4_base` | The parameter controlling the size and shape of the base $4$-lobe feature. |
| `c8_base` | The parameter controlling the size and shape of the base $8$-lobe feature. |
| `c4_top` | The parameter controlling the size and shape of the top $4$-lobe feature. |
| `c8_top` | The parameter controlling the size and shape of the top $8$-lobe feature. |
| `twist_linear` | The rotation (rad) of the top. This creates a linear twist between the base and top. |
| `twist_amplitude` | The amplitude (rad) of the oscillating twist between the base and top. |
| `twist_cycles` | The number of cycles of the oscillating twist between the base and top. |
| `perimeter_ratio` | The ratio between the top and base perimeters. |
| `height` | The height (mm). |
| `mass` | The mass (g). |
| `thickness` | The wall thickness (mm). |

### `c4` and `c8` Relationship

![c4 & c8 relationship](https://github.com/bu-shapelab/gcs/blob/main/misc/images/cs.svg)

* Adopted from [*Overvelde and Bertoldi, 2014*](https://doi.org/10.1016/j.jmps.2013.11.014)

### `twist_linear`, `twist_amplitude`, and `twist_cycles` Relationship

![twist relationship](https://github.com/bu-shapelab/gcs/blob/main/misc/images/twist.svg)

## Download

`gcs` requires [Python](https://www.python.org) version 3.8 (or higher). To install, run the command:

```bash
pip install gcs-shape
```

### Requirements

* [bentley-ottmann](https://pypi.org/project/bentley-ottmann/) (version: 7.3.0)
* [mapbox_earcut](https://pypi.org/project/mapbox-earcut/) (version: 1.0.0 or higher)
* [numpy](https://pypi.org/project/numpy/) (version: 1.21.5 or higher)
* [numpy-stl](https://pypi.org/project/numpy-stl/) (version: 2.17.1 or higher)
* [pandas](https://pypi.org/project/pandas/) (version: 1.4.1 or higher)
* [scipy](https://pypi.org/project/scipy/) (version: 1.7.3 or higher)

### Supported Operating Systems

`gcs` is operating system independent. The package has been tested on the following operating systems:

* MacOS Ventura 13.4.1
* Ubuntu 22.04
* Windows 10

## Quickstart

```python
import gcs

# Create a generalized cylindrical shell
shape = gcs.GCS(c4_base=0.3,
                c8_base=-0.2,
                c4_top=0.4,
                c8_top=-0.3,
                twist_linear=2,
                twist_amplitude=0.05,
                twist_cycles=3,
                perimeter_ratio=1.5,
                height=20,
                mass=2.1,
                thickness=0.48)

# Assert the shape is valid
print(shape.valid)

# Save shape to STL file
gcs.io.save_mesh(file='shape.stl', shape=shape)
```

## Contributing

The contribution guidelines can be found in [CONTRIBUTING.md](https://github.com/bu-shapelab/gcs/blob/main/CONTRIBUTING.md).

## Maintainers

* [Sam Silverman](https://github.com/samsilverman/) - [sssilver@bu.edu](mailto:sssilver@bu.edu)

## Citation

```text
@article{Snapp:2024:SuperlativeMechanicalEnergy,
author={Snapp, Kelsey L. and Verdier, Benjamin and Gongora, Aldair E. and Silverman, Samuel and Adesiji, Adedire D. and Morgan, Elise F. and Lawton, Timothy J. and Whiting, Emily and Brown, Keith A.},
title={Superlative mechanical energy absorbing efficiency discovered through self-driving lab-human partnership},
journal={Nature Communications},
year={2024},
month={May},
day={21},
volume={15},
number={1},
pages={4290},
issn={2041-1723},
doi={10.1038/s41467-024-48534-4},
url={https://doi.org/10.1038/s41467-024-48534-4}
}
```
