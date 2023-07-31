"""Example Data Integration.

When we retrieve the data from an external resource we normally go through 3 steps:

1. Define our request/query parameters
2. Make the request to receive the raw data
3. Transform the data into a specific format that we want for our use case

OpenBB SDK provides the tooling that a developer needs to create such an integration.
It requires the developer to define 3 things:

1. Define the request/query parameters
2. Define the resulting data schema
3. Define how to fetch raw data

This file has example code to do that.
"""


from datetime import date
from typing import Dict, List, Optional

from openbb_provider.abstract.data import Data, QueryParams
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.helpers import data_transformer

# This is the Example Data Model definition.
# It will be referenced by the name "Example" in the router.py file.

class ExampleQueryParams(QueryParams):
    """Example query.

    This is the definition of our query parameters.
    If the endpoint is going to have no request/query parameters this class
    can be left blank.

    Parameter
    ---------
    limit : int (default: 0)
        A number of values to return. 0 is return all.
    """
    limit: Optional[int]  # limit the number of values returned.


class ExampleData(Data):
    """Example data.

    This is the definition of the output data in the format we want to use it.
    The example data schema is very simple. Just a date and a corresponding number.
    """
    date: date
    number: int


class ExampleFetcher(Fetcher[ExampleQueryParams, ExampleData]):
    """Example Fetcher class

    This class is responsible for the actual data retrieval.
    It handles standardization of input arguments (the query parameters), fetching the
    data and converting it into a format that we want.
    """
    @staticmethod
    def transform_query(
        query: ExampleQueryParams, extra_params: Optional[Dict] = None
    ) -> ExampleQueryParams:
        return ExampleQueryParams(
            limit=query.limit,
            **extra_params if extra_params else {},
        )

    @staticmethod
    def extract_data(
        query: ExampleQueryParams, credentials: Optional[Dict[str, str]]
    ) -> ExampleData:
        if credentials:
            api_key = credentials.get("super_quant_api_key")

        example_response = [
            {"2021-02-01": 1},
            {"2021-03-01": 2},
            {"2021-04-01": 3},
            {"2021-05-01": 42},
            ]

        return [ExampleData(date=k, number=v) for i in example_response for k,v in i.items()]

    @staticmethod
    def transform_data(data: List[ExampleData]) -> List[ExampleData]:
        return data_transformer(data, ExampleData)
