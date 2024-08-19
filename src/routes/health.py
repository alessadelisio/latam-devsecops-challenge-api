from flask import Blueprint

from src.config import logger

router = Blueprint("health", __name__)


@router.route("/health", methods=["GET"])
def health():
    """Health endpoint to check if the service
    is up and running."""

    logger.info("Health endpoint reached successfully.")
    return {"status": "ok", "code": 200}
