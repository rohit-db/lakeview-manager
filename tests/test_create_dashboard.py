import pytest


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
