"""
This package contains models for the dashboard application.

Modules:
    datasets: Models related to datasets used in the dashboard.
    pages: Models related to pages within the dashboard.
    widgets: Models related to different types of widgets in the dashboard.
    layout: Models related to the layout of widgets on a page.
    specifications: Models related to widget specifications.
    dashboard: The main dashboard model that ties everything together.
    utils: Utility functions used across the models.

Hierarchy:
- DashboardModel: Represents the entire dashboard configuration.
  - DatasetModel: Represents datasets used in the dashboard.
  - PageModel: Represents individual pages within the dashboard.
    - LayoutModel: Defines the layout and positioning of widgets on a page.
      - TextWidgetModel: Represents text-based widgets.
      - VisualizationWidgetModel: Represents visualization widgets (e.g., charts, graphs).
        - QueryModel: Represents queries associated with visualization widgets.
          - QueryDetailsModel: Contains details of a query, such as dataset and fields.
          - FieldModel: Represents individual fields used in a query.
        - SpecModel: Specifies settings for visual elements in visualization widgets.
          - EncodingModel: General encoding settings for visual elements.
          - FieldEncodingModel: Encoding settings specific to filter widgets.
          - FrameModel: Frame settings for visualization widgets (e.g., titles, descriptions).
      - PositionModel: Specifies the position and size of widgets on a page.
"""

from .datasets import DatasetModel, ParameterModel
from .pages import PageModel
from .widgets import TextWidgetModel, VisualizationWidgetModel, FilterWidgetModel, QueryModel, FieldModel, QueryDetailsModel
from .layout import LayoutModel, PositionModel
from .specs import SpecModel, TableSpecModel, EncodingModel, FrameModel, ColumnModel
from .dashboard import DashboardModel
from .utils import generate_unique_id

__all__ = [
    "DatasetModel",
    "ParameterModel",
    "PageModel",
    "TextWidgetModel",
    "VisualizationWidgetModel",
    "FilterWidgetModel",
    "LayoutModel",
    "PositionModel",
    "SpecModel",
    "TableSpecModel",
    "EncodingModel",
    "FrameModel",
    "ColumnModel",
    "DashboardModel",
    "QueryModel",
    "QueryDetailsModel",
    "FieldModel",
    "DashboardModel",
    "generate_unique_id",
]