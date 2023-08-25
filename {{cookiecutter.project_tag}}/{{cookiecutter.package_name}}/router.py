"""{{cookiecutter.project_name}} router command example."""

import requests
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel

router = Router(prefix="")


@router.command(methods=["GET"])
def get_example(symbol: str = "AAPL") -> OBBject[dict]:
    """Get options data."""
    base_url = "https://www.cboe.com/education/tools/trade-optimizer/symbol-info"

    response = requests.get(base_url + f"?symbol={symbol}", timeout=5).json()
    return OBBject(results=response["details"])


@router.command(methods=["POST"])
def post_example(
    data: dict,
    bid_col: str = "bid",
    ask_col: str = "ask",
) -> OBBject[dict]:
    """Calculate mid and spread."""
    bid = data[bid_col]
    ask = data[ask_col]
    mid = (bid + ask) / 2
    spread = ask - bid

    return OBBject(results={"mid": mid, "spread": spread})


# pylint: disable=unused-argument
@router.command(model="Example")
def model_example(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return OBBject(results=Query(**locals()).execute())
