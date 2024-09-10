import os
import dotenv
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.dashboards import DashboardView
from typing import Dict, Any

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


def main():
    config = get_config()
    client = initialize_client(config)
    # Use list method with parameters
    dashboards_iterator = client.lakeview.list(page_size=300, view=DashboardView.DASHBOARD_VIEW_BASIC)

    # Iterate over the generator object
    for dashboard in dashboards_iterator:
        # print(f"Display Name: {dashboard.display_name}, Dashboard ID: {dashboard.dashboard_id}")

        # path and parent_path are not included in the list response 
        # if dashboard.parent_path is not None and "/Users/rohit.bhagwat@databricks.com" in dashboard.parent_path and "Test Dashboard" in dashboard.display_name: 
        if "Test Dashboard" in dashboard.display_name:
            print(f"Delete Dashboard with ID: {dashboard.dashboard_id} and Display Name: {dashboard.display_name} in path {dashboard.parent_path}")

if __name__ == "__main__":
    main()