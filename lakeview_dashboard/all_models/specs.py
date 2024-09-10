from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union

class EncodingModel(BaseModel):
    """
    Encodings for visual elements in widgets.

    Attributes:
        fields (Optional[List[Dict[str, str]]]): The fields to be encoded.
        x (Optional[Dict[str, Any]]): The x-axis encoding.
        y (Optional[Dict[str, Any]]): The y-axis encoding.
        color (Optional[Dict[str, Any]]): The color encoding.
        label (Optional[Dict[str, Any]]): The label encoding.
    """
    fields: Optional[List[Dict[str, str]]] = None
    x: Optional[Dict[str, Any]] = None
    y: Optional[Dict[str, Any]] = None
    color: Optional[Dict[str, Any]] = None
    label: Optional[Dict[str, Any]] = None

class FrameModel(BaseModel):
    """
    Frame settings for widgets.

    Attributes:
        showTitle (bool): Whether to show the title. Default is True.
        title (Optional[str]): The title of the frame.
    """
    showTitle: bool = True
    title: Optional[str] = None

class ColumnModel(BaseModel):
    """
    Represents a column in a table widget.

    Attributes:
        fieldName (str): The name of the field.
        booleanValues (Optional[List[str]]): The boolean values for the column.
        imageUrlTemplate (Optional[str]): The template for the image URL.
        imageTitleTemplate (Optional[str]): The template for the image title.
        imageWidth (Optional[str]): The width of the image.
        imageHeight (Optional[str]): The height of the image.
        linkUrlTemplate (Optional[str]): The template for the link URL.
        linkTextTemplate (Optional[str]): The template for the link text.
        linkTitleTemplate (Optional[str]): The template for the link title.
        linkOpenInNewTab (Optional[bool]): Whether to open the link in a new tab.
        type (Optional[str]): The type of the column.
        displayAs (Optional[str]): How to display the column.
        visible (Optional[bool]): Whether the column is visible.
        order (Optional[int]): The order of the column.
        title (Optional[str]): The title of the column.
        allowSearch (Optional[bool]): Whether to allow search in the column.
        alignContent (Optional[str]): How to align the content.
        allowHTML (Optional[bool]): Whether to allow HTML content.
        highlightLinks (Optional[bool]): Whether to highlight links.
        useMonospaceFont (Optional[bool]): Whether to use a monospace font.
        preserveWhitespace (Optional[bool]): Whether to preserve whitespace.
        displayName (Optional[str]): The display name of the column.
        numberFormat (Optional[str]): The number format for the column.
    """
    fieldName: str
    booleanValues: Optional[List[str]] = None
    imageUrlTemplate: Optional[str] = None
    imageTitleTemplate: Optional[str] = None
    imageWidth: Optional[str] = None
    imageHeight: Optional[str] = None
    linkUrlTemplate: Optional[str] = None
    linkTextTemplate: Optional[str] = None
    linkTitleTemplate: Optional[str] = None
    linkOpenInNewTab: Optional[bool] = None
    type: Optional[str] = None
    displayAs: Optional[str] = None
    visible: Optional[bool] = None
    order: Optional[int] = None
    title: Optional[str] = None
    allowSearch: Optional[bool] = None
    alignContent: Optional[str] = None
    allowHTML: Optional[bool] = None
    highlightLinks: Optional[bool] = None
    useMonospaceFont: Optional[bool] = None
    preserveWhitespace: Optional[bool] = None
    displayName: Optional[str] = None
    numberFormat: Optional[str] = None

class TableSpecModel(BaseModel):
    """
    Represents the specification for a table widget.

    Attributes:
        version (int): The version of the specification.
        widgetType (str): The type of the widget.
        encodings (Dict[str, Any]): The encodings for the widget.
        frame (FrameModel): The frame settings for the widget.
        columns (List[ColumnModel]): The columns in the table.
        invisibleColumns (Optional[List[Union[str, Dict[str, Any]]]]): The invisible columns in the table.
        allowHTMLByDefault (Optional[bool]): Whether to allow HTML by default.
        itemsPerPage (Optional[int]): The number of items per page.
        paginationSize (Optional[str]): The size of the pagination.
        condensed (Optional[bool]): Whether the table is condensed.
        withRowNumber (Optional[bool]): Whether to show row numbers.
    """
    version: int
    widgetType: str
    encodings: Dict[str, Any]
    frame: FrameModel
    columns: List[ColumnModel]
    invisibleColumns: Optional[List[Union[str, Dict[str, Any]]]] = None
    allowHTMLByDefault: Optional[bool] = None
    itemsPerPage: Optional[int] = None
    paginationSize: Optional[str] = None
    condensed: Optional[bool] = None
    withRowNumber: Optional[bool] = None

class SpecModel(BaseModel):
    """
    Represents the specification for a visualization widget.

    Attributes:
        version (int): The version of the specification.
        widgetType (str): The type of the widget.
        encodings (EncodingModel): The encodings for the widget.
        frame (FrameModel): The frame settings for the widget.
    """
    version: Optional[int] = None
    widgetType: str
    encodings: EncodingModel
    frame: FrameModel = Field(default_factory=lambda: FrameModel(showTitle=True, title="Default Title"))