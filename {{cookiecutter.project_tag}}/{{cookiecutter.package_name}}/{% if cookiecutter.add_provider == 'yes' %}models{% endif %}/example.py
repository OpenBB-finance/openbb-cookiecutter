"""Example Data Integration.

When we retrieve the data from an external resource we go through 3 steps:

1. Define our request/query parameters.
2. Make the request to receive the raw data.
3. Transform the data into a specific format that we want for our use case.

Note: The format of the QueryParams and Data is defined by a pydantic model that can
be entirely custom, or inherit from the OpenBB standardized models.

The OpenBB SDK equips developers with tools to streamline the integration process.
Specifically, developers are required to:

1. Define the request/query parameters.
2. Define the resulting data schema.
3. Define how to fetch raw data.

The emphasis on the first two steps is to ensure developers fully understand their data,
encapsulated by the "Know Your Data" principle.

This file has example code and interacts with an OpenBB example standard.
"""

from typing import Dict, List, Optional, Any
from pydantic import Field

from {{cookiecutter.package_name}}.standard_models.example_standard import (
    StandardData, StandardQueryParams
)
from openbb_provider.abstract.fetcher import Fetcher

class ExampleQueryParams(StandardQueryParams):
    """Example provider query.

    This is the definition of our query parameters that are specific to this provider.
    Because it shares the `symbol` parameter with the standardized model from which
    we inherit, we only need to add extra parameters that are provider-specific.
    """

    limit: Optional[int] = Field(
        default=2, description="The number of results to return per page."
    )  # We use pydantic's Field to add a description to the parameter and default value

class ExampleData(StandardData):
    """Example provider data.

    This is the output data in the format we want to use it.
    The example data schema is the usual OHLCV data.
    """

    # As our data is the same as the standardized one, all we need to do is
    # declare the Config class to map the field names to the provider's data.
    class Config:
        fields = {
            "open": "o",
            "high": "h",
            "low": "l",
            "close": "c",
            "volume": "v",
        }

    # In the case that you have fields that are not covered by the standardized model,
    # you can add them here.

class ExampleFetcher(
    Fetcher[
        ExampleQueryParams,
        ExampleData,
    ]
):
    """Example Fetcher class.

    This class is responsible for the actual data retrieval.
    It handles standardization of input arguments (the query parameters), fetching the
    data and converting it into a format that we want.
    """

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> ExampleQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        # Both the standard and provider-specific query parameters are unpacked below.
        return ExampleQueryParams(**params)

    @staticmethod
    def extract_data(
        query: ExampleQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> ExampleData:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        In the case that you specified inside your Provider class that it requires
        credentials, you can access them here.
        """
        api_key = (
            credentials.get("{{cookiecutter.package_name}}_api_key")
            if credentials
            else ""
        )

        # Here we mock an example_response for brevity.
        example_response = [
            {
                "o": 2,
                "h": 5,
                "l": 1,
                "c": 4,
                "v": 5,
            },
            {
                "o": 4,
                "h": 7,
                "l": 3,
                "c": 6,
                "v": 10,
            },
        ]

        return [ExampleData(**d) for d in example_response]

    @staticmethod
    def transform_data(data: List[ExampleData]) -> List[ExampleData]:
        """Define example transform_data.

        Here we return data as-is, but you can transform it into a different format if
        you wish. This part is useful for any data post-processing that you need to do.
        """
        return data
