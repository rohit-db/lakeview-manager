from pydantic import BaseModel, Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any

class DatasetModel(BaseModel):
    name: str
    displayName: str
    query: str

class PositionModel(BaseModel):
    x: int
    y: int
    width: int
    height: int

class QueryModel(BaseModel):
    name: str
    query: Dict[str, Any]

class SpecModel(BaseModel):
    version: int
    widgetType: str
    encodings: Dict[str, Any]
    frame: Optional[Dict[str, Any]]

class WidgetModel(BaseModel):
    name: str
    textbox_spec: Optional[str] = None
    queries: Optional[List[QueryModel]] = None
    spec: Optional[SpecModel] = None

    # Use model_validator to exclude the spec field if it is not needed
    @model_validator(mode='before')
    @classmethod
    def check_spec_requirement(cls, values):
        if values.get('textbox_spec'):
            values.pop('spec', None)  # Remove spec field entirely if it's a text widget
        return values

class LayoutModel(BaseModel):
    widget: WidgetModel
    position: PositionModel

class PageModel(BaseModel):
    name: str
    displayName: str
    layout: List[LayoutModel]

class DashboardModel(BaseModel):
    displayName: Optional[str] = Field(default=None, exclude=True)
    datasets: List[DatasetModel]
    pages: List[PageModel]
    warehouse_id: Optional[str] = Field(default=None, exclude=True)
    model_config = ConfigDict(populate_by_name=True)  # Allows population using field names

    @model_validator(mode='before')
    @classmethod
    def remove_none_fields(cls, values):
        return {k: v for k, v in values.items() if v is not None}
