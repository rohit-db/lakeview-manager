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


# Running Tests
Run tests with:

```bash
pytest
```