import pytest
import json
import os
# from lakeview_dashboard.models import DashboardModel
from lakeview_dashboard.all_models import DashboardModel


def test_create_dashboard(lakeview_dashboard, sample_dashboard):
    print("Creating dashboard...")
    create_response = lakeview_dashboard.create_dashboard(sample_dashboard)
    assert create_response.dashboard_id is not None
    print("Dashboard created:", create_response.dashboard_id)

    dashboard_id = create_response.dashboard_id
    print("Dashboard ID:", dashboard_id)

    print("Fetching dashboard details...")
    get_response = lakeview_dashboard.get_dashboard(dashboard_id)
    assert get_response.display_name == sample_dashboard.displayName

    print("Deleting dashboard...")
    lakeview_dashboard.delete_dashboard(dashboard_id)


def test_create_dashboard_with_json(lakeview_dashboard):
    print("Creating dashboard...")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = (os.path.join(current_dir, "sample_dashboard.json"))
    with open(json_file_path, "r") as file:
        dashboard_data = json.load(file)

    sample_dashboard = DashboardModel(**dashboard_data)
    create_response = lakeview_dashboard.create_dashboard(sample_dashboard)
    assert create_response.dashboard_id is not None
    print("Dashboard created:", create_response.dashboard_id)

    dashboard_id = create_response.dashboard_id
    print("Dashboard ID:", dashboard_id)

    print("Deleting dashboard...")
    lakeview_dashboard.delete_dashboard(dashboard_id)


def test_create_dashboard_with_workspace_client(workspace_client, lakeview_dashboard):
    print("Creating dashboard...")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = (os.path.join(current_dir, "sample_dashboard.json"))
    with open(json_file_path, "r") as file:
        dashboard_data = json.load(file)

    display_name = dashboard_data.get("displayName")
    print(display_name)
    create_response = workspace_client.lakeview.create(
        display_name=display_name, serialized_dashboard=json.dumps(dashboard_data))
    assert create_response.dashboard_id is not None
    print("Dashboard created:", create_response.dashboard_id)

    dashboard_id = create_response.dashboard_id
    print("Dashboard ID:", dashboard_id)

    print("Deleting dashboard...")
    lakeview_dashboard.delete_dashboard(dashboard_id)
