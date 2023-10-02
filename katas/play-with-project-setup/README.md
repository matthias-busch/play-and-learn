# Setting up a poetry managed Python package from scratch

## Steps

1. Creating a new python package skeleton the `--src` option uses the src layout for the project:
    ```shell
    poetry new --src <PACKAGE-NAME>
    ```

2. Add your `dev` dependencies so anything related to type-checking, tests, linting etc.:
    ```shell
    poetry add --group dev mypy pytest pytest-cov pre-commit ruff
    ```

3. Install your `dev` dependencies:
    ```shell
    poetry install with dev
    ```

4. Add tool specific configurations for mypy, pytest to your [pyproject.toml](pyproject.toml).

5. Add a simple [dummy.py](src/play_with_project_setup/dummy.py) Python module and a simple [test_dummy.py](tests/test_dummy.py) module to your package so you can run dev tools against them with:
    ```shell
    poetry run mypy
    ```
    or
    ```
    poetry run pytest --cov=play_with_project_setup --cov-report term-missing
    ```

6. Create a [.pre-commit-config.yaml](../../.pre-commit-config.yaml) in the root and configure all the hooks you like.

7. Create the CI/CD pipelines that define the GitHub Actions to run checks for pre-commit, pytest and mypy:
    - [check-lint](../../.github/workflows/kata_project_setup_check_lint.yaml)
    - [check-mypy](../../.github/workflows/kata_project_setup_check_mypy.yaml)
    - [check-pytest](../../.github/workflows/kata_project_setup_check_pytest.yaml)
