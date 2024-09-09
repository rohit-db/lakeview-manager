# from lakeview_dashboard.dashboard import LakeviewDashboard
# from lakeview_dashboard.models import *
# import dotenv
# import os
# from databricks.sdk import WorkspaceClient
# import datetime

# # Load environment variables from .env file
# dotenv.load_dotenv()

# # Configure API settings
# DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")
# HOST = "https://adb-984752964297111.11.azuredatabricks.net/"

# # Initialize the Workspace Client
# w = WorkspaceClient(host=HOST, token=DATABRICKS_TOKEN)

# # Initialize the LakeviewDashboard class with the Workspace Client
# dashboard = LakeviewDashboard(client=w)

# sample_dataset = DatasetModel(
#     name="3753abac",
#     displayName="Untitled dataset",
#     query="select * from rohitb_demo.costa_mart.employees"
# )

# sample_text_widget = WidgetModel(
#     name="a3070c2b",
#     textbox_spec="# My Dashboard\nThis is a sample dashboard"
#     # Remove or adjust the spec field since it's a text-based widget.
# )

# sample_bar_widget = WidgetModel(
#     name="0f229c5c",
#     queries=[QueryModel(
#         name="main_query",
#         query={
#             "datasetName": "3753abac",
#             "fields": [
#                 {"name": "JobTitle", "expression": "`JobTitle`"},
#                 {"name": "count(*)", "expression": "COUNT(`*`)"}
#             ],
#             "disaggregated": False
#         }
#     )],
#     spec=SpecModel(
#         version=3,
#         widgetType="bar",
#         encodings={
#             "x": {"fieldName": "JobTitle", "scale": {"type": "categorical"}, "displayName": "JobTitle"},
#             "y": {"fieldName": "count(*)", "scale": {"type": "quantitative"}, "displayName": "Count of Records"}
#         },
#         frame={"showTitle": True, "showDescription": True, "title": "Widget Title", "description": "Widget Description"}
#     )
# )

# sample_filter_widget = WidgetModel(
#     name="369c6d3c",
#     queries=[QueryModel(
#         name="dashboards/01ef6ea5962117a785de77ef4aeede11/datasets/01ef6ea599a91ca68bed95fd24f84c52_JobTitle",
#         query={
#             "datasetName": "3753abac",
#             "fields": [
#                 {"name": "JobTitle", "expression": "`JobTitle`"},
#                 {"name": "JobTitle_associativity", "expression": "COUNT_IF(`associative_filter_predicate_group`)"}
#             ],
#             "disaggregated": False
#         }
#     )],
#     spec=SpecModel(
#         version=2,
#         widgetType="filter-single-select",
#         encodings={
#             "fields": [
#                 {"fieldName": "JobTitle", "displayName": "JobTitle", "queryName": "dashboards/01ef6ea5962117a785de77ef4aeede11/datasets/01ef6ea599a91ca68bed95fd24f84c52_JobTitle"}
#             ]
#         },
#         frame={"showTitle": True, "title": "Filter Title"}
#     )
# )

# sample_layouts = [
#     LayoutModel(widget=sample_text_widget, position=PositionModel(x=0, y=0, width=6, height=2)),
#     LayoutModel(widget=sample_bar_widget, position=PositionModel(x=0, y=3, width=3, height=6)),
#     LayoutModel(widget=sample_filter_widget, position=PositionModel(x=0, y=2, width=2, height=1))
# ]

# sample_page = PageModel(
#     name="b266a226",
#     displayName="New Page",
#     layout=sample_layouts
# )

# sample_dashboard = DashboardModel(
#     displayName=f"Test Dashboard {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
#     datasets=[sample_dataset],
#     pages=[sample_page],
#     warehouse_id="d1184b8c2a8a87eb"
# )


# # Create Dashboard
# print("Creating dashboard...")
# create_response = dashboard.create_dashboard(sample_dashboard)
# print("Dashboard created:", create_response.dashboard_id)

# # Get Dashboard ID from the response
# dashboard_id = create_response.dashboard_id
# print("Dashboard ID:", dashboard_id)

# # Get Dashboard
# print("Fetching dashboard details...")
# get_response = dashboard.get_dashboard(dashboard_id)
# # print("Dashboard details:", get_response)

# # Update Dashboard (modify the display name as an example)
# sample_dashboard.displayName = f"Updated Test Dashboard {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
# print("Updating dashboard...", dashboard_id)
# update_response = dashboard.update_dashboard(dashboard_id, sample_dashboard)
# print("Dashboard updated:", update_response)

# # Delete Dashboard
# print("Deleting dashboard...")
# # delete_response = dashboard.delete_dashboard(dashboard_id)
# # print("Dashboard deleted:", delete_response)
