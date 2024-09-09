from .models import *
from databricks.sdk import WorkspaceClient
from typing import List, Dict, Any


class LakeviewDashboard:
    def __init__(self, client: WorkspaceClient):
        self.client = client

    def create_dashboard(self, dashboard_data: DashboardModel) -> Dict[str, Any]:
        # Convert to JSON string with exclude_none to omit fields set to None
        serialized_dashboard = dashboard_data.model_dump_json(by_alias=True, exclude_none=True)

        # Debug: Print the serialized JSON to verify the structure
        # print("Serialized Dashboard JSON:", serialized_dashboard)

        response = self.client.lakeview.create(
            display_name=dashboard_data.displayName,  # Use correct attribute name
            serialized_dashboard=serialized_dashboard,
            warehouse_id=dashboard_data.warehouse_id
        )
        return response



    def update_dashboard(self, dashboard_id: str, updates: DashboardModel) -> Dict[str, Any]:
        # Convert to JSON string with exclude_none to omit fields set to None
        serialized_dashboard = updates.model_dump_json(by_alias=True, exclude_none=True)

        # Debug: Print the serialized JSON to verify the structure
        print("Serialized Dashboard JSON for Update:", serialized_dashboard)

        # Correctly update the dashboard with the right parameters
        response = self.client.lakeview.update(
            dashboard_id=dashboard_id,  # Pass the dashboard ID
            display_name=updates.displayName,  # Pass display name
            serialized_dashboard=serialized_dashboard,  # Provide the serialized dashboard as a string
            warehouse_id=updates.warehouse_id  # Pass the warehouse ID
        )
        return response


    def get_dashboard(self, dashboard_id: str) -> Dict[str, Any]:
        # Use the client to get dashboard details
        response = self.client.lakeview.get(dashboard_id=dashboard_id)
        return response

    def delete_dashboard(self, dashboard_id: str) -> bool:
        # Use the client to delete the dashboard
        self.client.lakeview.trash(dashboard_id=dashboard_id)
        return True  # Assume success unless an exception is raised
