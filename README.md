<h1 align="center">
  <img src="https://github.com/bu-shapelab/gcs/blob/main/misc/images/logo.jpeg" width="400">
</h1>

[![Explore the Docs](https://img.shields.io/static/v1.svg?label=📚&message=Explore%20the%20Docs&color=green)](TODO)
[![Report a Bug](https://img.shields.io/static/v1.svg?label=🐛&message=Report%20a%20Bug&color=green)](https://github.com/bu-shapelab/gcs/issues)
[![Request a Feature](https://img.shields.io/static/v1.svg?label=💻&message=Request%20a%20Feature&color=green)](https://github.com/bu-shapelab/gcs/issues)
[![Read the Paper](https://img.shields.io/static/v1.svg?label=DOI&message=TODO&color=blue)](TODO)

`gcs` is a Python library for creating generalized cylindrical shells (GCS).

![GCS examples](https://github.com/bu-shapelab/gcs/blob/main/misc/images/examples.jpeg)

GCS are parameterized by 11 values:

| Syntax | Description |
| - | - |
| `c1_base` | The base $4$-lobe parameter. |
| `c2_base` | The base $8$-lobe parameter. |
| `c1_top` | The top $4$-lobe parameter. |
| `c2_top` | The top $8$-lobe parameter. |
| `twist_linear` | The linear twist. |
| `twist_amplitude` | The oscillating twist amplitude. |
| `twist_period` | The oscillating twist period. |
| `perimeter_ratio` | The ratio between the top and base perimeters. |
| `height` | The height (mm). |
| `mass` | The mass (g). |
| `thickness` | The wall thickness (mm). |

### `c1` and `c2` Relationship

![c1 & c2 relationship](https://github.com/bu-shapelab/gcs/blob/main/misc/images/cs.svg)

* Adopted from [*Overvelde and Bertoldi, 2014*](https://doi.org/10.1016/j.jmps.2013.11.014)

### `twist_linear`, `twist_amplitude`, and `twist_period` Relationship

![twist relationship](https://github.com/bu-shapelab/gcs/blob/main/misc/images/twist.svg)

## Download

```bash
pip install gcs
```

### Requirements

* [bentley-ottmann](https://pypi.org/project/bentley-ottmann/) (version: 7.3.0)
* [numpy](https://pypi.org/project/numpy/) (version: 1.21.5 or higher)
* [numpy-stl](https://pypi.org/project/numpy-stl/) (version: 2.17.1 or higher)
* [pandas](https://pypi.org/project/pandas/) (version: 1.4.1 or higher)
* [scipy](https://pypi.org/project/scipy/) (version: 1.7.3 or higher)

## Contributing

The contribution guidelines can be found in [CONTRIBUTING.md](https://github.com/bu-shapelab/gcs/blob/main/CONTRIBUTING.md).

## Maintainers

* [Sam Silverman](https://github.com/samsilverman/) - [sssilver@bu.edu](mailto:sssilver@bu.edu)

## Citation

```text
TODO
```
