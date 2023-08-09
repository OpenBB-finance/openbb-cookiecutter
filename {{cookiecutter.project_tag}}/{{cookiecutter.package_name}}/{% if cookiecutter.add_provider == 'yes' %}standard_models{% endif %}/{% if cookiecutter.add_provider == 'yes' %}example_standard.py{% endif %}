"""Example OpenBB Standard.

Inside the `openbb_sdk/sdk/provider/openbb_provider/standard_models` you will find all
the standardized data models that are used by the OpenBB SDK.

The standardized models are used to create an unified data structure that can be
expected by the user on every call/return of a command. This way, the user can
know which parameters and return fields will always be available and which ones
are specific to each provider.

Below, we have an example of the standardized QueryParams and Data models for our
example command.

In the case that the provider has extra fields that are not covered by the standardized
models, the provider can create its own models. This will be exposed as extra_params in
the case of QueryParams and any extra return fields will be appended to the output data.
"""

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from pydantic import Field, PositiveFloat


class StandardQueryParams(QueryParams):
    """Example standard Query.

    Here we define the standardized query parameters that are shared by two or more
    providers.
    """

    symbol: str = Field(
        description="The symbol of the stock.",
    )


class StandardData(Data):
    """Example standard price Data.

    Here we define the standardized data model that is shared by two or more providers.
    """

    open: PositiveFloat = Field(description="The open price of the stock.")
    high: PositiveFloat = Field(description="The high price of the stock.")
    low: PositiveFloat = Field(description="The low price of the stock.")
    close: PositiveFloat = Field(description="The close price of the stock.")
    volume: PositiveFloat = Field(description="The volume of the stock.")
