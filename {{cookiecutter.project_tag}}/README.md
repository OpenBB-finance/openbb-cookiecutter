# OpenBB SDK v4 Cookiecutter Template

## Introduction

This is the generated cookiecutter template for the OpenBB SDK v4.
It is used to help you create a new project that can be integrated into the existing
structure of the SDK.

With it you can:

* Create a new project
* Build custom commands
* Interact with the standardization framework
* Build custom services and applications on top of the framework

## Getting Started

Depending on your choices during the cookiecutter generation process, you will have a
different project structure that is catered to your needs. It is recommended that you
check out our example files to learn more about how to build your project.

Based on your choices, we recommend you check out the files in the following order:

* `README.md`
{% if cookiecutter.add_provider == 'yes'%}* `{{cookiecutter.package_name}}/standard_models/example_standard.py`
* `{{cookiecutter.package_name}}/models/example.py`
* `{{cookiecutter.package_name}}/__init__.py`
{% endif %}{% if cookiecutter.add_command == 'yes'%}* `{{cookiecutter.package_name}}/router.py`{% endif %}
