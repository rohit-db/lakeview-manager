"""
Model Definitions for Databricks Lakeview Dashboards

Defines Pydantic models representing the structure of a Databricks Lakeview Dashboard 
configuration, capturing datasets, pages, widgets, positions, and their related properties.

Hierarchy:
- DashboardModel: Represents the entire dashboard configuration.
  - DatasetModel: Datasets used in the dashboard.
  - PageModel: Pages within the dashboard.
    - LayoutModel: Layouts of widgets on a page.
      - WidgetModel: Individual widgets (visualizations or text).
        - QueryModel: Queries associated with widgets.
          - QueryDetailsModel: Details of a query (e.g., dataset, fields).
          - FieldModel: Fields used in a query.
        - SpecModel: Specifications for widget visualization.
          - EncodingModel: Encoding settings for visual elements.
          - FieldEncodingModel: Encodings specific to filter widgets.
      - PositionModel: Specifies the position and size of widgets on a page.
"""

from pydantic import BaseModel, Field, model_validator
from typing import List, Optional, Dict, Any
import uuid

def generate_unique_id():
    """Generates a unique identifier for models."""
    return uuid.uuid4().hex[:8]

class FieldModel(BaseModel):
    """Represents a field in a query."""
    name: str
    expression: str

class QueryDetailsModel(BaseModel):
    """Represents the details of a query."""
    datasetName: str
    fields: List[FieldModel]
    disaggregated: bool = False

class QueryModel(BaseModel):
    """Represents a query associated with a widget."""
    name: str
    query: QueryDetailsModel  

class FieldEncodingModel(BaseModel):
    """Encodings for fields in filter widgets."""
    fieldName: str
    displayName: str
    queryName: str

class EncodingModel(BaseModel):
    """Encodings for visual elements in widgets."""
    fieldName: Optional[str] = None
    scale: Optional[Dict[str, Any]] = None
    displayName: Optional[str] = None

class SpecModel(BaseModel):
    """Specifies visualization settings for widgets."""
    version: int
    widgetType: str
    encodings: Dict[str, Any]
    frame: Optional[Dict[str, Any]] = None

class WidgetModel(BaseModel):
    """Represents a widget in a dashboard."""
    name: Optional[str] = Field(default_factory=generate_unique_id)
    textbox_spec: Optional[str] = None
    queries: Optional[List[QueryModel]] = None
    spec: Optional[SpecModel] = None

    @model_validator(mode='before')
    @classmethod
    def check_spec_requirement(cls, values):
        """Validates widget configuration based on type."""
        if values.get('textbox_spec'):
            values.pop('spec', None)
            values.pop('queries', None)
        elif not values.get('spec') or not values.get('queries'):
            raise ValueError("Visualization widgets require 'spec' and 'queries'")
        return values

class DatasetModel(BaseModel):
    """Represents a dataset in the dashboard."""
    name: Optional[str] = Field(default_factory=generate_unique_id)
    displayName: str
    query: str

class PositionModel(BaseModel):
    """Defines the position and size of a widget on a page."""
    x: int
    y: int
    width: int
    height: int

class LayoutModel(BaseModel):
    """Defines the layout configuration of a widget on a page."""
    widget: WidgetModel
    position: PositionModel

class PageModel(BaseModel):
    """Represents a page in the dashboard."""
    name: Optional[str] = Field(default_factory=generate_unique_id)
    displayName: str
    layout: List[LayoutModel]

class DashboardModel(BaseModel):
    """Represents the entire dashboard configuration."""
    displayName: Optional[str] = Field(default=None, exclude=True)
    datasets: List[DatasetModel]
    pages: List[PageModel]
    warehouse_id: Optional[str] = Field(default=None, exclude=True)
    
    @model_validator(mode='before')
    @classmethod
    def remove_none_fields(cls, values):
        """Removes None values to ensure a clean JSON output."""
        return {k: v for k, v in values.items() if v is not None}
