# import pytest
# import datetime
# import os
# import dotenv
# from lakeview_dashboard.dashboard import LakeviewDashboard
# from lakeview_dashboard.models import *
# from databricks.sdk import WorkspaceClient

# # Load environment variables from .env file
# dotenv.load_dotenv()

# # Configure API settings
# DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")
# HOST = "https://adb-984752964297111.11.azuredatabricks.net/"

# # Initialize the Workspace Client
# w = WorkspaceClient(host=HOST, token=DATABRICKS_TOKEN)

# # Initialize the LakeviewDashboard class with the Workspace Client
# dashboard = LakeviewDashboard(client=w)


# @pytest.fixture
# def sample_dashboard():
#     sample_dataset = DatasetModel(
#         name="3753abac",
#         displayName="Untitled dataset",
#         query="select * from rohitb_demo.costa_mart.employees"
#     )

#     sample_text_widget = WidgetModel(
#         name="a3070c2b",
#         textbox_spec="# My Dashboard\nThis is a sample dashboard"
#         # Remove or adjust the spec field since it's a text-based widget.
#     )

#     sample_bar_widget = WidgetModel(
#         name="0f229c5c",
#         queries=[QueryModel(
#             name="main_query",
#             query={
#                 "datasetName": "3753abac",
#                 "fields": [
#                     {"name": "JobTitle", "expression": "`JobTitle`"},
#                     {"name": "count(*)", "expression": "COUNT(`*`)"}
#                 ],
#                 "disaggregated": False
#             }
#         )],
#         spec=SpecModel(
#             version=3,
#             widgetType="bar",
#             encodings={
#                 "x": {"fieldName": "JobTitle", "scale": {"type": "categorical"}, "displayName": "JobTitle"},
#                 "y": {"fieldName": "count(*)", "scale": {"type": "quantitative"}, "displayName": "Count of Records"}
#             },
#             frame={"showTitle": True, "showDescription": True,
#                    "title": "Widget Title", "description": "Widget Description"}
#         )
#     )

#     sample_filter_widget = WidgetModel(
#         name="369c6d3c",
#         queries=[QueryModel(
#             name="dashboards/01ef6ea5962117a785de77ef4aeede11/datasets/01ef6ea599a91ca68bed95fd24f84c52_JobTitle",
#             query={
#                 "datasetName": "3753abac",
#                 "fields": [
#                     {"name": "JobTitle", "expression": "`JobTitle`"},
#                     {"name": "JobTitle_associativity",
#                         "expression": "COUNT_IF(`associative_filter_predicate_group`)"}
#                 ],
#                 "disaggregated": False
#             }
#         )],
#         spec=SpecModel(
#             version=2,
#             widgetType="filter-single-select",
#             encodings={
#                 "fields": [
#                     {"fieldName": "JobTitle", "displayName": "JobTitle",
#                         "queryName": "dashboards/01ef6ea5962117a785de77ef4aeede11/datasets/01ef6ea599a91ca68bed95fd24f84c52_JobTitle"}
#                 ]
#             },
#             frame={"showTitle": True, "title": "Filter Title"}
#         )
#     )

#     sample_layouts = [
#         LayoutModel(widget=sample_text_widget,
#                     position=PositionModel(x=0, y=0, width=6, height=2)),
#         LayoutModel(widget=sample_bar_widget, position=PositionModel(
#             x=0, y=3, width=3, height=6)),
#         LayoutModel(widget=sample_filter_widget,
#                     position=PositionModel(x=0, y=2, width=2, height=1))
#     ]

#     sample_page = PageModel(
#         name="b266a226",
#         displayName="New Page",
#         layout=sample_layouts
#     )

#     sample_dashboard = DashboardModel(
#         displayName=f"Test Dashboard {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
#         datasets=[sample_dataset],
#         pages=[sample_page],
#         warehouse_id="d1184b8c2a8a87eb"
#     )

#     return DashboardModel(
#         displayName=f"Test Dashboard {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
#         datasets=[sample_dataset],
#         pages=[sample_page],
#         warehouse_id="d1184b8c2a8a87eb"
#     )


# @pytest.mark.create
# def test_create_dashboard(sample_dashboard):
#     # Test creating a dashboard
#     print("Creating dashboard...")
#     create_response = dashboard.create_dashboard(sample_dashboard)
#     assert create_response.dashboard_id is not None
#     print("Dashboard created:", create_response.dashboard_id)

#     # Get Dashboard ID from the response
#     dashboard_id = create_response.dashboard_id
#     print("Dashboard ID:", dashboard_id)

#     # Fetch the dashboard
#     print("Fetching dashboard details...")
#     get_response = dashboard.get_dashboard(dashboard_id)
#     assert get_response.display_name == sample_dashboard.displayName

#     # Clean up: Delete the created dashboard
#     print("Deleting dashboard...")
#     dashboard.delete_dashboard(dashboard_id)


# @pytest.mark.update
# def test_update_dashboard(sample_dashboard):
#     # Test updating a dashboard
#     print("Creating dashboard for update...")
#     create_response = dashboard.create_dashboard(sample_dashboard)
#     dashboard_id = create_response.dashboard_id
#     print("Dashboard created:", dashboard_id)

#     # Modify the display name for the update
#     sample_dashboard.displayName = f"Updated Test Dashboard {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#     print("Updating dashboard...")
#     update_response = dashboard.update_dashboard(
#         dashboard_id, sample_dashboard)
#     assert update_response.display_name == sample_dashboard.displayName
#     print("Dashboard updated:", update_response.display_name)

#     # Clean up: Delete the updated dashboard
#     print("Deleting updated dashboard...")
#     dashboard.delete_dashboard(dashboard_id)


# @pytest.mark.delete
# def test_delete_dashboard(sample_dashboard):
#     # Test deleting a dashboard
#     print("Creating dashboard for deletion...")
#     create_response = dashboard.create_dashboard(sample_dashboard)
#     dashboard_id = create_response.dashboard_id
#     print("Dashboard created:", dashboard_id)

#     # Delete the created dashboard
#     print("Deleting dashboard...")
#     dashboard.delete_dashboard(dashboard_id)

#     # Add a delay to ensure deletion is processed
#     import time
#     time.sleep(2)

#     # Verify that the dashboard is deleted
#     print("Checking if dashboard still exists...")
#     try:
#         # Replace this with the actual method to get a dashboard
#         dashboard.get_dashboard(dashboard_id)
#         pytest.fail("Dashboard still exists after deletion")
#     except Exception as e:
#         print(f"Exception raised as expected: {str(e)}")
#         # Test passes if an exception is raised
