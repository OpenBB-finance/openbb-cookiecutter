"""{{ cookiecutter.package_name }} OpenBB SDK extension."""

{% if cookiecutter.add_provider == 'yes' %}from openbb_provider.abstract.provider import Provider
from {{cookiecutter.package_name}}.models.example import ExampleFetcher

# mypy: disable-error-code="list-item"

provider = Provider(
    name="{{cookiecutter.package_name}}",
    description="Data provider for {{cookiecutter.project_name}}.",
    # Only add 'required_credentials' if they are needed.
    # For multiple login details, list them all here.
    required_credentials=["api_key"],
    website="https://{{cookiecutter.project_tag}}.com",
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "Example": ExampleFetcher,
    }
)
{% endif %}

def install():
    from openbb_core.app.static.package_builder import \
        PackageBuilder  # pylint: disable=import-outside-toplevel

    PackageBuilder.build()

from openbb_core.app.static.app_factory import create_app as __create_app

sdk = __create_app()
obb = sdk
