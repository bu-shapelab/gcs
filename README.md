# CLS

![cls Spashscreen](misc/images/splashscreen.jpeg)

Simple library for creating continuous line structures (CLS). The library provides

1. An object representing a continuous line structure.

2. Operations on CLS structures.

## Getting Started

These instructions will get you a copy of ``cls`` up and running on your local machine.

### Prerequisites

You will need to install the following software:

* [Conda](https://docs.conda.io/en/latest/)

### Installation

1. Clone the repository.

    ```bash
    git clone https://github.com/samsilverman/cls.git
    ```

2. Create the conda environment.

    ```bash
    conda env create --file cls.yml
    ```

3. Activate the conda environment.

    ```bash
    conda activate cls
    ```

    **NOTE**: To deactivate the environment, run:

    ```bash
    conda deactivate cls
    ```

## Usage

Documentation is available in docstrings provided with the code.

The docstring examples assume that ``cls`` has been imported:

```python
>>> import cls
```

The following are available subpackages within ``cls``

* ``preview``
  * Functions for previewing CLS shapes.

* ``verify``
  * Functions for verifying the validity of CLS shapes.

* ``random``
  * Functions for generating random CLS shapes.

## Contact

Maintainers:

* Sam Silverman - [@sam_silverman](https://twitter.com/sam_silverman) - [sssilver@bu.edu](mailto:sssilver@bu.edu)
