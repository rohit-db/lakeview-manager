"""
This module contains models related to datasets used in the dashboard.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from .utils import generate_unique_id

class ParameterModel(BaseModel):
    """
    Represents a parameter in a query.

    Attributes:
        displayName (Optional[str]): The display name of the parameter.
        keyword (str): The keyword used in the query.
        dataType (str): The data type of the parameter. Default is "STRING".
        defaultSelection (Optional[Dict[str, Any]]): The default selection for the parameter.
    """
    displayName: Optional[str] = None
    keyword: str
    dataType: str = "STRING"
    defaultSelection: Optional[Dict[str, Any]] = None

class DatasetModel(BaseModel):
    """
    Represents a dataset in the dashboard.

    Attributes:
        name (Optional[str]): The unique identifier for the dataset. Default is generated using `generate_unique_id`.
        displayName (str): The display name of the dataset.
        query (str): The query associated with the dataset.
        parameters (Optional[List[ParameterModel]]): The list of parameters for the dataset.
    """
    name: Optional[str] = Field(default_factory=generate_unique_id)
    displayName: str
    query: str
    parameters: Optional[List[ParameterModel]] = None
