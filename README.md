# OpenBB Platform Extensions Cookiecutter

[Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) is a command-line utility that creates projects from templates.

This repo hosts the Cookiecutter template for setting up a new OpenBB Platform extension. This template helps in standardizing the structure of extensions and makes the setup process more efficient.

## Template Structure

The Cookiecutter template prompts the user for information and then generates a new extension project based on that information. The information includes:

- Your Name
- Your Email
- Extension Name
- Package Name (the name of the extension's Python package)

## Setup

Before using the Cookiecutter, ensure that you have Python installed on your system. Then, follow these steps to set up your environment:

1. Create a new virtual environment.

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

## Usage

1. Generate your new project:

   ```bash
   cookiecutter https://github.com/OpenBB-finance/openbb-cookiecutter --checkout develop
   ```

2. Go into the generated project directory and install the project's dependencies:

   ```bash
   cd <project-name>
   poetry install
   ```

3. Import `obb` and use your extension:

   ```python
   from package_name import obb

   obb.<package_name>.<command>
   exit()
   ```

   > On first launch, your extension will be automatically recognized and built by the OpenBB Platform v4. If you modify your extension, you can trigger the rebuild by using this command `python -c "import package_name; package_name.build()"`

   If your extension requires an API key you can pass it by doing the following:

   ```python
   obb.user.credentials.<package_name>_<key_name> = <key_value>
   ```

4. To launch the API, run:

   ```bash
   uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 8000 --reload
   ```

   Go to `http://localhost:8000/docs` to view the API documentation.

   In order to use any of the endpoints available, you'll need to get a valid authorization.
   You can do it in one of the following ways:

   - Using your [OpenBB Hub](https://my.openbb.co/) account
   - Use the default user: `openbb` and password: `openbb`

Remember to deactivate the virtual environment when you're finished by running `deactivate` in your terminal.

## Contributing

We welcome contributions to this template! Please feel free to open an issue or submit a pull request with your improvements.

## Contacts

If you have any questions about the cookiecutter or anything OpenBB, feel free to email us at `support@openbb.co`

If you want to say hi, or are interested in partnering with us, feel free to reach us at `hello@openbb.co`

Any of our social media platforms: [openbb.co/links](https://openbb.co/links)
