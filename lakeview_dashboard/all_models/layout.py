from pydantic import BaseModel, model_validator
from typing import Union
from .widgets import TextWidgetModel, VisualizationWidgetModel, FilterWidgetModel
from .specs import TableSpecModel, SpecModel

class PositionModel(BaseModel):
    """
    Defines the position and size of a widget on a page.

    Attributes:
        x (int): The x-coordinate of the widget.
        y (int): The y-coordinate of the widget.
        width (int): The width of the widget.
        height (int): The height of the widget.
    """
    x: int
    y: int
    width: int
    height: int

class LayoutModel(BaseModel):
    """
    Defines the layout configuration of a widget on a page.

    Attributes:
        widget (Union[TextWidgetModel, VisualizationWidgetModel, FilterWidgetModel]): The widget to be placed.
        position (PositionModel): The position and size of the widget.
    """
    widget: Union[TextWidgetModel, VisualizationWidgetModel, FilterWidgetModel]
    position: PositionModel

    @model_validator(mode='before')
    def validate_widget(cls, values):
        """
        Validates the widget data and ensures the correct widget type is instantiated.

        Args:
            values (dict): The values to validate.

        Returns:
            dict: The validated values.
        """
        widget_data = values.get('widget')
        if widget_data:
            if isinstance(widget_data, dict):
                if 'spec' in widget_data:
                    spec_data = widget_data.pop('spec')  # Remove 'spec' from widget_data
                    widget_type = spec_data.get('widgetType')
                    if widget_type == 'table':
                        # Ensure columns are included in TableSpecModel
                        encodings = spec_data.get('encodings', {})
                        columns = encodings.get('columns')
                        if columns:
                            table_spec_data = {**spec_data, 'columns': columns}
                            values['widget'] = VisualizationWidgetModel(
                                **widget_data, spec=TableSpecModel(**table_spec_data))
                        else:
                            raise ValueError(
                                f"Missing 'columns' field in TableSpecModel for widget: {widget_data}")
                    else:
                        # Handle other visualization types
                        values['widget'] = VisualizationWidgetModel(
                            **widget_data, spec=SpecModel(**spec_data))
                elif 'textbox_spec' in widget_data:
                    values['widget'] = TextWidgetModel(**widget_data)
                else:
                    values['widget'] = FilterWidgetModel(**widget_data)
            elif isinstance(widget_data, (TextWidgetModel, VisualizationWidgetModel, FilterWidgetModel)):
                values['widget'] = widget_data
            else:
                raise TypeError(
                    f"Unsupported widget type: {type(widget_data)}")
        return values
    
    # @model_validator(mode='before')
    # def validate_widget(cls, values):
