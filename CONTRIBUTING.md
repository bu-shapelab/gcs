# Contributing

1. Go to [samsilverman/gcs](https://github.com/samsilverman/gcs) and fork the project.

2. Clone the fork to your local computer:

    ```bash
    git clone https://github.com/YourUsername/gcs.git
    ```

3. Create the [Conda](https://docs.conda.io/en/latest/) environment:

    ```bash
    conda env create --file environment.yml
    ```

    Activate the environment with:

    ```bash
    conda activate gcs
    ```

4. Install the package and development tools in editable mode:

    ```bash
    python -m pip install -e ".[dev]"
    ```

5. Create your feature branch:

    ```bash
    git checkout -b feature/NewFeature
    ```

6. Commit your changes:

    ```bash
    git commit -m 'Add a new feature.'
    ```

7. Push to the branch:

    ```bash
    git push origin feature/NewFeature
    ```

8. Open a pull request.

    Prior to opening a pull request, the contribution must:

    1. *Meet the stylistic guidelines*:

        Set up your editor to follow [PEP 8](https://peps.python.org/pep-0008/).
        You can check your code with the [Pylint](https://github.com/pylint-dev/pylint) linter.

    2. *Pass the unit tests*:

        Run all tests:

        ```bash
        python -m pytest tests/ --cov=gcs
        ```

        Tests should cover the relevant public behavior and important internal geometry or verification logic.

        **TIP**: Run individual test file:

        ```bash
        python -m pytest tests/path/to/test_file.py
        ```

    3. *Describe release impact in the pull request*:

        Summarize the user-facing changes in the pull request description and indicate the expected release impact:

        - `no release` for changes that do not affect the published package
        - `patch` for backwards-compatible bug fixes or small improvements
        - `minor` for backwards-compatible new functionality
        - `major` for breaking changes to the public API or behavior

        Maintainers will use this guidance to decide the next version number and create the release tag after the pull request is merged.
