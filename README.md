# unit_tests
Python Unit Test Example

## Requirements
- [Install Python](https://www.python.org/downloads/) version == 3.8

## Setup local dev environment

Here are the steps to perform in order to run the code locally:

1. Create a virtual environment and install project dependencies
    ```shell script
    pipenv install --dev
    ```

## Running Code Validations (Black, Flake8, MyPy, Pytest)
1. Run black formatting and fix errors if any
    ```shell script
    pipenv run format
    ```
   
1. Run flake8 linter and fix errors if any
    ```shell script
    pipenv run lint
    ```

1. Run mypy type checker and fix errors if any
    ```shell script
    pipenv run typecheck
    ```

1. Run unit tests and fix errors if any
    ```shell script
    pipenv run tests
    ```

1. Run isort to order imports
    ```shell script
    pipenv run sort
    ```

## Deployment
1. (Optional) Export pipfile dependencies
    ```shell script
    pipenv run requirements
    ```

## Contributing
Pull requests are welcome. 
For major changes, please create a new branch and Jira issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## Project Structure
    unit_tests
    │
    ├── .coverage          <- Coverage library config
    │
    ├── .flake8            <- Flake8 library config
    │
    ├── pyproject.toml     <- Project configurations and dependencies are specified here
    │                         for pipenv, Black and Coverage
    │
    ├── README.md          <- The README for developers using this project.
    │
    ├── Pipfile            <- The requirements file used to install project dependencies
    │
    ├── tests              <- Unit and functional tests
    │   ├── fixtures       <- Reusable testing components
    │   └── test_main.py   <- Unit tests