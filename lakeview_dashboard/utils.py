from lakeview_dashboard.models import *


def replace_catalog_schema(query: str, old_catalog: str, old_schema: str, new_catalog: str, new_schema: str) -> str:
    """
    Replaces all occurrences of old catalog and schema in the SQL query with new catalog and schema.

    Args:
    - query (str): The original SQL query.
    - old_catalog (str): The old catalog name to replace.
    - old_schema (str): The old schema name to replace.
    - new_catalog (str): The new catalog name.
    - new_schema (str): The new schema name.

    Returns:
    - str: The updated SQL query with the new catalog and schema.
    """
    # Create the old and new prefix
    old_prefix = f"{old_catalog}.{old_schema}"
    new_prefix = f"{new_catalog}.{new_schema}"

    # Replace all occurrences of the old prefix with the new prefix
    updated_query = query.replace(old_prefix, new_prefix)
    return updated_query


def update_all_queries(dashboard: DashboardModel, old_catalog: str, old_schema: str, new_catalog: str, new_schema: str) -> DashboardModel:
    """
    Updates all SQL queries in the dashboard model with new catalog and schema names.

    Args:
    - dashboard (DashboardModel): The dashboard model to update.
    - old_catalog (str): The old catalog name to replace.
    - old_schema (str): The old schema name to replace.
    - new_catalog (str): The new catalog name.
    - new_schema (str): The new schema name.

    Returns:
    - DashboardModel: The updated dashboard model with modified queries.
    """
    # Iterate over each dataset in the dashboard
    for dataset in dashboard.datasets:
        # Update the SQL query for each dataset
        dataset.query = replace_catalog_schema(
            dataset.query, old_catalog, old_schema, new_catalog, new_schema)

    # Return the modified dashboard
    return dashboard
