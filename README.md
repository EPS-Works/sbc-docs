# SBC Documentation

This repository contains the Sphinx project for generating the documentation of the SBC, including hardware, firmware and SDK. It contains the configuration and source files necessary to build HTML, PDF, or other formats of documentation.

## Setup

Clone the repo along with submodules

```bash
git clone --recurse-submodules https://github.com/eps-works/sbc-docs.git
cd sbc-docs
git submodule update --init --recursive
```

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

> [!WARNING]
> Docstrings used by autocode are sourced from the sbc-sdk folder, which is a **submodule**. Update submodules regularly to ensure that the latest code and documentation are available, specially before a new build.
>
> `git submodule update --remote`

```bash
# In macOS/Linux
make html
make latexpdf  # Generates a PDF document
make epub      # Generates an EPUB document

# In Windows
sphinx-build -b html source build
```

After building, open `build/html/index.html` in a browser to view the documentation.

## Contributing

- Create a feature branch.
- Make changes and ensure the documentation builds successfully.
- Open a pull request.

> [!CAUTION]
> DO NOT EDIT **submodules** directly! Any changes made inside submodules may be overwritten when updated.
