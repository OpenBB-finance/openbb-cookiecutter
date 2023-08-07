"""{{ cookiecutter.package_name }} OpenBB SDK extension."""

{% if cookiecutter.add_provider == 'yes' %}from openbb_provider.abstract.provider import Provider
from {{cookiecutter.package_name}}.models.example import ExampleFetcher

# mypy: disable-error-code="list-item"

provider = Provider(
    name="{{cookiecutter.package_name}}",
    description="Data provider for {{cookiecutter.project_name}}.",
    # The required_credentials can be left out if the provider doesn't need credentials.
    # If the provider requires the use of 2 or more credentials, write each as a new
    # entry inside the list.
    required_credentials=["api_key"],
    website="https://{{cookiecutter.project_tag}}.com",
    # Below we define the fetchers that inform us of our provider's coverage.
    # The dict key is the name of the fetcher that will be used in the router.py file.
    fetcher_dict={
        "Example": ExampleFetcher,
    }
)
{% endif %}

def install():
    from openbb_core.app.static.package_builder import \
        PackageBuilder  # pylint: disable=import-outside-toplevel

    PackageBuilder.build()
