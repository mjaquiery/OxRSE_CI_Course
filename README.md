# OxRSE Continuous Integration course

![Python 3.6-3.8 on Ubuntu/Mac/Win](https://github.com/mjaquiery/OxRSE_CI_Course/workflows/Python%203.6-3.8%20on%20Ubuntu/Mac/Win/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/oxrse-ci-course/badge/?version=latest)](https://oxrse-ci-course.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/mjaquiery/OxRSE_CI_Course/branch/master/graph/badge.svg)](https://codecov.io/gh/mjaquiery/OxRSE_CI_Course)

This project contains a small Python project. We are going to use free cloud services to automate:

- unit testing on multiple Python versions
- unit testing on multiple operating systems
- coverage testing
- static analysis
- documentation generation

To make sure all dependencies are installed, we recommend creating a new virtual environment.
From the directory containing this file:

```bash
python3 -m pip install --user virtualenv
python3 -m venv venv
```

Activate the virtual environment:

Linux / macOS:
```bash
source venv/bin/activate
```

Windows cmd.exe:
```bash
venv\Scripts\activate.bat
```

Windows PowerShell:
```bash
venv\Scripts\Activate.ps1
```

Windows using Git Bash:
```bash
source venv\Scripts\activate
```

Upgrade the build tools and install this project:

```bash
pip install --upgrade pip setuptools wheel
pip install -e .[dev,docs]
```
