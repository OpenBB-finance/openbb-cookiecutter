"""{{ cookiecutter.package_name }} OpenBB Platform extension."""

from openbb_core.provider.abstract.provider import Provider
from {{cookiecutter.package_name}}.models.example import ExampleFetcher

# mypy: disable-error-code="list-item"

provider = Provider(
    name="{{cookiecutter.package_name}}",
    description="Data provider for {{cookiecutter.project_name}}.",
    # Only add 'credentials' if they are needed.
    # For multiple login details, list them all here.
    # credentials=["api_key"],
    website="https://{{cookiecutter.project_tag}}.com",
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "Example": ExampleFetcher,
    }
)
