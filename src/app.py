import os
from flask import Flask

from src.routes.employees import router as employees_router
from src.routes.health import router as health_router

from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.register_blueprint(employees_router)
    app.register_blueprint(health_router)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080))
    )
