# OpenBB SDK Extensions Cookiecutter Template

[Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) is a command-line utility that creates projects from templates.

This repo hosts the Cookiecutter template for setting up a new OpenBB SDK extension. This template helps in standardizing the structure of extensions and makes the setup process more efficient.

## Template Structure

The Cookiecutter template prompts the user for information and then generates a new extension project based on that information. The information includes:

- Your Name
- Your Email
- Extension Name
- Package Name (the name of the extension's Python package)
- If the extension is adding data retrieval functionality
- If the extension is adding data processing functionality

Depending on the inputs provided, the structure of the generated project will vary, accommodating the necessary files and directories for your extension.

## Usage

Before creating a new project using this template, ensure that you have Python installed on your system. Then, follow these steps:

1. Create a new virtual environment. This isolates the dependencies for this project from your other Python projects.

   For Linux or MacOS systems:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   For Windows:

   ```cmd
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install Cookiecutter and Poetry:

   ```bash
   pip install cookiecutter poetry
   ```

3. Generate your new project:

   ```bash
   cookiecutter -f https://github.com/OpenBB-finance/openbb-cookiecutter
   ```

4. Go into the generated project directory and install the project's dependencies:

   ```bash
   cd <project-name>
   poetry install
   ```

5. Install your package:

   ```python
   import <package-name>
   <package-name>.install()
   ```

6. Import obb and use your extension:

   ```python
   from openbb_core.app.static.app_factory import create_app as __create_app

   obb = __create_app()
   obb.<package-name>.<command-name>()
   ```

7. To launch the API, run:

   ```bash
   uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 8000 --reload
   ```

   Go to `http://localhost:8000/docs` to view the API documentation.

Remember to deactivate the virtual environment when you're finished by running `deactivate` in your terminal.

## Contributing

We welcome contributions to this template! Please feel free to open an issue or submit a pull request with your improvements.

## Contacts

If you have any questions about the cookiecutter or anything OpenBB, feel free to email us at `support@openbb.co`

If you want to say hi, or are interested in partnering with us, feel free to reach us at `hello@openbb.co`

Any of our social media platforms: [openbb.co/links](https://openbb.co/links)
