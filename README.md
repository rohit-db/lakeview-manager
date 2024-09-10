# LakeviewManager
LakeviewManager is a Python package for creating, managing, and automating Lakeview Dashboards in Databricks. It simplifies interactions with Databricks Lakeview APIs by providing utilities and abstractions, allowing users to focus on building and maintaining dashboards efficiently.

# Features
- Perform CRUD operations on Lakeview dashboards in Databricks.
- Simplifies JSON handling for dashboard definitions.
- Includes utility functions for common tasks.
- Integrates seamlessly with Databricks' Workspace Client.

# Installation
Requires Python 3.7+. Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables by creating a .env file:

```bash
DATABRICKS_TOKEN=your-databricks-api-token
```

# Usage
## Initialize th eWOrkspace Client and Lakeview Manager
To get started, initialize the Workspace Client and Lakeview Manager:

```python
from lakeview_dashboard import WorkspaceClient, LakeviewDashboard

DATABRICKS_TOKEN = "your_databricks_token"
HOST = "https://<databricks-instance>"

workspace_client = WorkspaceClient(token=DATABRICKS_TOKEN, host=HOST)
lakeview_dashboard = LakeviewDashboard(client=workspace_client)
```

## Example Operations
- **Creating a Dashboard**: Define the dashboard configuration using JSON or Python objects and create a new Lakeview Dashboard in Databricks.
- **Updating a Dashboard**: Modify existing dashboard configurations and update them in Databricks.
- **Updating Catalog and Schema names for queries in a dashboard**: This is useful when you want to rename the catalog or schema of a query in a dashboard.
- **Exporting a Dashboard**: Save the current configuration of a dashboard to a JSON file.
- **Importing a Dashboard**: Load a dashboard configuration from a JSON file into the current workspace.

## Example creating Dashboard Model

```python 
def create_sample_dashboard_model(config: Dict[str, Any]) -> DashboardModel:
    """Create and return a sample Dashboard Model."""
    # Create the dashboard from a Dashboard Model

    # Create a sample dataset
    sample_dataset = DatasetModel(
        name=generate_unique_id(),
        displayName="Untitled dataset",
        query="SELECT * FROM samples.nyctaxi.trips"
    )

    # Create text widgets
    sample_text_widget = TextWidgetModel(
        textbox_spec="# My Dashboard\nThis is a sample dashboard"
    )
    # Define the layout for widgets
    sample_layouts = [
        LayoutModel(widget=sample_text_widget,
                    position=PositionModel(x=0, y=0, width=5, height=2)),
        LayoutModel(widget=sample_text_widget_2,
                    position=PositionModel(x=6, y=0, width=1, height=2))    ]

    # Create a sample page with the layout
    sample_page = PageModel(
        displayName="New Page",
        layout=sample_layouts
    )

    # Create the dashboard model
    sample_dashboard = DashboardModel(
        displayName=f"Test Dashboard {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        datasets=[sample_dataset],
        pages=[sample_page],
        warehouse_id=config["WAREHOUSE_ID"]
    )

    return sample_dashboard

```

# Running Tests
Run tests with:

```bash
pytest
```

# Additional Information 
- Documentation: Detailed API Documentation can be found at [Lakeview API Documentation](https://docs.databricks.com/dev-tools/api/latest/lakeview.html)
