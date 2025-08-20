"""
Unit tests for the Flask application.

These tests use the Flask test client to simulate HTTP requests to
the application and verify that the responses are as expected.
"""

import pytest
from app import create_app


@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()


def test_root_returns_greeting(client):
    """Ensure the root endpoint returns the expected greeting."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hola Mundo"
