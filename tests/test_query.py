import pytest
from unittest.mock import patch
from src.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("src.routes.employees.execute_query")
def test_get_employees(mock_execute_query, client):
    mock_data = [
        {
            "EmpPhoneNo": "123-456-7890",
            "EmpSalary": 50000,
            "EmployeeName": "John Doe",
        },
        {
            "EmpPhoneNo": "098-765-4321",
            "EmpSalary": 60000,
            "EmployeeName": "Jane Smith",
        },
    ]
    mock_execute_query.return_value = mock_data

    response = client.get("/employees")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]["EmployeeName"] == "John Doe"
    assert data[1]["EmployeeName"] == "Jane Smith"
    mock_execute_query.assert_called_once()


@patch("src.routes.employees.execute_query")
def test_get_employees_error(mock_execute_query, client):
    mock_execute_query.side_effect = Exception("Database error")

    response = client.get("/employees")

    assert response.status_code == 500
    data = response.get_json()
    assert "error" in data
    assert "Database error" in data["error"]
