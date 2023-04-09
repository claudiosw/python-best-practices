# About

This repository has examples to help developers understand and improve their Python coding practices.

Related to this, there is a series of Linkedin posts that will be a suitable complement:

1. [Python Recommended coding practices - part 1: PEP8](https://www.linkedin.com/pulse/python-recommended-coding-practices-part-1-pep8-watanabe/) explains about PEP8, its name conventions, code layout and linters.
2. [Python Recommended coding practices - part 2: Clean Code](https://www.linkedin.com/pulse/python-recommended-coding-practices-part2-clean-code-watanabe/): In [this article](https://www.linkedin.com/pulse/python-recommended-coding-practices-part2-clean-code-watanabe/), I wrote about Python Clean Code practices.
3. [Python Recommended coding practices - part 3: SOLID Principles](https://www.linkedin.com/pulse/python-recommended-coding-practices-part-3-solid-watanabe/): In [this article](https://www.linkedin.com/pulse/python-recommended-coding-practices-part-3-solid-watanabe/), I wrote about the SOLID principles with Python examples.
4. [Testing in Python using Pytest and Mock](https://www.linkedin.com/pulse/testing-python-using-pytest-mock-claudio-shigueo-watanabe/): [In this article](https://www.linkedin.com/pulse/testing-python-using-pytest-mock-claudio-shigueo-watanabe/), I wrote about Pytest and Mock. I discussed basic use, fixtures, markers, parametrization and duration.

Each folder of this project is related to one specific topic:
* .vscode: This folder contain example of VSCode configuration.
* clean_code: This folder contains examples for "Clean Code" principles.
* documenting: This folder contains examples for code documentation.
* pep8: This folder contains examples for PEP8 style guidelines.
* solid: This folder contains examples for SOLID principles.
* testing: This folder contains examples for testing, including Pytest examples and using mocking.
* .gitignore: This file contain patterns for ignoring files and folders on your local computer to GitHub. 
* .pre-commit-config.yaml: This file containes configuration for all the pre-commit tasks. 


# Instalation

## On prompt, acess the directory that want to download the project
```
git clone https://github.com/claudiosw/python-best-practices.git
```

## Create the virtual environment:
```
python -m venv venv

```

## Run the virtual environment:
### Windows
```
venv\Scripts\activate

```
### Linux/MacOS
```
source venv/bin/activate
```

## Install the required Python packages:
```
pip install -r requirements.txt
pre-commit install
```
