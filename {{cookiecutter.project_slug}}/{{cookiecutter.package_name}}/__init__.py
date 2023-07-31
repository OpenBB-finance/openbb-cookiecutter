"""{{ cookiecutter.package_name }} OpenBB SDK extension."""

def install():
    from openbb_core.app.static.package_builder import \
        PackageBuilder  # pylint: disable=import-outside-toplevel

    PackageBuilder.build()
