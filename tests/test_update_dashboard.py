import pytest
import datetime
from lakeview_dashboard.all_models import DashboardModel
from lakeview_dashboard.utils import update_all_queries
import json

def test_update_dashboard_name(lakeview_dashboard, sample_dashboard):
    print("Creating dashboard...")
    create_response = lakeview_dashboard.create_dashboard(sample_dashboard)
    assert create_response.dashboard_id is not None
    print("Dashboard created:", create_response.dashboard_id)

    dashboard_id = create_response.dashboard_id
    print("Dashboard ID:", dashboard_id)
    
    print("Updating dashboard...")

    sample_dashboard.displayName = f"Updated Dashboard {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    update_response = lakeview_dashboard.update_dashboard(dashboard_id, sample_dashboard)
    assert update_response.display_name == sample_dashboard.displayName
    print("Dashboard updated:", update_response.display_name)

    print("Deleting dashboard...")
    lakeview_dashboard.delete_dashboard(dashboard_id)

def test_update_dashboard_schema(lakeview_dashboard, sample_dashboard):
    print("Creating dashboard...")
    create_response = lakeview_dashboard.create_dashboard(sample_dashboard)
    assert create_response.dashboard_id is not None
    print("Dashboard created:", create_response.dashboard_id)

    dashboard_id = create_response.dashboard_id
    print("Dashboard ID:", dashboard_id)
    
    # Define old and new catalog and schema names
    old_catalog = "rohitb_demo"
    old_schema = "costa_mart"
    new_catalog = "new_catalog_name"
    new_schema = "new_schema_name"

    print("Updating dashboard catalog and schema..")
    updated_dashboard = update_all_queries(sample_dashboard, old_catalog, old_schema, new_catalog, new_schema)

    print(updated_dashboard.datasets)
    print("Updated Dashboard JSON:", updated_dashboard.model_dump_json(by_alias=True, exclude_none=True))

    print("Updating dashboard")
    update_response = lakeview_dashboard.update_dashboard(dashboard_id, updated_dashboard)
    updated_response_dashboard = DashboardModel(**json.loads(update_response.serialized_dashboard))
    assert updated_response_dashboard.datasets[0].query == updated_dashboard.datasets[0].query
    assert updated_response_dashboard.datasets[1].query == updated_dashboard.datasets[1].query
    print("Dashboard updated:", update_response.display_name)

    print("Deleting dashboard...")
    lakeview_dashboard.delete_dashboard(dashboard_id)

