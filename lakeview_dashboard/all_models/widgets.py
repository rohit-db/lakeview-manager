"""
This module contains models related to different types of widgets in the dashboard.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Union, Dict, Any
from .specs import SpecModel, TableSpecModel
from .utils import generate_unique_id


class WidgetParameterModel(BaseModel):
    """
    Represents a parameter in a widget.

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

class FieldModel(BaseModel):
    """Represents a field in a query."""
    name: str
    expression: str


class QueryDetailsModel(BaseModel):
    """
    Represents the details of a query.

    Attributes:
        datasetName (str): The name of the dataset.
        fields (Optional[List[Dict[str, str]]]): The fields to be queried.
        disaggregated (bool): Whether the query is disaggregated. Default is False.
        parameters (Optional[List[Dict[str, Any]]]): The parameters for the query.
    """
    datasetName: str
    fields: Optional[List[FieldModel]] = None
    disaggregated: bool = False
    parameters: Optional[List[WidgetParameterModel]] = None

class QueryModel(BaseModel):
    """
    Represents a query associated with a widget.

    Attributes:
        name (str): The name of the query.
        query (QueryDetailsModel): The details of the query.
    """
    name: str
    query: QueryDetailsModel


class TextWidgetModel(BaseModel):
    """
    Represents a text widget in a dashboard.

    Attributes:
        name (Optional[str]): The unique identifier for the widget. Default is generated using `generate_unique_id`.
        textbox_spec (str): The specification for the text box.
    """
    name: Optional[str] = Field(default_factory=generate_unique_id)
    textbox_spec: str


class VisualizationWidgetModel(BaseModel):
    """
    Represents a visualization widget in a dashboard.

    Attributes:
        name (Optional[str]): The unique identifier for the widget. Default is generated using `generate_unique_id`.
        queries (List[QueryModel]): The list of queries associated with the widget.
        spec (Union[SpecModel, TableSpecModel]): The specification for the visualization.
    """
    name: Optional[str] = Field(default_factory=generate_unique_id)
    queries: List[QueryModel]
    spec: Union[SpecModel, TableSpecModel]


class FilterWidgetModel(BaseModel):
    """
    Represents a filter widget in a dashboard.

    Attributes:
        name (Optional[str]): The unique identifier for the widget. Default is generated using `generate_unique_id`.
        queries (List[QueryModel]): The list of queries associated with the widget.
        spec (SpecModel): The specification for the filter.
    """
    name: Optional[str] = Field(default_factory=generate_unique_id)
    queries: List[QueryModel]
    spec: SpecModel
