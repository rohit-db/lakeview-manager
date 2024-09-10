import pytest
import os
import dotenv
import json
from databricks.sdk import WorkspaceClient
from lakeview_dashboard.dashboard import LakeviewDashboard
from lakeview_dashboard.models import *
import datetime

# Load environment variables from .env file
dotenv.load_dotenv()


@pytest.fixture(scope="session")
def api_configuration():
    """
    Fixture to set up the API configuration.
    This is executed once per test session.
    """
    # Configure API settings
    databricks_token = os.getenv("DATABRICKS_TOKEN")
    host = "https://adb-984752964297111.11.azuredatabricks.net/"

    if not databricks_token:
        raise ValueError("DATABRICKS_TOKEN environment variable not set.")

    return {
        "DATABRICKS_TOKEN": databricks_token,
        "HOST": host
    }


@pytest.fixture(scope="module")
def workspace_client(api_configuration):
    """
    Fixture to initialize the Workspace Client for Databricks.
    This fixture is set up once per module and reused in all tests within the module.
    """
    client = WorkspaceClient(
        host=api_configuration["HOST"], token=api_configuration["DATABRICKS_TOKEN"])
    return client


@pytest.fixture(scope="function")
def lakeview_dashboard(workspace_client):
    """
    Fixture to initialize the LakeviewDashboard class with the Workspace Client.
    This fixture depends on the workspace_client fixture.
    """
    return LakeviewDashboard(client=workspace_client)


@pytest.fixture(scope="function")
def sample_dashboard_from_file():
    # Load the sample dashboard from a JSON file
    with open("./tests/sample_dashboard.json", "r") as file:
        dashboard_data = json.load(file)

    # Convert the JSON data to a DashboardModel instance
    return DashboardModel(**dashboard_data)


@pytest.fixture(scope="function")
def sample_dashboard():
    sample_dataset = DatasetModel(
        name="3753abac",
        displayName="Untitled dataset",
        query="select * from rohitb_demo.costa_mart.employees"
    )

    sample_dataset_2 = DatasetModel(
        name="3753abad",
        displayName="Untitled dataset",
        query="select * from rohitb_demo.costa_mart.employees e join rohitb_demo.costa_mart.stores s on e.StoreId = s.storeID where s.storeID > 82"
    )

    sample_text_widget = WidgetModel(
        name="a3070c2b",
        textbox_spec="# My Dashboard\nThis is a sample dashboard"
        # Remove or adjust the spec field since it's a text-based widget.
    )

    sample_layouts = [
        LayoutModel(widget=sample_text_widget,
                    position=PositionModel(x=0, y=0, width=6, height=2))
    ]

    sample_page = PageModel(
        name="b266a226",
        displayName="New Page",
        layout=sample_layouts
    )

    sample_dashboard = DashboardModel(
        displayName=f"Test Dashboard {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        datasets=[sample_dataset],
        pages=[sample_page],
        warehouse_id="d1184b8c2a8a87eb"
    )

    return DashboardModel(
        displayName=f"Test Dashboard {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        datasets=[sample_dataset, sample_dataset_2],
        pages=[sample_page],
        warehouse_id="d1184b8c2a8a87eb"
    )