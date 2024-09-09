# import test_dashboard_basics
# # Configure API settings

# # Initialize the Workspace Client
# w = WorkspaceClient(host=HOST, token=DATABRICKS_TOKEN)

# # Initialize the LakeviewDashboard class with the Workspace Client
# dashboard = LakeviewDashboard(client=w)

# def test_update_dash_modify_schema(sample_dashboard):

#     print("Creating dashboard...")
#     create_response = dashboard.create_dashboard(sample_dashboard)
#     print("Dashboard created:", create_response.dashboard_id)

#     # Define old and new catalog and schema names
#     old_catalog = "old_catalog_name"
#     old_schema = "old_schema_name"
#     new_catalog = "new_catalog_name"
#     new_schema = "new_schema_name"

#     # # Update all queries in the dashboard
#     # updated_dashboard = update_all_queries(sample_dashboard, old_catalog, old_schema, new_catalog, new_schema)

#     # # Print updated dashboard to verify
#     # print("Updated Dashboard JSON:", updated_dashboard.json(by_alias=True, exclude_none=True))

#     # # Test the update functionality
#     # update_response = dashboard.update_dashboard(dashboard_id, updated_dashboard, etag=etag)
