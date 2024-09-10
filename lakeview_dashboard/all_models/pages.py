"""
This module contains models related to pages within the dashboard.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from .layout import LayoutModel
from .utils import generate_unique_id

class PageModel(BaseModel):
    """
    Represents a page in the dashboard.

    Attributes:
        name (Optional[str]): The unique identifier for the page. Default is generated using `generate_unique_id`.
        displayName (str): The display name of the page.
        layout (List[LayoutModel]): The layout configuration of the page.
    """
    name: Optional[str] = Field(default_factory=generate_unique_id)
    displayName: str
    layout: List[LayoutModel]