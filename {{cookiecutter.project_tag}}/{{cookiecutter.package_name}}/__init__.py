"""{{ cookiecutter.package_name }} OpenBB Platform extension."""

import os
from pathlib import Path
from typing import List, Optional, Union

from openbb_core.app.static.build_utils import build as _build
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


_this_dir = Path(os.path.dirname(os.path.realpath(__file__)))


def build(
    modules: Optional[Union[str, List[str]]] = None,
    lint: bool = True,
    verbose: bool = False,
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
    verbose : bool, optional
        Enable/disable verbose mode
    """

    _build(directory=_this_dir, modules=modules, lint=lint, verbose=verbose)


def create_app():
    from openbb_core.app.static.app_factory import BaseApp as __BaseApp
    from openbb_core.app.static.app_factory import create_app as __create_app

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
