import json
import os
import datetime
import logging
from typing import Dict, Any

import dotenv
from databricks.sdk import WorkspaceClient
from lakeview_dashboard.dashboard import LakeviewDashboard
from lakeview_dashboard.models import *
import datetime

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
    dashboard_json = json.loads(dashboard.serialized_dashboard)
    dashboard_model = DashboardModel(**dashboard_json)
    return dashboard_model

def main():
    config = get_config()
    client = initialize_client(config)
    lakeview_manager = LakeviewDashboard(client)

    dashboard_id = "01ef6a4327221667b44f87de263f6c71"
    # Using the databricks sdk to export and store in a json file  
    export_dashboard_to_json(lakeview_manager, dashboard_id, file_path=f"{dashboard_id}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json") 
    
    # Using the lakeview api to load the lakeview manager dashboard model  
    dashboard_model = load_dashboard_model_from_existing_dashboard(lakeview_manager, dashboard_id)
    # Interact using dashboard model 
    print(dashboard_model.display_name)

    # Create dashboard using dashboard_model
    lakeview_manager.create_dashboard(dashboard_model)


if __name__ == "__main__":
    main()