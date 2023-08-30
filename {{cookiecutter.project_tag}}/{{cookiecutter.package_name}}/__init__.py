"""{{ cookiecutter.package_name }} OpenBB SDK extension."""

from typing import List, Optional, Union
from openbb_provider.abstract.provider import Provider
from {{cookiecutter.package_name}}.models.example import ExampleFetcher

# mypy: disable-error-code="list-item"

provider = Provider(
    name="{{cookiecutter.package_name}}",
    description="Data provider for {{cookiecutter.project_name}}.",
    # Only add 'required_credentials' if they are needed.
    # For multiple login details, list them all here.
    # required_credentials=["api_key"],
    website="https://{{cookiecutter.project_tag}}.com",
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "Example": ExampleFetcher,
    }
)


def build(
    modules: Optional[Union[str, List[str]]] = None,
    lint: bool = True,
) -> None:
    """Build extension modules.

    Parameters
    ----------
    modules : Optional[List[str]], optional
        The modules to rebuild, by default None
        For example: "/news" or ["/news", "/crypto"]
        If None, all modules are rebuilt.
    lint : bool, optional
        Whether to lint the code, by default True
    """
    # pylint: disable=import-outside-toplevel
    import os
    from pathlib import Path
    from multiprocessing import Pool
    from openbb_core.app.static.package_builder import PackageBuilder

    current_dir = Path(os.path.dirname(os.path.realpath(__file__)))

    # `build` is running in a separate process. This avoids consecutive calls to this
    # function in the same interpreter to reuse objects already in memory. Not doing
    # this was causing docstrings to have repeated sections, for example.
    with Pool(processes=1) as pool:
        pool.apply(
            PackageBuilder(current_dir).build,
            args=(modules, lint),
        )

def create_app():
    from openbb_core.app.static.app_factory import (
        create_app as __create_app,
        BaseApp as __BaseApp,
    )

    try:
        # pylint: disable=import-outside-toplevel
        from {{cookiecutter.package_name}}.package.__extensions__ import Extensions as __Extensions

        obb: Union[__BaseApp, __Extensions] = __create_app(__Extensions)
    except (ImportError, ModuleNotFoundError):
        print(
            "Failed to import extensions. Run `{{cookiecutter.package_name}}.build()` to build extensions code."
        )
        obb = __create_app()

    return obb