"""OpenBB SDK Extension cookiecutter script.

This script automates the creation of a cookiecutter project template.
"""

import json
import sys


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via input() and return their answer."""
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def main():
    """Main entry point."""
    print("Welcome to the project generation script.")
    print("You will be asked a few questions to customize your project.\n")

    cookiecutter_context = "{{cookiecutter}}"
    cookiecutter_context = json.loads(cookiecutter_context)

    cookiecutter_context["full_name"] = input("Enter your full name: ")
    cookiecutter_context["email"] = input("Enter your email: ")
    cookiecutter_context["project_name"] = input("Enter the extension name: ")
    cookiecutter_context["project_slug"] = (
        cookiecutter_context["project_name"].lower().replace(" ", "_")
    )
    cookiecutter_context["package_name"] = (
        input("Enter the package name (defaults to extension name if blank): ")
        or cookiecutter_context["project_slug"]
    )
    cookiecutter_context["data_retrieval"] = query_yes_no(
        "Will your extension retrieve data from an API, a database or a file?"
    )
    cookiecutter_context["data_processing"] = query_yes_no(
        "Will your extension process data provided by the user?"
    )

    # Add a timestamp
    cookiecutter_context["_template"] = "{% now 'utc', '%Y%m%d%H%M%S' %}"

    with open("cookiecutter.json", "w") as f:
        json.dump(cookiecutter_context, f)


if __name__ == "__main__":
    main()
