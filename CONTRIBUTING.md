# Contributing

1. Go to [bu-shapelab/gcs](https://github.com/samsilverman/gcs) and fork the project.

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

4. Create your feature branch:

    ```bash
    git checkout -b feature/NewFeature
    ```

5. Commit your changes:

    ```bash
    git commit -m 'Add a new feature.'
    ```

6. Push to the branch:

    ```bash
    git push origin feature/NewFeature
    ```

7. Open a pull request.

    Prior to opening a pull request, the contribution must:

    1. *Meet the stylistic guidelines*:

        Set up your editor to follow [PEP 8](https://peps.python.org/pep-0008/).
        You can check your code with the [Pylint](https://github.com/pylint-dev/pylint) linter.

    2. *Pass the unit tests*:

        Run all tests:

        ```bash
        pytest tests/ --cov=gcs
        ```

        Tests should cover all code in a module. If coverage is not at 100%, implement additional unit tests.

        **TIP**: Run individual test file:

        ```bash
        pytest tests/SpecificTestFile.py
        ```

    3. *Rebuild documentation*:

        ```bash
        cd docs
        ```

        ```bash
        make html
        ```
