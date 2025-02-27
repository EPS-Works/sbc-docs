# SBC Documentation

This repository contains the Sphinx project for generating the documentation of the SBC, including hardware, firmware and SDK. It contains the configuration and source files necessary to build HTML, PDF, or other formats of documentation.

## Setup

To avoid conflicts with Python versions and dependencies, create and activate a virtual environment

```bash
python -m venv .venv  # Create a virtual environment

source .venv/bin/activate  # Activate on macOS/Linux
venv\Scripts\activate  # Activate on Windows
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

## Build

Generate the documentation in the required format

```bash
make html

make latexpdf  # Generates a PDF document
make epub      # Generates an EPUB document
```

After building, open `build/html/index.html` in a browser to view the documentation.

### Contributing

- Create a feature branch.
- Make changes and ensure the documentation builds successfully.
- Open a pull request.
