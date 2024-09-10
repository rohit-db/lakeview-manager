import json
import os
import datetime
import logging
from typing import Dict, Any

import dotenv
from databricks.sdk import WorkspaceClient
from lakeview_dashboard.dashboard import LakeviewDashboard
from lakeview_dashboard.all_models import (
    DashboardModel, DatasetModel, PageModel, LayoutModel, PositionModel,
    TextWidgetModel, VisualizationWidgetModel, QueryDetailsModel, SpecModel, EncodingModel, FrameModel, QueryModel, FieldModel, generate_unique_id
)
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
dotenv.load_dotenv()


def get_config() -> Dict[str, Any]:
    """Load configuration from environment variables."""
    return {
        "DATABRICKS_TOKEN": os.getenv("DATABRICKS_TOKEN"),
        "HOST": os.getenv("DATABRICKS_HOST", "https://adb-984752964297111.11.azuredatabricks.net/"),
        "WAREHOUSE_ID": os.getenv("WAREHOUSE_ID", "d1184b8c2a8a87eb")
    }


def initialize_client(config: Dict[str, Any]) -> WorkspaceClient:
    """Initialize and return a Workspace Client."""
    return WorkspaceClient(host=config["HOST"], token=config["DATABRICKS_TOKEN"])


def create_dashboard_from_json(lakeview_manager: LakeviewDashboard, json_file_path: str) -> Any:
    """Create a dashboard from a JSON file."""
    try:
        with open(json_file_path, "r") as file:
            dashboard_data = json.load(file)

        dashboard_data["displayName"] = f"{dashboard_data['displayName']} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        sample_dashboard = DashboardModel(**dashboard_data)
        return lakeview_manager.create_dashboard(sample_dashboard)
    except Exception as e:
        logger.error(f"Error creating dashboard from JSON: {e}")
        raise


def create_dashboard_from_model(lakeview_manager: LakeviewDashboard, dashboard_model: DashboardModel) -> Any:
    """Create a dashboard from a Dashboard Model."""
    try:
        return lakeview_manager.create_dashboard(dashboard_model)
    except Exception as e:
        logger.error(f"Error creating dashboard from model: {e}")
        raise


def create_sample_dashboard_model(config: Dict[str, Any]) -> DashboardModel:
    """Create and return a sample Dashboard Model."""
    # Create the dashboard from a Dashboard Model

    # Create a sample dataset
    sample_dataset = DatasetModel(
        name=generate_unique_id(),
        displayName="Untitled dataset",
        query="SELECT * FROM samples.nyctaxi.trips"
    )

    # Create text widgets
    sample_text_widget = TextWidgetModel(
        textbox_spec="# My Dashboard\nThis is a sample dashboard"
    )

    sample_text_widget_2 = TextWidgetModel(
        textbox_spec="## Another Heading"
    )

    # Create FieldModel instances
    fields = [
        FieldModel(name="pickup_datetime", expression="pickup_datetime"),
        FieldModel(name="trip_distance", expression="trip_distance")
    ]

    # Create QueryDetailsModel instance
    query_details = QueryDetailsModel(
        datasetName=sample_dataset.name,
        fields=fields,
        disaggregated=False
    )

    # Create QueryModel instance
    query_model = QueryModel(
        name="main_query",
        query=query_details
    )

    # Create SpecModel instance for a line chart
    spec = SpecModel(
        version=3,
        widgetType="line",
        encodings=EncodingModel(
            x={
                "fieldName": "pickup_datetime",
                "scale": {"type": "temporal"},
                "displayName": "Pickup DateTime"
            },
            y={
                "fieldName": "trip_distance",
                "scale": {"type": "quantitative"},
                "displayName": "Trip Distance"
            }
        ),
        frame=FrameModel(
            showTitle=True,
            title="Trip Distance Over Time"
        )
    )

    # Create VisualizationWidgetModel instance
    sample_line_widget = VisualizationWidgetModel(
        name=generate_unique_id(),
        queries=[query_model],
        spec=spec
    )
    # Define the layout for widgets
    sample_layouts = [
        LayoutModel(widget=sample_text_widget,
                    position=PositionModel(x=0, y=0, width=5, height=2)),
        LayoutModel(widget=sample_text_widget_2,
                    position=PositionModel(x=6, y=0, width=1, height=2)),
        LayoutModel(widget=sample_line_widget,
                    position=PositionModel(x=0, y=2, width=6, height=6))
    ]

    # Create a sample page with the layout
    sample_page = PageModel(
        displayName="New Page",
        layout=sample_layouts
    )

    # Create the dashboard model
    sample_dashboard = DashboardModel(
        displayName=f"Test Dashboard {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        datasets=[sample_dataset],
        pages=[sample_page],
        warehouse_id=config["WAREHOUSE_ID"]
    )

    return sample_dashboard


def main():
    config = get_config()
    client = initialize_client(config)
    lakeview_manager = LakeviewDashboard(client=client)

    sample_dashboard = create_sample_dashboard_model(config)
    print(sample_dashboard)
    create_response = create_dashboard_from_model(
        lakeview_manager, sample_dashboard)
    logger.info(f"Dashboard created with ID: {create_response.dashboard_id}")


if __name__ == "__main__":
    main()
