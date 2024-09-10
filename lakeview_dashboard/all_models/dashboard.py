from pydantic import BaseModel, Field, model_validator
from typing import List, Optional
from .pages import PageModel
from .datasets import DatasetModel
from .utils import generate_unique_id

class DashboardModel(BaseModel):
    """
    Represents the entire dashboard configuration.

    Attributes:
        displayName (Optional[str]): The display name of the dashboard.
        datasets (List[DatasetModel]): The list of datasets used in the dashboard.
        pages (List[PageModel]): The list of pages in the dashboard.
        warehouse_id (Optional[str]): The warehouse ID associated with the dashboard.
    """
    displayName: Optional[str] = Field(default=None, exclude=True)
    datasets: List[DatasetModel]
    pages: List[PageModel]
    warehouse_id: Optional[str] = Field(default=None, exclude=True)

    @model_validator(mode='before')
    def remove_none_fields(cls, values):
        """
        Removes None values to ensure a clean JSON output.

        Args:
            values (dict): The values to clean.

        Returns:
            dict: The cleaned values.
        """
        return {k: v for k, v in values.items() if v is not None}