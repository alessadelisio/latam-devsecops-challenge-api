from flask import Blueprint, jsonify

from src.config import logger
from src.services.query import execute_query

router = Blueprint("employees", __name__)


@router.route("/employees", methods=["GET"])
def get_employees() -> jsonify:
    """Fetch employee data from BigQuery and return it as JSON.

    This function executes a query to retrieve employee information from
    a BigQuery table and returns the results as a JSON response.

    Returns:
    - flask.Response: A JSON response containing employee data or an error message.

    Raises:
    - Exception: If there's an error executing the query or processing the results.
    """

    logger.info("Received request for employee data")
    try:
        results = execute_query()
        logger.info(
            f"Successfully retrieved {len(results)} employee records"
        )

        return jsonify(results), 200

    except Exception as error:
        logger.error(f"Error retrieving employee data: {str(error)}")

        return jsonify({"error": str(error)}), 500
