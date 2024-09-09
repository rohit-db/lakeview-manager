# LakeviewManager

**LakeviewManager** is a Python package for creating, managing, and automating Lakeview Dashboards in Databricks. It simplifies the process of interacting with Databricks Lakeview APIs by providing a set of utilities and abstractions, allowing users to focus on building and maintaining their dashboards effectively.

## Features

- Create, update, delete, and retrieve Lakeview dashboards in Databricks.
- Simplifies JSON handling for dashboard definitions.
- Provides flexible utility functions for common operations.
- Easily integrates with Databricks' Workspace Client.

## Installation

To use **LakeviewManager**, you'll need Python 3.7 or higher. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

Make sure to configure your environment variables by creating a .env file in the root directory of your project:

```DATABRICKS_TOKEN=your-databricks-api-token```

## Usage
Initialize the Workspace Client and LakeviewManager
To get started, initialize the Workspace Client and the LakeviewManager:

```python
from databricks.sdk import WorkspaceClient
from lakeview_dashboard.dashboard import LakeviewDashboard

# Configure API settings
DATABRICKS_TOKEN = "your_databricks_api_token"
HOST = "https://adb-984752964297111.11.azuredatabricks.net/"

# Initialize the Workspace Client
client = WorkspaceClient(host=HOST, token=DATABRICKS_TOKEN)

# Initialize the LakeviewDashboard class
dashboard_manager = LakeviewDashboard(client=client)
```

### Create a Dashboard
Use the provided JSON file to create a new dashboard:

```python
import json
from lakeview_dashboard.models import DashboardModel

# Load the dashboard configuration from a JSON file
with open("sample_dashboard.json", "r") as file:
    dashboard_data = json.load(file)

sample_dashboard = DashboardModel(**dashboard_data)

# Create the dashboard
create_response = dashboard_manager.create_dashboard(sample_dashboard)
print(f"Dashboard created with ID: {create_response.dashboard_id}")
```

### Update a Dashboard
Modify the existing dashboard properties and update:

```python
# Modify the dashboard's display name
sample_dashboard.displayName = "Updated Dashboard Name"

# Update the dashboard
update_response = dashboard_manager.update_dashboard(create_response.dashboard_id, sample_dashboard)
print(f"Dashboard updated: {update_response.display_name}")
```

### Delete a Dashboard
Delete a dashboard by its ID:

```python
# Delete the dashboard
dashboard_manager.delete_dashboard(create_response.dashboard_id)
print("Dashboard deleted.")
```

## Examples
You can find additional examples in the examples folder. Here are a few examples included:

- **Creating a Dashboard**: Example of creating a new dashboard using predefined JSON configurations.
- **Updating a Dashboard**: Example of updating a dashboard by modifying its properties.
- **Deleting a Dashboard**: Example of deleting a dashboard using its unique ID.


## Running Tests
To run the tests, use pytest:

```bash
pytest
```
This will execute all the tests defined in the tests folder.