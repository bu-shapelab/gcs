# gcs

[![Report a Bug](https://img.shields.io/static/v1.svg?label=🐛&message=Report%20a%20Bug&color=red)](https://github.com/bu-shapelab/gcs/issues)
[![Request a Feature](https://img.shields.io/static/v1.svg?label=💻&message=Request%20a%20Feature&color=yellow)](https://github.com/bu-shapelab/gcs/issues)
[![Read the Paper](https://img.shields.io/static/v1.svg?label=DOI&message=10.1038/s41467-024-48534-4&color=blue)](https://doi.org/10.1038/s41467-024-48534-4)

![Teaser](https://github.com/bu-shapelab/gcs/blob/main/assets/images/teaser.jpeg)

`gcs` is a Python library for creating generalized cylindrical shells (GCS).

The GCS design space uses eleven continuous parameters to generate trillions of geometrically diverse, manufacturable cylindrical-shell structures.
This compact parameterization enables large-scale optimization while capturing the nonlinear buckling, plasticity, and self-contact mechanisms that govern energy absorption.
This library is used in our paper:

   >Kelsey L. Snapp, Benjamin Verdier, Aldair E. Gongora, Samuel Silverman, Adedire D. Adesiji, Elise F. Morgan, Timothy J. Lawton, Emily Whiting, Keith A. Brown  
   [*Superlative mechanical energy absorbing efficiency discovered through self-driving lab-human partnership*](https://sam-silverman.com/assets/pdf/Snapp-SuperlativeMechanicalEnergy-Reduced.pdf)  
   Nature Communications (2024)

## Installation

The package requires Python 3.10 or later and is available on PyPI.
Install it with:

```bash
pip install gcs-shape
```

You can then import the package in Python:

```python
import gcs
```

## GCS Design Parameters

GCS are parameterized by 11 values:

| Syntax | Description |
| - | - |
| `c4_base` | Parameter controlling the size and shape of the base $4$-lobe feature. |
| `c8_base` | Parameter controlling the size and shape of the base $8$-lobe feature. |
| `c4_top` | Parameter controlling the size and shape of the top $4$-lobe feature. |
| `c8_top` | Parameter controlling the size and shape of the top $8$-lobe feature. |
| `twist_linear` | Rotation (rad) of the top. This creates a linear twist between the base and top. |
| `twist_amplitude` | Amplitude (rad) of the oscillating twist between the base and top. |
| `twist_cycles` | Number of cycles of the oscillating twist between the base and top. |
| `perimeter_ratio` | Ratio between the top and base perimeters. |
| `height` | Height (mm). |
| `mass` | Mass (g). |
| `thickness` | Wall thickness (mm). |

### `c4` and `c8` Relationship

The geometry of each top or bottom face is described by a polar equation whose shape is controlled by the parameters `c4` and `c8`.
This parameterization was adopted from [*Overvelde and Bertoldi (2014)*](https://doi.org/10.1016/j.jmps.2013.11.014).

![c4 & c8 relationship](https://github.com/bu-shapelab/gcs/blob/main/assets/images/c_relationship.svg)

### `twist_linear`, `twist_amplitude`, and `twist_cycles` Relationship

The parameters `twist_linear`, `twist_amplitude`, and `twist_cycles` control how the cross-section rotates as it is interpolated from the base face to the top face.
`twist_linear` sets the linear rotation, while `twist_amplitude` and `twist_cycles` control the amplitude and frequency of the oscillatory rotation along the height.

![twist relationship](https://github.com/bu-shapelab/gcs/blob/main/assets/images/twist_relationship.svg)

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

## Documentation

Documentation is provided in NumPy-style docstrings throughout the codebase.
Docstrings can be viewed interactively with Python's built-in `help()` function.
For example:

```python
import gcs
help(gcs.GCS)
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
