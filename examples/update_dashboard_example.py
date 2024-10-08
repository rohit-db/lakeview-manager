import json
import os
import datetime
import logging
from typing import Dict, Any

import dotenv
from databricks.sdk import WorkspaceClient
from lakeview_dashboard.dashboard import LakeviewDashboard
from lakeview_dashboard.all_models import DashboardModel

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

def export_dashboard_to_json(lakeview_manager: LakeviewDashboard, dashboard_id: str) -> Any:
    """Export a dashboard to a JSON file."""
    try:
        dashboard = lakeview_manager.get_dashboard(dashboard_id)
        dashboard_json = json.loads(dashboard.serialized_dashboard)

        with open(f"{dashboard_id}.json", "w") as file:
            json.dump(dashboard_json, file)
    except Exception as e:
        logger.error(f"Error exporting dashboard to JSON: {e}")
        raise

def load_dashboard_model_from_existing_dashboard(lakeview_manager: LakeviewDashboard, dashboard_id: str) -> Any:
    dashboard = lakeview_manager.get_dashboard(dashboard_id)
    dashboard_name = dashboard.display_name
    dashboard_json = json.loads(dashboard.serialized_dashboard)
    dashboard_model = DashboardModel(**dashboard_json)
    dashboard_model.displayName = dashboard_name
    return dashboard_model

def main():
    config = get_config()
    client = initialize_client(config)
    lakeview_manager = LakeviewDashboard(client)

    dashboard_id = "01ef6f946dcc15a68a45655f63f5f03d"
    # export_dashboard_to_json(lakeview_manager, dashboard_id)
    dashboard_model = load_dashboard_model_from_existing_dashboard(lakeview_manager, dashboard_id)

    dashboard_model.displayName = f"{dashboard_model.displayName} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    def find_widget_by_frame_title(dashboard_model: DashboardModel, frame_title: str) -> Any:
        """Find a widget by the frame's title within the dashboard_model."""
        widgets = []
        for page in dashboard_model.pages:
            for layout in page.layout:
                widget = layout.widget
                if hasattr(widget, 'spec') and hasattr(widget.spec, 'frame') and widget.spec.frame.title == frame_title:
                    widgets.append(widget)
        return widgets
    
    widgets = find_widget_by_frame_title(dashboard_model, "Top N Job Clusters")

    # Update the dashboard
    response = lakeview_manager.update_dashboard(dashboard_id, dashboard_model)
    print(f"Dashboard {response.display_name} updated successfully. Dashboard ID: {response.dashboard_id}. ETAG: {response.etag}")

if __name__ == "__main__":
    main()