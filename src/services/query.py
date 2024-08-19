from google.cloud import bigquery
from src.config import logger
from src.config import EMPLOYEE_QUERY

client = bigquery.Client()


def execute_query() -> list[dict]:
    """Execute a BigQuery query to fetch employee data.

    This function sends a query to BigQuery to retrieve employee information,
    including phone number, salary, and name.

    Returns:
    - list[dict]: A list of dictionaries, each containing details of an employee.

    Raises:
    - Exception: If there's an error executing the query or processing the results.
    """
    logger.info("Executing BigQuery query to fetch employee data")

    query_job = client.query(EMPLOYEE_QUERY)
    logger.info("Query job created")

    results = []
    for row in query_job.result():
        results.append(dict(row))

    logger.info(
        f"Query executed successfully, retrieved {len(results)} rows"
    )
    return results